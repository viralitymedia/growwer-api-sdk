# Deserialises the shared response fixtures through the generated Ruby client, offline.
#
# Each call is answered from tests/fixtures/ by a Faraday adapter set on the client's own connection,
# so the whole client path runs: URL, headers, status handling and the models. Run from the ruby/
# directory with `bundle exec rspec ../tests/ruby`.

require 'json'
require 'growwer'

FIXTURES = File.expand_path('../fixtures', __dir__)
MEDIA_ID = 'c1d2e3f4-a5b6-4c7d-8e9f-a0b1c2d3e4f5'
ORDER_ID = '0b9c6a4e-6f1d-4c39-9a51-2f5d7c1e8a01'
WEBHOOK_ID = '9d4c3f5b-6e7a-4b82-9d2e-3f4a5b6c7d8e'
PROJECT_ID = '5e0c2b7a-3d4f-4a1b-9c8d-7e6f5a4b3c2d'

# Answers every request with one canned response and records it. Faraday's own test adapter is not
# used because it ignores `on_data`, through which the client reads a download; a streamed response
# is delivered here the way Faraday's network adapters deliver it: body through `on_data`, empty body
# on the response.
class CannedAdapter < Faraday::Adapter
  def initialize(app, canned)
    super(app)
    @canned = canned
  end

  def call(env)
    super
    @canned[:sent] << env
    body = @canned[:body]
    if env.stream_response?
      env.request.on_data.call(body, body.bytesize, env)
      body = ''
    end
    save_response(env, @canned[:status], body, @canned[:headers])
    @app.call(env)
  end
end

RSpec.describe 'Growwer fixtures' do
  def fixture(name)
    File.binread(File.join(FIXTURES, name))
  end

  # A client whose every call is answered with one canned response, recording what was sent.
  def answer(status, body, headers = { 'Content-Type' => 'application/json' }, host: nil)
    @sent = []
    canned = { status: status, body: body, headers: headers, sent: @sent }
    config = Growwer::Configuration.new
    config.access_token = 'test-key'
    config.host = host if host
    config.configure_faraday_connection { |connection| connection.adapter(CannedAdapter, canned) }
    Growwer::ApiClient.new(config)
  end

  def sent
    expect(@sent.size).to eq(1)
    @sent.first
  end

  # A webhook body parsed the way a receiver parses it, without the API client.
  def event(name)
    Growwer::WebhookEvent.build_from_hash(JSON.parse(fixture(name)))
  end

  it 'calls production for getMe with the bearer key' do
    me = Growwer::AccountApi.new(answer(200, fixture('me.json'))).get_me

    expect(sent.method).to eq(:get)
    expect(sent.url.to_s).to eq('https://tool.growwer.com/api/v1/me')
    expect(sent.request_headers['Authorization']).to eq('Bearer test-key')
    expect(me).to be_a(Growwer::GetMe200Response)
    expect(me.buyer.balance.available.amount).to eq(250_000)
    expect(me.buyer.balance.available.currency).to eq('EUR')
    expect(me.seller.holiday_end_date).to be_nil
    expect(me.catalogue.eligible).to be(true)
    expect(me.catalogue.daily_cap).to eq(5000)
    expect(me.catalogue.remaining_today).to be_nil
    expect(me.mode).to eq('live')
  end

  it 'reads test mode and no seller from getMe with a test key' do
    me = Growwer::AccountApi.new(answer(200, fixture('me-test-key.json'))).get_me

    expect(me.mode).to eq('test')
    expect(me.seller).to be_nil
    expect(me.buyer.balance.available.amount).to eq(100_000)
    expect(me.catalogue.eligible).to be(true)
  end

  it 'lets the base URL be overridden' do
    Growwer::AccountApi.new(answer(200, fixture('me.json'), host: 'sandbox.example')).get_me

    expect(sent.url.to_s).to eq('https://sandbox.example/api/v1/me')
  end

  it 'reads items and total from listOrders, with both order types' do
    page = Growwer::BuyerOrdersApi.new(answer(200, fixture('orders-page.json'))).list_orders(limit: 2)

    expect(sent.url.query).to include('limit=2')
    expect(page).to be_a(Growwer::ListOrders200Response)
    expect(page.total).to eq(42)
    post, link_addition = page.items

    expect(post).to be_a(Growwer::Order)
    expect(post.type).to eq('post')
    expect(post.pending_action).to be_nil
    expect(post.delivery).to be_nil
    expect(post.draft).to be_nil
    expect(post.scheduled_publication_date).to be_nil
    expect(post.price.amount).to eq(12_500)
    expect(post.created_at).to eq(Time.utc(2026, 10, 1, 9, 30))
    expect(post.briefing).to be_a(Growwer::PostOrderBriefing)
    expect(post.briefing.title).to be_nil
    expect(post.briefing.links[0].type).to eq('dofollow')
    expect(post.state_history[0].reason).to be_nil
    expect(post.channel.created).to eq('api')

    expect(link_addition.type).to eq('link_addition')
    expect(link_addition.pending_action).to be_nil
    expect(link_addition.delivery).to be_nil
    expect(link_addition.draft).to be_nil
    expect(link_addition.project.id).to be_nil
    expect(link_addition.briefing).to be_a(Growwer::LinkAdditionOrderBriefing)
    expect(link_addition.briefing.link.anchor).to be_nil
    expect(link_addition.state_history[1].reason.code).to eq('no_seller_response')
    expect(link_addition.state_history[1].reason.additional_info).to be_nil
  end

  it 'still deserialises an order with fields this client does not know' do
    order = Growwer::BuyerOrdersApi.new(answer(200, fixture('order-with-unknown-field.json'))).get_order(ORDER_ID)

    expect(sent.url.path).to eq("/api/v1/orders/#{ORDER_ID}")
    expect(order.id).to eq(ORDER_ID)
    expect(order.pending_action).to eq('seller')
    expect(order.draft.has_file).to be(true)
    expect(order.channel.created).to eq('api')
    expect(order.briefing).to be_a(Growwer::PostOrderBriefing)
    expect(order.briefing.title).to eq('Choosing running shoes')
    expect(order.briefing.links[0].type).to eq('dofollow')
  end

  it 'still deserialises a link addition order with fields this client does not know' do
    order = Growwer::BuyerOrdersApi.new(answer(200, fixture('link-addition-order-with-unknown-field.json'))).get_order(ORDER_ID)

    expect(order.type).to eq('link_addition')
    expect(order.briefing).to be_a(Growwer::LinkAdditionOrderBriefing)
    expect(order.briefing.linking_from).to eq('https://blog.example/best-trails')
    expect(order.briefing.link.anchor).to eq('trail shoes')
    expect(order.briefing.link.type).to eq('nofollow')
  end

  it 'reads a catalogue media with a null previousPrice and linkAdditionOffer' do
    media = Growwer::CatalogueApi.new(answer(200, fixture('catalogue-media.json'))).get_catalogue_media(MEDIA_ID)

    expect(media).to be_a(Growwer::CatalogueMedia)
    expect(media.best_price).to be_nil
    expect(media.link_addition_offer).to be_nil
    expect(media.flash_offer).to be_nil
    expect(media.country).to be_nil
    expect(media.metrics.referring_domains).to be_nil
    expect(media.metrics.organic_traffic).to eq(15_400)
    expect(media.post_offer.price.amount).to eq(9000)
    expect(media.post_offer.previous_price).to be_nil
    expect(media.post_offer.prices['nofollow'].amount).to eq(7000)
    expect(media.post_offer.extras.homepage_listing).to be_nil
    expect(media.post_offer.extras.sensitive_topic.extra_price).to be_nil
  end

  it 'reads a catalogue media with a null linkType beside present offers' do
    media = Growwer::CatalogueApi.new(answer(200, fixture('catalogue-media-null-link-type.json')))
                                 .get_catalogue_media(MEDIA_ID)

    post_offer = media.post_offer
    expect(post_offer.link_type).to be_nil
    expect(post_offer.prices).to eq({})
    expect(post_offer.previous_price).to be_a(Growwer::MoneyOrNull)
    expect(post_offer.previous_price.amount).to eq(20_000)
    expect(post_offer.extras.homepage_listing.amount).to eq(2500)
    expect(post_offer.extras.sensitive_topic.extra_price.amount).to eq(3000)
    offer = media.link_addition_offer
    expect(offer).to be_a(Growwer::CatalogueOfferOrNull)
    expect(offer.link_type).to be_nil
    expect(offer.price.amount).to eq(6000)
    expect(offer.previous_price).to be_nil
  end

  it 'reads a catalogue media with its best-price badge' do
    media = Growwer::CatalogueApi.new(answer(200, fixture('catalogue-media-null-link-type.json')))
                                 .get_catalogue_media(MEDIA_ID)

    best_price = media.best_price
    expect(best_price).to be_a(Growwer::CatalogueMediaBestPrice)
    expect(best_price.badge).to eq('cheaper')
    expect(best_price.platform_count).to eq(3)
    expect(best_price.checked_on).to eq(Date.new(2026, 11, 12))
  end

  it 'sends the bestPrice filter of searchProjectMedias and reads an only_here badge' do
    page = Growwer::CatalogueApi.new(answer(200, fixture('project-medias-page.json')))
                                .search_project_medias(PROJECT_ID, best_price: true)

    expect(sent.url.path).to eq("/api/v1/projects/#{PROJECT_ID}/medias")
    expect(sent.url.query.split('&')).to include('bestPrice=true')
    media = page.items[0]
    expect(media).to be_a(Growwer::ProjectCatalogueMedia)
    expect(media.best_price).to be_a(Growwer::CatalogueMediaBestPrice)
    expect(media.best_price.badge).to eq('only_here')
    expect(media.best_price.platform_count).to eq(2)
    expect(media.best_price.checked_on).to eq(Date.new(2026, 11, 11))
  end

  it 'reads a project media without a badge as a nil bestPrice' do
    page = Growwer::CatalogueApi.new(answer(200, fixture('project-medias-page-no-badge.json')))
                                .search_project_medias(PROJECT_ID)

    expect(sent.url.query.to_s).not_to include('bestPrice')
    media = page.items[0]
    expect(media).to be_a(Growwer::ProjectCatalogueMedia)
    expect(media.best_price).to be_nil
    expect(media.domain).to eq('blog.example')
  end

  it 'reads a seller media with null competitiveFees' do
    media = Growwer::SellerMediasApi.new(answer(200, fixture('seller-media.json'))).get_seller_media(MEDIA_ID)

    expect(media).to be_a(Growwer::SellerMedia)
    expect(media.competitive_fees).to be_nil
    expect(media.competitive_fees_by_link_type).to be_nil
    expect(media.link_addition_offer).to be_nil
    option = media.post_offer.pricing_options[0]
    expect(option.fee_when_seller_writes_post.amount).to eq(6000)
    expect(option.fee_when_seller_does_not_write_post).to be_nil
    expect(option.current_cost).to be_nil
    expect(media.post_offer.extra_services[0].cost.amount).to eq(1500)
    expect(media.post_offer.extra_services[0].cost.amount_decimal).to eq('15.00')
  end

  it 'reads a seller media with competitiveFees that have one side null' do
    media = Growwer::SellerMediasApi.new(answer(200, fixture('seller-media-competitive-fees.json')))
                                    .get_seller_media(MEDIA_ID)

    expect(media.competitive_fees).to be_a(Growwer::SellerFeesOrNull)
    expect(media.competitive_fees.fee_when_seller_writes_post.amount).to eq(5400)
    expect(media.competitive_fees.fee_when_seller_does_not_write_post).to be_nil
  end

  it 'reads a seller media with competitiveFeesByLinkType per link type' do
    media = Growwer::SellerMediasApi.new(answer(200, fixture('seller-media-competitive-fees-by-link-type.json')))
                                    .get_seller_media(MEDIA_ID)

    fees = media.competitive_fees_by_link_type
    expect(fees.map(&:link_type)).to eq(%w[dofollow nofollow])
    expect(fees).to all(be_a(Growwer::SellerMediaCompetitiveFeesByLinkTypeInner))
    expect(fees[0].fee_when_seller_writes_post).to be_a(Growwer::MoneyOrNull)
    expect(fees[0].fee_when_seller_writes_post.amount).to eq(5400)
    expect(fees[0].fee_when_seller_writes_post.amount_decimal).to eq('54.00')
    expect(fees[0].fee_when_seller_does_not_write_post).to be_nil
    expect(fees[1].fee_when_seller_writes_post).to be_nil
    expect(fees[1].fee_when_seller_does_not_write_post.amount).to eq(3600)
    expect(fees[1].fee_when_seller_does_not_write_post.amount_decimal).to eq('36.00')
    expect(media.competitive_fees.fee_when_seller_writes_post.amount).to eq(5400)
    expect(media.competitive_fees.fee_when_seller_does_not_write_post.amount).to eq(3600)
  end

  it 'reads a saved_not_recommended warning from a seller media save' do
    saved = Growwer::SellerMediasApi.new(answer(200, fixture('seller-media-saved-not-recommended.json')))
                                    .update_seller_media(MEDIA_ID, 'key-1', Growwer::UpdateSellerMediaRequest.new)

    expect(saved).to be_a(Growwer::SellerMediaSaved)
    expect(saved.warnings.size).to eq(1)
    warning = saved.warnings[0]
    expect(warning).to be_a(Growwer::SellerMediaSavedAllOfWarnings)
    expect(warning.code).to eq('saved_not_recommended')
    expect(warning.details.competitive_fees.fee_when_seller_writes_post.amount).to eq(5400)
    expect(warning.details.competitive_fees.fee_when_seller_does_not_write_post).to be_nil
    expect(warning.details.competitors).to eq(['Prensalink'])
    expect(saved.domain).to eq('blog.example')
  end

  it 'makes the error envelope readable from the ApiError' do
    api = Growwer::CatalogueApi.new(
      answer(429, fixture('error.json'),
             { 'Content-Type' => 'application/json', 'Retry-After' => '3600', 'X-Request-Id' => '0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34' })
    )

    expect { api.get_catalogue_media(MEDIA_ID) }.to raise_error(Growwer::ApiError) do |error|
      expect(error.code).to eq(429)
      expect(error.response_headers['Retry-After']).to eq('3600')
      expect(error.response_headers['X-Request-Id']).to eq('0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34')
      envelope = Growwer::Error.build_from_hash(JSON.parse(error.response_body))
      expect(envelope.code).to eq('catalogue_daily_cap_reached')
      expect(envelope.request_id).to eq('0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34')
      expect(envelope.details).to eq('remaining' => 0)
    end
  end

  it 'returns the exact bytes of a binary download' do
    body = fixture('briefing.bin')
    client = answer(200, body,
                    { 'Content-Type' => 'application/octet-stream',
                      'Content-Disposition' => 'attachment; filename="briefing.docx"' })
    client.config.return_binary_data = true

    downloaded = Growwer::BuyerOrdersApi.new(client).download_order_briefing(ORDER_ID)

    expect(sent.url.path).to eq("/api/v1/orders/#{ORDER_ID}/briefing")
    expect(downloaded.b).to eq(body.b)
  end

  it 'parses an order event with fields this client does not know' do
    webhook_event = event('webhook-order-created.json')

    expect(webhook_event).to be_a(Growwer::WebhookEvent)
    expect(webhook_event.id).to eq('6a1f0c2e-3b4d-4e5f-8a9b-0c1d2e3f4a5b')
    expect(webhook_event.type).to eq('order.created')
    expect(webhook_event.mode).to eq('live')
    expect(webhook_event.api_version).to eq('v1')
    expect(webhook_event.created_at).to eq(Time.utc(2026, 10, 1, 9, 30, 5))
    expect(webhook_event.data).to be_a(Growwer::OrderEventData)
    order = webhook_event.data.order
    expect(order).to be_a(Growwer::Order)
    expect(order.id).to eq(ORDER_ID)
    expect(order.state).to eq('pending_acceptance')
    expect(order.price.amount).to eq(12_500)
    expect(order.briefing).to be_a(Growwer::PostOrderBriefing)
  end

  it 'parses a balance.low event with fields this client does not know' do
    webhook_event = event('webhook-balance-low.json')

    expect(webhook_event.type).to eq('balance.low')
    expect(webhook_event.mode).to eq('live')
    expect(webhook_event.data).to be_a(Growwer::BalanceLowEventData)
    expect(webhook_event.data.wallet.available_balance.amount).to eq(4500)
    expect(webhook_event.data.wallet.currency).to eq('EUR')
    expect(webhook_event.data.threshold.amount).to eq(5000)
  end

  it 'parses a webhook.test event with fields this client does not know' do
    webhook_event = event('webhook-test.json')

    expect(webhook_event.type).to eq('webhook.test')
    expect(webhook_event.mode).to eq('live')
    expect(webhook_event.data).to be_a(Growwer::WebhookTestEventData)
    expect(webhook_event.data.webhook_id).to eq(WEBHOOK_ID)
  end

  it 'sends the body and key of createWebhook and reads the secret' do
    request = Growwer::CreateWebhookRequest.new(
      url: 'https://hooks.shop.example/growwer',
      events: %w[order.created order.completed balance.low],
      low_balance_threshold: Growwer::Money.new(amount: 5000, currency: 'EUR')
    )

    webhook = Growwer::WebhooksApi.new(answer(201, fixture('webhook-with-secret.json'))).create_webhook('create-webhook-1', request)

    expect(sent.method).to eq(:post)
    expect(sent.url.to_s).to eq('https://tool.growwer.com/api/v1/webhooks')
    expect(sent.request_headers['Idempotency-Key']).to eq('create-webhook-1')
    expect(JSON.parse(sent.request_body)).to eq(
      'url' => 'https://hooks.shop.example/growwer',
      'events' => %w[order.created order.completed balance.low],
      'lowBalanceThreshold' => { 'amount' => 5000, 'currency' => 'EUR' }
    )
    expect(webhook).to be_a(Growwer::WebhookWithSecret)
    expect(webhook.id).to eq(WEBHOOK_ID)
    expect(webhook.secret).to start_with('whsec_')
    expect(webhook.events).to eq(%w[order.created order.completed balance.low])
    expect(webhook.low_balance_threshold.amount).to eq(5000)
    expect(webhook.enabled).to be(true)
    expect(webhook.disabled_reason).to be_nil
    expect(webhook.failing_since).to be_nil
  end

  it 'sends the amountDecimal of a Money it read back in updateWebhook' do
    read = Growwer::WebhooksApi.new(answer(200, fixture('webhook-with-secret.json')))
                               .rotate_webhook_secret(WEBHOOK_ID, 'rotate-webhook-1')
    threshold = read.low_balance_threshold
    expect(threshold.amount_decimal).to eq('50.00')

    Growwer::WebhooksApi.new(answer(200, fixture('webhook-with-secret.json')))
                        .update_webhook(WEBHOOK_ID, 'update-webhook-1',
                                        Growwer::UpdateWebhookRequest.new(low_balance_threshold: threshold))

    expect(sent.method).to eq(:patch)
    expect(sent.url.to_s).to eq("https://tool.growwer.com/api/v1/webhooks/#{WEBHOOK_ID}")
    expect(JSON.parse(sent.request_body)).to eq(
      'lowBalanceThreshold' => { 'amount' => 5000, 'currency' => 'EUR', 'amountDecimal' => '50.00' }
    )
  end
end
