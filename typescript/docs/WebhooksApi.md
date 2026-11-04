# WebhooksApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWebhook**](WebhooksApi.md#createwebhookoperation) | **POST** /api/v1/webhooks | Create a webhook subscription |
| [**deleteWebhook**](WebhooksApi.md#deletewebhook) | **DELETE** /api/v1/webhooks/{id} | Delete a webhook subscription |
| [**getWebhook**](WebhooksApi.md#getwebhook) | **GET** /api/v1/webhooks/{id} | Get a webhook subscription |
| [**listWebhookDeliveries**](WebhooksApi.md#listwebhookdeliveries) | **GET** /api/v1/webhooks/{id}/deliveries | List the deliveries of a webhook subscription |
| [**listWebhooks**](WebhooksApi.md#listwebhooks) | **GET** /api/v1/webhooks | List your webhook subscriptions |
| [**redeliverWebhook**](WebhooksApi.md#redeliverwebhook) | **POST** /api/v1/webhooks/{id}/deliveries/{deliveryId}/redeliver | Redeliver a webhook event |
| [**rotateWebhookSecret**](WebhooksApi.md#rotatewebhooksecret) | **POST** /api/v1/webhooks/{id}/rotate-secret | Rotate a webhook secret |
| [**sendWebhookTest**](WebhooksApi.md#sendwebhooktest) | **POST** /api/v1/webhooks/{id}/test | Send a test event |
| [**updateWebhook**](WebhooksApi.md#updatewebhookoperation) | **PATCH** /api/v1/webhooks/{id} | Edit a webhook subscription |



## createWebhook

> WebhookWithSecret createWebhook(idempotencyKey, createWebhookRequest)

Create a webhook subscription

Subscribes an HTTPS URL to the events you list. Growwer then POSTs each event to it, signed as Standard Webhooks signs (&#x60;webhook-id&#x60;, &#x60;webhook-timestamp&#x60;, &#x60;webhook-signature&#x60;) with the &#x60;secret&#x60; this answer carries. The secret is shown only here and on POST /webhooks/{id}/rotate-secret: store it now. A replay of this request under its &#x60;Idempotency-Key&#x60; answers the subscription without it.  The URL must be HTTPS and its host must resolve to public addresses only: a loopback, private, link-local, multicast or metadata address is refused with 422 &#x60;webhook_url_not_public&#x60;, a host that does not resolve with 422 &#x60;webhook_url_unresolvable&#x60;. &#x60;lowBalanceThreshold&#x60; is required with &#x60;balance.low&#x60; and refused without it. An account has at most 20 subscriptions per mode. Test keys get 403 &#x60;not_available_in_test_mode&#x60; for now.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from '@growwer/api';
import type { CreateWebhookOperationRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
    // CreateWebhookRequest
    createWebhookRequest: ...,
  } satisfies CreateWebhookOperationRequest;

  try {
    const data = await api.createWebhook(body);
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
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |
| **createWebhookRequest** | [CreateWebhookRequest](CreateWebhookRequest.md) |  | |

### Return type

[**WebhookWithSecret**](WebhookWithSecret.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The subscription and its signing secret. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **409** | The account already has 20 subscriptions in this mode (code &#x60;webhook_limit_reached&#x60;, with &#x60;details.limit&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is not valid (code &#x60;validation_failed&#x60;, also for a URL whose host is a single-label name), or the URL does not resolve or resolves to an address that is not public (codes &#x60;webhook_url_unresolvable&#x60;, &#x60;webhook_url_not_public&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteWebhook

> deleteWebhook(id, idempotencyKey)

Delete a webhook subscription

Deletes one of your webhook subscriptions and its delivery log. Deliveries still pending are not sent.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from '@growwer/api';
import type { DeleteWebhookRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string | The subscription.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
  } satisfies DeleteWebhookRequest;

  try {
    const data = await api.deleteWebhook(body);
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
| **id** | `string` | The subscription. | [Defaults to `undefined`] |
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
| **204** | The subscription was deleted. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getWebhook

> Webhook getWebhook(id)

Get a webhook subscription

One of your webhook subscriptions, without its secret. A subscription of the other mode is not found.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from '@growwer/api';
import type { GetWebhookRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string | The subscription.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetWebhookRequest;

  try {
    const data = await api.getWebhook(body);
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
| **id** | `string` | The subscription. | [Defaults to `undefined`] |

### Return type

[**Webhook**](Webhook.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The subscription. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listWebhookDeliveries

> ListWebhookDeliveries200Response listWebhookDeliveries(id, limit, offset)

List the deliveries of a webhook subscription

The events sent to the subscription in the last 30 days, newest first, each with its status and its latest 10 attempts: when, the status code your endpoint answered, how long it took and the start of its response body. Older deliveries are deleted.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from '@growwer/api';
import type { ListWebhookDeliveriesRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string | The subscription.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Deliveries per page, 1 to 100. (optional)
    limit: 56,
    // number | Deliveries to skip. (optional)
    offset: 56,
  } satisfies ListWebhookDeliveriesRequest;

  try {
    const data = await api.listWebhookDeliveries(body);
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
| **id** | `string` | The subscription. | [Defaults to `undefined`] |
| **limit** | `number` | Deliveries per page, 1 to 100. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Deliveries to skip. | [Optional] [Defaults to `0`] |

### Return type

[**ListWebhookDeliveries200Response**](ListWebhookDeliveries200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of the deliveries and how many there are in the last 30 days. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listWebhooks

> ListWebhooks200Response listWebhooks(limit, offset)

List your webhook subscriptions

Your webhook subscriptions in the mode of the key, newest first, disabled ones included. A live key lists the live ones and a test key the test ones.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from '@growwer/api';
import type { ListWebhooksRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // number | Subscriptions per page, 1 to 100. (optional)
    limit: 56,
    // number | Subscriptions to skip. (optional)
    offset: 56,
  } satisfies ListWebhooksRequest;

  try {
    const data = await api.listWebhooks(body);
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
| **limit** | `number` | Subscriptions per page, 1 to 100. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Subscriptions to skip. | [Optional] [Defaults to `0`] |

### Return type

[**ListWebhooks200Response**](ListWebhooks200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of your subscriptions and how many you have in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## redeliverWebhook

> WebhookDelivery redeliverWebhook(id, deliveryId, idempotencyKey)

Redeliver a webhook event

Queues a delivery that has succeeded or failed again, in a new round of retries, and answers it. It sends the same event with the same &#x60;webhook-id&#x60;, so a consumer that dedupes by it handles it once. Deliveries are kept 30 days. A delivery still pending, being sent or waiting for its next retry, answers 409 &#x60;webhook_delivery_pending&#x60; and takes none of the hour\&#39;s sends; so does a redelivery while the subscription has 10 test events and redeliveries pending, its limit for a redelivery, given in &#x60;details.limit&#x60;. The pending deliveries of events never redelivered do not count. A subscription takes at most 10 test events and redeliveries an hour: past them it answers 429 &#x60;webhook_send_limit_reached&#x60; with &#x60;Retry-After&#x60;. A disabled subscription answers 409 &#x60;webhook_disabled&#x60;.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from '@growwer/api';
import type { RedeliverWebhookRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string | The subscription.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | The delivery.
    deliveryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
  } satisfies RedeliverWebhookRequest;

  try {
    const data = await api.redeliverWebhook(body);
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
| **id** | `string` | The subscription. | [Defaults to `undefined`] |
| **deliveryId** | `string` | The delivery. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |

### Return type

[**WebhookDelivery**](WebhookDelivery.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The delivery, queued again. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The subscription is disabled (code &#x60;webhook_disabled&#x60;), the delivery is still pending or the subscription already has 10 test events and redeliveries pending, its limit in &#x60;details.limit&#x60; (code &#x60;webhook_delivery_pending&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## rotateWebhookSecret

> WebhookWithSecret rotateWebhookSecret(id, idempotencyKey)

Rotate a webhook secret

Gives the subscription a new signing secret and answers it: it is shown only here, so store it now. For 24 hours, until &#x60;previousSecretExpiresAt&#x60;, every delivery carries two signatures in &#x60;webhook-signature&#x60;, one with each secret, so you can switch without missing an event; after that only the new secret signs. A replay of this request under its &#x60;Idempotency-Key&#x60; answers the subscription without the secret.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from '@growwer/api';
import type { RotateWebhookSecretRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string | The subscription.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
  } satisfies RotateWebhookSecretRequest;

  try {
    const data = await api.rotateWebhookSecret(body);
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
| **id** | `string` | The subscription. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |

### Return type

[**WebhookWithSecret**](WebhookWithSecret.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The subscription and its new signing secret. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | Another request rotated the secret at the same time and its secret is the one in force (code &#x60;webhook_secret_rotation_conflict&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## sendWebhookTest

> WebhookDelivery sendWebhookTest(id, idempotencyKey)

Send a test event

Queues a &#x60;webhook.test&#x60; event for the subscription, whatever events it lists, and answers its delivery: follow it on GET /webhooks/{id}/deliveries. It is signed, retried and logged as any event. It normally supersedes the subscription\&#39;s earlier test events still pending: their deliveries fail and are not retried, so a test right after fixing the endpoint does not wait behind them; one that cannot be failed then is failed by the next test. A subscription takes at most 10 test events and redeliveries an hour: past them it answers 429 &#x60;webhook_send_limit_reached&#x60; with &#x60;Retry-After&#x60;. A disabled subscription answers 409 &#x60;webhook_disabled&#x60;. A test event that cannot be recorded answers 503 &#x60;webhook_test_unavailable&#x60;: nothing was sent, the attempt counts toward the hourly limit, and a retry needs a new &#x60;Idempotency-Key&#x60;.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from '@growwer/api';
import type { SendWebhookTestRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string | The subscription.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
  } satisfies SendWebhookTestRequest;

  try {
    const data = await api.sendWebhookTest(body);
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
| **id** | `string` | The subscription. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |

### Return type

[**WebhookDelivery**](WebhookDelivery.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The delivery of the test event, queued. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The subscription is disabled (code &#x60;webhook_disabled&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateWebhook

> Webhook updateWebhook(id, idempotencyKey, updateWebhookRequest)

Edit a webhook subscription

Changes only the fields you send. A new &#x60;url&#x60; is checked as on create. Dropping &#x60;balance.low&#x60; from &#x60;events&#x60; drops the threshold with it. &#x60;enabled: false&#x60; disables the subscription, which then gets no events; &#x60;enabled: true&#x60; enables it again, including one Growwer disabled because its endpoint answered 410 or failed for 5 days, and forgets its failures.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from '@growwer/api';
import type { UpdateWebhookOperationRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string | The subscription.
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
    // UpdateWebhookRequest
    updateWebhookRequest: ...,
  } satisfies UpdateWebhookOperationRequest;

  try {
    const data = await api.updateWebhook(body);
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
| **id** | `string` | The subscription. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |
| **updateWebhookRequest** | [UpdateWebhookRequest](UpdateWebhookRequest.md) |  | |

### Return type

[**Webhook**](Webhook.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The subscription as edited. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is not valid (code &#x60;validation_failed&#x60;, also for a URL whose host is a single-label name), or the new URL does not resolve or resolves to an address that is not public (codes &#x60;webhook_url_unresolvable&#x60;, &#x60;webhook_url_not_public&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

