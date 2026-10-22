# CatalogueApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**discardMedia**](CatalogueApi.md#discardmedia) | **PUT** /api/v1/projects/{id}/discards/{mediaId} | Discard a media for a project |
| [**favouriteMedia**](CatalogueApi.md#favouritemedia) | **PUT** /api/v1/projects/{id}/favourites/{mediaId} | Add a media to the favourites of a project |
| [**getCatalogueMedia**](CatalogueApi.md#getcataloguemedia) | **GET** /api/v1/medias/{id} | Get a media |
| [**listFlashOffers**](CatalogueApi.md#listflashoffers) | **GET** /api/v1/flash-offers | List flash offers |
| [**requestMedias**](CatalogueApi.md#requestmediasoperation) | **POST** /api/v1/projects/{id}/media-requests | Request specific medias for a project |
| [**searchProjectMedias**](CatalogueApi.md#searchprojectmedias) | **GET** /api/v1/projects/{id}/medias | Search the catalogue for a project |
| [**undiscardMedia**](CatalogueApi.md#undiscardmedia) | **DELETE** /api/v1/projects/{id}/discards/{mediaId} | Restore a discarded media for a project |
| [**unfavouriteMedia**](CatalogueApi.md#unfavouritemedia) | **DELETE** /api/v1/projects/{id}/favourites/{mediaId} | Remove a media from the favourites of a project |



## discardMedia

> discardMedia(id, mediaId, idempotencyKey)

Discard a media for a project

Discards a media for one of your projects, as the web does. Discarding it again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

### Example

```ts
import {
  Configuration,
  CatalogueApi,
} from '@growwer/api';
import type { DiscardMediaRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CatalogueApi(config);

  const body = {
    // string | The project.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | The media.
    mediaId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
  } satisfies DiscardMediaRequest;

  try {
    const data = await api.discardMedia(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` | The project. | [Defaults to `undefined`] |
| **mediaId** | `string` | The media. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is discarded for the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## favouriteMedia

> favouriteMedia(id, mediaId, idempotencyKey)

Add a media to the favourites of a project

Marks a media as a favourite of one of your projects, as the heart on the web does. Adding a favourite again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

### Example

```ts
import {
  Configuration,
  CatalogueApi,
} from '@growwer/api';
import type { FavouriteMediaRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CatalogueApi(config);

  const body = {
    // string | The project.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | The media.
    mediaId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
  } satisfies FavouriteMediaRequest;

  try {
    const data = await api.favouriteMedia(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` | The project. | [Defaults to `undefined`] |
| **mediaId** | `string` | The media. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is a favourite of the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getCatalogueMedia

> CatalogueMedia getCatalogueMedia(id)

Get a media

One media of the catalogue: an active, public media. A media you have ordered is always readable, even if it has since left the catalogue, and is open to every account. Otherwise the catalogue is open to accounts with recent completed orders (see &#x60;catalogue.eligible&#x60; on GET /me), and the media counts towards the distinct medias the account may see per day (UTC). For the media\&#39;s state in one of your projects, search the project with GET /projects/{id}/medias.

### Example

```ts
import {
  Configuration,
  CatalogueApi,
} from '@growwer/api';
import type { GetCatalogueMediaRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CatalogueApi(config);

  const body = {
    // string | The media.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetCatalogueMediaRequest;

  try {
    const data = await api.getCatalogueMedia(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` | The media. | [Defaults to `undefined`] |

### Return type

[**CatalogueMedia**](CatalogueMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


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

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listFlashOffers

> ListFlashOffers200Response listFlashOffers(projectId, source, sort, domain, websiteType, language, country, topics, notBannedTopics, minTraffic, maxTraffic, trafficTrendUpward, minDomainRating, maxDomainRating, minLinkedToReferringRatio, maxLinkedToReferringRatio, minPostPrice, maxPostPrice, postLinkType, promotedSocialNetwork, withoutAdvertisingLabel, homepageListing, hasLinkAddition, minLinkAdditionPrice, maxLinkAdditionPrice, linkAdditionLinkType, recommended, favourite, requested, bought, discarded, _new, ranksGoalKeyword, ranksAiKeyword, limit, offset)

List flash offers

The medias on a flash offer, a time-limited discount, in the catalogue of one of your projects. It is GET /projects/{id}/medias with &#x60;flashOffer&#x3D;true&#x60;, and takes the same parameters except &#x60;flashOffer&#x60; and &#x60;savedFilterId&#x60;. The catalogue access and the daily distinct-media limit of that operation apply.

### Example

```ts
import {
  Configuration,
  CatalogueApi,
} from '@growwer/api';
import type { ListFlashOffersRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CatalogueApi(config);

  const body = {
    // string | The project to search flash offers for.
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // 'all' | 'recommended' | 'favourite' | 'discarded' | 'requested' | 'bought' | Which of the project\'s medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state. (optional)
    source: source_example,
    // '-growwerRank' | 'postPrice' | 'linkAdditionPrice' | 'matchedAt' | '-matchedAt' | '-traffic' | '-domainRating' | 'linkedToReferringRatio' | '-referringDomains' | The order. Without it, the web\'s default order: medias on the project\'s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first. (optional)
    sort: sort_example,
    // string | Medias whose domain contains this text, 1 to 255 characters. (optional)
    domain: domain_example,
    // string | A comma-separated list of website types: `blog`, `press`. (optional)
    websiteType: websiteType_example,
    // string | A comma-separated list of language codes, as in GET /vocabulary. (optional)
    language: language_example,
    // string | A comma-separated list of country codes, as in GET /vocabulary. (optional)
    country: country_example,
    // string | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. (optional)
    topics: topics_example,
    // boolean | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise. (optional)
    notBannedTopics: true,
    // number | Minimum monthly organic traffic. (optional)
    minTraffic: 56,
    // number | Maximum monthly organic traffic. (optional)
    maxTraffic: 56,
    // boolean | Medias whose traffic is growing. Only `true` applies it; omit it otherwise. (optional)
    trafficTrendUpward: true,
    // number | Minimum domain rating, 0 to 100. (optional)
    minDomainRating: 56,
    // number | Maximum domain rating, 0 to 100. (optional)
    maxDomainRating: 56,
    // number | Minimum ratio of linked domains to referring domains, such as 0.5. (optional)
    minLinkedToReferringRatio: 8.14,
    // number | Maximum ratio of linked domains to referring domains, such as 1.5. (optional)
    maxLinkedToReferringRatio: 8.14,
    // number | Minimum post price, in cents. (optional)
    minPostPrice: 56,
    // number | Maximum post price, in cents. (optional)
    maxPostPrice: 56,
    // string | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`. (optional)
    postLinkType: postLinkType_example,
    // string | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`. (optional)
    promotedSocialNetwork: promotedSocialNetwork_example,
    // boolean | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise. (optional)
    withoutAdvertisingLabel: true,
    // boolean | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise. (optional)
    homepageListing: true,
    // boolean | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise. (optional)
    hasLinkAddition: true,
    // number | Minimum link addition price, in cents. (optional)
    minLinkAdditionPrice: 56,
    // number | Maximum link addition price, in cents. (optional)
    maxLinkAdditionPrice: 56,
    // string | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`. (optional)
    linkAdditionLinkType: linkAdditionLinkType_example,
    // boolean | `true`: only the medias Growwer recommends for the project; `false`: only the others. (optional)
    recommended: true,
    // boolean | `true`: only your favourites for the project; `false`: leave them out. (optional)
    favourite: true,
    // boolean | `true`: only the medias you requested for the project; `false`: leave them out. (optional)
    requested: true,
    // boolean | `true`: only medias you bought for the project; `false`: leave them out. (optional)
    bought: true,
    // boolean | `true`: only the medias you discarded for the project; `false`: leave them out. (optional)
    discarded: true,
    // boolean | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise. (optional)
    _new: true,
    // string | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project. (optional)
    ranksGoalKeyword: ranksGoalKeyword_example,
    // string | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`. (optional)
    ranksAiKeyword: ranksAiKeyword_example,
    // number | Medias per page, 1 to 100. (optional)
    limit: 56,
    // number | Medias to skip, at most 99900. (optional)
    offset: 56,
  } satisfies ListFlashOffersRequest;

  try {
    const data = await api.listFlashOffers(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectId** | `string` | The project to search flash offers for. | [Defaults to `undefined`] |
| **source** | `all`, `recommended`, `favourite`, `discarded`, `requested`, `bought` | Which of the project\&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [Optional] [Defaults to `undefined`] [Enum: all, recommended, favourite, discarded, requested, bought] |
| **sort** | `-growwerRank`, `postPrice`, `linkAdditionPrice`, `matchedAt`, `-matchedAt`, `-traffic`, `-domainRating`, `linkedToReferringRatio`, `-referringDomains` | The order. Without it, the web\&#39;s default order: medias on the project\&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [Optional] [Defaults to `undefined`] [Enum: -growwerRank, postPrice, linkAdditionPrice, matchedAt, -matchedAt, -traffic, -domainRating, linkedToReferringRatio, -referringDomains] |
| **domain** | `string` | Medias whose domain contains this text, 1 to 255 characters. | [Optional] [Defaults to `undefined`] |
| **websiteType** | `string` | A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [Optional] [Defaults to `undefined`] |
| **language** | `string` | A comma-separated list of language codes, as in GET /vocabulary. | [Optional] [Defaults to `undefined`] |
| **country** | `string` | A comma-separated list of country codes, as in GET /vocabulary. | [Optional] [Defaults to `undefined`] |
| **topics** | `string` | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [Optional] [Defaults to `undefined`] |
| **notBannedTopics** | `boolean` | Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **minTraffic** | `number` | Minimum monthly organic traffic. | [Optional] [Defaults to `undefined`] |
| **maxTraffic** | `number` | Maximum monthly organic traffic. | [Optional] [Defaults to `undefined`] |
| **trafficTrendUpward** | `boolean` | Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **minDomainRating** | `number` | Minimum domain rating, 0 to 100. | [Optional] [Defaults to `undefined`] |
| **maxDomainRating** | `number` | Maximum domain rating, 0 to 100. | [Optional] [Defaults to `undefined`] |
| **minLinkedToReferringRatio** | `number` | Minimum ratio of linked domains to referring domains, such as 0.5. | [Optional] [Defaults to `undefined`] |
| **maxLinkedToReferringRatio** | `number` | Maximum ratio of linked domains to referring domains, such as 1.5. | [Optional] [Defaults to `undefined`] |
| **minPostPrice** | `number` | Minimum post price, in cents. | [Optional] [Defaults to `undefined`] |
| **maxPostPrice** | `number` | Maximum post price, in cents. | [Optional] [Defaults to `undefined`] |
| **postLinkType** | `string` | A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [Optional] [Defaults to `undefined`] |
| **promotedSocialNetwork** | `string` | A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [Optional] [Defaults to `undefined`] |
| **withoutAdvertisingLabel** | `boolean` | Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **homepageListing** | `boolean` | Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **hasLinkAddition** | `boolean` | Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **minLinkAdditionPrice** | `number` | Minimum link addition price, in cents. | [Optional] [Defaults to `undefined`] |
| **maxLinkAdditionPrice** | `number` | Maximum link addition price, in cents. | [Optional] [Defaults to `undefined`] |
| **linkAdditionLinkType** | `string` | A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [Optional] [Defaults to `undefined`] |
| **recommended** | `boolean` | &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [Optional] [Defaults to `undefined`] |
| **favourite** | `boolean` | &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [Optional] [Defaults to `undefined`] |
| **requested** | `boolean` | &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [Optional] [Defaults to `undefined`] |
| **bought** | `boolean` | &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [Optional] [Defaults to `undefined`] |
| **discarded** | `boolean` | &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [Optional] [Defaults to `undefined`] |
| **_new** | `boolean` | Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **ranksGoalKeyword** | `string` | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [Optional] [Defaults to `undefined`] |
| **ranksAiKeyword** | `string` | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [Optional] [Defaults to `undefined`] |
| **limit** | `number` | Medias per page, 1 to 100. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Medias to skip, at most 99900. | [Optional] [Defaults to `0`] |

### Return type

[**ListFlashOffers200Response**](ListFlashOffers200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


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

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## requestMedias

> RequestMedias201Response requestMedias(id, idempotencyKey, requestMediasRequest)

Request specific medias for a project

Asks Growwer to find the medias of these domains for one of your projects, as the \&quot;request specific domains\&quot; form on the web does. Each entry may be a domain or a URL; it is read as its full domain, lowercased. Repeated domains are requested once, and a domain already requested changes nothing. Up to 200 distinct domains per call. They then appear in the project\&#39;s catalogue with &#x60;project.requested&#x60; true (&#x60;requested&#x3D;true&#x60; on GET /projects/{id}/medias) once Growwer lists them.

### Example

```ts
import {
  Configuration,
  CatalogueApi,
} from '@growwer/api';
import type { RequestMediasOperationRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CatalogueApi(config);

  const body = {
    // string | The project.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
    // RequestMediasRequest
    requestMediasRequest: ...,
  } satisfies RequestMediasOperationRequest;

  try {
    const data = await api.requestMedias(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` | The project. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |
| **requestMediasRequest** | [RequestMediasRequest](RequestMediasRequest.md) |  | |

### Return type

[**RequestMedias201Response**](RequestMedias201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


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
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## searchProjectMedias

> ListFlashOffers200Response searchProjectMedias(id, source, sort, savedFilterId, domain, websiteType, language, country, topics, notBannedTopics, minTraffic, maxTraffic, trafficTrendUpward, minDomainRating, maxDomainRating, minLinkedToReferringRatio, maxLinkedToReferringRatio, minPostPrice, maxPostPrice, postLinkType, promotedSocialNetwork, withoutAdvertisingLabel, homepageListing, hasLinkAddition, minLinkAdditionPrice, maxLinkAdditionPrice, linkAdditionLinkType, recommended, favourite, requested, flashOffer, bought, discarded, _new, ranksGoalKeyword, ranksAiKeyword, limit, offset)

Search the catalogue for a project

The medias the catalogue offers for one of your projects, as the web lists them, with each media\&#39;s state in the project. Filter with the parameters below, which all combine, or apply one of your saved filters with &#x60;savedFilterId&#x60; alone. The catalogue is open to accounts with recent completed orders (see &#x60;catalogue.eligible&#x60; on GET /me), and each account can see a limited number of distinct medias per day (UTC) across the catalogue operations; medias seen again the same day are free.

### Example

```ts
import {
  Configuration,
  CatalogueApi,
} from '@growwer/api';
import type { SearchProjectMediasRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CatalogueApi(config);

  const body = {
    // string | The project.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // 'all' | 'recommended' | 'favourite' | 'discarded' | 'requested' | 'bought' | Which of the project\'s medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state. (optional)
    source: source_example,
    // '-growwerRank' | 'postPrice' | 'linkAdditionPrice' | 'matchedAt' | '-matchedAt' | '-traffic' | '-domainRating' | 'linkedToReferringRatio' | '-referringDomains' | The order. Without it, the web\'s default order: medias on the project\'s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first. (optional)
    sort: sort_example,
    // string | Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, `source` or `sort`. A filter saved on the web that uses a filter the API does not support is refused with 422 `saved_filter_unsupported`. (optional)
    savedFilterId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Medias whose domain contains this text, 1 to 255 characters. (optional)
    domain: domain_example,
    // string | A comma-separated list of website types: `blog`, `press`. (optional)
    websiteType: websiteType_example,
    // string | A comma-separated list of language codes, as in GET /vocabulary. (optional)
    language: language_example,
    // string | A comma-separated list of country codes, as in GET /vocabulary. (optional)
    country: country_example,
    // string | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. (optional)
    topics: topics_example,
    // boolean | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise. (optional)
    notBannedTopics: true,
    // number | Minimum monthly organic traffic. (optional)
    minTraffic: 56,
    // number | Maximum monthly organic traffic. (optional)
    maxTraffic: 56,
    // boolean | Medias whose traffic is growing. Only `true` applies it; omit it otherwise. (optional)
    trafficTrendUpward: true,
    // number | Minimum domain rating, 0 to 100. (optional)
    minDomainRating: 56,
    // number | Maximum domain rating, 0 to 100. (optional)
    maxDomainRating: 56,
    // number | Minimum ratio of linked domains to referring domains, such as 0.5. (optional)
    minLinkedToReferringRatio: 8.14,
    // number | Maximum ratio of linked domains to referring domains, such as 1.5. (optional)
    maxLinkedToReferringRatio: 8.14,
    // number | Minimum post price, in cents. (optional)
    minPostPrice: 56,
    // number | Maximum post price, in cents. (optional)
    maxPostPrice: 56,
    // string | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`. (optional)
    postLinkType: postLinkType_example,
    // string | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`. (optional)
    promotedSocialNetwork: promotedSocialNetwork_example,
    // boolean | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise. (optional)
    withoutAdvertisingLabel: true,
    // boolean | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise. (optional)
    homepageListing: true,
    // boolean | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise. (optional)
    hasLinkAddition: true,
    // number | Minimum link addition price, in cents. (optional)
    minLinkAdditionPrice: 56,
    // number | Maximum link addition price, in cents. (optional)
    maxLinkAdditionPrice: 56,
    // string | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`. (optional)
    linkAdditionLinkType: linkAdditionLinkType_example,
    // boolean | `true`: only the medias Growwer recommends for the project; `false`: only the others. (optional)
    recommended: true,
    // boolean | `true`: only your favourites for the project; `false`: leave them out. (optional)
    favourite: true,
    // boolean | `true`: only the medias you requested for the project; `false`: leave them out. (optional)
    requested: true,
    // boolean | `true`: only medias with a flash offer running; `false`: leave them out. (optional)
    flashOffer: true,
    // boolean | `true`: only medias you bought for the project; `false`: leave them out. (optional)
    bought: true,
    // boolean | `true`: only the medias you discarded for the project; `false`: leave them out. (optional)
    discarded: true,
    // boolean | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise. (optional)
    _new: true,
    // string | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project. (optional)
    ranksGoalKeyword: ranksGoalKeyword_example,
    // string | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`. (optional)
    ranksAiKeyword: ranksAiKeyword_example,
    // number | Medias per page, 1 to 100. (optional)
    limit: 56,
    // number | Medias to skip, at most 99900. (optional)
    offset: 56,
  } satisfies SearchProjectMediasRequest;

  try {
    const data = await api.searchProjectMedias(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` | The project. | [Defaults to `undefined`] |
| **source** | `all`, `recommended`, `favourite`, `discarded`, `requested`, `bought` | Which of the project\&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [Optional] [Defaults to `undefined`] [Enum: all, recommended, favourite, discarded, requested, bought] |
| **sort** | `-growwerRank`, `postPrice`, `linkAdditionPrice`, `matchedAt`, `-matchedAt`, `-traffic`, `-domainRating`, `linkedToReferringRatio`, `-referringDomains` | The order. Without it, the web\&#39;s default order: medias on the project\&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [Optional] [Defaults to `undefined`] [Enum: -growwerRank, postPrice, linkAdditionPrice, matchedAt, -matchedAt, -traffic, -domainRating, linkedToReferringRatio, -referringDomains] |
| **savedFilterId** | `string` | Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, &#x60;source&#x60; or &#x60;sort&#x60;. A filter saved on the web that uses a filter the API does not support is refused with 422 &#x60;saved_filter_unsupported&#x60;. | [Optional] [Defaults to `undefined`] |
| **domain** | `string` | Medias whose domain contains this text, 1 to 255 characters. | [Optional] [Defaults to `undefined`] |
| **websiteType** | `string` | A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [Optional] [Defaults to `undefined`] |
| **language** | `string` | A comma-separated list of language codes, as in GET /vocabulary. | [Optional] [Defaults to `undefined`] |
| **country** | `string` | A comma-separated list of country codes, as in GET /vocabulary. | [Optional] [Defaults to `undefined`] |
| **topics** | `string` | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [Optional] [Defaults to `undefined`] |
| **notBannedTopics** | `boolean` | Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **minTraffic** | `number` | Minimum monthly organic traffic. | [Optional] [Defaults to `undefined`] |
| **maxTraffic** | `number` | Maximum monthly organic traffic. | [Optional] [Defaults to `undefined`] |
| **trafficTrendUpward** | `boolean` | Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **minDomainRating** | `number` | Minimum domain rating, 0 to 100. | [Optional] [Defaults to `undefined`] |
| **maxDomainRating** | `number` | Maximum domain rating, 0 to 100. | [Optional] [Defaults to `undefined`] |
| **minLinkedToReferringRatio** | `number` | Minimum ratio of linked domains to referring domains, such as 0.5. | [Optional] [Defaults to `undefined`] |
| **maxLinkedToReferringRatio** | `number` | Maximum ratio of linked domains to referring domains, such as 1.5. | [Optional] [Defaults to `undefined`] |
| **minPostPrice** | `number` | Minimum post price, in cents. | [Optional] [Defaults to `undefined`] |
| **maxPostPrice** | `number` | Maximum post price, in cents. | [Optional] [Defaults to `undefined`] |
| **postLinkType** | `string` | A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [Optional] [Defaults to `undefined`] |
| **promotedSocialNetwork** | `string` | A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [Optional] [Defaults to `undefined`] |
| **withoutAdvertisingLabel** | `boolean` | Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **homepageListing** | `boolean` | Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **hasLinkAddition** | `boolean` | Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **minLinkAdditionPrice** | `number` | Minimum link addition price, in cents. | [Optional] [Defaults to `undefined`] |
| **maxLinkAdditionPrice** | `number` | Maximum link addition price, in cents. | [Optional] [Defaults to `undefined`] |
| **linkAdditionLinkType** | `string` | A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [Optional] [Defaults to `undefined`] |
| **recommended** | `boolean` | &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [Optional] [Defaults to `undefined`] |
| **favourite** | `boolean` | &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [Optional] [Defaults to `undefined`] |
| **requested** | `boolean` | &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [Optional] [Defaults to `undefined`] |
| **flashOffer** | `boolean` | &#x60;true&#x60;: only medias with a flash offer running; &#x60;false&#x60;: leave them out. | [Optional] [Defaults to `undefined`] |
| **bought** | `boolean` | &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [Optional] [Defaults to `undefined`] |
| **discarded** | `boolean` | &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [Optional] [Defaults to `undefined`] |
| **_new** | `boolean` | Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [Optional] [Defaults to `undefined`] |
| **ranksGoalKeyword** | `string` | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [Optional] [Defaults to `undefined`] |
| **ranksAiKeyword** | `string` | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [Optional] [Defaults to `undefined`] |
| **limit** | `number` | Medias per page, 1 to 100. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Medias to skip, at most 99900. | [Optional] [Defaults to `0`] |

### Return type

[**ListFlashOffers200Response**](ListFlashOffers200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


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

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## undiscardMedia

> undiscardMedia(id, mediaId, idempotencyKey)

Restore a discarded media for a project

Restores a media you discarded for one of your projects. Restoring one that is not discarded changes nothing. It works for any media, even one the catalogue no longer shows.

### Example

```ts
import {
  Configuration,
  CatalogueApi,
} from '@growwer/api';
import type { UndiscardMediaRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CatalogueApi(config);

  const body = {
    // string | The project.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | The media.
    mediaId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
  } satisfies UndiscardMediaRequest;

  try {
    const data = await api.undiscardMedia(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` | The project. | [Defaults to `undefined`] |
| **mediaId** | `string` | The media. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is not discarded for the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## unfavouriteMedia

> unfavouriteMedia(id, mediaId, idempotencyKey)

Remove a media from the favourites of a project

Removes a media from the favourites of one of your projects. Removing one that is not a favourite changes nothing. It works for any media, even one the catalogue no longer shows.

### Example

```ts
import {
  Configuration,
  CatalogueApi,
} from '@growwer/api';
import type { UnfavouriteMediaRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CatalogueApi(config);

  const body = {
    // string | The project.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | The media.
    mediaId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
  } satisfies UnfavouriteMediaRequest;

  try {
    const data = await api.unfavouriteMedia(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` | The project. | [Defaults to `undefined`] |
| **mediaId** | `string` | The media. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The media is not a favourite of the project. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

