# Growwer.Api.Api.ManagedServicesApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**EstimateManagedServiceProposals**](ManagedServicesApi.md#estimatemanagedserviceproposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/estimate | Estimate accepting proposals |
| [**GetManagedServiceCampaign**](ManagedServicesApi.md#getmanagedservicecampaign) | **GET** /api/v1/managed-service/campaigns/{id} | Get a managed service campaign |
| [**GetManagedServiceProposalsSummary**](ManagedServicesApi.md#getmanagedserviceproposalssummary) | **GET** /api/v1/managed-service/campaigns/{id}/proposals-summary | Download the summary of a campaign&#39;s proposals |
| [**ListManagedServiceCampaigns**](ManagedServicesApi.md#listmanagedservicecampaigns) | **GET** /api/v1/managed-service/campaigns | List your managed service campaigns |
| [**ListManagedServiceProposals**](ManagedServicesApi.md#listmanagedserviceproposals) | **GET** /api/v1/managed-service/campaigns/{id}/proposals | List the proposals of a campaign |
| [**RequestManagedServiceCampaign**](ManagedServicesApi.md#requestmanagedservicecampaign) | **POST** /api/v1/managed-service/campaign-requests | Request a new campaign |
| [**RequestManagedServiceInfo**](ManagedServicesApi.md#requestmanagedserviceinfo) | **POST** /api/v1/managed-service/info-requests | Ask about the managed service |
| [**ReviewManagedServiceProposals**](ManagedServicesApi.md#reviewmanagedserviceproposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/review | Accept or reject proposals |

<a id="estimatemanagedserviceproposals"></a>
# **EstimateManagedServiceProposals**
> ManagedServiceProposalsEstimate EstimateManagedServiceProposals (Guid id, ManagedServiceProposalsEstimateRequest? managedServiceProposalsEstimateRequest = null)

Estimate accepting proposals

Totals the campaign's accepted proposals that still await their order and the `proposed` ones you name in `accept`, and compares the total with your wallet's available balance. Each proposal counts at its `currentPrice`, or at its `proposedPrice` when the media no longer offers the service. Nothing is accepted, charged or reserved, so a read-only key may call it and it takes no Idempotency-Key.  The estimate is advisory: accepting a proposal charges nothing. The team charges your wallet when it places the order for an accepted proposal, and the same balance pays for the orders you place yourself.

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
    public class EstimateManagedServiceProposalsExample
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
            var apiInstance = new ManagedServicesApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var managedServiceProposalsEstimateRequest = new ManagedServiceProposalsEstimateRequest?(); // ManagedServiceProposalsEstimateRequest? |  (optional) 

            try
            {
                // Estimate accepting proposals
                ManagedServiceProposalsEstimate result = apiInstance.EstimateManagedServiceProposals(id, managedServiceProposalsEstimateRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ManagedServicesApi.EstimateManagedServiceProposals: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the EstimateManagedServiceProposalsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Estimate accepting proposals
    ApiResponse<ManagedServiceProposalsEstimate> response = apiInstance.EstimateManagedServiceProposalsWithHttpInfo(id, managedServiceProposalsEstimateRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ManagedServicesApi.EstimateManagedServiceProposalsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **managedServiceProposalsEstimateRequest** | [**ManagedServiceProposalsEstimateRequest?**](ManagedServiceProposalsEstimateRequest?.md) |  | [optional]  |

### Return type

[**ManagedServiceProposalsEstimate**](ManagedServiceProposalsEstimate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The totals and how your wallet covers them. |  -  |
| **400** | The body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The campaign is not yours, or a proposal named in &#x60;accept&#x60; is not one of the campaign&#39;s (code &#x60;not_found&#x60;, with &#x60;details.proposalId&#x60;). |  -  |
| **409** | A proposal named in &#x60;accept&#x60; is not awaiting your review (code &#x60;invalid_state&#x60;, with &#x60;details.proposalIds&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getmanagedservicecampaign"></a>
# **GetManagedServiceCampaign**
> ManagedServiceCampaign GetManagedServiceCampaign (Guid id)

Get a managed service campaign

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
    public class GetManagedServiceCampaignExample
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
            var apiInstance = new ManagedServicesApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 

            try
            {
                // Get a managed service campaign
                ManagedServiceCampaign result = apiInstance.GetManagedServiceCampaign(id);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ManagedServicesApi.GetManagedServiceCampaign: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetManagedServiceCampaignWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get a managed service campaign
    ApiResponse<ManagedServiceCampaign> response = apiInstance.GetManagedServiceCampaignWithHttpInfo(id);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ManagedServicesApi.GetManagedServiceCampaignWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |

### Return type

[**ManagedServiceCampaign**](ManagedServiceCampaign.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The campaign. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getmanagedserviceproposalssummary"></a>
# **GetManagedServiceProposalsSummary**
> FileParameter GetManagedServiceProposalsSummary (Guid id, string? extended = null)

Download the summary of a campaign's proposals

The PDF the campaign page offers: the proposals awaiting your review, accepted or being published, newest first, in your language. With `extended=true` it also shows each proposal's price, the price it was proposed at (`proposedPrice`).

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
    public class GetManagedServiceProposalsSummaryExample
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
            var apiInstance = new ManagedServicesApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var extended = "true";  // string? | Whether to show the prices. (optional)  (default to false)

            try
            {
                // Download the summary of a campaign's proposals
                FileParameter result = apiInstance.GetManagedServiceProposalsSummary(id, extended);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ManagedServicesApi.GetManagedServiceProposalsSummary: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetManagedServiceProposalsSummaryWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Download the summary of a campaign's proposals
    ApiResponse<FileParameter> response = apiInstance.GetManagedServiceProposalsSummaryWithHttpInfo(id, extended);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ManagedServicesApi.GetManagedServiceProposalsSummaryWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **extended** | **string?** | Whether to show the prices. | [optional] [default to false] |

### Return type

[**FileParameter**](FileParameter.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The summary. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listmanagedservicecampaigns"></a>
# **ListManagedServiceCampaigns**
> ListManagedServiceCampaigns200Response ListManagedServiceCampaigns (int? limit = null, int? offset = null)

List your managed service campaigns

The campaigns your managed service runs for you, newest first. Without a managed service the list is empty: GET /me says whether you have one.

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
    public class ListManagedServiceCampaignsExample
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
            var apiInstance = new ManagedServicesApi(httpClient, config, httpClientHandler);
            var limit = 20;  // int? | Campaigns per page, 1 to 100. (optional)  (default to 20)
            var offset = 0;  // int? | Campaigns to skip. (optional)  (default to 0)

            try
            {
                // List your managed service campaigns
                ListManagedServiceCampaigns200Response result = apiInstance.ListManagedServiceCampaigns(limit, offset);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ManagedServicesApi.ListManagedServiceCampaigns: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListManagedServiceCampaignsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List your managed service campaigns
    ApiResponse<ListManagedServiceCampaigns200Response> response = apiInstance.ListManagedServiceCampaignsWithHttpInfo(limit, offset);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ManagedServicesApi.ListManagedServiceCampaignsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **limit** | **int?** | Campaigns per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int?** | Campaigns to skip. | [optional] [default to 0] |

### Return type

[**ListManagedServiceCampaigns200Response**](ListManagedServiceCampaigns200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of your campaigns and how many you have in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listmanagedserviceproposals"></a>
# **ListManagedServiceProposals**
> ListManagedServiceProposals200Response ListManagedServiceProposals (Guid id, string? state = null, int? limit = null, int? offset = null)

List the proposals of a campaign

The medias the team proposes for the campaign, newest first. Those `proposed` await your review (POST /managed-service/campaigns/{id}/proposals/review).

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
    public class ListManagedServiceProposalsExample
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
            var apiInstance = new ManagedServicesApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var state = proposed,accepted;  // string? | Only proposals in these states, comma-separated: `proposed`, `accepted`, `cancelled`, `purchase_started`, `purchase_finished`. (optional) 
            var limit = 20;  // int? | Proposals per page, 1 to 100. (optional)  (default to 20)
            var offset = 0;  // int? | Proposals to skip. (optional)  (default to 0)

            try
            {
                // List the proposals of a campaign
                ListManagedServiceProposals200Response result = apiInstance.ListManagedServiceProposals(id, state, limit, offset);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ManagedServicesApi.ListManagedServiceProposals: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListManagedServiceProposalsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List the proposals of a campaign
    ApiResponse<ListManagedServiceProposals200Response> response = apiInstance.ListManagedServiceProposalsWithHttpInfo(id, state, limit, offset);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ManagedServicesApi.ListManagedServiceProposalsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **state** | **string?** | Only proposals in these states, comma-separated: &#x60;proposed&#x60;, &#x60;accepted&#x60;, &#x60;cancelled&#x60;, &#x60;purchase_started&#x60;, &#x60;purchase_finished&#x60;. | [optional]  |
| **limit** | **int?** | Proposals per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int?** | Proposals to skip. | [optional] [default to 0] |

### Return type

[**ListManagedServiceProposals200Response**](ListManagedServiceProposals200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of the campaign&#39;s proposals and how many match in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="requestmanagedservicecampaign"></a>
# **RequestManagedServiceCampaign**
> ManagedServiceRequestSent RequestManagedServiceCampaign (string idempotencyKey, ManagedServiceRequest managedServiceRequest)

Request a new campaign

Asks your account manager for a new campaign, as the managed service page does: the team emails you to agree on it. For accounts with a managed service (GET /me `managedService.active`); without one, POST /managed-service/info-requests asks about the service.  The API admits a limited number of such requests per user and UTC day (5 by default; the refusal message states the current limit). Past it, it answers 429 `managed_service_request_limit_reached`, with `Retry-After` the time to the next UTC midnight. A request that is refused (4xx) does not count; one that fails on the server (5xx) does, as it may have been sent.

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
    public class RequestManagedServiceCampaignExample
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
            var apiInstance = new ManagedServicesApi(httpClient, config, httpClientHandler);
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var managedServiceRequest = new ManagedServiceRequest(); // ManagedServiceRequest | 

            try
            {
                // Request a new campaign
                ManagedServiceRequestSent result = apiInstance.RequestManagedServiceCampaign(idempotencyKey, managedServiceRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ManagedServicesApi.RequestManagedServiceCampaign: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the RequestManagedServiceCampaignWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Request a new campaign
    ApiResponse<ManagedServiceRequestSent> response = apiInstance.RequestManagedServiceCampaignWithHttpInfo(idempotencyKey, managedServiceRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ManagedServicesApi.RequestManagedServiceCampaignWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **managedServiceRequest** | [**ManagedServiceRequest**](ManagedServiceRequest.md) |  |  |

### Return type

[**ManagedServiceRequestSent**](ManagedServiceRequestSent.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request was sent. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **409** | You have no managed service yet (code &#x60;managed_service_required&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="requestmanagedserviceinfo"></a>
# **RequestManagedServiceInfo**
> ManagedServiceRequestSent RequestManagedServiceInfo (string idempotencyKey, ManagedServiceRequest managedServiceRequest)

Ask about the managed service

Asks the team about the managed service for your website, as the managed service landing page does: the team contacts you. For accounts without a managed service (GET /me `managedService.active`); with one, POST /managed-service/campaign-requests requests a new campaign.  The API admits a limited number of such requests per user and UTC day (5 by default; the refusal message states the current limit). Past it, it answers 429 `managed_service_request_limit_reached`, with `Retry-After` the time to the next UTC midnight. A request that is refused (4xx) does not count; one that fails on the server (5xx) does, as it may have been sent.

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
    public class RequestManagedServiceInfoExample
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
            var apiInstance = new ManagedServicesApi(httpClient, config, httpClientHandler);
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var managedServiceRequest = new ManagedServiceRequest(); // ManagedServiceRequest | 

            try
            {
                // Ask about the managed service
                ManagedServiceRequestSent result = apiInstance.RequestManagedServiceInfo(idempotencyKey, managedServiceRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ManagedServicesApi.RequestManagedServiceInfo: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the RequestManagedServiceInfoWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Ask about the managed service
    ApiResponse<ManagedServiceRequestSent> response = apiInstance.RequestManagedServiceInfoWithHttpInfo(idempotencyKey, managedServiceRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ManagedServicesApi.RequestManagedServiceInfoWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **managedServiceRequest** | [**ManagedServiceRequest**](ManagedServiceRequest.md) |  |  |

### Return type

[**ManagedServiceRequestSent**](ManagedServiceRequestSent.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request was sent. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **409** | You already have a managed service (code &#x60;managed_service_exists&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="reviewmanagedserviceproposals"></a>
# **ReviewManagedServiceProposals**
> ManagedServiceProposalReview ReviewManagedServiceProposals (Guid id, string idempotencyKey, ManagedServiceProposalReviewRequest managedServiceProposalReviewRequest)

Accept or reject proposals

Decides on every proposal of the campaign that awaits your review (`state` `proposed`), as the campaign page does: name each one once, with `accept` or `reject`, and a comment for the team to reject one. Their order in the body does not matter. Accepting charges nothing: the team places the orders for the accepted proposals and your wallet pays for them then. POST /managed-service/campaigns/{id}/proposals/estimate says what they would cost.  When every proposal is accepted the campaign moves to `proposal_accepted`; when one is rejected the team is told and prepares others. A proposal someone else moved on the campaign page while the request ran is answered in the state it reached.

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
    public class ReviewManagedServiceProposalsExample
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
            var apiInstance = new ManagedServicesApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
            var managedServiceProposalReviewRequest = new ManagedServiceProposalReviewRequest(); // ManagedServiceProposalReviewRequest | 

            try
            {
                // Accept or reject proposals
                ManagedServiceProposalReview result = apiInstance.ReviewManagedServiceProposals(id, idempotencyKey, managedServiceProposalReviewRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ManagedServicesApi.ReviewManagedServiceProposals: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ReviewManagedServiceProposalsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Accept or reject proposals
    ApiResponse<ManagedServiceProposalReview> response = apiInstance.ReviewManagedServiceProposalsWithHttpInfo(id, idempotencyKey, managedServiceProposalReviewRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ManagedServicesApi.ReviewManagedServiceProposalsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **managedServiceProposalReviewRequest** | [**ManagedServiceProposalReviewRequest**](ManagedServiceProposalReviewRequest.md) |  |  |

### Return type

[**ManagedServiceProposalReview**](ManagedServiceProposalReview.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The campaign and the proposals you reviewed, as they now are. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The campaign is not yours, or a proposal named is not one of the campaign&#39;s (code &#x60;not_found&#x60;, with &#x60;details.proposalId&#x60;). |  -  |
| **409** | No proposal of the campaign awaits your review (code &#x60;no_pending_proposals&#x60;), or a proposal named does not (code &#x60;invalid_state&#x60;, with &#x60;details.proposalIds&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is invalid (code &#x60;validation_failed&#x60;), or it leaves out proposals awaiting your review (code &#x60;review_incomplete&#x60;, with &#x60;details.missingProposalIds&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

