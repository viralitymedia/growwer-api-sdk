// Deserialises the shared response fixtures through the generated Go client, offline.
//
// Each call is answered from tests/fixtures/ by an http.RoundTripper set on the client's
// http.Client, so the whole client path runs: URL, headers, status handling and the models.
package fixtures

import (
	"bytes"
	"context"
	"errors"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"reflect"
	"strings"
	"testing"
	"time"

	growwer "github.com/viralitymedia/growwer-api-sdk/go"
)

const (
	mediaID = "c1d2e3f4-a5b6-4c7d-8e9f-a0b1c2d3e4f5"
	orderID = "0b9c6a4e-6f1d-4c39-9a51-2f5d7c1e8a01"
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
	equal(t, "holidayEndDate set", me.Seller.HolidayEndDate.Get() == nil, true)
	equal(t, "eligible", me.Catalogue.Eligible, true)
	equal(t, "dailyCap", me.Catalogue.DailyCap, int32(5000))
	equal(t, "remainingToday set", me.Catalogue.RemainingToday.Get() == nil, true)
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
	equal(t, "linkAdditionOffer", media.LinkAdditionOffer.Get() == nil, true)
	option := media.PostOffer.PricingOptions[0]
	equal(t, "feeWhenSellerWritesPost", option.FeeWhenSellerWritesPost.Get().Amount, int32(6000))
	equal(t, "feeWhenSellerDoesNotWritePost", option.FeeWhenSellerDoesNotWritePost.Get() == nil, true)
	equal(t, "currentCost", option.CurrentCost.Get() == nil, true)
	equal(t, "extra cost", media.PostOffer.ExtraServices[0].Cost.Amount, int32(1500))
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
