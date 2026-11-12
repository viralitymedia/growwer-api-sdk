// Deserialises the shared response fixtures through the generated Go client, offline.
//
// Each call is answered from tests/fixtures/ by an http.RoundTripper set on the client's
// http.Client, so the whole client path runs: URL, headers, status handling and the models.
package fixtures

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"reflect"
	"strings"
	"testing"
	"time"

	growwer "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

const (
	mediaID = "c1d2e3f4-a5b6-4c7d-8e9f-a0b1c2d3e4f5"
	orderID   = "0b9c6a4e-6f1d-4c39-9a51-2f5d7c1e8a01"
	webhookID = "9d4c3f5b-6e7a-4b82-9d2e-3f4a5b6c7d8e"
)

func fixture(t *testing.T, name string) []byte {
	t.Helper()
	body, err := os.ReadFile(filepath.Join("..", "fixtures", name))
	if err != nil {
		t.Fatal(err)
	}
	return body
}

// cannedTransport answers every request with one response and records what was sent.
type cannedTransport struct {
	status  int
	body    []byte
	headers http.Header
	sent    []*http.Request
}

func (c *cannedTransport) RoundTrip(request *http.Request) (*http.Response, error) {
	c.sent = append(c.sent, request)
	return &http.Response{
		StatusCode: c.status,
		Status:     http.StatusText(c.status),
		Header:     c.headers,
		Body:       io.NopCloser(bytes.NewReader(c.body)),
		Request:    request,
	}, nil
}

func answer(status int, body []byte, headers http.Header) (*growwer.APIClient, *cannedTransport) {
	if headers == nil {
		headers = http.Header{"Content-Type": {"application/json"}}
	}
	transport := &cannedTransport{status: status, body: body, headers: headers}
	config := growwer.NewConfiguration()
	config.HTTPClient = &http.Client{Transport: transport}
	return growwer.NewAPIClient(config), transport
}

func authorised() context.Context {
	return context.WithValue(context.Background(), growwer.ContextAccessToken, "test-key")
}

func sent(t *testing.T, transport *cannedTransport) *http.Request {
	t.Helper()
	if len(transport.sent) != 1 {
		t.Fatalf("sent %d requests, want 1", len(transport.sent))
	}
	return transport.sent[0]
}

func equal[T any](t *testing.T, name string, got, want T) {
	t.Helper()
	if !reflect.DeepEqual(got, want) {
		t.Errorf("%s = %#v, want %#v", name, got, want)
	}
}

func check(t *testing.T, err error) {
	t.Helper()
	if err != nil {
		t.Fatal(err)
	}
}

func TestGetMeCallsProductionWithTheBearerKey(t *testing.T) {
	client, transport := answer(200, fixture(t, "me.json"), nil)

	me, _, err := client.AccountAPI.GetMe(authorised()).Execute()
	check(t, err)

	request := sent(t, transport)
	equal(t, "method", request.Method, "GET")
	equal(t, "url", request.URL.String(), "https://tool.growwer.com/api/v1/me")
	equal(t, "Authorization", request.Header.Get("Authorization"), "Bearer test-key")
	equal(t, "available", me.Buyer.Balance.Available.Amount, int32(250000))
	equal(t, "currency", me.Buyer.Balance.Available.Currency, "EUR")
	if me.Seller.Get() == nil {
		t.Fatal("seller = nil, want the live key's seller side")
	}
	equal(t, "holidayEndDate set", me.Seller.Get().HolidayEndDate.Get() == nil, true)
	equal(t, "eligible", me.Catalogue.Eligible, true)
	equal(t, "dailyCap", me.Catalogue.DailyCap, int32(5000))
	equal(t, "remainingToday set", me.Catalogue.RemainingToday.Get() == nil, true)
	equal(t, "mode", me.Mode, "live")
}

func TestGetMeWithATestKeyReadsTestModeAndNoSeller(t *testing.T) {
	client, _ := answer(200, fixture(t, "me-test-key.json"), nil)

	me, _, err := client.AccountAPI.GetMe(authorised()).Execute()
	check(t, err)

	equal(t, "mode", me.Mode, "test")
	equal(t, "seller set", me.Seller.IsSet(), true)
	equal(t, "seller nil", me.Seller.Get() == nil, true)
	equal(t, "available", me.Buyer.Balance.Available.Amount, int32(100000))
	equal(t, "eligible", me.Catalogue.Eligible, true)
}

func TestTheBaseUrlIsOverridable(t *testing.T) {
	client, transport := answer(200, fixture(t, "me.json"), nil)
	client.GetConfig().Servers = growwer.ServerConfigurations{{URL: "https://sandbox.example"}}

	_, _, err := client.AccountAPI.GetMe(authorised()).Execute()
	check(t, err)

	equal(t, "url", sent(t, transport).URL.String(), "https://sandbox.example/api/v1/me")
}

func TestListOrdersReadsItemsAndTotalWithBothOrderTypes(t *testing.T) {
	client, transport := answer(200, fixture(t, "orders-page.json"), nil)

	page, _, err := client.BuyerOrdersAPI.ListOrders(authorised()).Limit(2).Execute()
	check(t, err)

	equal(t, "limit", sent(t, transport).URL.Query().Get("limit"), "2")
	equal(t, "total", page.Total, int32(42))
	if len(page.Items) != 2 {
		t.Fatalf("items = %d, want 2", len(page.Items))
	}
	post, linkAddition := page.Items[0], page.Items[1]

	equal(t, "post type", post.Type, "post")
	equal(t, "post pendingAction", post.PendingAction.Get() == nil, true)
	equal(t, "post delivery", post.Delivery.Get() == nil, true)
	equal(t, "post draft", post.Draft.Get() == nil, true)
	equal(t, "post scheduledPublicationDate", post.ScheduledPublicationDate.Get() == nil, true)
	equal(t, "post price", post.Price.Amount, int32(12500))
	equal(t, "post createdAt", post.CreatedAt.Equal(time.Date(2026, 10, 1, 9, 30, 0, 0, time.UTC)), true)
	if post.Briefing.PostOrderBriefing == nil || post.Briefing.LinkAdditionOrderBriefing != nil {
		t.Fatalf("post briefing = %#v, want a PostOrderBriefing only", post.Briefing)
	}
	equal(t, "post title", post.Briefing.PostOrderBriefing.Title.Get() == nil, true)
	equal(t, "post link type", post.Briefing.PostOrderBriefing.Links[0].Type, "dofollow")
	equal(t, "post reason", post.StateHistory[0].Reason.Get() == nil, true)
	equal(t, "post channel", post.Channel.Created, "api")

	equal(t, "link type", linkAddition.Type, "link_addition")
	equal(t, "link pendingAction", linkAddition.PendingAction.Get() == nil, true)
	equal(t, "link delivery", linkAddition.Delivery.Get() == nil, true)
	equal(t, "link draft", linkAddition.Draft.Get() == nil, true)
	equal(t, "link project id", linkAddition.Project.Id.Get() == nil, true)
	if linkAddition.Briefing.LinkAdditionOrderBriefing == nil || linkAddition.Briefing.PostOrderBriefing != nil {
		t.Fatalf("link briefing = %#v, want a LinkAdditionOrderBriefing only", linkAddition.Briefing)
	}
	equal(t, "linkingFrom", linkAddition.Briefing.LinkAdditionOrderBriefing.LinkingFrom, "https://blog.example/best-trails")
	equal(t, "anchor", linkAddition.Briefing.LinkAdditionOrderBriefing.Link.Anchor.Get() == nil, true)
	equal(t, "reason code", linkAddition.StateHistory[1].Reason.Get().Code, "no_seller_response")
	equal(t, "reason info", linkAddition.StateHistory[1].Reason.Get().AdditionalInfo.Get() == nil, true)
}

func TestAnOrderWithFieldsThisClientDoesNotKnowStillDeserialises(t *testing.T) {
	client, transport := answer(200, fixture(t, "order-with-unknown-field.json"), nil)

	order, _, err := client.BuyerOrdersAPI.GetOrder(authorised(), orderID).Execute()
	check(t, err)

	equal(t, "path", sent(t, transport).URL.Path, "/api/v1/orders/"+orderID)
	equal(t, "id", order.Id, orderID)
	equal(t, "pendingAction", order.GetPendingAction(), "seller")
	equal(t, "hasFile", order.Draft.Get().HasFile, true)
	equal(t, "channel", order.Channel.Created, "api")
	if order.Briefing.PostOrderBriefing == nil || order.Briefing.LinkAdditionOrderBriefing != nil {
		t.Fatalf("briefing = %#v, want a PostOrderBriefing only", order.Briefing)
	}
	equal(t, "title", *order.Briefing.PostOrderBriefing.Title.Get(), "Choosing running shoes")
	equal(t, "link type", order.Briefing.PostOrderBriefing.Links[0].Type, "dofollow")
}

func TestALinkAdditionOrderWithFieldsThisClientDoesNotKnowStillDeserialises(t *testing.T) {
	client, _ := answer(200, fixture(t, "link-addition-order-with-unknown-field.json"), nil)

	order, _, err := client.BuyerOrdersAPI.GetOrder(authorised(), orderID).Execute()
	check(t, err)

	equal(t, "type", order.Type, "link_addition")
	if order.Briefing.LinkAdditionOrderBriefing == nil || order.Briefing.PostOrderBriefing != nil {
		t.Fatalf("briefing = %#v, want a LinkAdditionOrderBriefing only", order.Briefing)
	}
	briefing := order.Briefing.LinkAdditionOrderBriefing
	equal(t, "linkingFrom", briefing.LinkingFrom, "https://blog.example/best-trails")
	equal(t, "anchor", *briefing.Link.Anchor.Get(), "trail shoes")
	equal(t, "link type", briefing.Link.Type, "nofollow")
}

func TestACatalogueMediaReadsANullPreviousPriceAndLinkAdditionOffer(t *testing.T) {
	client, _ := answer(200, fixture(t, "catalogue-media.json"), nil)

	media, _, err := client.CatalogueAPI.GetCatalogueMedia(authorised(), mediaID).Execute()
	check(t, err)

	equal(t, "linkAdditionOffer", media.LinkAdditionOffer.Get() == nil, true)
	equal(t, "flashOffer", media.FlashOffer.Get() == nil, true)
	equal(t, "country", media.Country.Get() == nil, true)
	equal(t, "referringDomains", media.Metrics.ReferringDomains.Get() == nil, true)
	equal(t, "organicTraffic", *media.Metrics.OrganicTraffic.Get(), float32(15400))
	equal(t, "price", media.PostOffer.Price.Amount, int32(9000))
	equal(t, "previousPrice", media.PostOffer.PreviousPrice.Get() == nil, true)
	equal(t, "nofollow", media.PostOffer.Prices["nofollow"].Amount, int32(7000))
	equal(t, "homepageListing", media.PostOffer.Extras.HomepageListing.Get() == nil, true)
	equal(t, "extraPrice", media.PostOffer.Extras.SensitiveTopic.ExtraPrice.Get() == nil, true)
}

func TestACatalogueMediaReadsANullLinkTypeBesidePresentOffers(t *testing.T) {
	client, _ := answer(200, fixture(t, "catalogue-media-null-link-type.json"), nil)

	media, _, err := client.CatalogueAPI.GetCatalogueMedia(authorised(), mediaID).Execute()
	check(t, err)

	postOffer := media.PostOffer
	equal(t, "postOffer linkType", postOffer.LinkType.Get() == nil, true)
	equal(t, "prices", len(postOffer.Prices), 0)
	var previousPrice *growwer.MoneyOrNull = postOffer.PreviousPrice.Get()
	equal(t, "previousPrice", previousPrice.Amount, int32(20000))
	equal(t, "homepageListing", postOffer.Extras.HomepageListing.Get().Amount, int32(2500))
	equal(t, "extraPrice", postOffer.Extras.SensitiveTopic.ExtraPrice.Get().Amount, int32(3000))
	var offer *growwer.CatalogueOfferOrNull = media.LinkAdditionOffer.Get()
	if offer == nil {
		t.Fatal("linkAdditionOffer: got null, want an offer")
	}
	equal(t, "linkAdditionOffer linkType", offer.LinkType.Get() == nil, true)
	equal(t, "linkAdditionOffer price", offer.Price.Amount, int32(6000))
	equal(t, "linkAdditionOffer previousPrice", offer.PreviousPrice.Get() == nil, true)
}

func TestASellerMediaReadsNullCompetitiveFees(t *testing.T) {
	client, _ := answer(200, fixture(t, "seller-media.json"), nil)

	media, _, err := client.SellerMediasAPI.GetSellerMedia(authorised(), mediaID).Execute()
	check(t, err)

	equal(t, "competitiveFees", media.CompetitiveFees.Get() == nil, true)
	equal(t, "competitiveFeesByLinkType", media.CompetitiveFeesByLinkType == nil, true)
	equal(t, "linkAdditionOffer", media.LinkAdditionOffer.Get() == nil, true)
	option := media.PostOffer.PricingOptions[0]
	equal(t, "feeWhenSellerWritesPost", option.FeeWhenSellerWritesPost.Get().Amount, int32(6000))
	equal(t, "feeWhenSellerDoesNotWritePost", option.FeeWhenSellerDoesNotWritePost.Get() == nil, true)
	equal(t, "currentCost", option.CurrentCost.Get() == nil, true)
	equal(t, "extra cost", media.PostOffer.ExtraServices[0].Cost.Amount, int32(1500))
	equal(t, "extra cost amountDecimal", media.PostOffer.ExtraServices[0].Cost.GetAmountDecimal(), "15.00")
}

func TestASellerMediaReadsCompetitiveFeesWithOneSideNull(t *testing.T) {
	client, _ := answer(200, fixture(t, "seller-media-competitive-fees.json"), nil)

	media, _, err := client.SellerMediasAPI.GetSellerMedia(authorised(), mediaID).Execute()
	check(t, err)

	var fees *growwer.SellerFeesOrNull = media.CompetitiveFees.Get()
	if fees == nil {
		t.Fatal("competitiveFees: got null, want fees")
	}
	equal(t, "feeWhenSellerWritesPost", fees.FeeWhenSellerWritesPost.Get().Amount, int32(5400))
	equal(t, "feeWhenSellerDoesNotWritePost", fees.FeeWhenSellerDoesNotWritePost.Get() == nil, true)
}

func TestASellerMediaReadsCompetitiveFeesByLinkTypePerLinkType(t *testing.T) {
	client, _ := answer(200, fixture(t, "seller-media-competitive-fees-by-link-type.json"), nil)

	media, _, err := client.SellerMediasAPI.GetSellerMedia(authorised(), mediaID).Execute()
	check(t, err)

	var fees []growwer.SellerMediaCompetitiveFeesByLinkTypeInner = media.CompetitiveFeesByLinkType
	if len(fees) != 2 {
		t.Fatalf("competitiveFeesByLinkType: got %d entries, want 2", len(fees))
	}
	equal(t, "first linkType", fees[0].LinkType, "dofollow")
	equal(t, "first feeWhenSellerWritesPost", fees[0].FeeWhenSellerWritesPost.Get().Amount, int32(5400))
	equal(t, "first feeWhenSellerWritesPost amountDecimal", fees[0].FeeWhenSellerWritesPost.Get().GetAmountDecimal(), "54.00")
	equal(t, "first feeWhenSellerDoesNotWritePost", fees[0].FeeWhenSellerDoesNotWritePost.Get() == nil, true)
	equal(t, "second linkType", fees[1].LinkType, "nofollow")
	equal(t, "second feeWhenSellerWritesPost", fees[1].FeeWhenSellerWritesPost.Get() == nil, true)
	if fees[1].FeeWhenSellerDoesNotWritePost.Get() == nil {
		t.Fatal("second feeWhenSellerDoesNotWritePost: got null, want 3600")
	}
	equal(t, "second feeWhenSellerDoesNotWritePost", fees[1].FeeWhenSellerDoesNotWritePost.Get().Amount, int32(3600))
	equal(t, "second feeWhenSellerDoesNotWritePost amountDecimal", fees[1].FeeWhenSellerDoesNotWritePost.Get().GetAmountDecimal(), "36.00")
	competitive := media.CompetitiveFees.Get()
	if competitive == nil {
		t.Fatal("competitiveFees: got null, want fees")
	}
	equal(t, "competitiveFees feeWhenSellerWritesPost", competitive.FeeWhenSellerWritesPost.Get().Amount, int32(5400))
	equal(t, "competitiveFees feeWhenSellerDoesNotWritePost", competitive.FeeWhenSellerDoesNotWritePost.Get().Amount, int32(3600))
}

// Pins the generated client's current behaviour, which the README documents: a SellerMedia read with
// a null competitiveFeesByLinkType marshals without the key, and the same client then refuses that
// JSON because the key is required. A failure here means the generator changed that behaviour, and
// the README's Go note on competitiveFeesByLinkType needs revisiting.
func TestPinnedAMarshalledSellerMediaWithANilCompetitiveFeesByLinkTypeIsRefusedWhenReadBack(t *testing.T) {
	var media growwer.SellerMedia
	check(t, json.Unmarshal(fixture(t, "seller-media.json"), &media))
	equal(t, "competitiveFeesByLinkType", media.CompetitiveFeesByLinkType == nil, true)

	marshalled, err := json.Marshal(media)
	check(t, err)
	var keys map[string]interface{}
	check(t, json.Unmarshal(marshalled, &keys))
	_, present := keys["competitiveFeesByLinkType"]
	equal(t, "competitiveFeesByLinkType key present", present, false)

	var readBack growwer.SellerMedia
	err = json.Unmarshal(marshalled, &readBack)
	if err == nil {
		t.Fatal("unmarshalling the marshalled seller media succeeded, want the required-property error")
	}
	equal(t, "error", err.Error(), "no value given for required property competitiveFeesByLinkType")
}

func TestAnOrderEventParsesWithFieldsThisClientDoesNotKnow(t *testing.T) {
	var event growwer.WebhookEvent
	check(t, json.Unmarshal(fixture(t, "webhook-order-created.json"), &event))

	equal(t, "id", event.Id, "6a1f0c2e-3b4d-4e5f-8a9b-0c1d2e3f4a5b")
	equal(t, "type", event.Type, "order.created")
	equal(t, "mode", event.Mode, "live")
	equal(t, "apiVersion", event.ApiVersion, "v1")
	equal(t, "createdAt", event.CreatedAt.Equal(time.Date(2026, 10, 1, 9, 30, 5, 0, time.UTC)), true)
	if event.Data.OrderEventData == nil || event.Data.BalanceLowEventData != nil || event.Data.WebhookTestEventData != nil {
		t.Fatalf("data = %#v, want an OrderEventData only", event.Data)
	}
	order := event.Data.OrderEventData.Order
	equal(t, "order id", order.Id, orderID)
	equal(t, "order state", order.State, "pending_acceptance")
	equal(t, "order price", order.Price.Amount, int32(12500))
	if order.Briefing.PostOrderBriefing == nil {
		t.Fatalf("briefing = %#v, want a PostOrderBriefing", order.Briefing)
	}
	equal(t, "order title", *order.Briefing.PostOrderBriefing.Title.Get(), "Choosing running shoes")
}

func TestABalanceLowEventParsesWithFieldsThisClientDoesNotKnow(t *testing.T) {
	var event growwer.WebhookEvent
	check(t, json.Unmarshal(fixture(t, "webhook-balance-low.json"), &event))

	equal(t, "type", event.Type, "balance.low")
	equal(t, "mode", event.Mode, "live")
	if event.Data.BalanceLowEventData == nil || event.Data.OrderEventData != nil || event.Data.WebhookTestEventData != nil {
		t.Fatalf("data = %#v, want a BalanceLowEventData only", event.Data)
	}
	data := event.Data.BalanceLowEventData
	equal(t, "availableBalance", data.Wallet.AvailableBalance.Amount, int32(4500))
	equal(t, "currency", data.Wallet.Currency, "EUR")
	equal(t, "threshold", data.Threshold.Amount, int32(5000))
}

func TestAWebhookTestEventParsesWithFieldsThisClientDoesNotKnow(t *testing.T) {
	var event growwer.WebhookEvent
	check(t, json.Unmarshal(fixture(t, "webhook-test.json"), &event))

	equal(t, "type", event.Type, "webhook.test")
	equal(t, "mode", event.Mode, "live")
	if event.Data.WebhookTestEventData == nil || event.Data.OrderEventData != nil || event.Data.BalanceLowEventData != nil {
		t.Fatalf("data = %#v, want a WebhookTestEventData only", event.Data)
	}
	equal(t, "webhookId", event.Data.WebhookTestEventData.WebhookId, webhookID)
}

func TestCreateWebhookSendsTheBodyAndKeyAndReadsTheSecret(t *testing.T) {
	client, transport := answer(201, fixture(t, "webhook-with-secret.json"), nil)
	events := []growwer.WebhookEventType{
		growwer.WEBHOOKEVENTTYPE_ORDER_CREATED,
		growwer.WEBHOOKEVENTTYPE_ORDER_COMPLETED,
		growwer.WEBHOOKEVENTTYPE_BALANCE_LOW,
	}
	body := growwer.NewCreateWebhookRequest("https://hooks.shop.example/growwer", events)
	body.SetLowBalanceThreshold(growwer.Money{Amount: 5000, Currency: "EUR"})

	webhook, _, err := client.WebhooksAPI.CreateWebhook(authorised()).
		IdempotencyKey("create-webhook-1").
		CreateWebhookRequest(*body).
		Execute()
	check(t, err)

	request := sent(t, transport)
	equal(t, "method", request.Method, "POST")
	equal(t, "url", request.URL.String(), "https://tool.growwer.com/api/v1/webhooks")
	equal(t, "Idempotency-Key", request.Header.Get("Idempotency-Key"), "create-webhook-1")
	if request.GetBody == nil {
		t.Fatal("the request body cannot be read back")
	}
	reader, err := request.GetBody()
	check(t, err)
	var sentBody map[string]interface{}
	check(t, json.NewDecoder(reader).Decode(&sentBody))
	equal(t, "body", sentBody, map[string]interface{}{
		"url":                 "https://hooks.shop.example/growwer",
		"events":              []interface{}{"order.created", "order.completed", "balance.low"},
		"lowBalanceThreshold": map[string]interface{}{"amount": float64(5000), "currency": "EUR"},
	})

	equal(t, "id", webhook.Id, webhookID)
	equal(t, "secret prefix", strings.HasPrefix(webhook.GetSecret(), "whsec_"), true)
	equal(t, "events", webhook.Events, events)
	if webhook.LowBalanceThreshold.Get() == nil {
		t.Fatal("lowBalanceThreshold = nil, want 5000")
	}
	equal(t, "lowBalanceThreshold", webhook.LowBalanceThreshold.Get().Amount, int32(5000))
	equal(t, "enabled", webhook.Enabled, true)
	equal(t, "disabledReason set", webhook.DisabledReason.Get() == nil, true)
	equal(t, "failingSince set", webhook.FailingSince.Get() == nil, true)
}

func TestUpdateWebhookSendsTheAmountDecimalOfAMoneyItRead(t *testing.T) {
	reader, _ := answer(200, fixture(t, "webhook-with-secret.json"), nil)
	read, _, err := reader.WebhooksAPI.RotateWebhookSecret(authorised(), webhookID).
		IdempotencyKey("rotate-webhook-1").
		Execute()
	check(t, err)
	threshold := read.LowBalanceThreshold.Get()
	if threshold == nil {
		t.Fatal("lowBalanceThreshold = nil, want 5000")
	}
	equal(t, "read amountDecimal", threshold.GetAmountDecimal(), "50.00")

	client, transport := answer(200, fixture(t, "webhook-with-secret.json"), nil)
	body := growwer.NewUpdateWebhookRequest()
	body.SetLowBalanceThreshold(*threshold)
	_, _, err = client.WebhooksAPI.UpdateWebhook(authorised(), webhookID).
		IdempotencyKey("update-webhook-1").
		UpdateWebhookRequest(*body).
		Execute()
	check(t, err)

	request := sent(t, transport)
	equal(t, "method", request.Method, "PATCH")
	equal(t, "url", request.URL.String(), "https://tool.growwer.com/api/v1/webhooks/"+webhookID)
	if request.GetBody == nil {
		t.Fatal("the request body cannot be read back")
	}
	sentReader, err := request.GetBody()
	check(t, err)
	var sentBody map[string]interface{}
	check(t, json.NewDecoder(sentReader).Decode(&sentBody))
	equal(t, "body", sentBody, map[string]interface{}{
		"lowBalanceThreshold": map[string]interface{}{"amount": float64(5000), "currency": "EUR", "amountDecimal": "50.00"},
	})
}

func TestTheErrorEnvelopeIsReadableFromTheError(t *testing.T) {
	client, _ := answer(429, fixture(t, "error.json"), http.Header{
		"Content-Type": {"application/json"},
		"Retry-After":  {"3600"},
		"X-Request-Id": {"0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34"},
	})

	_, response, err := client.CatalogueAPI.GetCatalogueMedia(authorised(), mediaID).Execute()

	var apiError *growwer.GenericOpenAPIError
	if !errors.As(err, &apiError) {
		t.Fatalf("err = %#v, want a *GenericOpenAPIError", err)
	}
	equal(t, "status", response.StatusCode, 429)
	equal(t, "Retry-After", response.Header.Get("Retry-After"), "3600")
	equal(t, "X-Request-Id", response.Header.Get("X-Request-Id"), "0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34")
	envelope, ok := apiError.Model().(growwer.Error)
	if !ok {
		t.Fatalf("model = %#v, want a growwer.Error", apiError.Model())
	}
	equal(t, "code", envelope.Code, "catalogue_daily_cap_reached")
	equal(t, "requestId", envelope.RequestId, "0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34")
	equal(t, "details", envelope.Details, map[string]interface{}{"remaining": float64(0)})
	equal(t, "body has code", strings.Contains(string(apiError.Body()), "catalogue_daily_cap_reached"), true)
}

func TestABinaryDownloadReturnsTheExactBytes(t *testing.T) {
	body := fixture(t, "briefing.bin")
	client, transport := answer(200, body, http.Header{
		"Content-Type":        {"application/octet-stream"},
		"Content-Disposition": {`attachment; filename="briefing.docx"`},
	})

	file, _, err := client.BuyerOrdersAPI.DownloadOrderBriefing(authorised(), orderID).Execute()
	check(t, err)
	defer os.Remove(file.Name())
	defer file.Close()

	equal(t, "path", sent(t, transport).URL.Path, "/api/v1/orders/"+orderID+"/briefing")
	downloaded, err := io.ReadAll(file)
	check(t, err)
	equal(t, "bytes", downloaded, body)
}
