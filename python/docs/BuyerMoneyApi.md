# growwer.BuyerMoneyApi

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_buyer_transaction_document**](BuyerMoneyApi.md#download_buyer_transaction_document) | **GET** /api/v1/wallets/buyer/transactions/{id}/document | Download the document of a wallet movement
[**get_buyer_wallet**](BuyerMoneyApi.md#get_buyer_wallet) | **GET** /api/v1/wallets/buyer | Get your buyer wallet
[**get_invoice_pdf**](BuyerMoneyApi.md#get_invoice_pdf) | **GET** /api/v1/invoices/{id}/pdf | Download an invoice
[**list_buyer_transactions**](BuyerMoneyApi.md#list_buyer_transactions) | **GET** /api/v1/wallets/buyer/transactions | List your buyer wallet movements
[**list_invoices**](BuyerMoneyApi.md#list_invoices) | **GET** /api/v1/invoices | List your invoices


# **download_buyer_transaction_document**
> bytes download_buyer_transaction_document(id)

Download the document of a wallet movement

The document Growwer attached to a movement of your buyer wallet. 404 when the movement has none (`hasDocument` is false) or the file cannot be read.

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
    api_instance = growwer.BuyerMoneyApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Download the document of a wallet movement
        api_response = api_instance.download_buyer_transaction_document(id)
        print("The response of BuyerMoneyApi->download_buyer_transaction_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerMoneyApi->download_buyer_transaction_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

**bytes**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The document, with its own content type and name. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buyer_wallet**
> GetBuyerWallet200Response get_buyer_wallet()

Get your buyer wallet

The balance you buy with, and the page where you top it up.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.get_buyer_wallet200_response import GetBuyerWallet200Response
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
    api_instance = growwer.BuyerMoneyApi(api_client)

    try:
        # Get your buyer wallet
        api_response = api_instance.get_buyer_wallet()
        print("The response of BuyerMoneyApi->get_buyer_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerMoneyApi->get_buyer_wallet: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetBuyerWallet200Response**](GetBuyerWallet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Your buyer wallet. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_pdf**
> bytes get_invoice_pdf(id)

Download an invoice

The PDF of one of your invoices.

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
    api_instance = growwer.BuyerMoneyApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Download an invoice
        api_response = api_instance.get_invoice_pdf(id)
        print("The response of BuyerMoneyApi->get_invoice_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerMoneyApi->get_invoice_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

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
**200** | The invoice. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_transactions**
> ListBuyerTransactions200Response list_buyer_transactions(limit=limit, offset=offset)

List your buyer wallet movements

Every movement of your buyer wallet, newest first: top-ups, order debits and their refunds, gifts and manual corrections.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.list_buyer_transactions200_response import ListBuyerTransactions200Response
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
    api_instance = growwer.BuyerMoneyApi(api_client)
    limit = 20 # int | Movements per page, 1 to 100. (optional) (default to 20)
    offset = 0 # int | Movements to skip. (optional) (default to 0)

    try:
        # List your buyer wallet movements
        api_response = api_instance.list_buyer_transactions(limit=limit, offset=offset)
        print("The response of BuyerMoneyApi->list_buyer_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerMoneyApi->list_buyer_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Movements per page, 1 to 100. | [optional] [default to 20]
 **offset** | **int**| Movements to skip. | [optional] [default to 0]

### Return type

[**ListBuyerTransactions200Response**](ListBuyerTransactions200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of your movements and how many there are in all. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> ListInvoices200Response list_invoices(limit=limit, offset=offset)

List your invoices

The invoices of your top-ups, newest first.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.list_invoices200_response import ListInvoices200Response
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
    api_instance = growwer.BuyerMoneyApi(api_client)
    limit = 20 # int | Invoices per page, 1 to 100. (optional) (default to 20)
    offset = 0 # int | Invoices to skip. (optional) (default to 0)

    try:
        # List your invoices
        api_response = api_instance.list_invoices(limit=limit, offset=offset)
        print("The response of BuyerMoneyApi->list_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerMoneyApi->list_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Invoices per page, 1 to 100. | [optional] [default to 20]
 **offset** | **int**| Invoices to skip. | [optional] [default to 0]

### Return type

[**ListInvoices200Response**](ListInvoices200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of your invoices and how many you have in all. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

