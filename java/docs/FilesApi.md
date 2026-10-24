# FilesApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**uploadFile**](FilesApi.md#uploadFile) | **POST** /api/v1/files | Upload a file |


<a id="uploadFile"></a>
# **uploadFile**
> UploadFile201Response uploadFile(idempotencyKey, _file)

Upload a file

Uploads a document (odt, doc, docx or txt, up to 8 MB) for a later write to reference by its &#x60;id&#x60;. A file belongs to you, can be used by one write, and expires 24 hours after it was uploaded; an expired or used file is answered like an unknown one.  You may hold 20 files that no write has used yet and that have not expired. Past them it answers 429 &#x60;file_limit_reached&#x60;, with &#x60;details.limit&#x60; the number you may hold and &#x60;Retry-After&#x60; the seconds until the first of them expires; using one of them in a write frees its place at once. A file refused as invalid (422) is refused before they are counted, and a refused upload stores nothing.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    File _file = new File("/path/to/file"); // File | 
    try {
      UploadFile201Response result = apiInstance.uploadFile(idempotencyKey, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#uploadFile");
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
| **_file** | **File**|  | |

### Return type

[**UploadFile201Response**](UploadFile201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The file, stored until &#x60;expiresAt&#x60;. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | No file was sent as the &#x60;file&#x60; field, or it is too large, not an odt, doc, docx or txt document, or its name is longer than 255 characters (code &#x60;validation_failed&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

