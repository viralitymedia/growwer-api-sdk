# TestHelpersApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**advanceTestOrder**](TestHelpersApi.md#advanceTestOrder) | **POST** /api/v1/test-helpers/orders/{id}/advance | Advance a test order |
| [**resetTestData**](TestHelpersApi.md#resetTestData) | **POST** /api/v1/test-helpers/reset | Reset your test data |
| [**topUpTestWallet**](TestHelpersApi.md#topUpTestWallet) | **POST** /api/v1/test-helpers/wallet/top-up | Top up your test wallet |


<a id="advanceTestOrder"></a>
# **advanceTestOrder**
> Order advanceTestOrder(id, idempotencyKey, advanceTestOrderRequest)

Advance a test order

Test keys only. Moves one of your test orders at once to &#x60;to&#x60;, without waiting for the simulated seller: &#x60;accepted&#x60; or &#x60;rejected&#x60; (by the seller, from &#x60;pending_acceptance&#x60;), &#x60;draft_delivered&#x60; (the sample draft, from &#x60;pending_draft&#x60; or &#x60;pending_draft_update&#x60;), &#x60;draft_update_requested&#x60; (as if you sent the draft back, from &#x60;pending_draft_review&#x60;), &#x60;published&#x60; (delivered for your review, from &#x60;pending_order_delivery&#x60;, &#x60;scheduled&#x60; or &#x60;pending_order_delivery_update&#x60;), &#x60;update_requested&#x60; (as if you sent the delivery back, from &#x60;pending_order_delivery_review&#x60;) or &#x60;cancelled_by_growwer&#x60; (from any state that is not finished). The order and your test wallet change as that move changes them live, a rejection or a cancellation refunding the price, and the simulated seller carries on from the new state. A post with a future &#x60;scheduledPublicationDate&#x60; waits in &#x60;scheduled&#x60; until that date once the simulated seller delivers it; &#x60;published&#x60; skips the wait. A target its state does not allow answers 409 &#x60;invalid_transition&#x60; with the targets it allows. A live key gets 403 &#x60;test_mode_only&#x60;.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.TestHelpersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    TestHelpersApi apiInstance = new TestHelpersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    AdvanceTestOrderRequest advanceTestOrderRequest = new AdvanceTestOrderRequest(); // AdvanceTestOrderRequest | 
    try {
      Order result = apiInstance.advanceTestOrder(id, idempotencyKey, advanceTestOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestHelpersApi#advanceTestOrder");
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
| **id** | **UUID**|  | |
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **advanceTestOrderRequest** | [**AdvanceTestOrderRequest**](AdvanceTestOrderRequest.md)|  | |

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
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without enough recent orders delivered and approved, whose quota rises to the full cap once it has them: a trial refusal&#39;s message names that threshold, which &#x60;details.minOrders&#x60; (how many orders) and &#x60;details.windowDays&#x60; (within how many days) repeat, and an order lifts the quota only once it is delivered and approved, so one placed today usually does not lift today&#39;s quota; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

<a id="resetTestData"></a>
# **resetTestData**
> resetTestData(idempotencyKey)

Reset your test data

Test keys only. Deletes your test projects, orders and uploaded test files, and returns your test wallet to its opening balance of 1,000.00 EUR with no movements. Your API keys and webhook subscriptions stay, and nothing of your live account changes. It takes no body. A live key gets 403 &#x60;test_mode_only&#x60;.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.TestHelpersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    TestHelpersApi apiInstance = new TestHelpersApi(defaultClient);
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    try {
      apiInstance.resetTestData(idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestHelpersApi#resetTestData");
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
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |

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
| **204** | Your test data is deleted and your test wallet is back at 1,000.00 EUR. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;), or it is a live key (code &#x60;test_mode_only&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without enough recent orders delivered and approved, whose quota rises to the full cap once it has them: a trial refusal&#39;s message names that threshold, which &#x60;details.minOrders&#x60; (how many orders) and &#x60;details.windowDays&#x60; (within how many days) repeat, and an order lifts the quota only once it is delivered and approved, so one placed today usually does not lift today&#39;s quota; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

<a id="topUpTestWallet"></a>
# **topUpTestWallet**
> TopUpTestWallet200Response topUpTestWallet(idempotencyKey, topUpTestWalletRequest)

Top up your test wallet

Test keys only. Credits your test wallet, the buyer wallet a test key spends from, with fictitious money: more than nothing and at most 10,000.00 EUR per call. It never touches your real wallets, takes no payment and issues no invoice; the movement shows in GET /wallets/buyer/transactions for a test key as a confirmed &#x60;deposit&#x60;. A live key gets 403 &#x60;test_mode_only&#x60;.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.TestHelpersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    TestHelpersApi apiInstance = new TestHelpersApi(defaultClient);
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    TopUpTestWalletRequest topUpTestWalletRequest = new TopUpTestWalletRequest(); // TopUpTestWalletRequest | 
    try {
      TopUpTestWallet200Response result = apiInstance.topUpTestWallet(idempotencyKey, topUpTestWalletRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestHelpersApi#topUpTestWallet");
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
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **topUpTestWalletRequest** | [**TopUpTestWalletRequest**](TopUpTestWalletRequest.md)|  | |

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
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without enough recent orders delivered and approved, whose quota rises to the full cap once it has them: a trial refusal&#39;s message names that threshold, which &#x60;details.minOrders&#x60; (how many orders) and &#x60;details.windowDays&#x60; (within how many days) repeat, and an order lifts the quota only once it is delivered and approved, so one placed today usually does not lift today&#39;s quota; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. On POST /webhooks/{id}/test and POST /webhooks/{id}/deliveries/{deliveryId}/redeliver, also when the subscription took 10 test events and redeliveries in the last hour (code &#x60;webhook_send_limit_reached&#x60;): &#x60;details.limit&#x60; is that limit and &#x60;Retry-After&#x60; the time until the next one fits. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). On POST /webhooks/{id}/test, also when the test event cannot be recorded, so nothing was sent (code &#x60;webhook_test_unavailable&#x60;): the attempt still counts toward the 10 test events and redeliveries an hour, and a retry needs a new &#x60;Idempotency-Key&#x60;. Retry later. |  * Retry-After -  <br>  |

