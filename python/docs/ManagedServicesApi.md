# growwer.ManagedServicesApi

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**estimate_managed_service_proposals**](ManagedServicesApi.md#estimate_managed_service_proposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/estimate | Estimate accepting proposals
[**get_managed_service_campaign**](ManagedServicesApi.md#get_managed_service_campaign) | **GET** /api/v1/managed-service/campaigns/{id} | Get a managed service campaign
[**get_managed_service_proposals_summary**](ManagedServicesApi.md#get_managed_service_proposals_summary) | **GET** /api/v1/managed-service/campaigns/{id}/proposals-summary | Download the summary of a campaign&#39;s proposals
[**list_managed_service_campaigns**](ManagedServicesApi.md#list_managed_service_campaigns) | **GET** /api/v1/managed-service/campaigns | List your managed service campaigns
[**list_managed_service_proposals**](ManagedServicesApi.md#list_managed_service_proposals) | **GET** /api/v1/managed-service/campaigns/{id}/proposals | List the proposals of a campaign
[**request_managed_service_campaign**](ManagedServicesApi.md#request_managed_service_campaign) | **POST** /api/v1/managed-service/campaign-requests | Request a new campaign
[**request_managed_service_info**](ManagedServicesApi.md#request_managed_service_info) | **POST** /api/v1/managed-service/info-requests | Ask about the managed service
[**review_managed_service_proposals**](ManagedServicesApi.md#review_managed_service_proposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/review | Accept or reject proposals


# **estimate_managed_service_proposals**
> ManagedServiceProposalsEstimate estimate_managed_service_proposals(id, managed_service_proposals_estimate_request=managed_service_proposals_estimate_request)

Estimate accepting proposals

Totals the campaign's accepted proposals that still await their order and the `proposed` ones you name in `accept`, and compares the total with your wallet's available balance. Each proposal counts at its `currentPrice`, or at its `proposedPrice` when the media no longer offers the service. Nothing is accepted, charged or reserved, so a read-only key may call it and it takes no Idempotency-Key.

The estimate is advisory: accepting a proposal charges nothing. The team charges your wallet when it places the order for an accepted proposal, and the same balance pays for the orders you place yourself.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.managed_service_proposals_estimate import ManagedServiceProposalsEstimate
from growwer.models.managed_service_proposals_estimate_request import ManagedServiceProposalsEstimateRequest
from growwer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tool.growwer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = growwer.Configuration(
    host = "https://tool.growwer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = growwer.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with growwer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = growwer.ManagedServicesApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    managed_service_proposals_estimate_request = growwer.ManagedServiceProposalsEstimateRequest() # ManagedServiceProposalsEstimateRequest |  (optional)

    try:
        # Estimate accepting proposals
        api_response = api_instance.estimate_managed_service_proposals(id, managed_service_proposals_estimate_request=managed_service_proposals_estimate_request)
        print("The response of ManagedServicesApi->estimate_managed_service_proposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedServicesApi->estimate_managed_service_proposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **managed_service_proposals_estimate_request** | [**ManagedServiceProposalsEstimateRequest**](ManagedServiceProposalsEstimateRequest.md)|  | [optional] 

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
**200** | The totals and how your wallet covers them. |  -  |
**400** | The body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**404** | The campaign is not yours, or a proposal named in &#x60;accept&#x60; is not one of the campaign&#39;s (code &#x60;not_found&#x60;, with &#x60;details.proposalId&#x60;). |  -  |
**409** | A proposal named in &#x60;accept&#x60; is not awaiting your review (code &#x60;invalid_state&#x60;, with &#x60;details.proposalIds&#x60;). |  -  |
**422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_service_campaign**
> ManagedServiceCampaign get_managed_service_campaign(id)

Get a managed service campaign

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.managed_service_campaign import ManagedServiceCampaign
from growwer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tool.growwer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = growwer.Configuration(
    host = "https://tool.growwer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = growwer.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with growwer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = growwer.ManagedServicesApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a managed service campaign
        api_response = api_instance.get_managed_service_campaign(id)
        print("The response of ManagedServicesApi->get_managed_service_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedServicesApi->get_managed_service_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

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
**200** | The campaign. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_service_proposals_summary**
> bytes get_managed_service_proposals_summary(id, extended=extended)

Download the summary of a campaign's proposals

The PDF the campaign page offers: the proposals awaiting your review, accepted or being published, newest first, in your language. With `extended=true` it also shows each proposal's price, the price it was proposed at (`proposedPrice`).

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tool.growwer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = growwer.Configuration(
    host = "https://tool.growwer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = growwer.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with growwer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = growwer.ManagedServicesApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    extended = 'false' # str | Whether to show the prices. (optional) (default to 'false')

    try:
        # Download the summary of a campaign's proposals
        api_response = api_instance.get_managed_service_proposals_summary(id, extended=extended)
        print("The response of ManagedServicesApi->get_managed_service_proposals_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedServicesApi->get_managed_service_proposals_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **extended** | **str**| Whether to show the prices. | [optional] [default to &#39;false&#39;]

### Return type

**bytes**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The summary. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_managed_service_campaigns**
> ListManagedServiceCampaigns200Response list_managed_service_campaigns(limit=limit, offset=offset)

List your managed service campaigns

The campaigns your managed service runs for you, newest first. Without a managed service the list is empty: GET /me says whether you have one.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.list_managed_service_campaigns200_response import ListManagedServiceCampaigns200Response
from growwer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tool.growwer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = growwer.Configuration(
    host = "https://tool.growwer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = growwer.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with growwer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = growwer.ManagedServicesApi(api_client)
    limit = 20 # int | Campaigns per page, 1 to 100. (optional) (default to 20)
    offset = 0 # int | Campaigns to skip. (optional) (default to 0)

    try:
        # List your managed service campaigns
        api_response = api_instance.list_managed_service_campaigns(limit=limit, offset=offset)
        print("The response of ManagedServicesApi->list_managed_service_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedServicesApi->list_managed_service_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Campaigns per page, 1 to 100. | [optional] [default to 20]
 **offset** | **int**| Campaigns to skip. | [optional] [default to 0]

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
**200** | A page of your campaigns and how many you have in all. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_managed_service_proposals**
> ListManagedServiceProposals200Response list_managed_service_proposals(id, state=state, limit=limit, offset=offset)

List the proposals of a campaign

The medias the team proposes for the campaign, newest first. Those `proposed` await your review (POST /managed-service/campaigns/{id}/proposals/review).

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.list_managed_service_proposals200_response import ListManagedServiceProposals200Response
from growwer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tool.growwer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = growwer.Configuration(
    host = "https://tool.growwer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = growwer.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with growwer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = growwer.ManagedServicesApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    state = 'proposed,accepted' # str | Only proposals in these states, comma-separated: `proposed`, `accepted`, `cancelled`, `purchase_started`, `purchase_finished`. (optional)
    limit = 20 # int | Proposals per page, 1 to 100. (optional) (default to 20)
    offset = 0 # int | Proposals to skip. (optional) (default to 0)

    try:
        # List the proposals of a campaign
        api_response = api_instance.list_managed_service_proposals(id, state=state, limit=limit, offset=offset)
        print("The response of ManagedServicesApi->list_managed_service_proposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedServicesApi->list_managed_service_proposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **state** | **str**| Only proposals in these states, comma-separated: &#x60;proposed&#x60;, &#x60;accepted&#x60;, &#x60;cancelled&#x60;, &#x60;purchase_started&#x60;, &#x60;purchase_finished&#x60;. | [optional] 
 **limit** | **int**| Proposals per page, 1 to 100. | [optional] [default to 20]
 **offset** | **int**| Proposals to skip. | [optional] [default to 0]

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
**200** | A page of the campaign&#39;s proposals and how many match in all. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_managed_service_campaign**
> ManagedServiceRequestSent request_managed_service_campaign(idempotency_key, managed_service_request)

Request a new campaign

Asks your account manager for a new campaign, as the managed service page does: the team emails you to agree on it. For accounts with a managed service (GET /me `managedService.active`); without one, POST /managed-service/info-requests asks about the service.

You may send 5 such requests per UTC day through the API. Past them it answers 429 `managed_service_request_limit_reached`, with `Retry-After` the time to the next UTC midnight. A request that is refused (4xx) does not count; one that fails on the server (5xx) does, as it may have been sent.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.managed_service_request import ManagedServiceRequest
from growwer.models.managed_service_request_sent import ManagedServiceRequestSent
from growwer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tool.growwer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = growwer.Configuration(
    host = "https://tool.growwer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = growwer.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with growwer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = growwer.ManagedServicesApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    managed_service_request = growwer.ManagedServiceRequest() # ManagedServiceRequest | 

    try:
        # Request a new campaign
        api_response = api_instance.request_managed_service_campaign(idempotency_key, managed_service_request)
        print("The response of ManagedServicesApi->request_managed_service_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedServicesApi->request_managed_service_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **managed_service_request** | [**ManagedServiceRequest**](ManagedServiceRequest.md)|  | 

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
**202** | The request was sent. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
**409** | You have no managed service yet (code &#x60;managed_service_required&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_managed_service_info**
> ManagedServiceRequestSent request_managed_service_info(idempotency_key, managed_service_request)

Ask about the managed service

Asks the team about the managed service for your website, as the managed service landing page does: the team contacts you. For accounts without a managed service (GET /me `managedService.active`); with one, POST /managed-service/campaign-requests requests a new campaign.

You may send 5 such requests per UTC day through the API. Past them it answers 429 `managed_service_request_limit_reached`, with `Retry-After` the time to the next UTC midnight. A request that is refused (4xx) does not count; one that fails on the server (5xx) does, as it may have been sent.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.managed_service_request import ManagedServiceRequest
from growwer.models.managed_service_request_sent import ManagedServiceRequestSent
from growwer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tool.growwer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = growwer.Configuration(
    host = "https://tool.growwer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = growwer.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with growwer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = growwer.ManagedServicesApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    managed_service_request = growwer.ManagedServiceRequest() # ManagedServiceRequest | 

    try:
        # Ask about the managed service
        api_response = api_instance.request_managed_service_info(idempotency_key, managed_service_request)
        print("The response of ManagedServicesApi->request_managed_service_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedServicesApi->request_managed_service_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **managed_service_request** | [**ManagedServiceRequest**](ManagedServiceRequest.md)|  | 

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
**202** | The request was sent. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
**409** | You already have a managed service (code &#x60;managed_service_exists&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_managed_service_proposals**
> ManagedServiceProposalReview review_managed_service_proposals(id, idempotency_key, managed_service_proposal_review_request)

Accept or reject proposals

Decides on every proposal of the campaign that awaits your review (`state` `proposed`), as the campaign page does: name each one once, with `accept` or `reject`, and a comment for the team to reject one. Their order in the body does not matter. Accepting charges nothing: the team places the orders for the accepted proposals and your wallet pays for them then. POST /managed-service/campaigns/{id}/proposals/estimate says what they would cost.

When every proposal is accepted the campaign moves to `proposal_accepted`; when one is rejected the team is told and prepares others. A proposal someone else moved on the campaign page while the request ran is answered in the state it reached.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.managed_service_proposal_review import ManagedServiceProposalReview
from growwer.models.managed_service_proposal_review_request import ManagedServiceProposalReviewRequest
from growwer.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tool.growwer.com
# See configuration.py for a list of all supported configuration parameters.
configuration = growwer.Configuration(
    host = "https://tool.growwer.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = growwer.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with growwer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = growwer.ManagedServicesApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    managed_service_proposal_review_request = growwer.ManagedServiceProposalReviewRequest() # ManagedServiceProposalReviewRequest | 

    try:
        # Accept or reject proposals
        api_response = api_instance.review_managed_service_proposals(id, idempotency_key, managed_service_proposal_review_request)
        print("The response of ManagedServicesApi->review_managed_service_proposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedServicesApi->review_managed_service_proposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **idempotency_key** | **str**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **managed_service_proposal_review_request** | [**ManagedServiceProposalReviewRequest**](ManagedServiceProposalReviewRequest.md)|  | 

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
**200** | The campaign and the proposals you reviewed, as they now are. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
**404** | The campaign is not yours, or a proposal named is not one of the campaign&#39;s (code &#x60;not_found&#x60;, with &#x60;details.proposalId&#x60;). |  -  |
**409** | No proposal of the campaign awaits your review (code &#x60;no_pending_proposals&#x60;), or a proposal named does not (code &#x60;invalid_state&#x60;, with &#x60;details.proposalIds&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**422** | The body is invalid (code &#x60;validation_failed&#x60;), or it leaves out proposals awaiting your review (code &#x60;review_incomplete&#x60;, with &#x60;details.missingProposalIds&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

