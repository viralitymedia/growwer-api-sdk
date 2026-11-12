# AccountApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMe**](AccountApi.md#getme) | **GET** /api/v1/me | Your account |
| [**getVocabulary**](AccountApi.md#getvocabulary) | **GET** /api/v1/vocabulary | Codes and names |



## getMe

> GetMe200Response getMe()

Your account

Profile basics, the buyer and seller balances, whether your seller account is restricted, whether the catalogue is open to you, whether you have a managed service, and whether the key you called with is live or test. A test key reads its test wallet as the buyer balance (1,000.00 EUR until test orders and top-ups move it), never your real balance, and no seller side.

### Example

```ts
import {
  Configuration,
  AccountApi,
} from '@growwer/api';
import type { GetMeRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AccountApi(config);

  try {
    const data = await api.getMe();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMe200Response**](GetMe200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your account. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without enough recent orders delivered and approved, whose quota rises to the full cap once it has them: a trial refusal\&#39;s message names that threshold, which &#x60;details.minOrders&#x60; (how many orders) and &#x60;details.windowDays&#x60; (within how many days) repeat, and an order lifts the quota only once it is delivered and approved, so one placed today usually does not lift today\&#39;s quota; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getVocabulary

> GetVocabulary200Response getVocabulary()

Codes and names

The countries, languages, topics, product types, link types and order states that other operations take and return. Names are in English.

### Example

```ts
import {
  Configuration,
  AccountApi,
} from '@growwer/api';
import type { GetVocabularyRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AccountApi(config);

  try {
    const data = await api.getVocabulary();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetVocabulary200Response**](GetVocabulary200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Every code, with its English name where it has one. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without enough recent orders delivered and approved, whose quota rises to the full cap once it has them: a trial refusal\&#39;s message names that threshold, which &#x60;details.minOrders&#x60; (how many orders) and &#x60;details.windowDays&#x60; (within how many days) repeat, and an order lifts the quota only once it is delivered and approved, so one placed today usually does not lift today\&#39;s quota; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

