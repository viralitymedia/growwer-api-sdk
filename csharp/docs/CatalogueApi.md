# Growwer.Api.Api.CatalogueApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**DiscardMedia**](CatalogueApi.md#discardmedia) | **PUT** /api/v1/projects/{id}/discards/{mediaId} | Discard a media for a project |
| [**FavouriteMedia**](CatalogueApi.md#favouritemedia) | **PUT** /api/v1/projects/{id}/favourites/{mediaId} | Add a media to the favourites of a project |
| [**GetCatalogueMedia**](CatalogueApi.md#getcataloguemedia) | **GET** /api/v1/medias/{id} | Get a media |
| [**ListFlashOffers**](CatalogueApi.md#listflashoffers) | **GET** /api/v1/flash-offers | List flash offers |
| [**RequestMedias**](CatalogueApi.md#requestmedias) | **POST** /api/v1/projects/{id}/media-requests | Request specific medias for a project |
| [**SearchProjectMedias**](CatalogueApi.md#searchprojectmedias) | **GET** /api/v1/projects/{id}/medias | Search the catalogue for a project |
| [**UndiscardMedia**](CatalogueApi.md#undiscardmedia) | **DELETE** /api/v1/projects/{id}/discards/{mediaId} | Restore a discarded media for a project |
| [**UnfavouriteMedia**](CatalogueApi.md#unfavouritemedia) | **DELETE** /api/v1/projects/{id}/favourites/{mediaId} | Remove a media from the favourites of a project |

<a id="discardmedia"></a>
# **DiscardMedia**
> void DiscardMedia (Guid id, Guid mediaId, string idempotencyKey)

Discard a media for a project

Discards a media for one of your projects, as the web does. Discarding it again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class DiscardMediaExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new CatalogueApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | The project.
            var mediaId = "mediaId_example";  // Guid | The media.
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

            try
            {
                // Discard a media for a project
                apiInstance.DiscardMedia(id, mediaId, idempotencyKey);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CatalogueApi.DiscardMedia: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DiscardMediaWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Discard a media for a project
    apiInstance.DiscardMediaWithHttpInfo(id, mediaId, idempotencyKey);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CatalogueApi.DiscardMediaWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | The project. |  |
| **mediaId** | **Guid** | The media. |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is discarded for the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="favouritemedia"></a>
# **FavouriteMedia**
> void FavouriteMedia (Guid id, Guid mediaId, string idempotencyKey)

Add a media to the favourites of a project

Marks a media as a favourite of one of your projects, as the heart on the web does. Adding a favourite again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class FavouriteMediaExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new CatalogueApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | The project.
            var mediaId = "mediaId_example";  // Guid | The media.
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

            try
            {
                // Add a media to the favourites of a project
                apiInstance.FavouriteMedia(id, mediaId, idempotencyKey);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CatalogueApi.FavouriteMedia: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the FavouriteMediaWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Add a media to the favourites of a project
    apiInstance.FavouriteMediaWithHttpInfo(id, mediaId, idempotencyKey);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CatalogueApi.FavouriteMediaWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | The project. |  |
| **mediaId** | **Guid** | The media. |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is a favourite of the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getcataloguemedia"></a>
# **GetCatalogueMedia**
> CatalogueMedia GetCatalogueMedia (Guid id)

Get a media

One media of the catalogue: an active, public media. A media you have ordered is always readable, even if it has since left the catalogue, and is open to every account. Otherwise the media counts towards the distinct medias the account may see per day (UTC): the full daily cap for accounts with recent completed orders, a smaller trial quota for other accounts (see `catalogue.eligible`, `catalogue.dailyCap` and `catalogue.remainingToday` on GET /me). For the media's state in one of your projects, search the project with GET /projects/{id}/medias.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class GetCatalogueMediaExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new CatalogueApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | The media.

            try
            {
                // Get a media
                CatalogueMedia result = apiInstance.GetCatalogueMedia(id);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CatalogueApi.GetCatalogueMedia: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetCatalogueMediaWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get a media
    ApiResponse<CatalogueMedia> response = apiInstance.GetCatalogueMediaWithHttpInfo(id);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CatalogueApi.GetCatalogueMediaWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | The media. |  |

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
| **403** | The catalogue is open to accounts with recent completed orders, as buyer or as seller, and to other accounts within a daily trial quota; this account has no such order and the trial quota is off (code &#x60;catalogue_requires_recent_order&#x60;). GET /me reports &#x60;catalogue.eligible&#x60; and &#x60;catalogue.dailyCap&#x60;. |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listflashoffers"></a>
# **ListFlashOffers**
> ListFlashOffers200Response ListFlashOffers (Guid projectId, string? source = null, string? sort = null, string? domain = null, string? websiteType = null, string? language = null, string? country = null, string? topics = null, bool? notBannedTopics = null, int? minTraffic = null, int? maxTraffic = null, bool? trafficTrendUpward = null, int? minDomainRating = null, int? maxDomainRating = null, decimal? minLinkedToReferringRatio = null, decimal? maxLinkedToReferringRatio = null, int? minPostPrice = null, int? maxPostPrice = null, string? postLinkType = null, string? promotedSocialNetwork = null, bool? withoutAdvertisingLabel = null, bool? homepageListing = null, bool? hasLinkAddition = null, int? minLinkAdditionPrice = null, int? maxLinkAdditionPrice = null, string? linkAdditionLinkType = null, bool? recommended = null, bool? favourite = null, bool? requested = null, bool? bought = null, bool? discarded = null, bool? varNew = null, string? ranksGoalKeyword = null, string? ranksAiKeyword = null, int? limit = null, int? offset = null)

List flash offers

The medias on a flash offer, a time-limited discount, in the catalogue of one of your projects. It is GET /projects/{id}/medias with `flashOffer=true`, and takes the same parameters except `flashOffer` and `savedFilterId`. The catalogue access and the daily limit of that operation apply: each new media costs one unit, a page that holds no new media, an empty one included, costs one, and repeating a request already answered the same day is free while the media lists, topics and language of the project stay as they were.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class ListFlashOffersExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new CatalogueApi(httpClient, config, httpClientHandler);
            var projectId = "projectId_example";  // Guid | The project to search flash offers for.
            var source = "all";  // string? | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state. (optional) 
            var sort = "-growwerRank";  // string? | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first. (optional) 
            var domain = "domain_example";  // string? | Medias whose domain contains this text, 1 to 255 characters. (optional) 
            var websiteType = "websiteType_example";  // string? | A comma-separated list of website types: `blog`, `press`. (optional) 
            var language = "language_example";  // string? | A comma-separated list of language codes, as in GET /vocabulary. (optional) 
            var country = "country_example";  // string? | A comma-separated list of country codes, as in GET /vocabulary. (optional) 
            var topics = "topics_example";  // string? | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. (optional) 
            var notBannedTopics = true;  // bool? | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise. (optional) 
            var minTraffic = 56;  // int? | Minimum monthly organic traffic. (optional) 
            var maxTraffic = 56;  // int? | Maximum monthly organic traffic. (optional) 
            var trafficTrendUpward = true;  // bool? | Medias whose traffic is growing. Only `true` applies it; omit it otherwise. (optional) 
            var minDomainRating = 56;  // int? | Minimum domain rating, 0 to 100. (optional) 
            var maxDomainRating = 56;  // int? | Maximum domain rating, 0 to 100. (optional) 
            var minLinkedToReferringRatio = 8.14D;  // decimal? | Minimum ratio of linked domains to referring domains, such as 0.5. (optional) 
            var maxLinkedToReferringRatio = 8.14D;  // decimal? | Maximum ratio of linked domains to referring domains, such as 1.5. (optional) 
            var minPostPrice = 56;  // int? | Minimum post price, in cents. (optional) 
            var maxPostPrice = 56;  // int? | Maximum post price, in cents. (optional) 
            var postLinkType = "postLinkType_example";  // string? | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`. (optional) 
            var promotedSocialNetwork = "promotedSocialNetwork_example";  // string? | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`. (optional) 
            var withoutAdvertisingLabel = true;  // bool? | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise. (optional) 
            var homepageListing = true;  // bool? | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise. (optional) 
            var hasLinkAddition = true;  // bool? | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise. (optional) 
            var minLinkAdditionPrice = 56;  // int? | Minimum link addition price, in cents. (optional) 
            var maxLinkAdditionPrice = 56;  // int? | Maximum link addition price, in cents. (optional) 
            var linkAdditionLinkType = "linkAdditionLinkType_example";  // string? | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`. (optional) 
            var recommended = true;  // bool? | `true`: only the medias Growwer recommends for the project; `false`: only the others. (optional) 
            var favourite = true;  // bool? | `true`: only your favourites for the project; `false`: leave them out. (optional) 
            var requested = true;  // bool? | `true`: only the medias you requested for the project; `false`: leave them out. (optional) 
            var bought = true;  // bool? | `true`: only medias you bought for the project; `false`: leave them out. (optional) 
            var discarded = true;  // bool? | `true`: only the medias you discarded for the project; `false`: leave them out. (optional) 
            var varNew = true;  // bool? | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise. (optional) 
            var ranksGoalKeyword = "ranksGoalKeyword_example";  // string? | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project. (optional) 
            var ranksAiKeyword = "ranksAiKeyword_example";  // string? | A comma-separated list of AI answer engines: medias the web lists an AI keyword of the project for, from any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`. (optional) 
            var limit = 20;  // int? | Medias per page, 1 to 100. (optional)  (default to 20)
            var offset = 0;  // int? | Medias to skip, at most 99900. (optional)  (default to 0)

            try
            {
                // List flash offers
                ListFlashOffers200Response result = apiInstance.ListFlashOffers(projectId, source, sort, domain, websiteType, language, country, topics, notBannedTopics, minTraffic, maxTraffic, trafficTrendUpward, minDomainRating, maxDomainRating, minLinkedToReferringRatio, maxLinkedToReferringRatio, minPostPrice, maxPostPrice, postLinkType, promotedSocialNetwork, withoutAdvertisingLabel, homepageListing, hasLinkAddition, minLinkAdditionPrice, maxLinkAdditionPrice, linkAdditionLinkType, recommended, favourite, requested, bought, discarded, varNew, ranksGoalKeyword, ranksAiKeyword, limit, offset);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CatalogueApi.ListFlashOffers: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListFlashOffersWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List flash offers
    ApiResponse<ListFlashOffers200Response> response = apiInstance.ListFlashOffersWithHttpInfo(projectId, source, sort, domain, websiteType, language, country, topics, notBannedTopics, minTraffic, maxTraffic, trafficTrendUpward, minDomainRating, maxDomainRating, minLinkedToReferringRatio, maxLinkedToReferringRatio, minPostPrice, maxPostPrice, postLinkType, promotedSocialNetwork, withoutAdvertisingLabel, homepageListing, hasLinkAddition, minLinkAdditionPrice, maxLinkAdditionPrice, linkAdditionLinkType, recommended, favourite, requested, bought, discarded, varNew, ranksGoalKeyword, ranksAiKeyword, limit, offset);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CatalogueApi.ListFlashOffersWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The project to search flash offers for. |  |
| **source** | **string?** | Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [optional]  |
| **sort** | **string?** | The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [optional]  |
| **domain** | **string?** | Medias whose domain contains this text, 1 to 255 characters. | [optional]  |
| **websiteType** | **string?** | A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [optional]  |
| **language** | **string?** | A comma-separated list of language codes, as in GET /vocabulary. | [optional]  |
| **country** | **string?** | A comma-separated list of country codes, as in GET /vocabulary. | [optional]  |
| **topics** | **string?** | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [optional]  |
| **notBannedTopics** | **bool?** | Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **minTraffic** | **int?** | Minimum monthly organic traffic. | [optional]  |
| **maxTraffic** | **int?** | Maximum monthly organic traffic. | [optional]  |
| **trafficTrendUpward** | **bool?** | Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **minDomainRating** | **int?** | Minimum domain rating, 0 to 100. | [optional]  |
| **maxDomainRating** | **int?** | Maximum domain rating, 0 to 100. | [optional]  |
| **minLinkedToReferringRatio** | **decimal?** | Minimum ratio of linked domains to referring domains, such as 0.5. | [optional]  |
| **maxLinkedToReferringRatio** | **decimal?** | Maximum ratio of linked domains to referring domains, such as 1.5. | [optional]  |
| **minPostPrice** | **int?** | Minimum post price, in cents. | [optional]  |
| **maxPostPrice** | **int?** | Maximum post price, in cents. | [optional]  |
| **postLinkType** | **string?** | A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional]  |
| **promotedSocialNetwork** | **string?** | A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [optional]  |
| **withoutAdvertisingLabel** | **bool?** | Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **homepageListing** | **bool?** | Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **hasLinkAddition** | **bool?** | Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **minLinkAdditionPrice** | **int?** | Minimum link addition price, in cents. | [optional]  |
| **maxLinkAdditionPrice** | **int?** | Maximum link addition price, in cents. | [optional]  |
| **linkAdditionLinkType** | **string?** | A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional]  |
| **recommended** | **bool?** | &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [optional]  |
| **favourite** | **bool?** | &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [optional]  |
| **requested** | **bool?** | &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [optional]  |
| **bought** | **bool?** | &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [optional]  |
| **discarded** | **bool?** | &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [optional]  |
| **varNew** | **bool?** | Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **ranksGoalKeyword** | **string?** | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [optional]  |
| **ranksAiKeyword** | **string?** | A comma-separated list of AI answer engines: medias the web lists an AI keyword of the project for, from any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [optional]  |
| **limit** | **int?** | Medias per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int?** | Medias to skip, at most 99900. | [optional] [default to 0] |

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
| **403** | The catalogue is open to accounts with recent completed orders, as buyer or as seller, and to other accounts within a daily trial quota; this account has no such order and the trial quota is off (code &#x60;catalogue_requires_recent_order&#x60;). GET /me reports &#x60;catalogue.eligible&#x60; and &#x60;catalogue.dailyCap&#x60;. |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="requestmedias"></a>
# **RequestMedias**
> RequestMedias201Response RequestMedias (Guid id, string idempotencyKey, RequestMediasRequest requestMediasRequest)

Request specific medias for a project

Asks Growwer to find the medias of these domains for one of your projects, as the \"request specific domains\" form on the web does. Each entry may be a domain or a URL; it is read as its full domain, lowercased. Repeated domains are requested once, and a domain already requested changes nothing. Up to 200 distinct domains per call. They then appear in the project's catalogue with `project.requested` true (`requested=true` on GET /projects/{id}/medias) once Growwer lists them.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class RequestMediasExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new CatalogueApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | The project.
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var requestMediasRequest = new RequestMediasRequest(); // RequestMediasRequest | 

            try
            {
                // Request specific medias for a project
                RequestMedias201Response result = apiInstance.RequestMedias(id, idempotencyKey, requestMediasRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CatalogueApi.RequestMedias: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the RequestMediasWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Request specific medias for a project
    ApiResponse<RequestMedias201Response> response = apiInstance.RequestMediasWithHttpInfo(id, idempotencyKey, requestMediasRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CatalogueApi.RequestMediasWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | The project. |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **requestMediasRequest** | [**RequestMediasRequest**](RequestMediasRequest.md) |  |  |

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
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="searchprojectmedias"></a>
# **SearchProjectMedias**
> ListFlashOffers200Response SearchProjectMedias (Guid id, string? source = null, string? sort = null, Guid? savedFilterId = null, string? domain = null, string? websiteType = null, string? language = null, string? country = null, string? topics = null, bool? notBannedTopics = null, int? minTraffic = null, int? maxTraffic = null, bool? trafficTrendUpward = null, int? minDomainRating = null, int? maxDomainRating = null, decimal? minLinkedToReferringRatio = null, decimal? maxLinkedToReferringRatio = null, int? minPostPrice = null, int? maxPostPrice = null, string? postLinkType = null, string? promotedSocialNetwork = null, bool? withoutAdvertisingLabel = null, bool? homepageListing = null, bool? hasLinkAddition = null, int? minLinkAdditionPrice = null, int? maxLinkAdditionPrice = null, string? linkAdditionLinkType = null, bool? recommended = null, bool? favourite = null, bool? requested = null, bool? flashOffer = null, bool? bought = null, bool? discarded = null, bool? varNew = null, string? ranksGoalKeyword = null, string? ranksAiKeyword = null, int? limit = null, int? offset = null)

Search the catalogue for a project

The medias the catalogue offers for one of your projects, as the web lists them, with each media's state in the project. Filter with the parameters below, which all combine, or apply one of your saved filters with `savedFilterId` alone. Each account can see a limited number of distinct medias per day (UTC) across the catalogue operations: the full daily cap for accounts with recent completed orders, as buyer or as seller, and a smaller trial quota for other accounts, which rises to the full cap after a completed order (see `catalogue.eligible`, `catalogue.dailyCap` and `catalogue.remainingToday` on GET /me). Each new media of a page costs one unit of that limit, and a page that holds no new media, an empty one included, costs one unit, so a `total` costs at least one; repeating a request already answered the same day is free, and so are medias seen again that day. A change of the media lists of the project (a media request, a favourite, a discard), its topics or its language makes the same request a new one.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class SearchProjectMediasExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new CatalogueApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | The project.
            var source = "all";  // string? | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state. (optional) 
            var sort = "-growwerRank";  // string? | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first. (optional) 
            var savedFilterId = "savedFilterId_example";  // Guid? | Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, `source` or `sort`. A filter saved on the web that uses a filter the API does not support is refused with 422 `saved_filter_unsupported`. (optional) 
            var domain = "domain_example";  // string? | Medias whose domain contains this text, 1 to 255 characters. (optional) 
            var websiteType = "websiteType_example";  // string? | A comma-separated list of website types: `blog`, `press`. (optional) 
            var language = "language_example";  // string? | A comma-separated list of language codes, as in GET /vocabulary. (optional) 
            var country = "country_example";  // string? | A comma-separated list of country codes, as in GET /vocabulary. (optional) 
            var topics = "topics_example";  // string? | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. (optional) 
            var notBannedTopics = true;  // bool? | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise. (optional) 
            var minTraffic = 56;  // int? | Minimum monthly organic traffic. (optional) 
            var maxTraffic = 56;  // int? | Maximum monthly organic traffic. (optional) 
            var trafficTrendUpward = true;  // bool? | Medias whose traffic is growing. Only `true` applies it; omit it otherwise. (optional) 
            var minDomainRating = 56;  // int? | Minimum domain rating, 0 to 100. (optional) 
            var maxDomainRating = 56;  // int? | Maximum domain rating, 0 to 100. (optional) 
            var minLinkedToReferringRatio = 8.14D;  // decimal? | Minimum ratio of linked domains to referring domains, such as 0.5. (optional) 
            var maxLinkedToReferringRatio = 8.14D;  // decimal? | Maximum ratio of linked domains to referring domains, such as 1.5. (optional) 
            var minPostPrice = 56;  // int? | Minimum post price, in cents. (optional) 
            var maxPostPrice = 56;  // int? | Maximum post price, in cents. (optional) 
            var postLinkType = "postLinkType_example";  // string? | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`. (optional) 
            var promotedSocialNetwork = "promotedSocialNetwork_example";  // string? | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`. (optional) 
            var withoutAdvertisingLabel = true;  // bool? | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise. (optional) 
            var homepageListing = true;  // bool? | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise. (optional) 
            var hasLinkAddition = true;  // bool? | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise. (optional) 
            var minLinkAdditionPrice = 56;  // int? | Minimum link addition price, in cents. (optional) 
            var maxLinkAdditionPrice = 56;  // int? | Maximum link addition price, in cents. (optional) 
            var linkAdditionLinkType = "linkAdditionLinkType_example";  // string? | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`. (optional) 
            var recommended = true;  // bool? | `true`: only the medias Growwer recommends for the project; `false`: only the others. (optional) 
            var favourite = true;  // bool? | `true`: only your favourites for the project; `false`: leave them out. (optional) 
            var requested = true;  // bool? | `true`: only the medias you requested for the project; `false`: leave them out. (optional) 
            var flashOffer = true;  // bool? | `true`: only medias with a flash offer running; `false`: leave them out. (optional) 
            var bought = true;  // bool? | `true`: only medias you bought for the project; `false`: leave them out. (optional) 
            var discarded = true;  // bool? | `true`: only the medias you discarded for the project; `false`: leave them out. (optional) 
            var varNew = true;  // bool? | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise. (optional) 
            var ranksGoalKeyword = "ranksGoalKeyword_example";  // string? | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project. (optional) 
            var ranksAiKeyword = "ranksAiKeyword_example";  // string? | A comma-separated list of AI answer engines: medias the web lists an AI keyword of the project for, from any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`. (optional) 
            var limit = 20;  // int? | Medias per page, 1 to 100. (optional)  (default to 20)
            var offset = 0;  // int? | Medias to skip, at most 99900. (optional)  (default to 0)

            try
            {
                // Search the catalogue for a project
                ListFlashOffers200Response result = apiInstance.SearchProjectMedias(id, source, sort, savedFilterId, domain, websiteType, language, country, topics, notBannedTopics, minTraffic, maxTraffic, trafficTrendUpward, minDomainRating, maxDomainRating, minLinkedToReferringRatio, maxLinkedToReferringRatio, minPostPrice, maxPostPrice, postLinkType, promotedSocialNetwork, withoutAdvertisingLabel, homepageListing, hasLinkAddition, minLinkAdditionPrice, maxLinkAdditionPrice, linkAdditionLinkType, recommended, favourite, requested, flashOffer, bought, discarded, varNew, ranksGoalKeyword, ranksAiKeyword, limit, offset);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CatalogueApi.SearchProjectMedias: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the SearchProjectMediasWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search the catalogue for a project
    ApiResponse<ListFlashOffers200Response> response = apiInstance.SearchProjectMediasWithHttpInfo(id, source, sort, savedFilterId, domain, websiteType, language, country, topics, notBannedTopics, minTraffic, maxTraffic, trafficTrendUpward, minDomainRating, maxDomainRating, minLinkedToReferringRatio, maxLinkedToReferringRatio, minPostPrice, maxPostPrice, postLinkType, promotedSocialNetwork, withoutAdvertisingLabel, homepageListing, hasLinkAddition, minLinkAdditionPrice, maxLinkAdditionPrice, linkAdditionLinkType, recommended, favourite, requested, flashOffer, bought, discarded, varNew, ranksGoalKeyword, ranksAiKeyword, limit, offset);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CatalogueApi.SearchProjectMediasWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | The project. |  |
| **source** | **string?** | Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [optional]  |
| **sort** | **string?** | The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [optional]  |
| **savedFilterId** | **Guid?** | Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, &#x60;source&#x60; or &#x60;sort&#x60;. A filter saved on the web that uses a filter the API does not support is refused with 422 &#x60;saved_filter_unsupported&#x60;. | [optional]  |
| **domain** | **string?** | Medias whose domain contains this text, 1 to 255 characters. | [optional]  |
| **websiteType** | **string?** | A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [optional]  |
| **language** | **string?** | A comma-separated list of language codes, as in GET /vocabulary. | [optional]  |
| **country** | **string?** | A comma-separated list of country codes, as in GET /vocabulary. | [optional]  |
| **topics** | **string?** | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [optional]  |
| **notBannedTopics** | **bool?** | Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **minTraffic** | **int?** | Minimum monthly organic traffic. | [optional]  |
| **maxTraffic** | **int?** | Maximum monthly organic traffic. | [optional]  |
| **trafficTrendUpward** | **bool?** | Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **minDomainRating** | **int?** | Minimum domain rating, 0 to 100. | [optional]  |
| **maxDomainRating** | **int?** | Maximum domain rating, 0 to 100. | [optional]  |
| **minLinkedToReferringRatio** | **decimal?** | Minimum ratio of linked domains to referring domains, such as 0.5. | [optional]  |
| **maxLinkedToReferringRatio** | **decimal?** | Maximum ratio of linked domains to referring domains, such as 1.5. | [optional]  |
| **minPostPrice** | **int?** | Minimum post price, in cents. | [optional]  |
| **maxPostPrice** | **int?** | Maximum post price, in cents. | [optional]  |
| **postLinkType** | **string?** | A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional]  |
| **promotedSocialNetwork** | **string?** | A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [optional]  |
| **withoutAdvertisingLabel** | **bool?** | Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **homepageListing** | **bool?** | Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **hasLinkAddition** | **bool?** | Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **minLinkAdditionPrice** | **int?** | Minimum link addition price, in cents. | [optional]  |
| **maxLinkAdditionPrice** | **int?** | Maximum link addition price, in cents. | [optional]  |
| **linkAdditionLinkType** | **string?** | A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional]  |
| **recommended** | **bool?** | &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [optional]  |
| **favourite** | **bool?** | &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [optional]  |
| **requested** | **bool?** | &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [optional]  |
| **flashOffer** | **bool?** | &#x60;true&#x60;: only medias with a flash offer running; &#x60;false&#x60;: leave them out. | [optional]  |
| **bought** | **bool?** | &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [optional]  |
| **discarded** | **bool?** | &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [optional]  |
| **varNew** | **bool?** | Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional]  |
| **ranksGoalKeyword** | **string?** | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [optional]  |
| **ranksAiKeyword** | **string?** | A comma-separated list of AI answer engines: medias the web lists an AI keyword of the project for, from any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [optional]  |
| **limit** | **int?** | Medias per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int?** | Medias to skip, at most 99900. | [optional] [default to 0] |

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
| **403** | The catalogue is open to accounts with recent completed orders, as buyer or as seller, and to other accounts within a daily trial quota; this account has no such order and the trial quota is off (code &#x60;catalogue_requires_recent_order&#x60;). GET /me reports &#x60;catalogue.eligible&#x60; and &#x60;catalogue.dailyCap&#x60;. |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **422** | A parameter is not valid (code &#x60;validation_failed&#x60;; &#x60;details.fields&#x60; names it), or the saved filter uses a web filter the API does not support (code &#x60;saved_filter_unsupported&#x60;; &#x60;details.field&#x60; names it). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="undiscardmedia"></a>
# **UndiscardMedia**
> void UndiscardMedia (Guid id, Guid mediaId, string idempotencyKey)

Restore a discarded media for a project

Restores a media you discarded for one of your projects. Restoring one that is not discarded changes nothing. It works for any media, even one the catalogue no longer shows.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class UndiscardMediaExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new CatalogueApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | The project.
            var mediaId = "mediaId_example";  // Guid | The media.
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

            try
            {
                // Restore a discarded media for a project
                apiInstance.UndiscardMedia(id, mediaId, idempotencyKey);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CatalogueApi.UndiscardMedia: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UndiscardMediaWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Restore a discarded media for a project
    apiInstance.UndiscardMediaWithHttpInfo(id, mediaId, idempotencyKey);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CatalogueApi.UndiscardMediaWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | The project. |  |
| **mediaId** | **Guid** | The media. |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is not discarded for the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="unfavouritemedia"></a>
# **UnfavouriteMedia**
> void UnfavouriteMedia (Guid id, Guid mediaId, string idempotencyKey)

Remove a media from the favourites of a project

Removes a media from the favourites of one of your projects. Removing one that is not a favourite changes nothing. It works for any media, even one the catalogue no longer shows.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class UnfavouriteMediaExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new CatalogueApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | The project.
            var mediaId = "mediaId_example";  // Guid | The media.
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

            try
            {
                // Remove a media from the favourites of a project
                apiInstance.UnfavouriteMedia(id, mediaId, idempotencyKey);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CatalogueApi.UnfavouriteMedia: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UnfavouriteMediaWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Remove a media from the favourites of a project
    apiInstance.UnfavouriteMediaWithHttpInfo(id, mediaId, idempotencyKey);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CatalogueApi.UnfavouriteMediaWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | The project. |  |
| **mediaId** | **Guid** | The media. |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is not a favourite of the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

