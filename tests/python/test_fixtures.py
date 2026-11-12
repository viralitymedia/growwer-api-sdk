"""Deserialises the shared response fixtures through the generated Python client, offline.

Each test answers one call from tests/fixtures/ in place of the network, at the urllib3 pool the
client sends through, so the whole client path runs: URL, headers, status handling and the models.
"""

import datetime
import json
import pathlib
import unittest
import uuid

import urllib3

from growwer import ApiClient, Configuration
from growwer.api import AccountApi, BuyerOrdersApi, CatalogueApi, SellerMediasApi, WebhooksApi
from growwer.exceptions import ApiException
from growwer.models import (
    BalanceLowEventData,
    CatalogueMedia,
    CatalogueOfferOrNull,
    CreateWebhookRequest,
    Error,
    GetMe200Response,
    LinkAdditionOrderBriefing,
    ListOrders200Response,
    Money,
    Order,
    OrderEventData,
    PostOrderBriefing,
    MoneyOrNull,
    SellerFeesOrNull,
    SellerMedia,
    SellerMediaCompetitiveFeesByLinkTypeInner,
    UpdateWebhookRequest,
    WebhookEvent,
    WebhookTestEventData,
    WebhookWithSecret,
)

FIXTURES = pathlib.Path(__file__).resolve().parent.parent / "fixtures"
MEDIA_ID = uuid.UUID("c1d2e3f4-a5b6-4c7d-8e9f-a0b1c2d3e4f5")
ORDER_ID = uuid.UUID("0b9c6a4e-6f1d-4c39-9a51-2f5d7c1e8a01")
WEBHOOK_ID = uuid.UUID("9d4c3f5b-6e7a-4b82-9d2e-3f4a5b6c7d8e")


def fixture(name):
    return (FIXTURES / name).read_bytes()


class FakePool:
    """Stands in for urllib3.PoolManager: records the request and returns one canned response."""

    def __init__(self, status, body, headers):
        self.response = urllib3.HTTPResponse(
            body=body, status=status, headers=headers, preload_content=True
        )
        self.requests = []
        self.bodies = []

    def request(self, method, url, **kwargs):
        self.requests.append((method, url, kwargs.get("headers", {})))
        self.bodies.append(kwargs.get("body"))
        return self.response


class FixtureTest(unittest.TestCase):
    def client(self, status, body, content_type="application/json", headers=None):
        client = ApiClient(Configuration(access_token="test-key"))
        self.pool = FakePool(status, body, {"Content-Type": content_type, **(headers or {})})
        client.rest_client.pool_manager = self.pool
        return client

    def sent(self):
        self.assertEqual(len(self.pool.requests), 1)
        return self.pool.requests[0]

    def test_get_me_calls_production_with_bearer_key(self):
        me = AccountApi(self.client(200, fixture("me.json"))).get_me()

        method, url, headers = self.sent()
        self.assertEqual(method, "GET")
        self.assertEqual(url, "https://tool.growwer.com/api/v1/me")
        self.assertEqual(headers["Authorization"], "Bearer test-key")
        self.assertIsInstance(me, GetMe200Response)
        self.assertEqual(me.buyer.balance.available.amount, 250000)
        self.assertEqual(me.buyer.balance.available.currency, "EUR")
        self.assertIsNone(me.seller.holiday_end_date)
        self.assertTrue(me.catalogue.eligible)
        self.assertEqual(me.catalogue.daily_cap, 5000)
        self.assertIsNone(me.catalogue.remaining_today)
        self.assertEqual(me.mode, "live")

    def test_get_me_with_a_test_key_reads_test_mode_and_no_seller(self):
        me = AccountApi(self.client(200, fixture("me-test-key.json"))).get_me()

        self.assertIsInstance(me, GetMe200Response)
        self.assertEqual(me.mode, "test")
        self.assertIsNone(me.seller)
        self.assertEqual(me.buyer.balance.available.amount, 100000)
        self.assertTrue(me.catalogue.eligible)

    def test_base_url_is_overridable(self):
        client = ApiClient(Configuration(host="https://sandbox.example", access_token="test-key"))
        self.pool = FakePool(200, fixture("me.json"), {"Content-Type": "application/json"})
        client.rest_client.pool_manager = self.pool

        AccountApi(client).get_me()

        self.assertEqual(self.sent()[1], "https://sandbox.example/api/v1/me")

    def test_list_orders_reads_items_and_total_with_both_order_types(self):
        page = BuyerOrdersApi(self.client(200, fixture("orders-page.json"))).list_orders(limit=2)

        self.assertIn("limit=2", self.sent()[1])
        self.assertIsInstance(page, ListOrders200Response)
        self.assertEqual(page.total, 42)
        post, link_addition = page.items

        self.assertIsInstance(post, Order)
        self.assertEqual(post.type, "post")
        self.assertIsNone(post.pending_action)
        self.assertIsNone(post.delivery)
        self.assertIsNone(post.draft)
        self.assertIsNone(post.scheduled_publication_date)
        self.assertEqual(post.price.amount, 12500)
        self.assertEqual(post.created_at, datetime.datetime(2026, 10, 1, 9, 30, tzinfo=datetime.timezone.utc))
        self.assertIsInstance(post.briefing.actual_instance, PostOrderBriefing)
        self.assertIsNone(post.briefing.actual_instance.title)
        self.assertEqual(post.briefing.actual_instance.links[0].type, "dofollow")
        self.assertIsNone(post.state_history[0].reason)
        self.assertEqual(post.channel.created, "api")

        self.assertEqual(link_addition.type, "link_addition")
        self.assertIsNone(link_addition.pending_action)
        self.assertIsNone(link_addition.delivery)
        self.assertIsNone(link_addition.draft)
        self.assertIsNone(link_addition.project.id)
        self.assertIsInstance(link_addition.briefing.actual_instance, LinkAdditionOrderBriefing)
        self.assertIsNone(link_addition.briefing.actual_instance.link.anchor)
        self.assertEqual(link_addition.state_history[1].reason.code, "no_seller_response")
        self.assertIsNone(link_addition.state_history[1].reason.additional_info)

    def test_order_with_fields_this_client_does_not_know_still_deserialises(self):
        order = BuyerOrdersApi(self.client(200, fixture("order-with-unknown-field.json"))).get_order(ORDER_ID)

        self.assertTrue(self.sent()[1].endswith(f"/api/v1/orders/{ORDER_ID}"))
        self.assertEqual(order.id, ORDER_ID)
        self.assertEqual(order.pending_action, "seller")
        self.assertTrue(order.draft.has_file)
        self.assertEqual(order.channel.created, "api")
        self.assertIsInstance(order.briefing.actual_instance, PostOrderBriefing)
        self.assertEqual(order.briefing.actual_instance.title, "Choosing running shoes")
        self.assertEqual(order.briefing.actual_instance.links[0].type, "dofollow")

    def test_link_addition_order_with_fields_this_client_does_not_know_still_deserialises(self):
        order = BuyerOrdersApi(
            self.client(200, fixture("link-addition-order-with-unknown-field.json"))
        ).get_order(ORDER_ID)

        self.assertEqual(order.type, "link_addition")
        briefing = order.briefing.actual_instance
        self.assertIsInstance(briefing, LinkAdditionOrderBriefing)
        self.assertEqual(briefing.linking_from, "https://blog.example/best-trails")
        self.assertEqual(briefing.link.anchor, "trail shoes")
        self.assertEqual(briefing.link.type, "nofollow")

    def test_catalogue_media_reads_null_previous_price_and_link_addition_offer(self):
        media = CatalogueApi(self.client(200, fixture("catalogue-media.json"))).get_catalogue_media(MEDIA_ID)

        self.assertIsInstance(media, CatalogueMedia)
        self.assertIsNone(media.link_addition_offer)
        self.assertIsNone(media.flash_offer)
        self.assertIsNone(media.country)
        self.assertIsNone(media.metrics.referring_domains)
        self.assertEqual(media.metrics.organic_traffic, 15400)
        self.assertEqual(media.post_offer.price.amount, 9000)
        self.assertIsNone(media.post_offer.previous_price)
        self.assertEqual(media.post_offer.prices["nofollow"].amount, 7000)
        self.assertIsNone(media.post_offer.extras.homepage_listing)
        self.assertIsNone(media.post_offer.extras.sensitive_topic.extra_price)

    def test_catalogue_media_reads_null_link_type_beside_present_offers(self):
        media = CatalogueApi(
            self.client(200, fixture("catalogue-media-null-link-type.json"))
        ).get_catalogue_media(MEDIA_ID)

        self.assertIsNone(media.post_offer.link_type)
        self.assertEqual(media.post_offer.prices, {})
        self.assertIsInstance(media.post_offer.previous_price, MoneyOrNull)
        self.assertEqual(media.post_offer.previous_price.amount, 20000)
        self.assertEqual(media.post_offer.extras.homepage_listing.amount, 2500)
        self.assertEqual(media.post_offer.extras.sensitive_topic.extra_price.amount, 3000)
        offer = media.link_addition_offer
        self.assertIsInstance(offer, CatalogueOfferOrNull)
        self.assertIsNone(offer.link_type)
        self.assertEqual(offer.price.amount, 6000)
        self.assertIsNone(offer.previous_price)

    def test_seller_media_reads_null_competitive_fees(self):
        media = SellerMediasApi(self.client(200, fixture("seller-media.json"))).get_seller_media(MEDIA_ID)

        self.assertIsInstance(media, SellerMedia)
        self.assertIsNone(media.competitive_fees)
        self.assertIsNone(media.competitive_fees_by_link_type)
        self.assertIsNone(media.link_addition_offer)
        option = media.post_offer.pricing_options[0]
        self.assertEqual(option.fee_when_seller_writes_post.amount, 6000)
        self.assertIsNone(option.fee_when_seller_does_not_write_post)
        self.assertIsNone(option.current_cost)
        self.assertEqual(media.post_offer.extra_services[0].cost.amount, 1500)
        self.assertEqual(media.post_offer.extra_services[0].cost.amount_decimal, "15.00")

    def test_seller_media_reads_competitive_fees_with_one_side_null(self):
        media = SellerMediasApi(
            self.client(200, fixture("seller-media-competitive-fees.json"))
        ).get_seller_media(MEDIA_ID)

        self.assertIsInstance(media.competitive_fees, SellerFeesOrNull)
        self.assertEqual(media.competitive_fees.fee_when_seller_writes_post.amount, 5400)
        self.assertIsNone(media.competitive_fees.fee_when_seller_does_not_write_post)

    def test_seller_media_reads_competitive_fees_per_link_type(self):
        media = SellerMediasApi(
            self.client(200, fixture("seller-media-competitive-fees-by-link-type.json"))
        ).get_seller_media(MEDIA_ID)

        fees = media.competitive_fees_by_link_type
        self.assertEqual([entry.link_type for entry in fees], ["dofollow", "nofollow"])
        self.assertIsInstance(fees[0], SellerMediaCompetitiveFeesByLinkTypeInner)
        self.assertIsInstance(fees[0].fee_when_seller_writes_post, MoneyOrNull)
        self.assertEqual(fees[0].fee_when_seller_writes_post.amount, 5400)
        self.assertEqual(fees[0].fee_when_seller_writes_post.amount_decimal, "54.00")
        self.assertIsNone(fees[0].fee_when_seller_does_not_write_post)
        self.assertIsNone(fees[1].fee_when_seller_writes_post)
        self.assertEqual(fees[1].fee_when_seller_does_not_write_post.amount, 3600)
        self.assertEqual(fees[1].fee_when_seller_does_not_write_post.amount_decimal, "36.00")
        self.assertEqual(media.competitive_fees.fee_when_seller_writes_post.amount, 5400)
        self.assertEqual(media.competitive_fees.fee_when_seller_does_not_write_post.amount, 3600)

    def test_order_event_parses_with_fields_this_client_does_not_know(self):
        event = WebhookEvent.from_json(fixture("webhook-order-created.json"))

        self.assertEqual(event.id, uuid.UUID("6a1f0c2e-3b4d-4e5f-8a9b-0c1d2e3f4a5b"))
        self.assertEqual(event.type, "order.created")
        self.assertEqual(event.mode, "live")
        self.assertEqual(event.api_version, "v1")
        self.assertEqual(event.created_at, datetime.datetime(2026, 10, 1, 9, 30, 5, tzinfo=datetime.timezone.utc))
        data = event.data.actual_instance
        self.assertIsInstance(data, OrderEventData)
        self.assertIsInstance(data.order, Order)
        self.assertEqual(data.order.id, ORDER_ID)
        self.assertEqual(data.order.state, "pending_acceptance")
        self.assertEqual(data.order.price.amount, 12500)
        self.assertIsInstance(data.order.briefing.actual_instance, PostOrderBriefing)

    def test_balance_low_event_parses_with_fields_this_client_does_not_know(self):
        event = WebhookEvent.from_json(fixture("webhook-balance-low.json"))

        self.assertEqual(event.type, "balance.low")
        self.assertEqual(event.mode, "live")
        data = event.data.actual_instance
        self.assertIsInstance(data, BalanceLowEventData)
        self.assertEqual(data.wallet.available_balance.amount, 4500)
        self.assertEqual(data.wallet.currency, "EUR")
        self.assertEqual(data.threshold.amount, 5000)

    def test_webhook_test_event_parses_with_fields_this_client_does_not_know(self):
        event = WebhookEvent.from_json(fixture("webhook-test.json"))

        self.assertEqual(event.type, "webhook.test")
        self.assertEqual(event.mode, "live")
        data = event.data.actual_instance
        self.assertIsInstance(data, WebhookTestEventData)
        self.assertEqual(data.webhook_id, WEBHOOK_ID)

    def test_create_webhook_sends_the_body_and_key_and_reads_the_secret(self):
        api = WebhooksApi(self.client(201, fixture("webhook-with-secret.json")))

        webhook = api.create_webhook(
            "create-webhook-1",
            CreateWebhookRequest(
                url="https://hooks.shop.example/growwer",
                events=["order.created", "order.completed", "balance.low"],
                low_balance_threshold=Money(amount=5000, currency="EUR"),
            ),
        )

        method, url, headers = self.sent()
        self.assertEqual(method, "POST")
        self.assertEqual(url, "https://tool.growwer.com/api/v1/webhooks")
        self.assertEqual(headers["Idempotency-Key"], "create-webhook-1")
        self.assertEqual(
            json.loads(self.pool.bodies[0]),
            {
                "url": "https://hooks.shop.example/growwer",
                "events": ["order.created", "order.completed", "balance.low"],
                "lowBalanceThreshold": {"amount": 5000, "currency": "EUR"},
            },
        )
        self.assertIsInstance(webhook, WebhookWithSecret)
        self.assertEqual(webhook.id, WEBHOOK_ID)
        self.assertTrue(webhook.secret.startswith("whsec_"))
        self.assertEqual(webhook.events, ["order.created", "order.completed", "balance.low"])
        self.assertEqual(webhook.low_balance_threshold.amount, 5000)
        self.assertTrue(webhook.enabled)
        self.assertIsNone(webhook.disabled_reason)
        self.assertIsNone(webhook.failing_since)

    def test_update_webhook_leaves_out_the_amount_decimal_of_a_money_it_read(self):
        read = WebhooksApi(self.client(200, fixture("webhook-with-secret.json"))).rotate_webhook_secret(
            WEBHOOK_ID, "rotate-webhook-1"
        )
        threshold = read.low_balance_threshold
        self.assertEqual(threshold.amount_decimal, "50.00")

        WebhooksApi(self.client(200, fixture("webhook-with-secret.json"))).update_webhook(
            WEBHOOK_ID, "update-webhook-1", UpdateWebhookRequest(low_balance_threshold=threshold)
        )

        method, url, headers = self.sent()
        self.assertEqual(method, "PATCH")
        self.assertEqual(url, f"https://tool.growwer.com/api/v1/webhooks/{WEBHOOK_ID}")
        self.assertEqual(
            json.loads(self.pool.bodies[0]),
            {"lowBalanceThreshold": {"amount": 5000, "currency": "EUR"}},
        )

    def test_error_envelope_is_readable_from_the_exception(self):
        api = CatalogueApi(
            self.client(429, fixture("error.json"), headers={"Retry-After": "3600", "X-Request-Id": "0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34"})
        )

        with self.assertRaises(ApiException) as raised:
            api.get_catalogue_media(MEDIA_ID)

        error = raised.exception
        self.assertEqual(error.status, 429)
        self.assertEqual(error.headers["Retry-After"], "3600")
        self.assertEqual(error.headers["X-Request-Id"], "0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34")
        self.assertIsInstance(error.data, Error)
        self.assertEqual(error.data.code, "catalogue_daily_cap_reached")
        self.assertEqual(error.data.request_id, "0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34")
        self.assertEqual(error.data.details, {"remaining": 0})
        self.assertEqual(json.loads(error.body)["code"], "catalogue_daily_cap_reached")

    def test_binary_download_returns_the_exact_bytes(self):
        body = fixture("briefing.bin")
        api = BuyerOrdersApi(
            self.client(
                200,
                body,
                content_type="application/octet-stream",
                headers={"Content-Disposition": 'attachment; filename="briefing.docx"'},
            )
        )

        downloaded = api.download_order_briefing(ORDER_ID)

        self.assertTrue(self.sent()[1].endswith(f"/api/v1/orders/{ORDER_ID}/briefing"))
        self.assertEqual(bytes(downloaded), body)


if __name__ == "__main__":
    unittest.main()
