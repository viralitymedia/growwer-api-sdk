// Deserialises the shared response fixtures through the generated TypeScript client, offline.
//
// Each call is answered from tests/fixtures/ by the client's own `fetchApi` hook, so the whole client
// path runs: URL, headers, status handling and the models. Compiled against the built package's
// type declarations, so a fixture field the generated types lack fails the compile, not only the run.

import {
  AccountApi,
  BuyerOrdersApi,
  CatalogueApi,
  CatalogueMediaBestPriceBadgeEnum,
  Configuration,
  ModelErrorFromJSON,
  ResponseError,
  SellerMediasApi,
  WebhookEventFromJSON,
  WebhooksApi,
} from '../../typescript/dist';
import type {
  BalanceLowEventData,
  CatalogueMediaBestPrice,
  LinkAdditionOrderBriefing,
  OrderEventData,
  PostOrderBriefing,
  SellerMediaCompetitiveFeesByLinkTypeInner,
  WebhookTestEventData,
} from '../../typescript/dist';

// Node globals, declared here so the test needs no @types/node beside the package's own toolchain.
declare function require(id: string): any;
declare const process: { exitCode?: number };
declare const __dirname: string;

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const FIXTURES = path.join(__dirname, '..', 'fixtures');
const MEDIA_ID = 'c1d2e3f4-a5b6-4c7d-8e9f-a0b1c2d3e4f5';
const ORDER_ID = '0b9c6a4e-6f1d-4c39-9a51-2f5d7c1e8a01';
const PROJECT_ID = '5e0c2b7a-3d4f-4a1b-9c8d-7e6f5a4b3c2d';
const WEBHOOK_ID = '9d4c3f5b-6e7a-4b82-9d2e-3f4a5b6c7d8e';
const POST_BRIEFING_FIELDS = ['additionalInfo', 'extraServices', 'hasProposedDraft', 'language', 'links', 'title'];

function fixture(name: string): Uint8Array {
  return new Uint8Array(fs.readFileSync(path.join(FIXTURES, name)));
}

function fixtureJson(name: string): unknown {
  return JSON.parse(fs.readFileSync(path.join(FIXTURES, name), 'utf8'));
}

interface Sent {
  url: string;
  method?: string;
  headers: Record<string, string>;
  body?: unknown;
}

// A configuration whose every call is answered with one canned response, recording what was sent.
function answer(
  sent: Sent[],
  status: number,
  body: Uint8Array,
  headers: Record<string, string> = { 'Content-Type': 'application/json' },
  basePath?: string,
): Configuration {
  return new Configuration({
    basePath,
    accessToken: 'test-key',
    fetchApi: async (url: RequestInfo | URL, init?: RequestInit) => {
      sent.push({
        url: String(url),
        method: init?.method,
        headers: (init?.headers ?? {}) as Record<string, string>,
        body: init?.body,
      });
      // TypeScript 5.7+ types a Node buffer view as Uint8Array<ArrayBufferLike>, which BodyInit omits.
      return new Response(body as unknown as BodyInit, { status, headers });
    },
  });
}

const tests: Array<[string, () => Promise<void>]> = [
  ['getMe calls production with the bearer key', async () => {
    const sent: Sent[] = [];
    const me = await new AccountApi(answer(sent, 200, fixture('me.json'))).getMe();

    assert.equal(sent.length, 1);
    assert.equal(sent[0].url, 'https://tool.growwer.com/api/v1/me');
    assert.equal(sent[0].headers.Authorization, 'Bearer test-key');
    assert.equal(me.buyer.balance.available.amount, 250000);
    assert.equal(me.buyer.balance.available.currency, 'EUR');
    assert.notEqual(me.seller, null);
    assert.equal(me.seller!.holidayEndDate, null);
    assert.equal(me.catalogue.eligible, true);
    assert.equal(me.catalogue.dailyCap, 5000);
    assert.equal(me.catalogue.remainingToday, null);
    assert.equal(me.mode, 'live');
  }],

  ['getMe with a test key reads test mode and no seller', async () => {
    const sent: Sent[] = [];
    const me = await new AccountApi(answer(sent, 200, fixture('me-test-key.json'))).getMe();

    assert.equal(me.mode, 'test');
    assert.equal(me.seller, null);
    assert.equal(me.buyer.balance.available.amount, 100000);
    assert.equal(me.catalogue.eligible, true);
  }],

  ['the base URL is overridable', async () => {
    const sent: Sent[] = [];
    const config = answer(sent, 200, fixture('me.json'), undefined, 'https://sandbox.example');
    await new AccountApi(config).getMe();

    assert.equal(sent[0].url, 'https://sandbox.example/api/v1/me');
  }],

  ['listOrders reads items and total, with both order types', async () => {
    const sent: Sent[] = [];
    const page = await new BuyerOrdersApi(answer(sent, 200, fixture('orders-page.json'))).listOrders({ limit: 2 });

    assert.ok(sent[0].url.includes('limit=2'), sent[0].url);
    assert.equal(page.total, 42);
    assert.equal(page.items.length, 2);
    const [post, linkAddition] = page.items;

    assert.equal(post.type, 'post');
    assert.equal(post.pendingAction, null);
    assert.equal(post.delivery, null);
    assert.equal(post.draft, null);
    assert.equal(post.scheduledPublicationDate, null);
    assert.equal(post.price.amount, 12500);
    assert.ok(post.createdAt instanceof Date);
    assert.equal(post.createdAt.toISOString(), '2026-10-01T09:30:00.000Z');
    const postBriefing = post.briefing as PostOrderBriefing;
    assert.equal(postBriefing.title, null);
    assert.equal(postBriefing.links[0].type, 'dofollow');
    assert.equal(post.stateHistory[0].reason, null);
    assert.equal(post.channel.created, 'api');

    assert.equal(linkAddition.type, 'link_addition');
    assert.equal(linkAddition.pendingAction, null);
    assert.equal(linkAddition.delivery, null);
    assert.equal(linkAddition.draft, null);
    assert.equal(linkAddition.project.id, null);
    const linkBriefing = linkAddition.briefing as LinkAdditionOrderBriefing;
    assert.equal(linkBriefing.linkingFrom, 'https://blog.example/best-trails');
    assert.equal(linkBriefing.link.anchor, null);
    assert.equal(linkAddition.stateHistory[1].reason?.code, 'no_seller_response');
    assert.equal(linkAddition.stateHistory[1].reason?.additionalInfo, null);
  }],

  ['an order with fields this client does not know still deserialises', async () => {
    const sent: Sent[] = [];
    const order = await new BuyerOrdersApi(answer(sent, 200, fixture('order-with-unknown-field.json')))
      .getOrder({ id: ORDER_ID });

    assert.ok(sent[0].url.endsWith(`/api/v1/orders/${ORDER_ID}`), sent[0].url);
    assert.equal(order.id, ORDER_ID);
    assert.equal(order.pendingAction, 'seller');
    assert.equal(order.draft?.hasFile, true);
    assert.equal(order.channel.created, 'api');
    // Read through the post member, which keeps only the fields it declares.
    assert.deepEqual(Object.keys(order.briefing).sort(), POST_BRIEFING_FIELDS);
    const briefing = order.briefing as PostOrderBriefing;
    assert.equal(briefing.title, 'Choosing running shoes');
    assert.deepEqual(Object.keys(briefing.links[0]).sort(), ['anchor', 'targetUrl', 'type']);
    assert.equal(briefing.links[0].type, 'dofollow');
  }],

  ['a link addition order with fields this client does not know still deserialises', async () => {
    const sent: Sent[] = [];
    const order = await new BuyerOrdersApi(answer(sent, 200, fixture('link-addition-order-with-unknown-field.json')))
      .getOrder({ id: ORDER_ID });

    assert.equal(order.type, 'link_addition');
    // Read through the link addition member, which keeps only the fields it declares.
    assert.deepEqual(Object.keys(order.briefing).sort(), ['additionalInfo', 'link', 'linkingFrom']);
    const briefing = order.briefing as LinkAdditionOrderBriefing;
    assert.equal(briefing.linkingFrom, 'https://blog.example/best-trails');
    assert.deepEqual(Object.keys(briefing.link).sort(), ['anchor', 'targetUrl', 'type']);
    assert.equal(briefing.link.anchor, 'trail shoes');
    assert.equal(briefing.link.type, 'nofollow');
  }],

  ['a catalogue media reads a null previousPrice and linkAdditionOffer', async () => {
    const sent: Sent[] = [];
    const media = await new CatalogueApi(answer(sent, 200, fixture('catalogue-media.json')))
      .getCatalogueMedia({ id: MEDIA_ID });

    assert.equal(media.bestPrice, null);
    assert.equal(media.linkAdditionOffer, null);
    assert.equal(media.flashOffer, null);
    assert.equal(media.country, null);
    assert.equal(media.metrics.referringDomains, null);
    assert.equal(media.metrics.organicTraffic, 15400);
    assert.equal(media.postOffer.price.amount, 9000);
    assert.equal(media.postOffer.previousPrice, null);
    assert.equal(media.postOffer.prices.nofollow.amount, 7000);
    assert.equal(media.postOffer.extras.homepageListing, null);
    assert.equal(media.postOffer.extras.sensitiveTopic.extraPrice, null);
  }],

  ['a catalogue media reads a null linkType beside present offers', async () => {
    const sent: Sent[] = [];
    const media = await new CatalogueApi(answer(sent, 200, fixture('catalogue-media-null-link-type.json')))
      .getCatalogueMedia({ id: MEDIA_ID });

    assert.equal(media.postOffer.linkType, null);
    assert.deepEqual(media.postOffer.prices, {});
    assert.equal(media.postOffer.previousPrice?.amount, 20000);
    assert.equal(media.postOffer.extras.homepageListing?.amount, 2500);
    assert.equal(media.postOffer.extras.sensitiveTopic.extraPrice?.amount, 3000);
    const offer = media.linkAdditionOffer;
    assert.notEqual(offer, null);
    assert.equal(offer!.linkType, null);
    assert.equal(offer!.price.amount, 6000);
    assert.equal(offer!.previousPrice, null);
  }],

  ['a catalogue media reads its best-price badge', async () => {
    const sent: Sent[] = [];
    const media = await new CatalogueApi(answer(sent, 200, fixture('catalogue-media-null-link-type.json')))
      .getCatalogueMedia({ id: MEDIA_ID });

    const bestPrice: CatalogueMediaBestPrice | null = media.bestPrice;
    assert.notEqual(bestPrice, null);
    assert.equal(bestPrice!.badge, CatalogueMediaBestPriceBadgeEnum.Cheaper);
    assert.equal(bestPrice!.platformCount, 3);
    assert.equal(bestPrice!.checkedOn.toISOString().slice(0, 10), '2026-11-12');
  }],

  ['searchProjectMedias sends the bestPrice filter and reads an only_here badge', async () => {
    const sent: Sent[] = [];
    const page = await new CatalogueApi(answer(sent, 200, fixture('project-medias-page.json')))
      .searchProjectMedias({ id: PROJECT_ID, bestPrice: true });

    const url = new URL(sent[0].url);
    assert.equal(url.pathname, `/api/v1/projects/${PROJECT_ID}/medias`);
    assert.equal(url.searchParams.get('bestPrice'), 'true');
    assert.equal(page.items[0].bestPrice?.badge, CatalogueMediaBestPriceBadgeEnum.OnlyHere);
    assert.equal(page.items[0].bestPrice?.platformCount, 2);
  }],

  ['a project media without a badge reads a null bestPrice', async () => {
    const sent: Sent[] = [];
    const page = await new CatalogueApi(answer(sent, 200, fixture('project-medias-page-no-badge.json')))
      .searchProjectMedias({ id: PROJECT_ID });

    assert.equal(new URL(sent[0].url).searchParams.has('bestPrice'), false);
    assert.equal(page.items[0].bestPrice, null);
    assert.equal(page.items[0].domain, 'blog.example');
  }],

  ['a seller media reads null competitiveFees', async () => {
    const sent: Sent[] = [];
    const media = await new SellerMediasApi(answer(sent, 200, fixture('seller-media.json')))
      .getSellerMedia({ id: MEDIA_ID });

    assert.equal(media.competitiveFees, null);
    assert.equal(media.competitiveFeesByLinkType, null);
    assert.equal(media.linkAdditionOffer, null);
    const option = media.postOffer.pricingOptions[0];
    assert.equal(option.feeWhenSellerWritesPost?.amount, 6000);
    assert.equal(option.feeWhenSellerDoesNotWritePost, null);
    assert.equal(option.currentCost, null);
    assert.equal(media.postOffer.extraServices[0].cost.amount, 1500);
    assert.equal(media.postOffer.extraServices[0].cost.amountDecimal, '15.00');
  }],

  ['a seller media reads competitiveFees with one side null', async () => {
    const sent: Sent[] = [];
    const media = await new SellerMediasApi(answer(sent, 200, fixture('seller-media-competitive-fees.json')))
      .getSellerMedia({ id: MEDIA_ID });

    assert.notEqual(media.competitiveFees, null);
    assert.equal(media.competitiveFees!.feeWhenSellerWritesPost?.amount, 5400);
    assert.equal(media.competitiveFees!.feeWhenSellerDoesNotWritePost, null);
  }],

  ['a seller media reads competitiveFeesByLinkType per link type', async () => {
    const sent: Sent[] = [];
    const media = await new SellerMediasApi(answer(sent, 200, fixture('seller-media-competitive-fees-by-link-type.json')))
      .getSellerMedia({ id: MEDIA_ID });

    const fees: SellerMediaCompetitiveFeesByLinkTypeInner[] | null = media.competitiveFeesByLinkType;
    assert.notEqual(fees, null);
    assert.deepEqual(fees!.map((entry) => entry.linkType), ['dofollow', 'nofollow']);
    assert.equal(fees![0].feeWhenSellerWritesPost?.amount, 5400);
    assert.equal(fees![0].feeWhenSellerWritesPost?.amountDecimal, '54.00');
    assert.equal(fees![0].feeWhenSellerDoesNotWritePost, null);
    assert.equal(fees![1].feeWhenSellerWritesPost, null);
    assert.equal(fees![1].feeWhenSellerDoesNotWritePost?.amount, 3600);
    assert.equal(fees![1].feeWhenSellerDoesNotWritePost?.amountDecimal, '36.00');
    assert.equal(media.competitiveFees?.feeWhenSellerWritesPost?.amount, 5400);
    assert.equal(media.competitiveFees?.feeWhenSellerDoesNotWritePost?.amount, 3600);
  }],

  ['an order event parses with fields this client does not know', async () => {
    const event = WebhookEventFromJSON(fixtureJson('webhook-order-created.json'));

    assert.equal(event.id, '6a1f0c2e-3b4d-4e5f-8a9b-0c1d2e3f4a5b');
    assert.equal(event.type, 'order.created');
    assert.equal(event.mode, 'live');
    assert.equal(event.apiVersion, 'v1');
    assert.equal(event.createdAt.toISOString(), '2026-10-01T09:30:05.000Z');
    // Read through the order member, which keeps only the fields it declares.
    assert.deepEqual(Object.keys(event.data), ['order']);
    const data = event.data as OrderEventData;
    assert.equal(data.order.id, ORDER_ID);
    assert.equal(data.order.state, 'pending_acceptance');
    assert.equal(data.order.price.amount, 12500);
    assert.equal((data.order.briefing as PostOrderBriefing).title, 'Choosing running shoes');
  }],

  ['a balance.low event parses with fields this client does not know', async () => {
    const event = WebhookEventFromJSON(fixtureJson('webhook-balance-low.json'));

    assert.equal(event.type, 'balance.low');
    assert.equal(event.mode, 'live');
    assert.deepEqual(Object.keys(event.data).sort(), ['threshold', 'wallet']);
    const data = event.data as BalanceLowEventData;
    assert.equal(data.wallet.availableBalance.amount, 4500);
    assert.equal(data.wallet.currency, 'EUR');
    assert.equal(data.threshold.amount, 5000);
  }],

  ['a webhook.test event parses with fields this client does not know', async () => {
    const event = WebhookEventFromJSON(fixtureJson('webhook-test.json'));

    assert.equal(event.type, 'webhook.test');
    assert.equal(event.mode, 'live');
    assert.deepEqual(Object.keys(event.data), ['webhookId']);
    assert.equal((event.data as WebhookTestEventData).webhookId, WEBHOOK_ID);
  }],

  ['createWebhook sends the body and key and reads the secret', async () => {
    const sent: Sent[] = [];
    const webhook = await new WebhooksApi(answer(sent, 201, fixture('webhook-with-secret.json'))).createWebhook({
      idempotencyKey: 'create-webhook-1',
      createWebhookRequest: {
        url: 'https://hooks.shop.example/growwer',
        events: new Set(['order.created', 'order.completed', 'balance.low'] as const),
        lowBalanceThreshold: { amount: 5000, currency: 'EUR' },
      },
    });

    assert.equal(sent.length, 1);
    assert.equal(sent[0].method, 'POST');
    assert.equal(sent[0].url, 'https://tool.growwer.com/api/v1/webhooks');
    assert.equal(sent[0].headers['Idempotency-Key'], 'create-webhook-1');
    assert.deepEqual(JSON.parse(String(sent[0].body)), {
      url: 'https://hooks.shop.example/growwer',
      events: ['order.created', 'order.completed', 'balance.low'],
      lowBalanceThreshold: { amount: 5000, currency: 'EUR' },
    });
    assert.equal(webhook.id, WEBHOOK_ID);
    assert.ok(webhook.secret?.startsWith('whsec_'), webhook.secret);
    assert.deepEqual(webhook.events, ['order.created', 'order.completed', 'balance.low']);
    assert.equal(webhook.lowBalanceThreshold?.amount, 5000);
    assert.equal(webhook.enabled, true);
    assert.equal(webhook.disabledReason, null);
    assert.equal(webhook.failingSince, null);
  }],

  ['updateWebhook leaves out the amountDecimal of a Money it read', async () => {
    const read = await new WebhooksApi(answer([], 200, fixture('webhook-with-secret.json')))
      .rotateWebhookSecret({ id: WEBHOOK_ID, idempotencyKey: 'rotate-webhook-1' });
    const threshold = read.lowBalanceThreshold;
    assert.equal(threshold?.amountDecimal, '50.00');

    const sent: Sent[] = [];
    await new WebhooksApi(answer(sent, 200, fixture('webhook-with-secret.json'))).updateWebhook({
      id: WEBHOOK_ID,
      idempotencyKey: 'update-webhook-1',
      updateWebhookRequest: { lowBalanceThreshold: threshold },
    });

    assert.equal(sent.length, 1);
    assert.equal(sent[0].method, 'PATCH');
    assert.equal(sent[0].url, `https://tool.growwer.com/api/v1/webhooks/${WEBHOOK_ID}`);
    assert.deepEqual(JSON.parse(String(sent[0].body)), {
      lowBalanceThreshold: { amount: 5000, currency: 'EUR' },
    });
  }],

  ['the error envelope is readable from the ResponseError', async () => {
    const sent: Sent[] = [];
    const api = new CatalogueApi(answer(sent, 429, fixture('error.json'), {
      'Content-Type': 'application/json',
      'Retry-After': '3600',
      'X-Request-Id': '0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34',
    }));

    const error = await api.getCatalogueMedia({ id: MEDIA_ID }).then(
      () => assert.fail('a 429 must reject'),
      (rejection: unknown) => rejection,
    );

    assert.ok(error instanceof ResponseError, String(error));
    const response = (error as ResponseError).response;
    assert.equal(response.status, 429);
    assert.equal(response.headers.get('Retry-After'), '3600');
    assert.equal(response.headers.get('X-Request-Id'), '0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34');
    const envelope = ModelErrorFromJSON(await response.json());
    assert.equal(envelope.code, 'catalogue_daily_cap_reached');
    assert.equal(envelope.requestId, '0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34');
    assert.deepEqual(envelope.details, { remaining: 0 });
  }],

  ['a binary download returns the exact bytes', async () => {
    const sent: Sent[] = [];
    const body = fixture('briefing.bin');
    const blob = await new BuyerOrdersApi(answer(sent, 200, body, {
      'Content-Type': 'application/octet-stream',
      'Content-Disposition': 'attachment; filename="briefing.docx"',
    })).downloadOrderBriefing({ id: ORDER_ID });

    assert.ok(sent[0].url.endsWith(`/api/v1/orders/${ORDER_ID}/briefing`), sent[0].url);
    assert.deepEqual(new Uint8Array(await blob.arrayBuffer()), body);
  }],
];

async function main(): Promise<void> {
  for (const [name, test] of tests) {
    await test();
    console.log(`ok - ${name}`);
  }
  console.log(`${tests.length} fixture tests passed`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
