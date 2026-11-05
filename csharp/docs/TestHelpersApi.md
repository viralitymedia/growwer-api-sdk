# Growwer.Api.Api.TestHelpersApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**AdvanceTestOrder**](TestHelpersApi.md#advancetestorder) | **POST** /api/v1/test-helpers/orders/{id}/advance | Advance a test order |
| [**ResetTestData**](TestHelpersApi.md#resettestdata) | **POST** /api/v1/test-helpers/reset | Reset your test data |
| [**TopUpTestWallet**](TestHelpersApi.md#topuptestwallet) | **POST** /api/v1/test-helpers/wallet/top-up | Top up your test wallet |

<a id="advancetestorder"></a>
# **AdvanceTestOrder**
> Order AdvanceTestOrder (Guid id, string idempotencyKey, AdvanceTestOrderRequest advanceTestOrderRequest)

Advance a test order

Test keys only. Moves one of your test orders at once to `to`, without waiting for the simulated seller: `accepted` or `rejected` (by the seller, from `pending_acceptance`), `draft_delivered` (the sample draft, from `pending_draft` or `pending_draft_update`), `draft_update_requested` (as if you sent the draft back, from `pending_draft_review`), `published` (delivered for your review, from `pending_order_delivery`, `scheduled` or `pending_order_delivery_update`), `update_requested` (as if you sent the delivery back, from `pending_order_delivery_review`) or `cancelled_by_growwer` (from any state that is not finished). The order and your test wallet change as that move changes them live, a rejection or a cancellation refunding the price, and the simulated seller carries on from the new state. A post with a future `scheduledPublicationDate` waits in `scheduled` until that date once the simulated seller delivers it; `published` skips the wait. A target its state does not allow answers 409 `invalid_transition` with the targets it allows. A live key gets 403 `test_mode_only`.

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
    public class AdvanceTestOrderExample
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
            var apiInstance = new TestHelpersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var advanceTestOrderRequest = new AdvanceTestOrderRequest(); // AdvanceTestOrderRequest | 

            try
            {
                // Advance a test order
                Order result = apiInstance.AdvanceTestOrder(id, idempotencyKey, advanceTestOrderRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling TestHelpersApi.AdvanceTestOrder: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the AdvanceTestOrderWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Advance a test order
    ApiResponse<Order> response = apiInstance.AdvanceTestOrderWithHttpInfo(id, idempotencyKey, advanceTestOrderRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling TestHelpersApi.AdvanceTestOrderWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **advanceTestOrderRequest** | [**AdvanceTestOrderRequest**](AdvanceTestOrderRequest.md) |  |  |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The test order, moved. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;), or it is a live key (code &#x60;test_mode_only&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The order&#39;s state does not allow &#x60;to&#x60; (code &#x60;invalid_transition&#x60;, with &#x60;details.validTargets&#x60;, the targets it allows, possibly none), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is not valid (code &#x60;validation_failed&#x60;): a &#x60;to&#x60; that is not one of the targets. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="resettestdata"></a>
# **ResetTestData**
> void ResetTestData (string idempotencyKey)

Reset your test data

Test keys only. Deletes your test projects, orders and uploaded test files, and returns your test wallet to its opening balance of 1,000.00 EUR with no movements. Your API keys and webhook subscriptions stay, and nothing of your live account changes. It takes no body. A live key gets 403 `test_mode_only`.

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
    public class ResetTestDataExample
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
            var apiInstance = new TestHelpersApi(httpClient, config, httpClientHandler);
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

            try
            {
                // Reset your test data
                apiInstance.ResetTestData(idempotencyKey);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling TestHelpersApi.ResetTestData: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ResetTestDataWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Reset your test data
    apiInstance.ResetTestDataWithHttpInfo(idempotencyKey);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling TestHelpersApi.ResetTestDataWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
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
| **204** | Your test data is deleted and your test wallet is back at 1,000.00 EUR. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;), or it is a live key (code &#x60;test_mode_only&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="topuptestwallet"></a>
# **TopUpTestWallet**
> TopUpTestWallet200Response TopUpTestWallet (string idempotencyKey, TopUpTestWalletRequest topUpTestWalletRequest)

Top up your test wallet

Test keys only. Credits your test wallet, the buyer wallet a test key spends from, with fictitious money: more than nothing and at most 10,000.00 EUR per call. It never touches your real wallets, takes no payment and issues no invoice; the movement shows in GET /wallets/buyer/transactions for a test key as a confirmed `deposit`. A live key gets 403 `test_mode_only`.

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
    public class TopUpTestWalletExample
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
            var apiInstance = new TestHelpersApi(httpClient, config, httpClientHandler);
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var topUpTestWalletRequest = new TopUpTestWalletRequest(); // TopUpTestWalletRequest | 

            try
            {
                // Top up your test wallet
                TopUpTestWallet200Response result = apiInstance.TopUpTestWallet(idempotencyKey, topUpTestWalletRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling TestHelpersApi.TopUpTestWallet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the TopUpTestWalletWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Top up your test wallet
    ApiResponse<TopUpTestWallet200Response> response = apiInstance.TopUpTestWalletWithHttpInfo(idempotencyKey, topUpTestWalletRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling TestHelpersApi.TopUpTestWalletWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **topUpTestWalletRequest** | [**TopUpTestWalletRequest**](TopUpTestWalletRequest.md) |  |  |

### Return type

[**TopUpTestWallet200Response**](TopUpTestWallet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your test wallet, credited. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;), or it is a live key (code &#x60;test_mode_only&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is not valid (code &#x60;validation_failed&#x60;): an &#x60;amount&#x60; that is not EUR, not more than nothing, or above 10,000.00 EUR. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

