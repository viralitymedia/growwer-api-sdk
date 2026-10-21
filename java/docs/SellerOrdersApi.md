# SellerOrdersApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acceptSellerOrder**](SellerOrdersApi.md#acceptSellerOrder) | **POST** /api/v1/seller/orders/{id}/accept | Accept an order |
| [**deliverSellerOrder**](SellerOrdersApi.md#deliverSellerOrder) | **POST** /api/v1/seller/orders/{id}/deliver | Deliver an order |
| [**deliverSellerOrderDraft**](SellerOrdersApi.md#deliverSellerOrderDraft) | **POST** /api/v1/seller/orders/{id}/deliver-draft | Deliver a draft |
| [**deliverSellerOrderDraftUpdate**](SellerOrdersApi.md#deliverSellerOrderDraftUpdate) | **POST** /api/v1/seller/orders/{id}/deliver-draft-update | Deliver a draft update |
| [**deliverSellerOrderUpdate**](SellerOrdersApi.md#deliverSellerOrderUpdate) | **POST** /api/v1/seller/orders/{id}/deliver-update | Deliver an update |
| [**downloadSellerOrderBriefing**](SellerOrdersApi.md#downloadSellerOrderBriefing) | **GET** /api/v1/seller/orders/{id}/briefing | Download the draft the buyer attached to an order |
| [**downloadSellerOrderDraft**](SellerOrdersApi.md#downloadSellerOrderDraft) | **GET** /api/v1/seller/orders/{id}/draft | Download the draft of an order you sell |
| [**getSellerOrder**](SellerOrdersApi.md#getSellerOrder) | **GET** /api/v1/seller/orders/{id} | Get an order you sell |
| [**listSellerOrders**](SellerOrdersApi.md#listSellerOrders) | **GET** /api/v1/seller/orders | List the orders you sell |
| [**refuteSellerOrderDraftUpdate**](SellerOrdersApi.md#refuteSellerOrderDraftUpdate) | **POST** /api/v1/seller/orders/{id}/refute-draft-update | Refuse a draft update |
| [**refuteSellerOrderUpdate**](SellerOrdersApi.md#refuteSellerOrderUpdate) | **POST** /api/v1/seller/orders/{id}/refute-update | Refuse an update |
| [**rejectSellerOrder**](SellerOrdersApi.md#rejectSellerOrder) | **POST** /api/v1/seller/orders/{id}/reject | Reject an order |


<a id="acceptSellerOrder"></a>
# **acceptSellerOrder**
> SellerOrder acceptSellerOrder(id, idempotencyKey)

Accept an order

Accepts an order placed on one of your medias (&#x60;state&#x60; &#x60;pending_acceptance&#x60;), as the web does. A post order whose draft is still to be written (by you or by Growwer) moves to &#x60;pending_draft&#x60;; any other order moves to &#x60;pending_order_delivery&#x60;. The buyer is told. Takes no body.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    try {
      SellerOrder result = apiInstance.acceptSellerOrder(id, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#acceptSellerOrder");
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
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The order, accepted. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The order is not waiting for your acceptance (code &#x60;invalid_state&#x60;), your seller account is restricted and accepts no orders (code &#x60;seller_restricted&#x60;; support can tell you why), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="deliverSellerOrder"></a>
# **deliverSellerOrder**
> SellerOrder deliverSellerOrder(id, idempotencyKey, sellerOrderPostDelivery)

Deliver an order

Delivers an order placed on one of your medias (&#x60;state&#x60; &#x60;pending_order_delivery&#x60;), as the web does. A post order takes the URL of the published post and the confirmation of its publication date; a link addition order takes no body, and any field is refused. The order moves to &#x60;pending_order_delivery_review&#x60; and the buyer is asked to review it, or, for a post order whose scheduled publication date is still to come, to &#x60;scheduled&#x60; without telling the buyer yet. The URL is checked to be a URL only, as the web does.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    SellerOrderPostDelivery sellerOrderPostDelivery = new SellerOrderPostDelivery(); // SellerOrderPostDelivery | 
    try {
      SellerOrder result = apiInstance.deliverSellerOrder(id, idempotencyKey, sellerOrderPostDelivery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#deliverSellerOrder");
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
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **sellerOrderPostDelivery** | [**SellerOrderPostDelivery**](SellerOrderPostDelivery.md)|  | [optional] |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The order, delivered or scheduled. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The order is not waiting for its delivery (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="deliverSellerOrderDraft"></a>
# **deliverSellerOrderDraft**
> SellerOrder deliverSellerOrderDraft(id, idempotencyKey, sellerOrderDraftFile)

Deliver a draft

Delivers the draft of a post order placed on one of your medias whose draft you write (&#x60;state&#x60; &#x60;pending_draft&#x60;), as the web does, from a file you uploaded with POST /files. The order moves to &#x60;pending_draft_review&#x60; when the buyer reviews drafts, otherwise to &#x60;pending_order_delivery&#x60;. The file is used up once the draft is delivered; a refused request leaves it usable.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    SellerOrderDraftFile sellerOrderDraftFile = new SellerOrderDraftFile(); // SellerOrderDraftFile | 
    try {
      SellerOrder result = apiInstance.deliverSellerOrderDraft(id, idempotencyKey, sellerOrderDraftFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#deliverSellerOrderDraft");
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
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **sellerOrderDraftFile** | [**SellerOrderDraftFile**](SellerOrderDraftFile.md)|  | |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The order, with its draft delivered. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The order is not waiting for a draft you write (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is not valid, or the file is not an odt, doc, docx or txt file of up to 8 MB (code &#x60;validation_failed&#x60;, with the messages of each field in &#x60;details.fields&#x60;), or &#x60;fileId&#x60; names no file you can use: it does not exist, has expired or was already used (code &#x60;file_unusable&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="deliverSellerOrderDraftUpdate"></a>
# **deliverSellerOrderDraftUpdate**
> SellerOrder deliverSellerOrderDraftUpdate(id, idempotencyKey, sellerOrderDraftFile)

Deliver a draft update

Delivers the draft update the buyer asked for on a post order placed on one of your medias whose draft you write (&#x60;state&#x60; &#x60;pending_draft_update&#x60;), as the web does, from a file you uploaded with POST /files. The order moves back to &#x60;pending_draft_review&#x60;. The file is used up once the draft is delivered; a refused request leaves it usable.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    SellerOrderDraftFile sellerOrderDraftFile = new SellerOrderDraftFile(); // SellerOrderDraftFile | 
    try {
      SellerOrder result = apiInstance.deliverSellerOrderDraftUpdate(id, idempotencyKey, sellerOrderDraftFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#deliverSellerOrderDraftUpdate");
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
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **sellerOrderDraftFile** | [**SellerOrderDraftFile**](SellerOrderDraftFile.md)|  | |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The order, with its updated draft delivered. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The buyer has not asked for an update of a draft you write (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is not valid, or the file is not an odt, doc, docx or txt file of up to 8 MB (code &#x60;validation_failed&#x60;, with the messages of each field in &#x60;details.fields&#x60;), or &#x60;fileId&#x60; names no file you can use: it does not exist, has expired or was already used (code &#x60;file_unusable&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="deliverSellerOrderUpdate"></a>
# **deliverSellerOrderUpdate**
> SellerOrder deliverSellerOrderUpdate(id, idempotencyKey, sellerOrderPostDelivery)

Deliver an update

Delivers the update the buyer asked for on an order placed on one of your medias (&#x60;state&#x60; &#x60;pending_order_delivery_update&#x60;), as the web does. A post order takes the URL of the published post, which may be the same as before, and the confirmation of its publication date; both must be sent. A link addition order takes no body, and any field is refused. The order moves back to &#x60;pending_order_delivery_review&#x60; and the buyer is asked to review it.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    SellerOrderPostDelivery sellerOrderPostDelivery = new SellerOrderPostDelivery(); // SellerOrderPostDelivery | 
    try {
      SellerOrder result = apiInstance.deliverSellerOrderUpdate(id, idempotencyKey, sellerOrderPostDelivery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#deliverSellerOrderUpdate");
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
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **sellerOrderPostDelivery** | [**SellerOrderPostDelivery**](SellerOrderPostDelivery.md)|  | [optional] |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The order, with the update delivered. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The buyer has not asked for an update (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="downloadSellerOrderBriefing"></a>
# **downloadSellerOrderBriefing**
> File downloadSellerOrderBriefing(id)

Download the draft the buyer attached to an order

The file the buyer attached to the briefing of a post order you sell. 404 when the order has none (&#x60;briefing.hasProposedDraft&#x60; is false) or the file cannot be read.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      File result = apiInstance.downloadSellerOrderBriefing(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#downloadSellerOrderBriefing");
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

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The file, with its own content type and name. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="downloadSellerOrderDraft"></a>
# **downloadSellerOrderDraft**
> File downloadSellerOrderDraft(id)

Download the draft of an order you sell

The file of the current draft of a post order you sell. 404 when the order has no draft file (&#x60;draft.hasFile&#x60; is false) or the file cannot be read. Earlier drafts are not available.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      File result = apiInstance.downloadSellerOrderDraft(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#downloadSellerOrderDraft");
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

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The file, with its own content type and name. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="getSellerOrder"></a>
# **getSellerOrder**
> SellerOrder getSellerOrder(id)

Get an order you sell

One order placed on one of your medias, with its briefing, its draft and its state history. An order you only bought is not found here; it is under GET /orders/{id}.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SellerOrder result = apiInstance.getSellerOrder(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#getSellerOrder");
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

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The order. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="listSellerOrders"></a>
# **listSellerOrders**
> ListSellerOrders200Response listSellerOrders(mediaId, state, updatedSince, sort, limit, offset)

List the orders you sell

The orders placed on your medias, newest first by default. To follow them, poll with &#x60;sort&#x3D;updatedAt&#x60; and &#x60;updatedSince&#x60; set to the &#x60;updatedAt&#x60; of the last order you saw: an order moves to the end of that list each time it changes state. The orders you bought are under GET /orders.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID mediaId = UUID.randomUUID(); // UUID | Only the orders on this media of yours.
    String state = "pending_acceptance,pending_order_delivery"; // String | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones.
    OffsetDateTime updatedSince = OffsetDateTime.now(); // OffsetDateTime | Only the orders whose `updatedAt` is at or after this instant, an ISO-8601 date-time with its offset (send `+` as `%2B`).
    String sort = "-createdAt"; // String | `-createdAt`, newest first, or `updatedAt`, least recently changed first. Orders of the same instant come in id order.
    Integer limit = 20; // Integer | Orders per page, 1 to 100.
    Integer offset = 0; // Integer | Orders to skip.
    try {
      ListSellerOrders200Response result = apiInstance.listSellerOrders(mediaId, state, updatedSince, sort, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#listSellerOrders");
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
| **mediaId** | **UUID**| Only the orders on this media of yours. | [optional] |
| **state** | **String**| Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones. | [optional] |
| **updatedSince** | **OffsetDateTime**| Only the orders whose &#x60;updatedAt&#x60; is at or after this instant, an ISO-8601 date-time with its offset (send &#x60;+&#x60; as &#x60;%2B&#x60;). | [optional] |
| **sort** | **String**| &#x60;-createdAt&#x60;, newest first, or &#x60;updatedAt&#x60;, least recently changed first. Orders of the same instant come in id order. | [optional] [default to -createdAt] [enum: -createdAt, updatedAt] |
| **limit** | **Integer**| Orders per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **Integer**| Orders to skip. | [optional] [default to 0] |

### Return type

[**ListSellerOrders200Response**](ListSellerOrders200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of the orders you sell and how many match in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="refuteSellerOrderDraftUpdate"></a>
# **refuteSellerOrderDraftUpdate**
> SellerOrder refuteSellerOrderDraftUpdate(id, idempotencyKey, sellerOrderRefutation)

Refuse a draft update

Refuses the draft update the buyer asked for on a post order placed on one of your medias whose draft you write (&#x60;state&#x60; &#x60;pending_draft_update&#x60;), as the web does. The order moves back to &#x60;pending_draft_review&#x60; and the buyer is told your reason. A draft Growwer or the buyer writes cannot be refused here.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    SellerOrderRefutation sellerOrderRefutation = new SellerOrderRefutation(); // SellerOrderRefutation | 
    try {
      SellerOrder result = apiInstance.refuteSellerOrderDraftUpdate(id, idempotencyKey, sellerOrderRefutation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#refuteSellerOrderDraftUpdate");
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
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **sellerOrderRefutation** | [**SellerOrderRefutation**](SellerOrderRefutation.md)|  | |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The order, with its draft back in review. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The buyer has not asked for an update of a draft you write, including when Growwer or the buyer writes the draft (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="refuteSellerOrderUpdate"></a>
# **refuteSellerOrderUpdate**
> SellerOrder refuteSellerOrderUpdate(id, idempotencyKey, sellerOrderRefutation)

Refuse an update

Refuses the update the buyer asked for on an order placed on one of your medias (&#x60;state&#x60; &#x60;pending_order_delivery_update&#x60;), as the web does. The order moves back to &#x60;pending_order_delivery_review&#x60; and the buyer is told your reason.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    SellerOrderRefutation sellerOrderRefutation = new SellerOrderRefutation(); // SellerOrderRefutation | 
    try {
      SellerOrder result = apiInstance.refuteSellerOrderUpdate(id, idempotencyKey, sellerOrderRefutation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#refuteSellerOrderUpdate");
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
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **sellerOrderRefutation** | [**SellerOrderRefutation**](SellerOrderRefutation.md)|  | |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The order, back in review. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The buyer has not asked for an update (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

<a id="rejectSellerOrder"></a>
# **rejectSellerOrder**
> SellerOrder rejectSellerOrder(id, idempotencyKey, sellerOrderRejection)

Reject an order

Rejects an order placed on one of your medias that you have not accepted yet (&#x60;state&#x60; &#x60;pending_acceptance&#x60;), as the web does. The order moves to &#x60;rejected_by_seller&#x60;, its price returns to the buyer, and the buyer is told your reason.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.SellerOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    SellerOrdersApi apiInstance = new SellerOrdersApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    SellerOrderRejection sellerOrderRejection = new SellerOrderRejection(); // SellerOrderRejection | 
    try {
      SellerOrder result = apiInstance.rejectSellerOrder(id, idempotencyKey, sellerOrderRejection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerOrdersApi#rejectSellerOrder");
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
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **sellerOrderRejection** | [**SellerOrderRejection**](SellerOrderRejection.md)|  | |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The order, rejected. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The order is not waiting for your acceptance (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

