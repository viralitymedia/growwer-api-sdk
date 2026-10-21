# CatalogueApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**discardMedia**](CatalogueApi.md#discardMedia) | **PUT** /api/v1/projects/{id}/discards/{mediaId} | Discard a media for a project |
| [**favouriteMedia**](CatalogueApi.md#favouriteMedia) | **PUT** /api/v1/projects/{id}/favourites/{mediaId} | Add a media to the favourites of a project |
| [**getCatalogueMedia**](CatalogueApi.md#getCatalogueMedia) | **GET** /api/v1/medias/{id} | Get a media |
| [**listFlashOffers**](CatalogueApi.md#listFlashOffers) | **GET** /api/v1/flash-offers | List flash offers |
| [**requestMedias**](CatalogueApi.md#requestMedias) | **POST** /api/v1/projects/{id}/media-requests | Request specific medias for a project |
| [**searchProjectMedias**](CatalogueApi.md#searchProjectMedias) | **GET** /api/v1/projects/{id}/medias | Search the catalogue for a project |
| [**undiscardMedia**](CatalogueApi.md#undiscardMedia) | **DELETE** /api/v1/projects/{id}/discards/{mediaId} | Restore a discarded media for a project |
| [**unfavouriteMedia**](CatalogueApi.md#unfavouriteMedia) | **DELETE** /api/v1/projects/{id}/favourites/{mediaId} | Remove a media from the favourites of a project |


<a id="discardMedia"></a>
# **discardMedia**
> discardMedia(id, mediaId, idempotencyKey)

Discard a media for a project

Discards a media for one of your projects, as the web does. Discarding it again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The project.
    UUID mediaId = UUID.randomUUID(); // UUID | The media.
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    try {
      apiInstance.discardMedia(id, mediaId, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#discardMedia");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID**| The project. | |
| **mediaId** | **UUID**| The media. | |
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is discarded for the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="favouriteMedia"></a>
# **favouriteMedia**
> favouriteMedia(id, mediaId, idempotencyKey)

Add a media to the favourites of a project

Marks a media as a favourite of one of your projects, as the heart on the web does. Adding a favourite again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The project.
    UUID mediaId = UUID.randomUUID(); // UUID | The media.
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    try {
      apiInstance.favouriteMedia(id, mediaId, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#favouriteMedia");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID**| The project. | |
| **mediaId** | **UUID**| The media. | |
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is a favourite of the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="getCatalogueMedia"></a>
# **getCatalogueMedia**
> CatalogueMedia getCatalogueMedia(id)

Get a media

One media of the catalogue: an active, public media. A media you have ordered is always readable, even if it has since left the catalogue, and is open to every account. Otherwise the catalogue is open to accounts with recent completed orders (see &#x60;catalogue.eligible&#x60; on GET /me), and the media counts towards the distinct medias the account may see per day (UTC). For the media&#39;s state in one of your projects, search the project with GET /projects/{id}/medias.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The media.
    try {
      CatalogueMedia result = apiInstance.getCatalogueMedia(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#getCatalogueMedia");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID**| The media. | |

### Return type

[**CatalogueMedia**](CatalogueMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The media. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The catalogue is open to accounts with recent completed orders, as buyer or as seller, and this account has none (code &#x60;catalogue_requires_recent_order&#x60;). GET /me reports &#x60;catalogue.eligible&#x60;. |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="listFlashOffers"></a>
# **listFlashOffers**
> ListFlashOffers200Response listFlashOffers(projectId, source, sort, domain, websiteType, language, country, topics, notBannedTopics, minTraffic, maxTraffic, trafficTrendUpward, minDomainRating, maxDomainRating, minLinkedToReferringRatio, maxLinkedToReferringRatio, minPostPrice, maxPostPrice, postLinkType, promotedSocialNetwork, withoutAdvertisingLabel, homepageListing, hasLinkAddition, minLinkAdditionPrice, maxLinkAdditionPrice, linkAdditionLinkType, recommended, favourite, requested, bought, discarded, _new, ranksGoalKeyword, ranksAiKeyword, limit, offset)

List flash offers

The medias on a flash offer, a time-limited discount, in the catalogue of one of your projects. It is GET /projects/{id}/medias with &#x60;flashOffer&#x3D;true&#x60;, and takes the same parameters except &#x60;flashOffer&#x60; and &#x60;savedFilterId&#x60;. The catalogue access and the daily distinct-media limit of that operation apply.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    UUID projectId = UUID.randomUUID(); // UUID | The project to search flash offers for.
    String source = "all"; // String | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state.
    String sort = "-growwerRank"; // String | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first.
    String domain = "domain_example"; // String | Medias whose domain contains this text, 1 to 255 characters.
    String websiteType = "websiteType_example"; // String | A comma-separated list of website types: `blog`, `press`.
    String language = "language_example"; // String | A comma-separated list of language codes, as in GET /vocabulary.
    String country = "country_example"; // String | A comma-separated list of country codes, as in GET /vocabulary.
    String topics = "topics_example"; // String | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them.
    Boolean notBannedTopics = true; // Boolean | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise.
    Integer minTraffic = 56; // Integer | Minimum monthly organic traffic.
    Integer maxTraffic = 56; // Integer | Maximum monthly organic traffic.
    Boolean trafficTrendUpward = true; // Boolean | Medias whose traffic is growing. Only `true` applies it; omit it otherwise.
    Integer minDomainRating = 56; // Integer | Minimum domain rating, 0 to 100.
    Integer maxDomainRating = 56; // Integer | Maximum domain rating, 0 to 100.
    BigDecimal minLinkedToReferringRatio = new BigDecimal(78); // BigDecimal | Minimum ratio of linked domains to referring domains, such as 0.5.
    BigDecimal maxLinkedToReferringRatio = new BigDecimal(78); // BigDecimal | Maximum ratio of linked domains to referring domains, such as 1.5.
    Integer minPostPrice = 56; // Integer | Minimum post price, in cents.
    Integer maxPostPrice = 56; // Integer | Maximum post price, in cents.
    String postLinkType = "postLinkType_example"; // String | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`.
    String promotedSocialNetwork = "promotedSocialNetwork_example"; // String | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`.
    Boolean withoutAdvertisingLabel = true; // Boolean | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise.
    Boolean homepageListing = true; // Boolean | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise.
    Boolean hasLinkAddition = true; // Boolean | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise.
    Integer minLinkAdditionPrice = 56; // Integer | Minimum link addition price, in cents.
    Integer maxLinkAdditionPrice = 56; // Integer | Maximum link addition price, in cents.
    String linkAdditionLinkType = "linkAdditionLinkType_example"; // String | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`.
    Boolean recommended = true; // Boolean | `true`: only the medias Growwer recommends for the project; `false`: only the others.
    Boolean favourite = true; // Boolean | `true`: only your favourites for the project; `false`: leave them out.
    Boolean requested = true; // Boolean | `true`: only the medias you requested for the project; `false`: leave them out.
    Boolean bought = true; // Boolean | `true`: only medias you bought for the project; `false`: leave them out.
    Boolean discarded = true; // Boolean | `true`: only the medias you discarded for the project; `false`: leave them out.
    Boolean _new = true; // Boolean | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise.
    String ranksGoalKeyword = "ranksGoalKeyword_example"; // String | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project.
    String ranksAiKeyword = "ranksAiKeyword_example"; // String | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`.
    Integer limit = 20; // Integer | Medias per page, 1 to 100.
    Integer offset = 0; // Integer | Medias to skip, at most 99900.
    try {
      ListFlashOffers200Response result = apiInstance.listFlashOffers(projectId, source, sort, domain, websiteType, language, country, topics, notBannedTopics, minTraffic, maxTraffic, trafficTrendUpward, minDomainRating, maxDomainRating, minLinkedToReferringRatio, maxLinkedToReferringRatio, minPostPrice, maxPostPrice, postLinkType, promotedSocialNetwork, withoutAdvertisingLabel, homepageListing, hasLinkAddition, minLinkAdditionPrice, maxLinkAdditionPrice, linkAdditionLinkType, recommended, favourite, requested, bought, discarded, _new, ranksGoalKeyword, ranksAiKeyword, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#listFlashOffers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectId** | **UUID**| The project to search flash offers for. | |
| **source** | **String**| Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [optional] [enum: all, recommended, favourite, discarded, requested, bought] |
| **sort** | **String**| The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [optional] [enum: -growwerRank, postPrice, linkAdditionPrice, matchedAt, -matchedAt, -traffic, -domainRating, linkedToReferringRatio, -referringDomains] |
| **domain** | **String**| Medias whose domain contains this text, 1 to 255 characters. | [optional] |
| **websiteType** | **String**| A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [optional] |
| **language** | **String**| A comma-separated list of language codes, as in GET /vocabulary. | [optional] |
| **country** | **String**| A comma-separated list of country codes, as in GET /vocabulary. | [optional] |
| **topics** | **String**| A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [optional] |
| **notBannedTopics** | **Boolean**| Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **minTraffic** | **Integer**| Minimum monthly organic traffic. | [optional] |
| **maxTraffic** | **Integer**| Maximum monthly organic traffic. | [optional] |
| **trafficTrendUpward** | **Boolean**| Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **minDomainRating** | **Integer**| Minimum domain rating, 0 to 100. | [optional] |
| **maxDomainRating** | **Integer**| Maximum domain rating, 0 to 100. | [optional] |
| **minLinkedToReferringRatio** | **BigDecimal**| Minimum ratio of linked domains to referring domains, such as 0.5. | [optional] |
| **maxLinkedToReferringRatio** | **BigDecimal**| Maximum ratio of linked domains to referring domains, such as 1.5. | [optional] |
| **minPostPrice** | **Integer**| Minimum post price, in cents. | [optional] |
| **maxPostPrice** | **Integer**| Maximum post price, in cents. | [optional] |
| **postLinkType** | **String**| A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **promotedSocialNetwork** | **String**| A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [optional] |
| **withoutAdvertisingLabel** | **Boolean**| Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **homepageListing** | **Boolean**| Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **hasLinkAddition** | **Boolean**| Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **minLinkAdditionPrice** | **Integer**| Minimum link addition price, in cents. | [optional] |
| **maxLinkAdditionPrice** | **Integer**| Maximum link addition price, in cents. | [optional] |
| **linkAdditionLinkType** | **String**| A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **recommended** | **Boolean**| &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [optional] |
| **favourite** | **Boolean**| &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **requested** | **Boolean**| &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **bought** | **Boolean**| &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **discarded** | **Boolean**| &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **_new** | **Boolean**| Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **ranksGoalKeyword** | **String**| A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [optional] |
| **ranksAiKeyword** | **String**| A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [optional] |
| **limit** | **Integer**| Medias per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **Integer**| Medias to skip, at most 99900. | [optional] [default to 0] |

### Return type

[**ListFlashOffers200Response**](ListFlashOffers200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of flash offers and how many there are in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The catalogue is open to accounts with recent completed orders, as buyer or as seller, and this account has none (code &#x60;catalogue_requires_recent_order&#x60;). GET /me reports &#x60;catalogue.eligible&#x60;. |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="requestMedias"></a>
# **requestMedias**
> RequestMedias201Response requestMedias(id, idempotencyKey, requestMediasRequest)

Request specific medias for a project

Asks Growwer to find the medias of these domains for one of your projects, as the \&quot;request specific domains\&quot; form on the web does. Each entry may be a domain or a URL; it is read as its full domain, lowercased. Repeated domains are requested once, and a domain already requested changes nothing. Up to 200 distinct domains per call. They then appear in the project&#39;s catalogue with &#x60;project.requested&#x60; true (&#x60;requested&#x3D;true&#x60; on GET /projects/{id}/medias) once Growwer lists them.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The project.
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    RequestMediasRequest requestMediasRequest = new RequestMediasRequest(); // RequestMediasRequest | 
    try {
      RequestMedias201Response result = apiInstance.requestMedias(id, idempotencyKey, requestMediasRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#requestMedias");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID**| The project. | |
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **requestMediasRequest** | [**RequestMediasRequest**](RequestMediasRequest.md)|  | |

### Return type

[**RequestMedias201Response**](RequestMedias201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The domains were requested: each distinct domain, as Growwer read it. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="searchProjectMedias"></a>
# **searchProjectMedias**
> ListFlashOffers200Response searchProjectMedias(id, source, sort, savedFilterId, domain, websiteType, language, country, topics, notBannedTopics, minTraffic, maxTraffic, trafficTrendUpward, minDomainRating, maxDomainRating, minLinkedToReferringRatio, maxLinkedToReferringRatio, minPostPrice, maxPostPrice, postLinkType, promotedSocialNetwork, withoutAdvertisingLabel, homepageListing, hasLinkAddition, minLinkAdditionPrice, maxLinkAdditionPrice, linkAdditionLinkType, recommended, favourite, requested, flashOffer, bought, discarded, _new, ranksGoalKeyword, ranksAiKeyword, limit, offset)

Search the catalogue for a project

The medias the catalogue offers for one of your projects, as the web lists them, with each media&#39;s state in the project. Filter with the parameters below, which all combine, or apply one of your saved filters with &#x60;savedFilterId&#x60; alone. The catalogue is open to accounts with recent completed orders (see &#x60;catalogue.eligible&#x60; on GET /me), and each account can see a limited number of distinct medias per day (UTC) across the catalogue operations; medias seen again the same day are free.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The project.
    String source = "all"; // String | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state.
    String sort = "-growwerRank"; // String | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first.
    UUID savedFilterId = UUID.randomUUID(); // UUID | Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, `source` or `sort`. A filter saved on the web that uses a filter the API does not support is refused with 422 `saved_filter_unsupported`.
    String domain = "domain_example"; // String | Medias whose domain contains this text, 1 to 255 characters.
    String websiteType = "websiteType_example"; // String | A comma-separated list of website types: `blog`, `press`.
    String language = "language_example"; // String | A comma-separated list of language codes, as in GET /vocabulary.
    String country = "country_example"; // String | A comma-separated list of country codes, as in GET /vocabulary.
    String topics = "topics_example"; // String | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them.
    Boolean notBannedTopics = true; // Boolean | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise.
    Integer minTraffic = 56; // Integer | Minimum monthly organic traffic.
    Integer maxTraffic = 56; // Integer | Maximum monthly organic traffic.
    Boolean trafficTrendUpward = true; // Boolean | Medias whose traffic is growing. Only `true` applies it; omit it otherwise.
    Integer minDomainRating = 56; // Integer | Minimum domain rating, 0 to 100.
    Integer maxDomainRating = 56; // Integer | Maximum domain rating, 0 to 100.
    BigDecimal minLinkedToReferringRatio = new BigDecimal(78); // BigDecimal | Minimum ratio of linked domains to referring domains, such as 0.5.
    BigDecimal maxLinkedToReferringRatio = new BigDecimal(78); // BigDecimal | Maximum ratio of linked domains to referring domains, such as 1.5.
    Integer minPostPrice = 56; // Integer | Minimum post price, in cents.
    Integer maxPostPrice = 56; // Integer | Maximum post price, in cents.
    String postLinkType = "postLinkType_example"; // String | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`.
    String promotedSocialNetwork = "promotedSocialNetwork_example"; // String | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`.
    Boolean withoutAdvertisingLabel = true; // Boolean | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise.
    Boolean homepageListing = true; // Boolean | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise.
    Boolean hasLinkAddition = true; // Boolean | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise.
    Integer minLinkAdditionPrice = 56; // Integer | Minimum link addition price, in cents.
    Integer maxLinkAdditionPrice = 56; // Integer | Maximum link addition price, in cents.
    String linkAdditionLinkType = "linkAdditionLinkType_example"; // String | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`.
    Boolean recommended = true; // Boolean | `true`: only the medias Growwer recommends for the project; `false`: only the others.
    Boolean favourite = true; // Boolean | `true`: only your favourites for the project; `false`: leave them out.
    Boolean requested = true; // Boolean | `true`: only the medias you requested for the project; `false`: leave them out.
    Boolean flashOffer = true; // Boolean | `true`: only medias with a flash offer running; `false`: leave them out.
    Boolean bought = true; // Boolean | `true`: only medias you bought for the project; `false`: leave them out.
    Boolean discarded = true; // Boolean | `true`: only the medias you discarded for the project; `false`: leave them out.
    Boolean _new = true; // Boolean | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise.
    String ranksGoalKeyword = "ranksGoalKeyword_example"; // String | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project.
    String ranksAiKeyword = "ranksAiKeyword_example"; // String | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`.
    Integer limit = 20; // Integer | Medias per page, 1 to 100.
    Integer offset = 0; // Integer | Medias to skip, at most 99900.
    try {
      ListFlashOffers200Response result = apiInstance.searchProjectMedias(id, source, sort, savedFilterId, domain, websiteType, language, country, topics, notBannedTopics, minTraffic, maxTraffic, trafficTrendUpward, minDomainRating, maxDomainRating, minLinkedToReferringRatio, maxLinkedToReferringRatio, minPostPrice, maxPostPrice, postLinkType, promotedSocialNetwork, withoutAdvertisingLabel, homepageListing, hasLinkAddition, minLinkAdditionPrice, maxLinkAdditionPrice, linkAdditionLinkType, recommended, favourite, requested, flashOffer, bought, discarded, _new, ranksGoalKeyword, ranksAiKeyword, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#searchProjectMedias");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID**| The project. | |
| **source** | **String**| Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [optional] [enum: all, recommended, favourite, discarded, requested, bought] |
| **sort** | **String**| The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [optional] [enum: -growwerRank, postPrice, linkAdditionPrice, matchedAt, -matchedAt, -traffic, -domainRating, linkedToReferringRatio, -referringDomains] |
| **savedFilterId** | **UUID**| Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, &#x60;source&#x60; or &#x60;sort&#x60;. A filter saved on the web that uses a filter the API does not support is refused with 422 &#x60;saved_filter_unsupported&#x60;. | [optional] |
| **domain** | **String**| Medias whose domain contains this text, 1 to 255 characters. | [optional] |
| **websiteType** | **String**| A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [optional] |
| **language** | **String**| A comma-separated list of language codes, as in GET /vocabulary. | [optional] |
| **country** | **String**| A comma-separated list of country codes, as in GET /vocabulary. | [optional] |
| **topics** | **String**| A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [optional] |
| **notBannedTopics** | **Boolean**| Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **minTraffic** | **Integer**| Minimum monthly organic traffic. | [optional] |
| **maxTraffic** | **Integer**| Maximum monthly organic traffic. | [optional] |
| **trafficTrendUpward** | **Boolean**| Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **minDomainRating** | **Integer**| Minimum domain rating, 0 to 100. | [optional] |
| **maxDomainRating** | **Integer**| Maximum domain rating, 0 to 100. | [optional] |
| **minLinkedToReferringRatio** | **BigDecimal**| Minimum ratio of linked domains to referring domains, such as 0.5. | [optional] |
| **maxLinkedToReferringRatio** | **BigDecimal**| Maximum ratio of linked domains to referring domains, such as 1.5. | [optional] |
| **minPostPrice** | **Integer**| Minimum post price, in cents. | [optional] |
| **maxPostPrice** | **Integer**| Maximum post price, in cents. | [optional] |
| **postLinkType** | **String**| A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **promotedSocialNetwork** | **String**| A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [optional] |
| **withoutAdvertisingLabel** | **Boolean**| Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **homepageListing** | **Boolean**| Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **hasLinkAddition** | **Boolean**| Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **minLinkAdditionPrice** | **Integer**| Minimum link addition price, in cents. | [optional] |
| **maxLinkAdditionPrice** | **Integer**| Maximum link addition price, in cents. | [optional] |
| **linkAdditionLinkType** | **String**| A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **recommended** | **Boolean**| &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [optional] |
| **favourite** | **Boolean**| &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **requested** | **Boolean**| &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **flashOffer** | **Boolean**| &#x60;true&#x60;: only medias with a flash offer running; &#x60;false&#x60;: leave them out. | [optional] |
| **bought** | **Boolean**| &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **discarded** | **Boolean**| &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **_new** | **Boolean**| Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **ranksGoalKeyword** | **String**| A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [optional] |
| **ranksAiKeyword** | **String**| A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [optional] |
| **limit** | **Integer**| Medias per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **Integer**| Medias to skip, at most 99900. | [optional] [default to 0] |

### Return type

[**ListFlashOffers200Response**](ListFlashOffers200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of matching medias and how many match in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The catalogue is open to accounts with recent completed orders, as buyer or as seller, and this account has none (code &#x60;catalogue_requires_recent_order&#x60;). GET /me reports &#x60;catalogue.eligible&#x60;. |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **422** | A parameter is not valid (code &#x60;validation_failed&#x60;; &#x60;details.fields&#x60; names it), or the saved filter uses a web filter the API does not support (code &#x60;saved_filter_unsupported&#x60;; &#x60;details.field&#x60; names it). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="undiscardMedia"></a>
# **undiscardMedia**
> undiscardMedia(id, mediaId, idempotencyKey)

Restore a discarded media for a project

Restores a media you discarded for one of your projects. Restoring one that is not discarded changes nothing. It works for any media, even one the catalogue no longer shows.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The project.
    UUID mediaId = UUID.randomUUID(); // UUID | The media.
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    try {
      apiInstance.undiscardMedia(id, mediaId, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#undiscardMedia");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID**| The project. | |
| **mediaId** | **UUID**| The media. | |
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is not discarded for the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="unfavouriteMedia"></a>
# **unfavouriteMedia**
> unfavouriteMedia(id, mediaId, idempotencyKey)

Remove a media from the favourites of a project

Removes a media from the favourites of one of your projects. Removing one that is not a favourite changes nothing. It works for any media, even one the catalogue no longer shows.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The project.
    UUID mediaId = UUID.randomUUID(); // UUID | The media.
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    try {
      apiInstance.unfavouriteMedia(id, mediaId, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#unfavouriteMedia");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID**| The project. | |
| **mediaId** | **UUID**| The media. | |
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is not a favourite of the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

