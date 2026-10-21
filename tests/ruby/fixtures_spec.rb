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
  end

  it 'lets the base URL be overridden' do
    Growwer::AccountApi.new(answer(200, fixture('me.json'), host: 'sandbox.example')).get_me

    expect(sent.url.to_s).to eq('https://sandbox.example/api/v1/me')
  end

  it 'reads items and total from listOrders, with both order types' do
    page = Growwer::OrdersApi.new(answer(200, fixture('orders-page.json'))).list_orders(limit: 2)

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
    order = Growwer::OrdersApi.new(answer(200, fixture('order-with-unknown-field.json'))).get_order(ORDER_ID)

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
    order = Growwer::OrdersApi.new(answer(200, fixture('link-addition-order-with-unknown-field.json'))).get_order(ORDER_ID)

    expect(order.type).to eq('link_addition')
    expect(order.briefing).to be_a(Growwer::LinkAdditionOrderBriefing)
    expect(order.briefing.linking_from).to eq('https://blog.example/best-trails')
    expect(order.briefing.link.anchor).to eq('trail shoes')
    expect(order.briefing.link.type).to eq('nofollow')
  end

  it 'reads a catalogue media with a null previousPrice and linkAdditionOffer' do
    media = Growwer::CatalogueApi.new(answer(200, fixture('catalogue-media.json'))).get_catalogue_media(MEDIA_ID)

    expect(media).to be_a(Growwer::CatalogueMedia)
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

  it 'reads a seller media with null competitiveFees' do
    media = Growwer::SellerMediasApi.new(answer(200, fixture('seller-media.json'))).get_seller_media(MEDIA_ID)

    expect(media).to be_a(Growwer::SellerMedia)
    expect(media.competitive_fees).to be_nil
    expect(media.link_addition_offer).to be_nil
    option = media.post_offer.pricing_options[0]
    expect(option.fee_when_seller_writes_post.amount).to eq(6000)
    expect(option.fee_when_seller_does_not_write_post).to be_nil
    expect(option.current_cost).to be_nil
    expect(media.post_offer.extra_services[0].cost.amount).to eq(1500)
  end

  it 'reads a seller media with competitiveFees that have one side null' do
    media = Growwer::SellerMediasApi.new(answer(200, fixture('seller-media-competitive-fees.json')))
                                    .get_seller_media(MEDIA_ID)

    expect(media.competitive_fees).to be_a(Growwer::SellerFeesOrNull)
    expect(media.competitive_fees.fee_when_seller_writes_post.amount).to eq(5400)
    expect(media.competitive_fees.fee_when_seller_does_not_write_post).to be_nil
  end

  it 'makes the error envelope readable from the ApiError' do
    api = Growwer::CatalogueApi.new(
      answer(429, fixture('error.json'),
             { 'Content-Type' => 'application/json', 'Retry-After' => '3600', 'X-Request-Id' => '4f1c2a9e8b7d6c5e' })
    )

    expect { api.get_catalogue_media(MEDIA_ID) }.to raise_error(Growwer::ApiError) do |error|
      expect(error.code).to eq(429)
      expect(error.response_headers['Retry-After']).to eq('3600')
      expect(error.response_headers['X-Request-Id']).to eq('4f1c2a9e8b7d6c5e')
      envelope = Growwer::Error.build_from_hash(JSON.parse(error.response_body))
      expect(envelope.code).to eq('catalogue_daily_cap_reached')
      expect(envelope.request_id).to eq('4f1c2a9e8b7d6c5e')
      expect(envelope.details).to eq('remaining' => 0)
    end
  end

  it 'returns the exact bytes of a binary download' do
    body = fixture('briefing.bin')
    client = answer(200, body,
                    { 'Content-Type' => 'application/octet-stream',
                      'Content-Disposition' => 'attachment; filename="briefing.docx"' })
    client.config.return_binary_data = true

    downloaded = Growwer::OrdersApi.new(client).download_order_briefing(ORDER_ID)

    expect(sent.url.path).to eq("/api/v1/orders/#{ORDER_ID}/briefing")
    expect(downloaded.b).to eq(body.b)
  end
end
