# growwer.AccountApi

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_me**](AccountApi.md#get_me) | **GET** /api/v1/me | Your account
[**get_vocabulary**](AccountApi.md#get_vocabulary) | **GET** /api/v1/vocabulary | Codes and names
[**put_seller_holiday**](AccountApi.md#put_seller_holiday) | **PUT** /api/v1/seller/holiday | Set your holiday


# **get_me**
> GetMe200Response get_me()

Your account

Profile basics, the buyer and seller balances, whether your seller account is restricted, whether the catalogue is open to you, and whether you have a managed service.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.get_me200_response import GetMe200Response
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
    api_instance = growwer.AccountApi(api_client)

    try:
        # Your account
        api_response = api_instance.get_me()
        print("The response of AccountApi->get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMe200Response**](GetMe200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Your account. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vocabulary**
> GetVocabulary200Response get_vocabulary()

Codes and names

The countries, languages, topics, product types, link types and order states that other operations take and return. Names are in English.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.get_vocabulary200_response import GetVocabulary200Response
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
    api_instance = growwer.AccountApi(api_client)

    try:
        # Codes and names
        api_response = api_instance.get_vocabulary()
        print("The response of AccountApi->get_vocabulary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_vocabulary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetVocabulary200Response**](GetVocabulary200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Every code, with its English name where it has one. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_seller_holiday**
> PutSellerHoliday200Response put_seller_holiday(idempotency_key, put_seller_holiday_request)

Set your holiday

Starts, changes or ends your holiday, as the holiday settings of your profile page do. While you are on holiday your medias take no orders. `endDate` is the day your holiday ends, at 00:00 of that day in Growwer's server time, and must be later than now; leave it out, or send null, for a holiday you end yourself. Ending the holiday takes no `endDate`.

A holiday that already is as you ask is answered 200 without a change. A restricted seller account stays on holiday until the restriction is lifted, so any change is refused. Your holiday is also in GET /me.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.put_seller_holiday200_response import PutSellerHoliday200Response
from growwer.models.put_seller_holiday_request import PutSellerHolidayRequest
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
    api_instance = growwer.AccountApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    put_seller_holiday_request = growwer.PutSellerHolidayRequest() # PutSellerHolidayRequest | 

    try:
        # Set your holiday
        api_response = api_instance.put_seller_holiday(idempotency_key, put_seller_holiday_request)
        print("The response of AccountApi->put_seller_holiday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->put_seller_holiday: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | 
 **put_seller_holiday_request** | [**PutSellerHolidayRequest**](PutSellerHolidayRequest.md)|  | 

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
**200** | Your holiday, as it now is. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
**409** | Your seller account is restricted, so its holiday cannot change (code &#x60;seller_restricted&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**422** | The body is not valid (code &#x60;validation_failed&#x60;): an &#x60;endDate&#x60; that is not a later day, or one sent with &#x60;onHoliday&#x60; false. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

