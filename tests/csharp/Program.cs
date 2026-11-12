// Deserialises the shared response fixtures through the generated C# client, offline.
//
// Each call is answered from tests/fixtures/ by an HttpMessageHandler handed to the client's own
// HttpClient, so the whole client path runs: URL, headers, status handling and the models. Run
// with `dotnet run --project tests/csharp` from the repository root.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading;
using System.Threading.Tasks;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

internal static class Program
{
    private static readonly string Fixtures = Path.Combine("tests", "fixtures");
    private static readonly Guid MediaId = Guid.Parse("c1d2e3f4-a5b6-4c7d-8e9f-a0b1c2d3e4f5");
    private static readonly Guid OrderId = Guid.Parse("0b9c6a4e-6f1d-4c39-9a51-2f5d7c1e8a01");
    private static readonly Guid ProjectId = Guid.Parse("5e0c2b7a-3d4f-4a1b-9c8d-7e6f5a4b3c2d");
    private static readonly Guid WebhookId = Guid.Parse("9d4c3f5b-6e7a-4b82-9d2e-3f4a5b6c7d8e");

    private static readonly List<HttpRequestMessage> Sent = new List<HttpRequestMessage>();
    private static readonly List<string> SentBodies = new List<string>();

    private static byte[] Fixture(string name) => File.ReadAllBytes(Path.Combine(Fixtures, name));

    private static void Equal(string name, object actual, object expected)
    {
        bool same = actual is byte[] a && expected is byte[] b ? a.SequenceEqual(b) : Equals(actual, expected);
        if (!same)
        {
            throw new Exception($"{name} = {actual ?? "null"}, want {expected ?? "null"}");
        }
    }

    /// <summary>Answers every request with one canned response and records what was sent.</summary>
    private sealed class Canned : HttpMessageHandler
    {
        private readonly HttpStatusCode status;
        private readonly byte[] body;
        private readonly string contentType;
        private readonly string[] headers;

        public Canned(HttpStatusCode status, byte[] body, string contentType, string[] headers)
        {
            this.status = status;
            this.body = body;
            this.contentType = contentType;
            this.headers = headers;
        }

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            Sent.Add(request);
            SentBodies.Add(request.Content?.ReadAsStringAsync(cancellationToken).GetAwaiter().GetResult());
            var response = new HttpResponseMessage(status) { RequestMessage = request, Content = new ByteArrayContent(body) };
            response.Content.Headers.ContentType = MediaTypeHeaderValue.Parse(contentType);
            for (int i = 0; i < headers.Length; i += 2)
            {
                if (!response.Headers.TryAddWithoutValidation(headers[i], headers[i + 1]))
                {
                    response.Content.Headers.TryAddWithoutValidation(headers[i], headers[i + 1]);
                }
            }
            return Task.FromResult(response);
        }
    }

    private static HttpClient Answer(HttpStatusCode status, byte[] body, string contentType, params string[] headers)
    {
        Sent.Clear();
        SentBodies.Clear();
        return new HttpClient(new Canned(status, body, contentType, headers));
    }

    private static HttpClient Answer(byte[] body) => Answer(HttpStatusCode.OK, body, "application/json");

    private static Configuration Key() => new Configuration { AccessToken = "test-key" };

    // Header names are case-insensitive, and .NET rewrites the ones it knows: X-Request-Id arrives
    // as X-Request-ID. The client's Multimap compares names exactly, so callers look them up this way.
    private static string Header(Multimap<string, string> headers, string name) =>
        headers.Where(header => string.Equals(header.Key, name, StringComparison.OrdinalIgnoreCase))
            .SelectMany(header => header.Value)
            .Single();

    private static HttpRequestMessage SentRequest()
    {
        Equal("requests sent", Sent.Count, 1);
        return Sent[0];
    }

    private static JObject SentBody()
    {
        Equal("requests sent", SentBodies.Count, 1);
        return JObject.Parse(SentBodies[0]);
    }

    private static void Keys(string name, JObject body, params string[] expected)
    {
        Equal(name, string.Join(",", body.Properties().Select(property => property.Name).OrderBy(key => key, StringComparer.Ordinal)),
            string.Join(",", expected.OrderBy(key => key, StringComparer.Ordinal)));
    }

    private static void GetMeCallsProductionWithTheBearerKey()
    {
        GetMe200Response me = new AccountApi(Answer(Fixture("me.json")), Key()).GetMe();

        Equal("method", SentRequest().Method, HttpMethod.Get);
        Equal("url", SentRequest().RequestUri.ToString(), "https://tool.growwer.com/api/v1/me");
        Equal("Authorization", SentRequest().Headers.Authorization?.ToString(), "Bearer test-key");
        Equal("available", me.Buyer.Balance.Available.Amount, 250000);
        Equal("currency", me.Buyer.Balance.Available.Currency, "EUR");
        Equal("holidayEndDate", me.Seller.HolidayEndDate, null);
        Equal("eligible", me.Catalogue.Eligible, true);
        Equal("dailyCap", me.Catalogue.DailyCap, 5000);
        Equal("remainingToday", me.Catalogue.RemainingToday, null);
        Equal("mode", me.Mode, GetMe200Response.ModeEnum.Live);
    }

    private static void GetMeWithATestKeyReadsTestModeAndNoSeller()
    {
        GetMe200Response me = new AccountApi(Answer(Fixture("me-test-key.json")), Key()).GetMe();

        Equal("mode", me.Mode, GetMe200Response.ModeEnum.Test);
        Equal("seller", me.Seller, null);
        Equal("available", me.Buyer.Balance.Available.Amount, 100000);
        Equal("eligible", me.Catalogue.Eligible, true);
    }

    private static WebhookEvent Event(string name) =>
        JsonConvert.DeserializeObject<WebhookEvent>(File.ReadAllText(Path.Combine(Fixtures, name)));

    private static void AnOrderEventParsesWithFieldsThisClientDoesNotKnow()
    {
        WebhookEvent webhookEvent = Event("webhook-order-created.json");

        Equal("id", webhookEvent.Id, Guid.Parse("6a1f0c2e-3b4d-4e5f-8a9b-0c1d2e3f4a5b"));
        Equal("type", webhookEvent.Type, WebhookEvent.TypeEnum.OrderCreated);
        Equal("mode", webhookEvent.Mode, WebhookEvent.ModeEnum.Live);
        Equal("apiVersion", webhookEvent.ApiVersion, WebhookEvent.ApiVersionEnum.V1);
        Equal("createdAt", webhookEvent.CreatedAt.ToUniversalTime(), new DateTime(2026, 10, 1, 9, 30, 5, DateTimeKind.Utc));
        Equal("data type", webhookEvent.Data.ActualInstance.GetType(), typeof(OrderEventData));
        Order order = webhookEvent.Data.GetOrderEventData().Order;
        Equal("order id", order.Id, OrderId);
        Equal("order state", order.State, "pending_acceptance");
        Equal("order price", order.Price.Amount, 12500);
        Equal("briefing type", order.Briefing.ActualInstance.GetType(), typeof(PostOrderBriefing));
    }

    private static void ABalanceLowEventParsesWithFieldsThisClientDoesNotKnow()
    {
        WebhookEvent webhookEvent = Event("webhook-balance-low.json");

        Equal("type", webhookEvent.Type, WebhookEvent.TypeEnum.BalanceLow);
        Equal("mode", webhookEvent.Mode, WebhookEvent.ModeEnum.Live);
        Equal("data type", webhookEvent.Data.ActualInstance.GetType(), typeof(BalanceLowEventData));
        BalanceLowEventData data = webhookEvent.Data.GetBalanceLowEventData();
        Equal("availableBalance", data.Wallet.AvailableBalance.Amount, 4500);
        Equal("currency", data.Wallet.Currency, "EUR");
        Equal("threshold", data.Threshold.Amount, 5000);
    }

    private static void AWebhookTestEventParsesWithFieldsThisClientDoesNotKnow()
    {
        WebhookEvent webhookEvent = Event("webhook-test.json");

        Equal("type", webhookEvent.Type, WebhookEvent.TypeEnum.WebhookTest);
        Equal("mode", webhookEvent.Mode, WebhookEvent.ModeEnum.Live);
        Equal("data type", webhookEvent.Data.ActualInstance.GetType(), typeof(WebhookTestEventData));
        Equal("webhookId", webhookEvent.Data.GetWebhookTestEventData().WebhookId, WebhookId);
    }

    private static void CreateWebhookSendsTheBodyAndKeyAndReadsTheSecret()
    {
        WebhookWithSecret webhook = new WebhooksApi(Answer(HttpStatusCode.Created, Fixture("webhook-with-secret.json"), "application/json"), Key())
            .CreateWebhook("create-webhook-1", new CreateWebhookRequest(
                url: "https://hooks.shop.example/growwer",
                events: new List<WebhookEventType> { WebhookEventType.OrderCreated, WebhookEventType.OrderCompleted, WebhookEventType.BalanceLow },
                lowBalanceThreshold: new Money(amount: 5000, currency: "EUR")));

        Equal("method", SentRequest().Method, HttpMethod.Post);
        Equal("url", SentRequest().RequestUri.ToString(), "https://tool.growwer.com/api/v1/webhooks");
        Equal("Idempotency-Key", string.Join(",", SentRequest().Headers.GetValues("Idempotency-Key")), "create-webhook-1");
        JObject body = SentBody();
        Keys("request keys", body, "url", "events", "lowBalanceThreshold");
        Equal("body url", (string)body["url"], "https://hooks.shop.example/growwer");
        Equal("body events", string.Join(",", body["events"].Select(item => (string)item)), "order.created,order.completed,balance.low");
        Equal("body threshold amount", (int)body["lowBalanceThreshold"]["amount"], 5000);
        Equal("body threshold currency", (string)body["lowBalanceThreshold"]["currency"], "EUR");
        Equal("id", webhook.Id, WebhookId);
        Equal("secret prefix", webhook.Secret.StartsWith("whsec_", StringComparison.Ordinal), true);
        Equal("events", string.Join(",", webhook.Events), "OrderCreated,OrderCompleted,BalanceLow");
        Equal("lowBalanceThreshold", webhook.LowBalanceThreshold.Amount, 5000);
        Equal("enabled", webhook.Enabled, true);
        Equal("disabledReason", webhook.DisabledReason, null);
        Equal("failingSince", webhook.FailingSince, null);
    }

    private static void UpdateWebhookLeavesOutTheAmountDecimalOfAMoneyItRead()
    {
        WebhookWithSecret read = new WebhooksApi(Answer(Fixture("webhook-with-secret.json")), Key())
            .RotateWebhookSecret(WebhookId, "rotate-webhook-1");
        MoneyOrNull threshold = read.LowBalanceThreshold;
        Equal("read amountDecimal", threshold.AmountDecimal, "50.00");

        new WebhooksApi(Answer(Fixture("webhook-with-secret.json")), Key())
            .UpdateWebhook(WebhookId, "update-webhook-1", new UpdateWebhookRequest(lowBalanceThreshold: threshold));

        Equal("method", SentRequest().Method, HttpMethod.Patch);
        Equal("url", SentRequest().RequestUri.ToString(), $"https://tool.growwer.com/api/v1/webhooks/{WebhookId}");
        JObject sentThreshold = (JObject)SentBody()["lowBalanceThreshold"];
        Keys("threshold keys", sentThreshold, "amount", "currency");
        Equal("threshold amount", (int)sentThreshold["amount"], 5000);
        Equal("threshold currency", (string)sentThreshold["currency"], "EUR");
    }

    // enabled is optional and not nullable: an update that leaves it out keeps the subscription's
    // state, so a C# bool the caller never set must not go out as false, which disables it.
    private static void UpdateWebhookWithoutEnabledLeavesItOut()
    {
        new WebhooksApi(Answer(Fixture("webhook-with-secret.json")), Key())
            .UpdateWebhook(WebhookId, "update-webhook-1", new UpdateWebhookRequest(url: "https://hooks.shop.example/v2"));

        Equal("method", SentRequest().Method, HttpMethod.Patch);
        JObject body = SentBody();
        Keys("request keys", body, "url");
        Equal("body url", (string)body["url"], "https://hooks.shop.example/v2");
    }

    private static void UpdateWebhookSendsEnabledSetToFalse()
    {
        var requests = new List<(string How, UpdateWebhookRequest Request)>
        {
            ("constructor", new UpdateWebhookRequest(enabled: false)),
            ("property", new UpdateWebhookRequest { Enabled = false }),
        };
        foreach (var (how, request) in requests)
        {
            new WebhooksApi(Answer(Fixture("webhook-with-secret.json")), Key())
                .UpdateWebhook(WebhookId, "update-webhook-1", request);

            JObject body = SentBody();
            Keys(how + " request keys", body, "enabled");
            Equal(how + " enabled type", body["enabled"].Type, JTokenType.Boolean);
            Equal(how + " enabled", (bool)body["enabled"], false);
        }
    }

    private static void AnOrderEstimateLeavesOutADraftReviewableItNeverSet()
    {
        byte[] estimate = System.Text.Encoding.UTF8.GetBytes(
            "{\"price\":{\"amount\":1800,\"currency\":\"EUR\"},\"availableBalance\":{\"amount\":50000,\"currency\":\"EUR\"},"
            + "\"missing\":{\"amount\":0,\"currency\":\"EUR\"},\"sufficientBalance\":true}");
        var briefing = new OrderEstimateRequestBriefing(new LinkAdditionOrderBriefingRequest(
            linkingFrom: "https://blog.example/post",
            link: new OrderLinkRequest(targetUrl: "https://shop.example", anchor: "trail shoes", type: OrderLinkRequest.TypeEnum.Dofollow)));
        var requests = new List<(OrderEstimateRequest Request, string[] Keys)>
        {
            (new OrderEstimateRequest(type: OrderEstimateRequest.TypeEnum.LinkAddition, projectId: ProjectId, mediaId: MediaId, briefing: briefing),
                new[] { "type", "projectId", "mediaId", "briefing" }),
            (new OrderEstimateRequest(type: OrderEstimateRequest.TypeEnum.LinkAddition, projectId: ProjectId, mediaId: MediaId, briefing: briefing, draftReviewable: false),
                new[] { "type", "projectId", "mediaId", "briefing", "draftReviewable" }),
        };
        foreach (var (request, keys) in requests)
        {
            new BuyerOrdersApi(Answer(estimate), Key()).EstimateOrder(request);

            JObject body = SentBody();
            Keys("request keys", body, keys);
            if (body["draftReviewable"] != null)
            {
                Equal("draftReviewable", (bool)body["draftReviewable"], false);
            }
        }
    }

    private static void TheBaseUrlIsOverridable()
    {
        Configuration configuration = Key();
        configuration.BasePath = "https://sandbox.example";
        new AccountApi(Answer(Fixture("me.json")), configuration).GetMe();

        Equal("url", SentRequest().RequestUri.ToString(), "https://sandbox.example/api/v1/me");
    }

    private static void ListOrdersReadsItemsAndTotalWithBothOrderTypes()
    {
        ListOrders200Response page = new BuyerOrdersApi(Answer(Fixture("orders-page.json")), Key()).ListOrders(limit: 2);

        Equal("query", SentRequest().RequestUri.Query.Contains("limit=2"), true);
        Equal("total", page.Total, 42);
        Equal("items", page.Items.Count, 2);
        Order post = page.Items[0];
        Order linkAddition = page.Items[1];

        Equal("post type", post.Type, Order.TypeEnum.Post);
        Equal("post pendingAction", (Order.PendingActionEnum?)post.PendingAction, null);
        Equal("post delivery", post.Delivery, null);
        Equal("post draft", post.Draft, null);
        Equal("post scheduledPublicationDate", post.ScheduledPublicationDate, null);
        Equal("post price", post.Price.Amount, 12500);
        Equal("post createdAt", post.CreatedAt.ToUniversalTime(), new DateTime(2026, 10, 1, 9, 30, 0, DateTimeKind.Utc));
        PostOrderBriefing postBriefing = post.Briefing.GetPostOrderBriefing();
        Equal("post title", postBriefing.Title, null);
        Equal("post link type", postBriefing.Links[0].Type, OrderLink.TypeEnum.Dofollow);
        Equal("post reason", post.StateHistory[0].Reason, null);
        Equal("post channel", post.Channel.Created, OrderChannel.CreatedEnum.Api);

        Equal("link type", linkAddition.Type, Order.TypeEnum.LinkAddition);
        Equal("link pendingAction", (Order.PendingActionEnum?)linkAddition.PendingAction, null);
        Equal("link delivery", linkAddition.Delivery, null);
        Equal("link draft", linkAddition.Draft, null);
        Equal("link project id", linkAddition.Project.Id, null);
        LinkAdditionOrderBriefing linkBriefing = linkAddition.Briefing.GetLinkAdditionOrderBriefing();
        Equal("linkingFrom", linkBriefing.LinkingFrom, "https://blog.example/best-trails");
        Equal("anchor", linkBriefing.Link.Anchor, null);
        Equal("reason code", linkAddition.StateHistory[1].Reason.Code, OrderStateHistoryInnerReason.CodeEnum.NoSellerResponse);
        Equal("reason info", linkAddition.StateHistory[1].Reason.AdditionalInfo, null);
    }

    private static void AnOrderWithFieldsThisClientDoesNotKnowStillDeserialises()
    {
        Order order = new BuyerOrdersApi(Answer(Fixture("order-with-unknown-field.json")), Key()).GetOrder(OrderId);

        Equal("path", SentRequest().RequestUri.AbsolutePath, "/api/v1/orders/" + OrderId);
        Equal("id", order.Id, OrderId);
        Equal("pendingAction", (Order.PendingActionEnum?)order.PendingAction, Order.PendingActionEnum.Seller);
        Equal("hasFile", order.Draft.HasFile, true);
        Equal("channel", order.Channel.Created, OrderChannel.CreatedEnum.Api);
        Equal("briefing type", order.Briefing.ActualInstance.GetType(), typeof(PostOrderBriefing));
        Equal("title", order.Briefing.GetPostOrderBriefing().Title, "Choosing running shoes");
        Equal("link type", order.Briefing.GetPostOrderBriefing().Links[0].Type, OrderLink.TypeEnum.Dofollow);
    }

    private static void ALinkAdditionOrderWithFieldsThisClientDoesNotKnowStillDeserialises()
    {
        Order order = new BuyerOrdersApi(Answer(Fixture("link-addition-order-with-unknown-field.json")), Key()).GetOrder(OrderId);

        Equal("type", order.Type, Order.TypeEnum.LinkAddition);
        Equal("briefing type", order.Briefing.ActualInstance.GetType(), typeof(LinkAdditionOrderBriefing));
        LinkAdditionOrderBriefing briefing = order.Briefing.GetLinkAdditionOrderBriefing();
        Equal("linkingFrom", briefing.LinkingFrom, "https://blog.example/best-trails");
        Equal("anchor", briefing.Link.Anchor, "trail shoes");
        Equal("link type", briefing.Link.Type, OrderLink.TypeEnum.Nofollow);
    }

    private static void ACatalogueMediaReadsANullPreviousPriceAndLinkAdditionOffer()
    {
        CatalogueMedia media = new CatalogueApi(Answer(Fixture("catalogue-media.json")), Key()).GetCatalogueMedia(MediaId);

        Equal("linkAdditionOffer", media.LinkAdditionOffer, null);
        Equal("flashOffer", media.FlashOffer, null);
        Equal("country", media.Country, null);
        Equal("referringDomains", media.Metrics.ReferringDomains, null);
        Equal("organicTraffic", media.Metrics.OrganicTraffic, 15400m);
        Equal("price", media.PostOffer.Price.Amount, 9000);
        Equal("previousPrice", media.PostOffer.PreviousPrice, null);
        Equal("nofollow", media.PostOffer.Prices["nofollow"].Amount, 7000);
        Equal("homepageListing", media.PostOffer.Extras.HomepageListing, null);
        Equal("extraPrice", media.PostOffer.Extras.SensitiveTopic.ExtraPrice, null);
    }

    private static void ACatalogueMediaReadsANullLinkTypeBesidePresentOffers()
    {
        CatalogueMedia media = new CatalogueApi(Answer(Fixture("catalogue-media-null-link-type.json")), Key())
            .GetCatalogueMedia(MediaId);

        CataloguePostOffer postOffer = media.PostOffer;
        Equal("postOffer linkType", postOffer.LinkType, null);
        Equal("prices", postOffer.Prices.Count, 0);
        MoneyOrNull previousPrice = postOffer.PreviousPrice;
        Equal("previousPrice", previousPrice.Amount, 20000);
        Equal("homepageListing", postOffer.Extras.HomepageListing.Amount, 2500);
        Equal("extraPrice", postOffer.Extras.SensitiveTopic.ExtraPrice.Amount, 3000);
        CatalogueOfferOrNull offer = media.LinkAdditionOffer;
        if (offer == null)
        {
            throw new Exception("linkAdditionOffer: got null, want an offer");
        }
        Equal("linkAdditionOffer linkType", offer.LinkType, null);
        Equal("linkAdditionOffer price", offer.Price.Amount, 6000);
        Equal("linkAdditionOffer previousPrice", offer.PreviousPrice, null);
    }

    private static void ASellerMediaReadsNullCompetitiveFees()
    {
        SellerMedia media = new SellerMediasApi(Answer(Fixture("seller-media.json")), Key()).GetSellerMedia(MediaId);

        Equal("competitiveFees", media.CompetitiveFees, null);
        Equal("competitiveFeesByLinkType", media.CompetitiveFeesByLinkType, null);
        Equal("linkAdditionOffer", media.LinkAdditionOffer, null);
        SellerMediaPostOfferPricingOptionsInner option = media.PostOffer.PricingOptions[0];
        Equal("feeWhenSellerWritesPost", option.FeeWhenSellerWritesPost.Amount, 6000);
        Equal("feeWhenSellerDoesNotWritePost", option.FeeWhenSellerDoesNotWritePost, null);
        Equal("currentCost", option.CurrentCost, null);
        Equal("extra cost", media.PostOffer.ExtraServices[0].Cost.Amount, 1500);
        Equal("extra cost amountDecimal", media.PostOffer.ExtraServices[0].Cost.AmountDecimal, "15.00");
    }

    private static void ASellerMediaReadsCompetitiveFeesWithOneSideNull()
    {
        SellerMedia media = new SellerMediasApi(Answer(Fixture("seller-media-competitive-fees.json")), Key())
            .GetSellerMedia(MediaId);

        SellerFeesOrNull fees = media.CompetitiveFees;
        if (fees == null)
        {
            throw new Exception("competitiveFees: got null, want fees");
        }
        Equal("feeWhenSellerWritesPost", fees.FeeWhenSellerWritesPost.Amount, 5400);
        Equal("feeWhenSellerDoesNotWritePost", fees.FeeWhenSellerDoesNotWritePost, null);
    }

    private static void ASellerMediaReadsCompetitiveFeesByLinkTypePerLinkType()
    {
        SellerMedia media = new SellerMediasApi(Answer(Fixture("seller-media-competitive-fees-by-link-type.json")), Key())
            .GetSellerMedia(MediaId);

        List<SellerMediaCompetitiveFeesByLinkTypeInner> fees = media.CompetitiveFeesByLinkType;
        if (fees == null || fees.Count != 2)
        {
            throw new Exception($"competitiveFeesByLinkType: got {fees?.Count.ToString() ?? "null"} entries, want 2");
        }
        Equal("first linkType", fees[0].LinkType, SellerMediaCompetitiveFeesByLinkTypeInner.LinkTypeEnum.Dofollow);
        Equal("first feeWhenSellerWritesPost", fees[0].FeeWhenSellerWritesPost.Amount, 5400);
        Equal("first feeWhenSellerWritesPost amountDecimal", fees[0].FeeWhenSellerWritesPost.AmountDecimal, "54.00");
        Equal("first feeWhenSellerDoesNotWritePost", fees[0].FeeWhenSellerDoesNotWritePost, null);
        Equal("second linkType", fees[1].LinkType, SellerMediaCompetitiveFeesByLinkTypeInner.LinkTypeEnum.Nofollow);
        Equal("second feeWhenSellerWritesPost", fees[1].FeeWhenSellerWritesPost, null);
        Equal("second feeWhenSellerDoesNotWritePost", fees[1].FeeWhenSellerDoesNotWritePost.Amount, 3600);
        Equal("second feeWhenSellerDoesNotWritePost amountDecimal", fees[1].FeeWhenSellerDoesNotWritePost.AmountDecimal, "36.00");
        Equal("competitiveFees feeWhenSellerWritesPost", media.CompetitiveFees.FeeWhenSellerWritesPost.Amount, 5400);
        Equal("competitiveFees feeWhenSellerDoesNotWritePost", media.CompetitiveFees.FeeWhenSellerDoesNotWritePost.Amount, 3600);
    }

    private static void TheErrorEnvelopeIsReadableFromTheException()
    {
        var api = new CatalogueApi(Answer(HttpStatusCode.TooManyRequests, Fixture("error.json"), "application/json",
            "Retry-After", "3600", "X-Request-Id", "0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34"), Key());

        try
        {
            api.GetCatalogueMedia(MediaId);
            throw new Exception("a 429 must throw");
        }
        catch (ApiException exception)
        {
            Equal("status", exception.ErrorCode, 429);
            Equal("Retry-After", Header(exception.Headers, "Retry-After"), "3600");
            Equal("X-Request-Id", Header(exception.Headers, "X-Request-Id"), "0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34");
            Error envelope = JsonConvert.DeserializeObject<Error>((string)exception.ErrorContent);
            Equal("code", envelope.Code, "catalogue_daily_cap_reached");
            Equal("requestId", envelope.RequestId, "0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34");
            Equal("details", Convert.ToInt32(envelope.Details["remaining"]), 0);
        }
    }

    private static void ABinaryDownloadReturnsTheExactBytes()
    {
        byte[] body = Fixture("briefing.bin");
        FileParameter file = new BuyerOrdersApi(Answer(HttpStatusCode.OK, body, "application/octet-stream",
            "Content-Disposition", "attachment; filename=\"briefing.docx\""), Key()).DownloadOrderBriefing(OrderId);

        Equal("path", SentRequest().RequestUri.AbsolutePath, "/api/v1/orders/" + OrderId + "/briefing");
        using var copy = new MemoryStream();
        file.Content.CopyTo(copy);
        Equal("bytes", copy.ToArray(), body);
    }

    private static void AProjectMediaReadsAnAiKeywordWithANullSource()
    {
        ListFlashOffers200Response page = new CatalogueApi(Answer(Fixture("project-medias-page.json")), Key())
            .SearchProjectMedias(MediaId);

        List<ProjectCatalogueMediaAllOfProjectAiKeywords> keywords = page.Items[0].Project.AiKeywords;
        Equal("aiKeywords", keywords.Count, 2);
        Equal("source", keywords[0].Source, ProjectCatalogueMediaAllOfProjectAiKeywords.SourceEnum.Chatgpt);
        Equal("keyword", keywords[1].Keyword, "trail shoes");
        Equal("null source", keywords[1].Source, null);
    }

    // An optional, nullable property means something when it is null: a project's country null is
    // worldwide. One the caller never set must be left out of a PATCH, not sent as null.
    private static void AProjectUpdateWithOnlyANameLeavesTheCountryOut()
    {
        new ProjectsApi(Answer(Fixture("project.json")), Key())
            .UpdateProject(ProjectId, "key-1", new UpdateProjectRequest(name: "Trail running"));

        Equal("method", SentRequest().Method, HttpMethod.Patch);
        JObject body = SentBody();
        Keys("request keys", body, "name");
        Equal("name", (string)body["name"], "Trail running");
    }

    private static void AProjectUpdateSendsACountrySetToNull()
    {
        new ProjectsApi(Answer(Fixture("project.json")), Key())
            .UpdateProject(ProjectId, "key-1", new UpdateProjectRequest { Country = null });

        JObject body = SentBody();
        Keys("request keys", body, "country");
        Equal("country", body["country"].Type, JTokenType.Null);
    }

    private static void ASellerMediaUpdateWithoutALinkAdditionOfferLeavesItOut()
    {
        var option = new UpdateSellerMediaRequestPostOfferPricingOptionsInner(
            linkType: UpdateSellerMediaRequestPostOfferPricingOptionsInner.LinkTypeEnum.Dofollow,
            feeWhenSellerWritesPost: new MoneyOrNull(6000, "EUR"));
        var update = new UpdateSellerMediaRequest(postOffer: new UpdateSellerMediaRequestPostOffer(
            pricingOptions: new List<UpdateSellerMediaRequestPostOfferPricingOptionsInner> { option }));
        new SellerMediasApi(Answer(Fixture("seller-media.json")), Key()).UpdateSellerMedia(MediaId, "key-1", update);

        Equal("method", SentRequest().Method, HttpMethod.Patch);
        JObject body = SentBody();
        Keys("request keys", body, "postOffer");
        Keys("postOffer keys", (JObject)body["postOffer"], "pricingOptions");
        Keys("option keys", (JObject)body["postOffer"]["pricingOptions"][0], "linkType", "feeWhenSellerWritesPost");
    }

    private static void ASellerMediaUpdateSendsALinkAdditionOfferSetToNull()
    {
        new SellerMediasApi(Answer(Fixture("seller-media.json")), Key())
            .UpdateSellerMedia(MediaId, "key-1", new UpdateSellerMediaRequest { LinkAdditionOffer = null });

        JObject body = SentBody();
        Keys("request keys", body, "linkAdditionOffer");
        Equal("linkAdditionOffer", body["linkAdditionOffer"].Type, JTokenType.Null);
    }

    private static int Main()
    {
        var cases = new List<(string Name, Action Run)>
        {
            ("getMe calls production with the bearer key", GetMeCallsProductionWithTheBearerKey),
            ("getMe with a test key reads test mode and no seller", GetMeWithATestKeyReadsTestModeAndNoSeller),
            ("the base URL is overridable", TheBaseUrlIsOverridable),
            ("listOrders reads items and total, with both order types", ListOrdersReadsItemsAndTotalWithBothOrderTypes),
            ("an order with fields this client does not know still deserialises", AnOrderWithFieldsThisClientDoesNotKnowStillDeserialises),
            ("a link addition order with fields this client does not know still deserialises", ALinkAdditionOrderWithFieldsThisClientDoesNotKnowStillDeserialises),
            ("a catalogue media reads a null previousPrice and linkAdditionOffer", ACatalogueMediaReadsANullPreviousPriceAndLinkAdditionOffer),
            ("a catalogue media reads a null linkType beside present offers", ACatalogueMediaReadsANullLinkTypeBesidePresentOffers),
            ("a project media reads an AI keyword with a null source", AProjectMediaReadsAnAiKeywordWithANullSource),
            ("a seller media reads null competitiveFees", ASellerMediaReadsNullCompetitiveFees),
            ("a seller media reads competitiveFees with one side null", ASellerMediaReadsCompetitiveFeesWithOneSideNull),
            ("a seller media reads competitiveFeesByLinkType per link type", ASellerMediaReadsCompetitiveFeesByLinkTypePerLinkType),
            ("a project update with only a name leaves the country out", AProjectUpdateWithOnlyANameLeavesTheCountryOut),
            ("a project update sends a country set to null", AProjectUpdateSendsACountrySetToNull),
            ("a seller media update without a linkAdditionOffer leaves it out", ASellerMediaUpdateWithoutALinkAdditionOfferLeavesItOut),
            ("a seller media update sends a linkAdditionOffer set to null", ASellerMediaUpdateSendsALinkAdditionOfferSetToNull),
            ("the error envelope is readable from the ApiException", TheErrorEnvelopeIsReadableFromTheException),
            ("a binary download returns the exact bytes", ABinaryDownloadReturnsTheExactBytes),
            ("an order event parses with fields this client does not know", AnOrderEventParsesWithFieldsThisClientDoesNotKnow),
            ("a balance.low event parses with fields this client does not know", ABalanceLowEventParsesWithFieldsThisClientDoesNotKnow),
            ("a webhook.test event parses with fields this client does not know", AWebhookTestEventParsesWithFieldsThisClientDoesNotKnow),
            ("createWebhook sends the body and key and reads the secret", CreateWebhookSendsTheBodyAndKeyAndReadsTheSecret),
            ("updateWebhook leaves out the amountDecimal of a Money it read", UpdateWebhookLeavesOutTheAmountDecimalOfAMoneyItRead),
            ("updateWebhook without enabled leaves it out", UpdateWebhookWithoutEnabledLeavesItOut),
            ("updateWebhook sends enabled set to false", UpdateWebhookSendsEnabledSetToFalse),
            ("an order estimate leaves out a draftReviewable it never set", AnOrderEstimateLeavesOutADraftReviewableItNeverSet),
        };
        int failed = 0;
        foreach (var (name, run) in cases)
        {
            try
            {
                run();
                Console.WriteLine("ok - " + name);
            }
            catch (Exception exception)
            {
                failed++;
                Console.WriteLine("not ok - " + name + ": " + exception.Message);
            }
        }
        Console.WriteLine(failed == 0 ? cases.Count + " fixture tests passed" : failed + " fixture test(s) failed");
        return failed == 0 ? 0 : 1;
    }
}
