import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.api.AccountApi;
import com.growwer.api.api.CatalogueApi;
import com.growwer.api.api.OrdersApi;
import com.growwer.api.api.SellerMediasApi;
import com.growwer.api.model.CatalogueMedia;
import com.growwer.api.model.CatalogueOfferOrNull;
import com.growwer.api.model.CataloguePostOffer;
import com.growwer.api.model.GetMe200Response;
import com.growwer.api.model.LinkAdditionOrderBriefing;
import com.growwer.api.model.ListOrders200Response;
import com.growwer.api.model.MoneyOrNull;
import com.growwer.api.model.Order;
import com.growwer.api.model.PostOrderBriefing;
import com.growwer.api.model.SellerFeesOrNull;
import com.growwer.api.model.SellerMedia;
import com.growwer.api.model.SellerMediaPostOfferPricingOptionsInner;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.UUID;
import okhttp3.MediaType;
import okhttp3.Protocol;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.ResponseBody;

/**
 * Deserialises the shared response fixtures through the generated Java client, offline.
 *
 * <p>Each call is answered from tests/fixtures/ by an OkHttp interceptor added to the client's own
 * OkHttpClient, so the whole client path runs: URL, headers, status handling and the models. Run
 * with the single-file source launcher from the repository root.
 */
public class FixtureTest {
    private static final Path FIXTURES = Path.of("tests", "fixtures");
    private static final UUID MEDIA_ID = UUID.fromString("c1d2e3f4-a5b6-4c7d-8e9f-a0b1c2d3e4f5");
    private static final UUID ORDER_ID = UUID.fromString("0b9c6a4e-6f1d-4c39-9a51-2f5d7c1e8a01");

    private final List<Request> sent = new ArrayList<>();

    private static byte[] fixture(String name) throws Exception {
        return Files.readAllBytes(FIXTURES.resolve(name));
    }

    private static void equal(String name, Object actual, Object expected) {
        if (!Objects.deepEquals(actual, expected)) {
            throw new AssertionError(name + " = " + actual + ", want " + expected);
        }
    }

    /** A client whose every call is answered with one canned response, recording what was sent. */
    private ApiClient answer(int status, byte[] body, String contentType, String... headers) {
        sent.clear();
        ApiClient client = new ApiClient();
        client.setBearerToken("test-key");
        client.setHttpClient(client.getHttpClient().newBuilder().addInterceptor(chain -> {
            sent.add(chain.request());
            Response.Builder response = new Response.Builder()
                .request(chain.request())
                .protocol(Protocol.HTTP_1_1)
                .code(status)
                .message("canned")
                .header("Content-Type", contentType)
                .body(ResponseBody.create(body, MediaType.get(contentType)));
            for (int i = 0; i < headers.length; i += 2) {
                response.header(headers[i], headers[i + 1]);
            }
            return response.build();
        }).build());
        return client;
    }

    private ApiClient answer(byte[] body) {
        return answer(200, body, "application/json");
    }

    private Request sent() {
        equal("requests sent", sent.size(), 1);
        return sent.get(0);
    }

    void getMeCallsProductionWithTheBearerKey() throws Exception {
        GetMe200Response me = new AccountApi(answer(fixture("me.json"))).getMe();

        equal("method", sent().method(), "GET");
        equal("url", sent().url().toString(), "https://tool.growwer.com/api/v1/me");
        equal("Authorization", sent().header("Authorization"), "Bearer test-key");
        equal("available", me.getBuyer().getBalance().getAvailable().getAmount(), 250000);
        equal("currency", me.getBuyer().getBalance().getAvailable().getCurrency(), "EUR");
        equal("holidayEndDate", me.getSeller().getHolidayEndDate(), null);
        equal("eligible", me.getCatalogue().getEligible(), true);
    }

    void theBaseUrlIsOverridable() throws Exception {
        ApiClient client = answer(fixture("me.json"));
        client.setBasePath("https://sandbox.example");
        new AccountApi(client).getMe();

        equal("url", sent().url().toString(), "https://sandbox.example/api/v1/me");
    }

    void listOrdersReadsItemsAndTotalWithBothOrderTypes() throws Exception {
        ListOrders200Response page = new OrdersApi(answer(fixture("orders-page.json")))
            .listOrders(null, null, null, null, null, 2, null);

        equal("limit", sent().url().queryParameter("limit"), "2");
        equal("total", page.getTotal(), 42);
        equal("items", page.getItems().size(), 2);
        Order post = page.getItems().get(0);
        Order linkAddition = page.getItems().get(1);

        equal("post type", post.getType().getValue(), "post");
        equal("post pendingAction", post.getPendingAction(), null);
        equal("post delivery", post.getDelivery(), null);
        equal("post draft", post.getDraft(), null);
        equal("post scheduledPublicationDate", post.getScheduledPublicationDate(), null);
        equal("post price", post.getPrice().getAmount(), 12500);
        equal("post createdAt", post.getCreatedAt().toInstant(),
            OffsetDateTime.of(2026, 10, 1, 9, 30, 0, 0, ZoneOffset.UTC).toInstant());
        PostOrderBriefing postBriefing = post.getBriefing().getPostOrderBriefing();
        equal("post title", postBriefing.getTitle(), null);
        equal("post link type", postBriefing.getLinks().get(0).getType().getValue(), "dofollow");
        equal("post reason", post.getStateHistory().get(0).getReason(), null);
        equal("post channel", post.getChannel().getCreated().getValue(), "api");

        equal("link type", linkAddition.getType().getValue(), "link_addition");
        equal("link pendingAction", linkAddition.getPendingAction(), null);
        equal("link delivery", linkAddition.getDelivery(), null);
        equal("link draft", linkAddition.getDraft(), null);
        equal("link project id", linkAddition.getProject().getId(), null);
        LinkAdditionOrderBriefing linkBriefing = linkAddition.getBriefing().getLinkAdditionOrderBriefing();
        equal("linkingFrom", linkBriefing.getLinkingFrom(), "https://blog.example/best-trails");
        equal("anchor", linkBriefing.getLink().getAnchor(), null);
        equal("reason code", linkAddition.getStateHistory().get(1).getReason().getCode().getValue(), "no_seller_response");
        equal("reason info", linkAddition.getStateHistory().get(1).getReason().getAdditionalInfo(), null);
    }

    void anOrderWithFieldsThisClientDoesNotKnowStillDeserialises() throws Exception {
        Order order = new OrdersApi(answer(fixture("order-with-unknown-field.json"))).getOrder(ORDER_ID);

        equal("path", sent().url().encodedPath(), "/api/v1/orders/" + ORDER_ID);
        equal("id", order.getId(), ORDER_ID);
        equal("pendingAction", order.getPendingAction().getValue(), "seller");
        equal("hasFile", order.getDraft().getHasFile(), true);
        equal("channel", order.getChannel().getCreated().getValue(), "api");
        equal("briefing type", order.getBriefing().getActualInstance().getClass(), PostOrderBriefing.class);
        equal("title", order.getBriefing().getPostOrderBriefing().getTitle(), "Choosing running shoes");
        equal("link type", order.getBriefing().getPostOrderBriefing().getLinks().get(0).getType().getValue(), "dofollow");
    }

    void aLinkAdditionOrderWithFieldsThisClientDoesNotKnowStillDeserialises() throws Exception {
        Order order = new OrdersApi(answer(fixture("link-addition-order-with-unknown-field.json"))).getOrder(ORDER_ID);

        equal("type", order.getType().getValue(), "link_addition");
        equal("briefing type", order.getBriefing().getActualInstance().getClass(), LinkAdditionOrderBriefing.class);
        LinkAdditionOrderBriefing briefing = order.getBriefing().getLinkAdditionOrderBriefing();
        equal("linkingFrom", briefing.getLinkingFrom(), "https://blog.example/best-trails");
        equal("anchor", briefing.getLink().getAnchor(), "trail shoes");
        equal("link type", briefing.getLink().getType().getValue(), "nofollow");
    }

    void aCatalogueMediaReadsANullPreviousPriceAndLinkAdditionOffer() throws Exception {
        CatalogueMedia media = new CatalogueApi(answer(fixture("catalogue-media.json"))).getCatalogueMedia(MEDIA_ID);

        equal("linkAdditionOffer", media.getLinkAdditionOffer(), null);
        equal("flashOffer", media.getFlashOffer(), null);
        equal("country", media.getCountry(), null);
        equal("referringDomains", media.getMetrics().getReferringDomains(), null);
        equal("organicTraffic", media.getMetrics().getOrganicTraffic().intValue(), 15400);
        equal("price", media.getPostOffer().getPrice().getAmount(), 9000);
        equal("previousPrice", media.getPostOffer().getPreviousPrice(), null);
        equal("nofollow", media.getPostOffer().getPrices().get("nofollow").getAmount(), 7000);
        equal("homepageListing", media.getPostOffer().getExtras().getHomepageListing(), null);
        equal("extraPrice", media.getPostOffer().getExtras().getSensitiveTopic().getExtraPrice(), null);
    }

    void aCatalogueMediaReadsANullLinkTypeBesidePresentOffers() throws Exception {
        CatalogueMedia media = new CatalogueApi(answer(fixture("catalogue-media-null-link-type.json")))
            .getCatalogueMedia(MEDIA_ID);

        CataloguePostOffer postOffer = media.getPostOffer();
        equal("postOffer linkType", postOffer.getLinkType(), null);
        equal("prices", postOffer.getPrices(), Map.of());
        MoneyOrNull previousPrice = postOffer.getPreviousPrice();
        equal("previousPrice", previousPrice.getAmount(), 20000);
        equal("homepageListing", postOffer.getExtras().getHomepageListing().getAmount(), 2500);
        equal("extraPrice", postOffer.getExtras().getSensitiveTopic().getExtraPrice().getAmount(), 3000);
        CatalogueOfferOrNull offer = media.getLinkAdditionOffer();
        if (offer == null) {
            throw new AssertionError("linkAdditionOffer: got null, want an offer");
        }
        equal("linkAdditionOffer linkType", offer.getLinkType(), null);
        equal("linkAdditionOffer price", offer.getPrice().getAmount(), 6000);
        equal("linkAdditionOffer previousPrice", offer.getPreviousPrice(), null);
    }

    void aSellerMediaReadsNullCompetitiveFees() throws Exception {
        SellerMedia media = new SellerMediasApi(answer(fixture("seller-media.json"))).getSellerMedia(MEDIA_ID);

        equal("competitiveFees", media.getCompetitiveFees(), null);
        equal("linkAdditionOffer", media.getLinkAdditionOffer(), null);
        SellerMediaPostOfferPricingOptionsInner option = media.getPostOffer().getPricingOptions().get(0);
        equal("feeWhenSellerWritesPost", option.getFeeWhenSellerWritesPost().getAmount(), 6000);
        equal("feeWhenSellerDoesNotWritePost", option.getFeeWhenSellerDoesNotWritePost(), null);
        equal("currentCost", option.getCurrentCost(), null);
        equal("extra cost", media.getPostOffer().getExtraServices().get(0).getCost().getAmount(), 1500);
    }

    void aSellerMediaReadsCompetitiveFeesWithOneSideNull() throws Exception {
        SellerMedia media = new SellerMediasApi(answer(fixture("seller-media-competitive-fees.json")))
            .getSellerMedia(MEDIA_ID);

        SellerFeesOrNull fees = media.getCompetitiveFees();
        if (fees == null) {
            throw new AssertionError("competitiveFees: got null, want fees");
        }
        equal("feeWhenSellerWritesPost", fees.getFeeWhenSellerWritesPost().getAmount(), 5400);
        equal("feeWhenSellerDoesNotWritePost", fees.getFeeWhenSellerDoesNotWritePost(), null);
    }

    void theErrorEnvelopeIsReadableFromTheException() throws Exception {
        CatalogueApi api = new CatalogueApi(answer(429, fixture("error.json"), "application/json",
            "Retry-After", "3600", "X-Request-Id", "0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34"));

        try {
            api.getCatalogueMedia(MEDIA_ID);
            throw new AssertionError("a 429 must throw");
        } catch (ApiException exception) {
            equal("status", exception.getCode(), 429);
            Map<String, List<String>> headers = exception.getResponseHeaders();
            equal("Retry-After", headers.get("Retry-After"), List.of("3600"));
            equal("X-Request-Id", headers.get("X-Request-Id"), List.of("0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34"));
            com.growwer.api.model.Error envelope = com.growwer.api.model.Error.fromJson(exception.getResponseBody());
            equal("code", envelope.getCode(), "catalogue_daily_cap_reached");
            equal("requestId", envelope.getRequestId(), "0b8f6c2e-4a1d-4f3b-9c7e-5d2a8e1f6b34");
            equal("details", ((Number) envelope.getDetails().get("remaining")).intValue(), 0);
        }
    }

    void aBinaryDownloadReturnsTheExactBytes() throws Exception {
        byte[] body = fixture("briefing.bin");
        File file = new OrdersApi(answer(200, body, "application/octet-stream",
            "Content-Disposition", "attachment; filename=\"briefing.docx\"")).downloadOrderBriefing(ORDER_ID);

        try {
            equal("path", sent().url().encodedPath(), "/api/v1/orders/" + ORDER_ID + "/briefing");
            equal("bytes", Files.readAllBytes(file.toPath()), body);
        } finally {
            Files.deleteIfExists(file.toPath());
        }
    }

    @FunctionalInterface
    interface Case {
        void run() throws Exception;
    }

    public static void main(String[] args) throws Exception {
        FixtureTest test = new FixtureTest();
        Map<String, Case> cases = new java.util.LinkedHashMap<>();
        cases.put("getMe calls production with the bearer key", test::getMeCallsProductionWithTheBearerKey);
        cases.put("the base URL is overridable", test::theBaseUrlIsOverridable);
        cases.put("listOrders reads items and total, with both order types", test::listOrdersReadsItemsAndTotalWithBothOrderTypes);
        cases.put("an order with fields this client does not know still deserialises", test::anOrderWithFieldsThisClientDoesNotKnowStillDeserialises);
        cases.put("a link addition order with fields this client does not know still deserialises", test::aLinkAdditionOrderWithFieldsThisClientDoesNotKnowStillDeserialises);
        cases.put("a catalogue media reads a null previousPrice and linkAdditionOffer", test::aCatalogueMediaReadsANullPreviousPriceAndLinkAdditionOffer);
        cases.put("a catalogue media reads a null linkType beside present offers", test::aCatalogueMediaReadsANullLinkTypeBesidePresentOffers);
        cases.put("a seller media reads null competitiveFees", test::aSellerMediaReadsNullCompetitiveFees);
        cases.put("a seller media reads competitiveFees with one side null", test::aSellerMediaReadsCompetitiveFeesWithOneSideNull);
        cases.put("the error envelope is readable from the ApiException", test::theErrorEnvelopeIsReadableFromTheException);
        cases.put("a binary download returns the exact bytes", test::aBinaryDownloadReturnsTheExactBytes);
        for (Map.Entry<String, Case> entry : cases.entrySet()) {
            entry.getValue().run();
            System.out.println("ok - " + entry.getKey());
        }
        System.out.println(cases.size() + " fixture tests passed");
    }
}
