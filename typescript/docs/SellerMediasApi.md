# SellerMediasApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applySellerMediaCompetitiveFees**](SellerMediasApi.md#applysellermediacompetitivefees) | **POST** /api/v1/seller/medias/{id}/apply-competitive-fees | Set the competitive fees Growwer suggests |
| [**getSellerMedia**](SellerMediasApi.md#getsellermedia) | **GET** /api/v1/seller/medias/{id} | Get a media you sell on |
| [**listSellerMedias**](SellerMediasApi.md#listsellermedias) | **GET** /api/v1/seller/medias | List the medias you sell on |
| [**updateSellerMedia**](SellerMediasApi.md#updatesellermediaoperation) | **PATCH** /api/v1/seller/medias/{id} | Edit the fees of a media you sell on |



## applySellerMediaCompetitiveFees

> SellerMedia applySellerMediaCompetitiveFees(id, idempotencyKey)

Set the competitive fees Growwer suggests

Sets your post fees for the media to the competitive fees Growwer suggests, the &#x60;competitiveFees&#x60; of GET /seller/medias/{id}, as the button on the media edit page does. Each link type you offer gets the suggested fee on each side it already has a fee for; no link type gains a side it did not offer.  Two differences from the page: a side Growwer has no suggestion for keeps your fee (the page clears it), and the fixed fee the page falls back to when it cannot find a competitive one is never applied (the page applies it). When neither side has a suggestion, nothing changes and the answer is 409 &#x60;no_competitive_fees&#x60;. When your fees already are the suggested ones, or the suggestion is only for a side none of your link types offers, nothing changes and the answer is 200.  The fees set are your base fees: a running flash offer keeps discounting them. As with a fee edit, a change of the price may cancel the managed-service proposals accepted for the media whose price it changes. Send no body, or an empty object.

### Example

```ts
import {
  Configuration,
  SellerMediasApi,
} from '@growwer/api';
import type { ApplySellerMediaCompetitiveFeesRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SellerMediasApi(config);

  const body = {
    // string
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
  } satisfies ApplySellerMediaCompetitiveFeesRequest;

  try {
    const data = await api.applySellerMediaCompetitiveFees(body);
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
| **id** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The media, with the suggested fees set. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | Growwer has no competitive fees to suggest for the media now (code &#x60;no_competitive_fees&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is not empty, or the fees set break a rule of the media edit page (code &#x60;validation_failed&#x60;). Nothing changed. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getSellerMedia

> SellerMedia getSellerMedia(id)

Get a media you sell on

One of your medias, with your fees, its extras, the competitive fees Growwer suggests and how it performs. Another seller\&#39;s media is not found.

### Example

```ts
import {
  Configuration,
  SellerMediasApi,
} from '@growwer/api';
import type { GetSellerMediaRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SellerMediasApi(config);

  const body = {
    // string
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetSellerMediaRequest;

  try {
    const data = await api.getSellerMedia(body);
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
| **id** | `string` |  | [Defaults to `undefined`] |

### Return type

[**SellerMedia**](SellerMedia.md)

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
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSellerMedias

> ListSellerMedias200Response listSellerMedias(state, sort, limit, offset)

List the medias you sell on

Your medias in every state, with your fees and how they perform, newest first by default.

### Example

```ts
import {
  Configuration,
  SellerMediasApi,
} from '@growwer/api';
import type { ListSellerMediasRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SellerMediasApi(config);

  const body = {
    // string | Only the medias in one of these states, comma-separated: `analyzing`, `pending_review`, `active`, `deactivated`. An unknown state is refused with 422. (optional)
    state: active,deactivated,
    // '-createdAt' | 'createdAt' | '-numPublishedOrders' | 'numPublishedOrders' | '-publicationRate' | 'publicationRate' | By creation date, number of published orders or publication rate; a leading `-` sorts descending. Medias with no publication rate come first ascending, last descending. Ties come in id order. (optional)
    sort: sort_example,
    // number | Medias per page, 1 to 100. (optional)
    limit: 56,
    // number | Medias to skip. (optional)
    offset: 56,
  } satisfies ListSellerMediasRequest;

  try {
    const data = await api.listSellerMedias(body);
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
| **state** | `string` | Only the medias in one of these states, comma-separated: &#x60;analyzing&#x60;, &#x60;pending_review&#x60;, &#x60;active&#x60;, &#x60;deactivated&#x60;. An unknown state is refused with 422. | [Optional] [Defaults to `undefined`] |
| **sort** | `-createdAt`, `createdAt`, `-numPublishedOrders`, `numPublishedOrders`, `-publicationRate`, `publicationRate` | By creation date, number of published orders or publication rate; a leading &#x60;-&#x60; sorts descending. Medias with no publication rate come first ascending, last descending. Ties come in id order. | [Optional] [Defaults to `&#39;-createdAt&#39;`] [Enum: -createdAt, createdAt, -numPublishedOrders, numPublishedOrders, -publicationRate, publicationRate] |
| **limit** | `number` | Medias per page, 1 to 100. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Medias to skip. | [Optional] [Defaults to `0`] |

### Return type

[**ListSellerMedias200Response**](ListSellerMedias200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of your medias and how many match in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateSellerMedia

> SellerMedia updateSellerMedia(id, idempotencyKey, updateSellerMediaRequest)

Edit the fees of a media you sell on

Sets the fees of one of your medias, as the media edit page saves them. Send only the sections you change: a section you send replaces that section wholly, a section you leave out stays as it is.  - &#x60;postOffer.pricingOptions&#x60; lists every link type you offer for sponsored posts, at least one. A link type you leave out is no longer offered. Each option needs at least one fee, and every option must offer the same sides (written by you, written by the buyer or Growwer), as the page requires. Each fee is at least 1 EUR. - &#x60;linkAdditionOffer.pricingOptions&#x60; lists the link types you offer for adding a link to an existing article; &#x60;null&#x60; or an empty list stops offering link additions. - &#x60;extraServices&#x60; is the full list of extra services you offer; an empty list removes them all.  The fees are your base fees, the ones GET /seller/medias/{id} returns: while a flash offer runs, its discount keeps applying on top of them, and &#x60;currentCost&#x60; shows the result. &#x60;currentCost&#x60; may be sent back as read and is ignored. Characteristics, topics and comments are not edited here.  As on the page, a change of the post offer\&#39;s price may cancel the managed-service proposals accepted for the media whose price it changes, and raising the price above the best competitor\&#39;s tells Growwer\&#39;s support team. A restricted seller account may edit its fees.

### Example

```ts
import {
  Configuration,
  SellerMediasApi,
} from '@growwer/api';
import type { UpdateSellerMediaOperationRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SellerMediasApi(config);

  const body = {
    // string
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
    // UpdateSellerMediaRequest
    updateSellerMediaRequest: {"postOffer":{"pricingOptions":[{"linkType":"dofollow","feeWhenSellerWritesPost":{"amount":12000,"currency":"EUR"},"feeWhenSellerDoesNotWritePost":{"amount":10000,"currency":"EUR"}},{"linkType":"nofollow","feeWhenSellerWritesPost":{"amount":9000,"currency":"EUR"},"feeWhenSellerDoesNotWritePost":{"amount":7000,"currency":"EUR"}}]},"linkAdditionOffer":null,"extraServices":[{"name":"list_on_homepage","cost":{"amount":5000,"currency":"EUR"}}]},
  } satisfies UpdateSellerMediaOperationRequest;

  try {
    const data = await api.updateSellerMedia(body);
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
| **id** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |
| **updateSellerMediaRequest** | [UpdateSellerMediaRequest](UpdateSellerMediaRequest.md) |  | |

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The media, with the fees saved. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is not valid (code &#x60;validation_failed&#x60;): &#x60;details.fields&#x60; names each field by its path in the body, such as &#x60;postOffer.pricingOptions.0.feeWhenSellerWritesPost&#x60;, with the rule the media edit page applies. Nothing changed. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

