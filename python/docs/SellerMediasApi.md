# growwer.SellerMediasApi

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_seller_media_competitive_fees**](SellerMediasApi.md#apply_seller_media_competitive_fees) | **POST** /api/v1/seller/medias/{id}/apply-competitive-fees | Set the competitive fees Growwer suggests
[**create_seller_media**](SellerMediasApi.md#create_seller_media) | **POST** /api/v1/seller/medias | Register a media you sell on
[**delete_seller_media**](SellerMediasApi.md#delete_seller_media) | **DELETE** /api/v1/seller/medias/{id} | Delete a media you sell on
[**get_seller_media**](SellerMediasApi.md#get_seller_media) | **GET** /api/v1/seller/medias/{id} | Get a media you sell on
[**list_seller_medias**](SellerMediasApi.md#list_seller_medias) | **GET** /api/v1/seller/medias | List the medias you sell on
[**update_seller_media**](SellerMediasApi.md#update_seller_media) | **PATCH** /api/v1/seller/medias/{id} | Edit the offer of a media you sell on


# **apply_seller_media_competitive_fees**
> SellerMedia apply_seller_media_competitive_fees(id, idempotency_key)

Set the competitive fees Growwer suggests

Sets your post fees for the media to the competitive fees Growwer suggests, the `competitiveFees` of GET /seller/medias/{id}, as the button on the media edit page does. Each link type you offer gets the suggested fee on each side it already has a fee for; no link type gains a side it did not offer.

Two differences from the page: a side Growwer has no suggestion for keeps your fee (the page clears it), and the fixed fee the page falls back to when it cannot find a competitive one is never applied (the page applies it). When neither side has a suggestion, nothing changes and the answer is 409 `no_competitive_fees`. When your fees already are the suggested ones, or the suggestion is only for a side none of your link types offers, nothing changes and the answer is 200.

The fees set are your base fees: a running flash offer keeps discounting them. As with a fee edit, a change of the price may cancel the managed-service proposals accepted for the media whose price it changes. Send no body, or an empty object.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.seller_media import SellerMedia
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
    api_instance = growwer.SellerMediasApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

    try:
        # Set the competitive fees Growwer suggests
        api_response = api_instance.apply_seller_media_competitive_fees(id, idempotency_key)
        print("The response of SellerMediasApi->apply_seller_media_competitive_fees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SellerMediasApi->apply_seller_media_competitive_fees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **idempotency_key** | **str**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The media, with the suggested fees set. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**409** | Growwer has no competitive fees to suggest for the media now (code &#x60;no_competitive_fees&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**422** | The body is not empty, or the fees set break a rule of the media edit page (code &#x60;validation_failed&#x60;). Nothing changed. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_seller_media**
> SellerMedia create_seller_media(idempotency_key, create_seller_media_request)

Register a media you sell on

Registers one of your medias, as the media create page does. The media is created with `state: pending_review` and Growwer reviews it in the background, as for a media registered on the web; GET /seller/medias/{id} shows its state.

- `rootUrl` is the media's root URL; `typology` is `blog` or `press`.
- `country` and `language` take the codes GET /vocabulary publishes; `topics` and `bannedTopics` take its topic ids, at most 100 each, and no topic may be both; `bannedTopics` left out bans none.
- `postOffer.pricingOptions` lists every link type you offer for sponsored posts, at least one. Each option needs at least one fee, and every option must offer the same sides (written by you, written by the buyer or Growwer), as the page requires. Each fee is at least 1 EUR, sent in cents.
- `postOffer.maximumLinks` is how many links a sponsored post may hold, 1 to 4; `postOffer.advertisingLabellingPolicy` whether posts are labelled as advertising, `never` when left out; `postOffer.promotedSocialNetworks` the social networks posts are promoted on, none when left out.
- `linkAdditionOffer.pricingOptions` lists the link types you offer for adding a link to an existing article; left out, `null` or an empty list offers none.
- `extraServices` lists the extra services you offer, none when left out. It is sent at the top level, although GET /seller/medias/{id} reads it inside `postOffer`.
- `acceptMediaPublishingTerms` and `declareMediaOwnership` must be `true`: they accept the media publishing terms and declare that you own or manage the media, as the page's checkboxes do, and are recorded as your consents for the media.

A media registered already, by you or by anyone else, is refused with 409 `media_already_registered`, and each such refusal counts toward a daily limit of refusals (429 `media_duplicate_limit_reached` once reached); medias not registered yet are never limited by it.

To register many medias, call this operation once per media, each call with its own `Idempotency-Key` and its own answer (201, 409, 422 or 429); there is no batch operation. The request limits apply to the loop as to any calls (600 requests per minute per user and 300 per key), and each 409 `media_already_registered` counts toward the daily limit of refusals as it does for a single call. Retry a call that got no answer with its same `Idempotency-Key`, as for any write.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.create_seller_media_request import CreateSellerMediaRequest
from growwer.models.seller_media import SellerMedia
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
    api_instance = growwer.SellerMediasApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    create_seller_media_request = {"rootUrl":"https://www.example.com","typology":"blog","country":"ES","language":"es","topics":[3,7],"bannedTopics":[12],"postOffer":{"pricingOptions":[{"linkType":"dofollow","feeWhenSellerWritesPost":{"amount":12000,"currency":"EUR"},"feeWhenSellerDoesNotWritePost":{"amount":10000,"currency":"EUR"}}],"maximumLinks":2,"advertisingLabellingPolicy":"always","promotedSocialNetworks":["twitter"]},"linkAdditionOffer":{"pricingOptions":[{"linkType":"dofollow","fee":{"amount":6000,"currency":"EUR"}}]},"extraServices":[{"name":"list_on_homepage","cost":{"amount":5000,"currency":"EUR"}}],"acceptMediaPublishingTerms":true,"declareMediaOwnership":true} # CreateSellerMediaRequest | 

    try:
        # Register a media you sell on
        api_response = api_instance.create_seller_media(idempotency_key, create_seller_media_request)
        print("The response of SellerMediasApi->create_seller_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SellerMediasApi->create_seller_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **create_seller_media_request** | [**CreateSellerMediaRequest**](CreateSellerMediaRequest.md)|  | 

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The media, registered with &#x60;state: pending_review&#x60;. &#x60;Location&#x60; is its URL. |  * Location - The URL of the new media. <br>  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
**409** | Nothing was registered: your seller account is restricted (code &#x60;seller_restricted&#x60;); or the media is registered already (code &#x60;media_already_registered&#x60;), with &#x60;details.mediaId&#x60; naming it only when it is yours, and the refusal counts toward the daily limit of such refusals; or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**422** | The body is not valid (code &#x60;validation_failed&#x60;): &#x60;details.fields&#x60; names each field by its path in the body, such as &#x60;postOffer.pricingOptions.0.feeWhenSellerWritesPost&#x60; or &#x60;topics.1&#x60;, with the rule the media create page applies. Nothing was registered, and the refusal does not count toward the daily limit of &#x60;media_already_registered&#x60; refusals. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_seller_media**
> delete_seller_media(id, idempotency_key)

Delete a media you sell on

Deletes one of your medias, in any state, as the media delete button does. The media must have no order in progress: close or reject its orders first. The API never cancels an order for you, and an order placed while the delete runs is refused, never cancelled.

What goes with the media, as on the web:

- A running flash offer ends with it, and its managed-service proposals are deleted.
- Its finished orders stay, with the media's URL; they read `media.id` null.
- Buyers' favourites and discards of the domain stay, as they are kept by domain.
- The catalogue search drops the media shortly after the 204, as the search index updates asynchronously.

Repeating the call with the same `Idempotency-Key` answers the same 204 with `Idempotent-Replayed: true`; a new key after the delete answers 404.

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
    api_instance = growwer.SellerMediasApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

    try:
        # Delete a media you sell on
        api_instance.delete_seller_media(id, idempotency_key)
    except Exception as e:
        print("Exception when calling SellerMediasApi->delete_seller_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **idempotency_key** | **str**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 

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
**204** | The media was deleted. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**409** | Nothing was deleted. Your seller account is restricted (code &#x60;seller_restricted&#x60;); the media has orders that are not finished (code &#x60;media_has_active_orders&#x60;, &#x60;details.orderIds&#x60; lists them: close or reject them first); or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_media**
> SellerMedia get_seller_media(id)

Get a media you sell on

One of your medias, with your fees, its extras, the competitive fees Growwer suggests and how it performs. Another seller's media is not found.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.seller_media import SellerMedia
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
    api_instance = growwer.SellerMediasApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a media you sell on
        api_response = api_instance.get_seller_media(id)
        print("The response of SellerMediasApi->get_seller_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SellerMediasApi->get_seller_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The media. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_seller_medias**
> ListSellerMedias200Response list_seller_medias(state=state, sort=sort, limit=limit, offset=offset)

List the medias you sell on

Your medias in every state, with your fees and how they perform, newest first by default.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.list_seller_medias200_response import ListSellerMedias200Response
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
    api_instance = growwer.SellerMediasApi(api_client)
    state = 'active,deactivated' # str | Only the medias in one of these states, comma-separated: `analyzing`, `pending_review`, `active`, `deactivated`. An unknown state is refused with 422. (optional)
    sort = '-createdAt' # str | By creation date, number of published orders or publication rate; a leading `-` sorts descending. Medias with no publication rate come first ascending, last descending. Ties come in id order. (optional) (default to '-createdAt')
    limit = 20 # int | Medias per page, 1 to 100. (optional) (default to 20)
    offset = 0 # int | Medias to skip. (optional) (default to 0)

    try:
        # List the medias you sell on
        api_response = api_instance.list_seller_medias(state=state, sort=sort, limit=limit, offset=offset)
        print("The response of SellerMediasApi->list_seller_medias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SellerMediasApi->list_seller_medias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Only the medias in one of these states, comma-separated: &#x60;analyzing&#x60;, &#x60;pending_review&#x60;, &#x60;active&#x60;, &#x60;deactivated&#x60;. An unknown state is refused with 422. | [optional] 
 **sort** | **str**| By creation date, number of published orders or publication rate; a leading &#x60;-&#x60; sorts descending. Medias with no publication rate come first ascending, last descending. Ties come in id order. | [optional] [default to &#39;-createdAt&#39;]
 **limit** | **int**| Medias per page, 1 to 100. | [optional] [default to 20]
 **offset** | **int**| Medias to skip. | [optional] [default to 0]

### Return type

[**ListSellerMedias200Response**](ListSellerMedias200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of your medias and how many match in all. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_seller_media**
> SellerMedia update_seller_media(id, idempotency_key, update_seller_media_request)

Edit the offer of a media you sell on

Sets the fees, extra services, typology and post offer characteristics of one of your medias, as the media edit page saves them. Send only the fields you change: a field you send replaces that field wholly, a field you leave out stays as it is, inside `postOffer` too (sending only `postOffer.maximumLinks` keeps your fees).

- `typology` is `blog` or `press`.
- `postOffer.pricingOptions` lists every link type you offer for sponsored posts, at least one. A link type you leave out is no longer offered. Each option needs at least one fee, and every option must offer the same sides (written by you, written by the buyer or Growwer), as the page requires. Each fee is at least 1 EUR.
- `postOffer.maximumLinks` is how many links a sponsored post may hold, 1 to 4; `postOffer.advertisingLabellingPolicy` whether posts are labelled as advertising (`always` or `never`); `postOffer.promotedSocialNetworks` the full list of social networks posts are promoted on, each once (an empty list for none).
- `linkAdditionOffer.pricingOptions` lists the link types you offer for adding a link to an existing article; `null` or an empty list stops offering link additions.
- `extraServices` is the full list of extra services you offer; an empty list removes them all. It is sent at the top level, although GET /seller/medias/{id} reads it inside `postOffer`.

The fees are your base fees, the ones GET /seller/medias/{id} returns: while a flash offer runs, its discount keeps applying on top of them, and `currentCost` shows the result. `currentCost` may be sent back as read and is ignored. Country, language, topics and comments are not edited here.

As on the page, a change of the post offer's price may cancel the managed-service proposals accepted for the media whose price it changes, and raising the price above the best competitor's tells Growwer's support team. A restricted seller account may edit its offer.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.seller_media import SellerMedia
from growwer.models.update_seller_media_request import UpdateSellerMediaRequest
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
    api_instance = growwer.SellerMediasApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    update_seller_media_request = {"typology":"blog","postOffer":{"maximumLinks":2,"advertisingLabellingPolicy":"always","promotedSocialNetworks":["twitter","newsletter"],"pricingOptions":[{"linkType":"dofollow","feeWhenSellerWritesPost":{"amount":12000,"currency":"EUR"},"feeWhenSellerDoesNotWritePost":{"amount":10000,"currency":"EUR"}},{"linkType":"nofollow","feeWhenSellerWritesPost":{"amount":9000,"currency":"EUR"},"feeWhenSellerDoesNotWritePost":{"amount":7000,"currency":"EUR"}}]},"linkAdditionOffer":null,"extraServices":[{"name":"list_on_homepage","cost":{"amount":5000,"currency":"EUR"}}]} # UpdateSellerMediaRequest | 

    try:
        # Edit the offer of a media you sell on
        api_response = api_instance.update_seller_media(id, idempotency_key, update_seller_media_request)
        print("The response of SellerMediasApi->update_seller_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SellerMediasApi->update_seller_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **idempotency_key** | **str**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **update_seller_media_request** | [**UpdateSellerMediaRequest**](UpdateSellerMediaRequest.md)|  | 

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The media, with the changes saved. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**409** | The &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**422** | The body is not valid (code &#x60;validation_failed&#x60;): &#x60;details.fields&#x60; names each field by its path in the body, such as &#x60;postOffer.pricingOptions.0.feeWhenSellerWritesPost&#x60;, with the rule the media edit page applies. Nothing changed. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the units of the catalogue it may spend per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): each new media costs one unit and a response that holds no new media, an empty one or a count included, costs one unless the same request was answered today while the media lists, topics and language of its project stayed as they were, which is free; &#x60;details.remaining&#x60; says how many units still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and a request already answered today stays readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. On POST /seller/medias, also when you sent as many medias that are already registered as you may per UTC day (code &#x60;media_duplicate_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias not registered yet are still accepted. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

