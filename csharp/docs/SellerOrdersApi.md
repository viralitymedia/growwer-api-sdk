# Growwer.Api.Api.SellerOrdersApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**AcceptSellerOrder**](SellerOrdersApi.md#acceptsellerorder) | **POST** /api/v1/seller/orders/{id}/accept | Accept an order |
| [**DeliverSellerOrder**](SellerOrdersApi.md#deliversellerorder) | **POST** /api/v1/seller/orders/{id}/deliver | Deliver an order |
| [**DeliverSellerOrderDraft**](SellerOrdersApi.md#deliversellerorderdraft) | **POST** /api/v1/seller/orders/{id}/deliver-draft | Deliver a draft |
| [**DeliverSellerOrderDraftUpdate**](SellerOrdersApi.md#deliversellerorderdraftupdate) | **POST** /api/v1/seller/orders/{id}/deliver-draft-update | Deliver a draft update |
| [**DeliverSellerOrderUpdate**](SellerOrdersApi.md#deliversellerorderupdate) | **POST** /api/v1/seller/orders/{id}/deliver-update | Deliver an update |
| [**DownloadSellerOrderBriefing**](SellerOrdersApi.md#downloadsellerorderbriefing) | **GET** /api/v1/seller/orders/{id}/briefing | Download the draft the buyer attached to an order |
| [**DownloadSellerOrderDraft**](SellerOrdersApi.md#downloadsellerorderdraft) | **GET** /api/v1/seller/orders/{id}/draft | Download the draft of an order you sell |
| [**GetSellerOrder**](SellerOrdersApi.md#getsellerorder) | **GET** /api/v1/seller/orders/{id} | Get an order you sell |
| [**ListSellerOrders**](SellerOrdersApi.md#listsellerorders) | **GET** /api/v1/seller/orders | List the orders you sell |
| [**RefuteSellerOrderDraftUpdate**](SellerOrdersApi.md#refutesellerorderdraftupdate) | **POST** /api/v1/seller/orders/{id}/refute-draft-update | Refuse a draft update |
| [**RefuteSellerOrderUpdate**](SellerOrdersApi.md#refutesellerorderupdate) | **POST** /api/v1/seller/orders/{id}/refute-update | Refuse an update |
| [**RejectSellerOrder**](SellerOrdersApi.md#rejectsellerorder) | **POST** /api/v1/seller/orders/{id}/reject | Reject an order |

<a id="acceptsellerorder"></a>
# **AcceptSellerOrder**
> SellerOrder AcceptSellerOrder (Guid id, string idempotencyKey)

Accept an order

Accepts an order placed on one of your medias (`state` `pending_acceptance`), as the web does. A post order whose draft is still to be written (by you or by Growwer) moves to `pending_draft`; any other order moves to `pending_order_delivery`. The buyer is told. Takes no body.

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
    public class AcceptSellerOrderExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

            try
            {
                // Accept an order
                SellerOrder result = apiInstance.AcceptSellerOrder(id, idempotencyKey);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.AcceptSellerOrder: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the AcceptSellerOrderWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Accept an order
    ApiResponse<SellerOrder> response = apiInstance.AcceptSellerOrderWithHttpInfo(id, idempotencyKey);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.AcceptSellerOrderWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

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
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The order is not waiting for your acceptance (code &#x60;invalid_state&#x60;), your seller account is restricted and accepts no orders (code &#x60;seller_restricted&#x60;; support can tell you why), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="deliversellerorder"></a>
# **DeliverSellerOrder**
> SellerOrder DeliverSellerOrder (Guid id, string idempotencyKey, SellerOrderPostDelivery? sellerOrderPostDelivery = null)

Deliver an order

Delivers an order placed on one of your medias (`state` `pending_order_delivery`), as the web does. A post order takes the URL of the published post and the confirmation of its publication date; a link addition order takes no body, and any field is refused. The order moves to `pending_order_delivery_review` and the buyer is asked to review it, or, for a post order whose scheduled publication date is still to come, to `scheduled` without telling the buyer yet. The URL is checked to be a URL only, as the web does.

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
    public class DeliverSellerOrderExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var sellerOrderPostDelivery = new SellerOrderPostDelivery?(); // SellerOrderPostDelivery? |  (optional) 

            try
            {
                // Deliver an order
                SellerOrder result = apiInstance.DeliverSellerOrder(id, idempotencyKey, sellerOrderPostDelivery);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.DeliverSellerOrder: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DeliverSellerOrderWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Deliver an order
    ApiResponse<SellerOrder> response = apiInstance.DeliverSellerOrderWithHttpInfo(id, idempotencyKey, sellerOrderPostDelivery);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.DeliverSellerOrderWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **sellerOrderPostDelivery** | [**SellerOrderPostDelivery?**](SellerOrderPostDelivery?.md) |  | [optional]  |

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
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The order is not waiting for its delivery (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="deliversellerorderdraft"></a>
# **DeliverSellerOrderDraft**
> SellerOrder DeliverSellerOrderDraft (Guid id, string idempotencyKey, SellerOrderDraftFile sellerOrderDraftFile)

Deliver a draft

Delivers the draft of a post order placed on one of your medias whose draft you write (`state` `pending_draft`), as the web does, from a file you uploaded with POST /files. The order moves to `pending_draft_review` when the buyer reviews drafts, otherwise to `pending_order_delivery`. The file is used up once the draft is delivered; a refused request leaves it usable.

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
    public class DeliverSellerOrderDraftExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var sellerOrderDraftFile = new SellerOrderDraftFile(); // SellerOrderDraftFile | 

            try
            {
                // Deliver a draft
                SellerOrder result = apiInstance.DeliverSellerOrderDraft(id, idempotencyKey, sellerOrderDraftFile);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.DeliverSellerOrderDraft: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DeliverSellerOrderDraftWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Deliver a draft
    ApiResponse<SellerOrder> response = apiInstance.DeliverSellerOrderDraftWithHttpInfo(id, idempotencyKey, sellerOrderDraftFile);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.DeliverSellerOrderDraftWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **sellerOrderDraftFile** | [**SellerOrderDraftFile**](SellerOrderDraftFile.md) |  |  |

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
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The order is not waiting for a draft you write (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is not valid, or the file is not an odt, doc, docx or txt file of up to 8 MB (code &#x60;validation_failed&#x60;, with the messages of each field in &#x60;details.fields&#x60;), or &#x60;fileId&#x60; names no file you can use: it does not exist, has expired or was already used (code &#x60;file_unusable&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="deliversellerorderdraftupdate"></a>
# **DeliverSellerOrderDraftUpdate**
> SellerOrder DeliverSellerOrderDraftUpdate (Guid id, string idempotencyKey, SellerOrderDraftFile sellerOrderDraftFile)

Deliver a draft update

Delivers the draft update the buyer asked for on a post order placed on one of your medias whose draft you write (`state` `pending_draft_update`), as the web does, from a file you uploaded with POST /files. The order moves back to `pending_draft_review`. The file is used up once the draft is delivered; a refused request leaves it usable.

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
    public class DeliverSellerOrderDraftUpdateExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var sellerOrderDraftFile = new SellerOrderDraftFile(); // SellerOrderDraftFile | 

            try
            {
                // Deliver a draft update
                SellerOrder result = apiInstance.DeliverSellerOrderDraftUpdate(id, idempotencyKey, sellerOrderDraftFile);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.DeliverSellerOrderDraftUpdate: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DeliverSellerOrderDraftUpdateWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Deliver a draft update
    ApiResponse<SellerOrder> response = apiInstance.DeliverSellerOrderDraftUpdateWithHttpInfo(id, idempotencyKey, sellerOrderDraftFile);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.DeliverSellerOrderDraftUpdateWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **sellerOrderDraftFile** | [**SellerOrderDraftFile**](SellerOrderDraftFile.md) |  |  |

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
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The buyer has not asked for an update of a draft you write (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is not valid, or the file is not an odt, doc, docx or txt file of up to 8 MB (code &#x60;validation_failed&#x60;, with the messages of each field in &#x60;details.fields&#x60;), or &#x60;fileId&#x60; names no file you can use: it does not exist, has expired or was already used (code &#x60;file_unusable&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="deliversellerorderupdate"></a>
# **DeliverSellerOrderUpdate**
> SellerOrder DeliverSellerOrderUpdate (Guid id, string idempotencyKey, SellerOrderPostDelivery? sellerOrderPostDelivery = null)

Deliver an update

Delivers the update the buyer asked for on an order placed on one of your medias (`state` `pending_order_delivery_update`), as the web does. A post order takes the URL of the published post, which may be the same as before, and the confirmation of its publication date; both must be sent. A link addition order takes no body, and any field is refused. The order moves back to `pending_order_delivery_review` and the buyer is asked to review it.

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
    public class DeliverSellerOrderUpdateExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var sellerOrderPostDelivery = new SellerOrderPostDelivery?(); // SellerOrderPostDelivery? |  (optional) 

            try
            {
                // Deliver an update
                SellerOrder result = apiInstance.DeliverSellerOrderUpdate(id, idempotencyKey, sellerOrderPostDelivery);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.DeliverSellerOrderUpdate: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DeliverSellerOrderUpdateWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Deliver an update
    ApiResponse<SellerOrder> response = apiInstance.DeliverSellerOrderUpdateWithHttpInfo(id, idempotencyKey, sellerOrderPostDelivery);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.DeliverSellerOrderUpdateWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **sellerOrderPostDelivery** | [**SellerOrderPostDelivery?**](SellerOrderPostDelivery?.md) |  | [optional]  |

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
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The buyer has not asked for an update (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="downloadsellerorderbriefing"></a>
# **DownloadSellerOrderBriefing**
> FileParameter DownloadSellerOrderBriefing (Guid id)

Download the draft the buyer attached to an order

The file the buyer attached to the briefing of a post order you sell. 404 when the order has none (`briefing.hasProposedDraft` is false) or the file cannot be read.

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
    public class DownloadSellerOrderBriefingExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 

            try
            {
                // Download the draft the buyer attached to an order
                FileParameter result = apiInstance.DownloadSellerOrderBriefing(id);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.DownloadSellerOrderBriefing: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DownloadSellerOrderBriefingWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Download the draft the buyer attached to an order
    ApiResponse<FileParameter> response = apiInstance.DownloadSellerOrderBriefingWithHttpInfo(id);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.DownloadSellerOrderBriefingWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |

### Return type

[**FileParameter**](FileParameter.md)

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
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="downloadsellerorderdraft"></a>
# **DownloadSellerOrderDraft**
> FileParameter DownloadSellerOrderDraft (Guid id)

Download the draft of an order you sell

The file of the current draft of a post order you sell. 404 when the order has no draft file (`draft.hasFile` is false) or the file cannot be read. Earlier drafts are not available.

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
    public class DownloadSellerOrderDraftExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 

            try
            {
                // Download the draft of an order you sell
                FileParameter result = apiInstance.DownloadSellerOrderDraft(id);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.DownloadSellerOrderDraft: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DownloadSellerOrderDraftWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Download the draft of an order you sell
    ApiResponse<FileParameter> response = apiInstance.DownloadSellerOrderDraftWithHttpInfo(id);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.DownloadSellerOrderDraftWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |

### Return type

[**FileParameter**](FileParameter.md)

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
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getsellerorder"></a>
# **GetSellerOrder**
> SellerOrder GetSellerOrder (Guid id)

Get an order you sell

One order placed on one of your medias, with its briefing, its draft and its state history. An order you only bought is not found here; it is under GET /orders/{id}.

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
    public class GetSellerOrderExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 

            try
            {
                // Get an order you sell
                SellerOrder result = apiInstance.GetSellerOrder(id);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.GetSellerOrder: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetSellerOrderWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get an order you sell
    ApiResponse<SellerOrder> response = apiInstance.GetSellerOrderWithHttpInfo(id);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.GetSellerOrderWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |

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
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listsellerorders"></a>
# **ListSellerOrders**
> ListSellerOrders200Response ListSellerOrders (Guid? mediaId = null, string? state = null, DateTime? updatedSince = null, string? sort = null, int? limit = null, int? offset = null)

List the orders you sell

The orders placed on your medias, newest first by default. To follow them, poll with `sort=updatedAt` and `updatedSince` set to the `updatedAt` of the last order you saw: an order moves to the end of that list each time it changes state. The orders you bought are under GET /orders.

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
    public class ListSellerOrdersExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var mediaId = "mediaId_example";  // Guid? | Only the orders on this media of yours. (optional) 
            var state = pending_acceptance,pending_order_delivery;  // string? | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones. (optional) 
            var updatedSince = DateTime.Parse("2013-10-20T19:20:30+01:00");  // DateTime? | Only the orders whose `updatedAt` is at or after this instant, an ISO-8601 date-time with its offset (send `+` as `%2B`). (optional) 
            var sort = "-createdAt";  // string? | `-createdAt`, newest first, or `updatedAt`, least recently changed first. Orders of the same instant come in id order. (optional)  (default to -createdAt)
            var limit = 20;  // int? | Orders per page, 1 to 100. (optional)  (default to 20)
            var offset = 0;  // int? | Orders to skip. (optional)  (default to 0)

            try
            {
                // List the orders you sell
                ListSellerOrders200Response result = apiInstance.ListSellerOrders(mediaId, state, updatedSince, sort, limit, offset);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.ListSellerOrders: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListSellerOrdersWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List the orders you sell
    ApiResponse<ListSellerOrders200Response> response = apiInstance.ListSellerOrdersWithHttpInfo(mediaId, state, updatedSince, sort, limit, offset);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.ListSellerOrdersWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **mediaId** | **Guid?** | Only the orders on this media of yours. | [optional]  |
| **state** | **string?** | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones. | [optional]  |
| **updatedSince** | **DateTime?** | Only the orders whose &#x60;updatedAt&#x60; is at or after this instant, an ISO-8601 date-time with its offset (send &#x60;+&#x60; as &#x60;%2B&#x60;). | [optional]  |
| **sort** | **string?** | &#x60;-createdAt&#x60;, newest first, or &#x60;updatedAt&#x60;, least recently changed first. Orders of the same instant come in id order. | [optional] [default to -createdAt] |
| **limit** | **int?** | Orders per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int?** | Orders to skip. | [optional] [default to 0] |

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
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="refutesellerorderdraftupdate"></a>
# **RefuteSellerOrderDraftUpdate**
> SellerOrder RefuteSellerOrderDraftUpdate (Guid id, string idempotencyKey, SellerOrderRefutation sellerOrderRefutation)

Refuse a draft update

Refuses the draft update the buyer asked for on a post order placed on one of your medias whose draft you write (`state` `pending_draft_update`), as the web does. The order moves back to `pending_draft_review` and the buyer is told your reason. A draft Growwer or the buyer writes cannot be refused here.

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
    public class RefuteSellerOrderDraftUpdateExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var sellerOrderRefutation = new SellerOrderRefutation(); // SellerOrderRefutation | 

            try
            {
                // Refuse a draft update
                SellerOrder result = apiInstance.RefuteSellerOrderDraftUpdate(id, idempotencyKey, sellerOrderRefutation);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.RefuteSellerOrderDraftUpdate: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the RefuteSellerOrderDraftUpdateWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Refuse a draft update
    ApiResponse<SellerOrder> response = apiInstance.RefuteSellerOrderDraftUpdateWithHttpInfo(id, idempotencyKey, sellerOrderRefutation);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.RefuteSellerOrderDraftUpdateWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **sellerOrderRefutation** | [**SellerOrderRefutation**](SellerOrderRefutation.md) |  |  |

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
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The buyer has not asked for an update of a draft you write, including when Growwer or the buyer writes the draft (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="refutesellerorderupdate"></a>
# **RefuteSellerOrderUpdate**
> SellerOrder RefuteSellerOrderUpdate (Guid id, string idempotencyKey, SellerOrderRefutation sellerOrderRefutation)

Refuse an update

Refuses the update the buyer asked for on an order placed on one of your medias (`state` `pending_order_delivery_update`), as the web does. The order moves back to `pending_order_delivery_review` and the buyer is told your reason.

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
    public class RefuteSellerOrderUpdateExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var sellerOrderRefutation = new SellerOrderRefutation(); // SellerOrderRefutation | 

            try
            {
                // Refuse an update
                SellerOrder result = apiInstance.RefuteSellerOrderUpdate(id, idempotencyKey, sellerOrderRefutation);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.RefuteSellerOrderUpdate: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the RefuteSellerOrderUpdateWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Refuse an update
    ApiResponse<SellerOrder> response = apiInstance.RefuteSellerOrderUpdateWithHttpInfo(id, idempotencyKey, sellerOrderRefutation);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.RefuteSellerOrderUpdateWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **sellerOrderRefutation** | [**SellerOrderRefutation**](SellerOrderRefutation.md) |  |  |

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
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The buyer has not asked for an update (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="rejectsellerorder"></a>
# **RejectSellerOrder**
> SellerOrder RejectSellerOrder (Guid id, string idempotencyKey, SellerOrderRejection sellerOrderRejection)

Reject an order

Rejects an order placed on one of your medias that you have not accepted yet (`state` `pending_acceptance`), as the web does. The order moves to `rejected_by_seller`, its price returns to the buyer, and the buyer is told your reason.

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
    public class RejectSellerOrderExample
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
            var apiInstance = new SellerOrdersApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var sellerOrderRejection = new SellerOrderRejection(); // SellerOrderRejection | 

            try
            {
                // Reject an order
                SellerOrder result = apiInstance.RejectSellerOrder(id, idempotencyKey, sellerOrderRejection);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SellerOrdersApi.RejectSellerOrder: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the RejectSellerOrderWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Reject an order
    ApiResponse<SellerOrder> response = apiInstance.RejectSellerOrderWithHttpInfo(id, idempotencyKey, sellerOrderRejection);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SellerOrdersApi.RejectSellerOrderWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **sellerOrderRejection** | [**SellerOrderRejection**](SellerOrderRejection.md) |  |  |

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
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The order is not waiting for your acceptance (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

