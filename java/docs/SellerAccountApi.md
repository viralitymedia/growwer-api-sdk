# SellerAccountApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**putSellerHoliday**](SellerAccountApi.md#putSellerHoliday) | **PUT** /api/v1/seller/holiday | Set your holiday |


<a id="putSellerHoliday"></a>
# **putSellerHoliday**
> PutSellerHoliday200Response putSellerHoliday(idempotencyKey, putSellerHolidayRequest)

Set your holiday

Starts, changes or ends your holiday, as the holiday settings of your profile page do. While you are on holiday your medias take no orders. &#x60;endDate&#x60; is the day your holiday ends, at 00:00 of that day in Growwer&#39;s server time, and must be later than now; leave it out, or send null, for a holiday you end yourself. Ending the holiday takes no &#x60;endDate&#x60;.  A holiday that already is as you ask is answered 200 without a change. A restricted seller account stays on holiday until the restriction is lifted, so any change is refused. Your holiday is also in GET /me.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerAccountApi apiInstance = new SellerAccountApi(defaultClient);
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    PutSellerHolidayRequest putSellerHolidayRequest = new PutSellerHolidayRequest(); // PutSellerHolidayRequest | 
    try {
      PutSellerHoliday200Response result = apiInstance.putSellerHoliday(idempotencyKey, putSellerHolidayRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerAccountApi#putSellerHoliday");
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
| **putSellerHolidayRequest** | [**PutSellerHolidayRequest**](PutSellerHolidayRequest.md)|  | |

### Return type

[**PutSellerHoliday200Response**](PutSellerHoliday200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your holiday, as it now is. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **409** | Your seller account is restricted, so its holiday cannot change (code &#x60;seller_restricted&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is not valid (code &#x60;validation_failed&#x60;): an &#x60;endDate&#x60; that is not a later day, or one sent with &#x60;onHoliday&#x60; false. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

