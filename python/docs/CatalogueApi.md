# growwer.CatalogueApi

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discard_media**](CatalogueApi.md#discard_media) | **PUT** /api/v1/projects/{id}/discards/{mediaId} | Discard a media for a project
[**favourite_media**](CatalogueApi.md#favourite_media) | **PUT** /api/v1/projects/{id}/favourites/{mediaId} | Add a media to the favourites of a project
[**get_catalogue_media**](CatalogueApi.md#get_catalogue_media) | **GET** /api/v1/medias/{id} | Get a media
[**list_flash_offers**](CatalogueApi.md#list_flash_offers) | **GET** /api/v1/flash-offers | List flash offers
[**request_medias**](CatalogueApi.md#request_medias) | **POST** /api/v1/projects/{id}/media-requests | Request specific medias for a project
[**search_project_medias**](CatalogueApi.md#search_project_medias) | **GET** /api/v1/projects/{id}/medias | Search the catalogue for a project
[**undiscard_media**](CatalogueApi.md#undiscard_media) | **DELETE** /api/v1/projects/{id}/discards/{mediaId} | Restore a discarded media for a project
[**unfavourite_media**](CatalogueApi.md#unfavourite_media) | **DELETE** /api/v1/projects/{id}/favourites/{mediaId} | Remove a media from the favourites of a project


# **discard_media**
> discard_media(id, media_id, idempotency_key)

Discard a media for a project

Discards a media for one of your projects, as the web does. Discarding it again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

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
    api_instance = growwer.CatalogueApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The project.
    media_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The media.
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

    try:
        # Discard a media for a project
        api_instance.discard_media(id, media_id, idempotency_key)
    except Exception as e:
        print("Exception when calling CatalogueApi->discard_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The project. | 
 **media_id** | **UUID**| The media. | 
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
**204** | The media is discarded for the project. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favourite_media**
> favourite_media(id, media_id, idempotency_key)

Add a media to the favourites of a project

Marks a media as a favourite of one of your projects, as the heart on the web does. Adding a favourite again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

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
    api_instance = growwer.CatalogueApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The project.
    media_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The media.
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

    try:
        # Add a media to the favourites of a project
        api_instance.favourite_media(id, media_id, idempotency_key)
    except Exception as e:
        print("Exception when calling CatalogueApi->favourite_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The project. | 
 **media_id** | **UUID**| The media. | 
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
**204** | The media is a favourite of the project. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalogue_media**
> CatalogueMedia get_catalogue_media(id)

Get a media

One media of the catalogue: an active, public media. A media you have ordered is always readable, even if it has since left the catalogue, and is open to every account. Otherwise the media counts towards the distinct medias the account may see per day (UTC): the full daily cap for accounts with recent completed orders, a smaller trial quota for other accounts (see `catalogue.eligible`, `catalogue.dailyCap` and `catalogue.remainingToday` on GET /me). For the media's state in one of your projects, search the project with GET /projects/{id}/medias.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.catalogue_media import CatalogueMedia
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
    api_instance = growwer.CatalogueApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The media.

    try:
        # Get a media
        api_response = api_instance.get_catalogue_media(id)
        print("The response of CatalogueApi->get_catalogue_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogueApi->get_catalogue_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The media. | 

### Return type

[**CatalogueMedia**](CatalogueMedia.md)

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
**403** | The catalogue is open to accounts with recent completed orders, as buyer or as seller, and to other accounts within a daily trial quota; this account has no such order and the trial quota is off (code &#x60;catalogue_requires_recent_order&#x60;). GET /me reports &#x60;catalogue.eligible&#x60; and &#x60;catalogue.dailyCap&#x60;. |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_flash_offers**
> ListFlashOffers200Response list_flash_offers(project_id, source=source, sort=sort, domain=domain, website_type=website_type, language=language, country=country, topics=topics, not_banned_topics=not_banned_topics, min_traffic=min_traffic, max_traffic=max_traffic, traffic_trend_upward=traffic_trend_upward, min_domain_rating=min_domain_rating, max_domain_rating=max_domain_rating, min_linked_to_referring_ratio=min_linked_to_referring_ratio, max_linked_to_referring_ratio=max_linked_to_referring_ratio, min_post_price=min_post_price, max_post_price=max_post_price, post_link_type=post_link_type, promoted_social_network=promoted_social_network, without_advertising_label=without_advertising_label, homepage_listing=homepage_listing, has_link_addition=has_link_addition, min_link_addition_price=min_link_addition_price, max_link_addition_price=max_link_addition_price, link_addition_link_type=link_addition_link_type, recommended=recommended, favourite=favourite, requested=requested, bought=bought, discarded=discarded, new=new, ranks_goal_keyword=ranks_goal_keyword, ranks_ai_keyword=ranks_ai_keyword, limit=limit, offset=offset)

List flash offers

The medias on a flash offer, a time-limited discount, in the catalogue of one of your projects. It is GET /projects/{id}/medias with `flashOffer=true`, and takes the same parameters except `flashOffer` and `savedFilterId`. The catalogue access and the daily distinct-media limit of that operation apply.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.list_flash_offers200_response import ListFlashOffers200Response
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
    api_instance = growwer.CatalogueApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The project to search flash offers for.
    source = 'source_example' # str | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state. (optional)
    sort = 'sort_example' # str | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first. (optional)
    domain = 'domain_example' # str | Medias whose domain contains this text, 1 to 255 characters. (optional)
    website_type = 'website_type_example' # str | A comma-separated list of website types: `blog`, `press`. (optional)
    language = 'language_example' # str | A comma-separated list of language codes, as in GET /vocabulary. (optional)
    country = 'country_example' # str | A comma-separated list of country codes, as in GET /vocabulary. (optional)
    topics = 'topics_example' # str | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. (optional)
    not_banned_topics = True # bool | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise. (optional)
    min_traffic = 56 # int | Minimum monthly organic traffic. (optional)
    max_traffic = 56 # int | Maximum monthly organic traffic. (optional)
    traffic_trend_upward = True # bool | Medias whose traffic is growing. Only `true` applies it; omit it otherwise. (optional)
    min_domain_rating = 56 # int | Minimum domain rating, 0 to 100. (optional)
    max_domain_rating = 56 # int | Maximum domain rating, 0 to 100. (optional)
    min_linked_to_referring_ratio = 3.4 # float | Minimum ratio of linked domains to referring domains, such as 0.5. (optional)
    max_linked_to_referring_ratio = 3.4 # float | Maximum ratio of linked domains to referring domains, such as 1.5. (optional)
    min_post_price = 56 # int | Minimum post price, in cents. (optional)
    max_post_price = 56 # int | Maximum post price, in cents. (optional)
    post_link_type = 'post_link_type_example' # str | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`. (optional)
    promoted_social_network = 'promoted_social_network_example' # str | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`. (optional)
    without_advertising_label = True # bool | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise. (optional)
    homepage_listing = True # bool | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise. (optional)
    has_link_addition = True # bool | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise. (optional)
    min_link_addition_price = 56 # int | Minimum link addition price, in cents. (optional)
    max_link_addition_price = 56 # int | Maximum link addition price, in cents. (optional)
    link_addition_link_type = 'link_addition_link_type_example' # str | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`. (optional)
    recommended = True # bool | `true`: only the medias Growwer recommends for the project; `false`: only the others. (optional)
    favourite = True # bool | `true`: only your favourites for the project; `false`: leave them out. (optional)
    requested = True # bool | `true`: only the medias you requested for the project; `false`: leave them out. (optional)
    bought = True # bool | `true`: only medias you bought for the project; `false`: leave them out. (optional)
    discarded = True # bool | `true`: only the medias you discarded for the project; `false`: leave them out. (optional)
    new = True # bool | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise. (optional)
    ranks_goal_keyword = 'ranks_goal_keyword_example' # str | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project. (optional)
    ranks_ai_keyword = 'ranks_ai_keyword_example' # str | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`. (optional)
    limit = 20 # int | Medias per page, 1 to 100. (optional) (default to 20)
    offset = 0 # int | Medias to skip, at most 99900. (optional) (default to 0)

    try:
        # List flash offers
        api_response = api_instance.list_flash_offers(project_id, source=source, sort=sort, domain=domain, website_type=website_type, language=language, country=country, topics=topics, not_banned_topics=not_banned_topics, min_traffic=min_traffic, max_traffic=max_traffic, traffic_trend_upward=traffic_trend_upward, min_domain_rating=min_domain_rating, max_domain_rating=max_domain_rating, min_linked_to_referring_ratio=min_linked_to_referring_ratio, max_linked_to_referring_ratio=max_linked_to_referring_ratio, min_post_price=min_post_price, max_post_price=max_post_price, post_link_type=post_link_type, promoted_social_network=promoted_social_network, without_advertising_label=without_advertising_label, homepage_listing=homepage_listing, has_link_addition=has_link_addition, min_link_addition_price=min_link_addition_price, max_link_addition_price=max_link_addition_price, link_addition_link_type=link_addition_link_type, recommended=recommended, favourite=favourite, requested=requested, bought=bought, discarded=discarded, new=new, ranks_goal_keyword=ranks_goal_keyword, ranks_ai_keyword=ranks_ai_keyword, limit=limit, offset=offset)
        print("The response of CatalogueApi->list_flash_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogueApi->list_flash_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| The project to search flash offers for. | 
 **source** | **str**| Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [optional] 
 **sort** | **str**| The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [optional] 
 **domain** | **str**| Medias whose domain contains this text, 1 to 255 characters. | [optional] 
 **website_type** | **str**| A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [optional] 
 **language** | **str**| A comma-separated list of language codes, as in GET /vocabulary. | [optional] 
 **country** | **str**| A comma-separated list of country codes, as in GET /vocabulary. | [optional] 
 **topics** | **str**| A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [optional] 
 **not_banned_topics** | **bool**| Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **min_traffic** | **int**| Minimum monthly organic traffic. | [optional] 
 **max_traffic** | **int**| Maximum monthly organic traffic. | [optional] 
 **traffic_trend_upward** | **bool**| Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **min_domain_rating** | **int**| Minimum domain rating, 0 to 100. | [optional] 
 **max_domain_rating** | **int**| Maximum domain rating, 0 to 100. | [optional] 
 **min_linked_to_referring_ratio** | **float**| Minimum ratio of linked domains to referring domains, such as 0.5. | [optional] 
 **max_linked_to_referring_ratio** | **float**| Maximum ratio of linked domains to referring domains, such as 1.5. | [optional] 
 **min_post_price** | **int**| Minimum post price, in cents. | [optional] 
 **max_post_price** | **int**| Maximum post price, in cents. | [optional] 
 **post_link_type** | **str**| A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] 
 **promoted_social_network** | **str**| A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [optional] 
 **without_advertising_label** | **bool**| Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **homepage_listing** | **bool**| Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **has_link_addition** | **bool**| Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **min_link_addition_price** | **int**| Minimum link addition price, in cents. | [optional] 
 **max_link_addition_price** | **int**| Maximum link addition price, in cents. | [optional] 
 **link_addition_link_type** | **str**| A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] 
 **recommended** | **bool**| &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [optional] 
 **favourite** | **bool**| &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [optional] 
 **requested** | **bool**| &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [optional] 
 **bought** | **bool**| &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [optional] 
 **discarded** | **bool**| &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [optional] 
 **new** | **bool**| Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **ranks_goal_keyword** | **str**| A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [optional] 
 **ranks_ai_keyword** | **str**| A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [optional] 
 **limit** | **int**| Medias per page, 1 to 100. | [optional] [default to 20]
 **offset** | **int**| Medias to skip, at most 99900. | [optional] [default to 0]

### Return type

[**ListFlashOffers200Response**](ListFlashOffers200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of flash offers and how many there are in all. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The catalogue is open to accounts with recent completed orders, as buyer or as seller, and to other accounts within a daily trial quota; this account has no such order and the trial quota is off (code &#x60;catalogue_requires_recent_order&#x60;). GET /me reports &#x60;catalogue.eligible&#x60; and &#x60;catalogue.dailyCap&#x60;. |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_medias**
> RequestMedias201Response request_medias(id, idempotency_key, request_medias_request)

Request specific medias for a project

Asks Growwer to find the medias of these domains for one of your projects, as the "request specific domains" form on the web does. Each entry may be a domain or a URL; it is read as its full domain, lowercased. Repeated domains are requested once, and a domain already requested changes nothing. Up to 200 distinct domains per call. They then appear in the project's catalogue with `project.requested` true (`requested=true` on GET /projects/{id}/medias) once Growwer lists them.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.request_medias201_response import RequestMedias201Response
from growwer.models.request_medias_request import RequestMediasRequest
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
    api_instance = growwer.CatalogueApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The project.
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    request_medias_request = growwer.RequestMediasRequest() # RequestMediasRequest | 

    try:
        # Request specific medias for a project
        api_response = api_instance.request_medias(id, idempotency_key, request_medias_request)
        print("The response of CatalogueApi->request_medias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogueApi->request_medias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The project. | 
 **idempotency_key** | **str**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **request_medias_request** | [**RequestMediasRequest**](RequestMediasRequest.md)|  | 

### Return type

[**RequestMedias201Response**](RequestMedias201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The domains were requested: each distinct domain, as Growwer read it. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_project_medias**
> ListFlashOffers200Response search_project_medias(id, source=source, sort=sort, saved_filter_id=saved_filter_id, domain=domain, website_type=website_type, language=language, country=country, topics=topics, not_banned_topics=not_banned_topics, min_traffic=min_traffic, max_traffic=max_traffic, traffic_trend_upward=traffic_trend_upward, min_domain_rating=min_domain_rating, max_domain_rating=max_domain_rating, min_linked_to_referring_ratio=min_linked_to_referring_ratio, max_linked_to_referring_ratio=max_linked_to_referring_ratio, min_post_price=min_post_price, max_post_price=max_post_price, post_link_type=post_link_type, promoted_social_network=promoted_social_network, without_advertising_label=without_advertising_label, homepage_listing=homepage_listing, has_link_addition=has_link_addition, min_link_addition_price=min_link_addition_price, max_link_addition_price=max_link_addition_price, link_addition_link_type=link_addition_link_type, recommended=recommended, favourite=favourite, requested=requested, flash_offer=flash_offer, bought=bought, discarded=discarded, new=new, ranks_goal_keyword=ranks_goal_keyword, ranks_ai_keyword=ranks_ai_keyword, limit=limit, offset=offset)

Search the catalogue for a project

The medias the catalogue offers for one of your projects, as the web lists them, with each media's state in the project. Filter with the parameters below, which all combine, or apply one of your saved filters with `savedFilterId` alone. Each account can see a limited number of distinct medias per day (UTC) across the catalogue operations: the full daily cap for accounts with recent completed orders, as buyer or as seller, and a smaller trial quota for other accounts, which rises to the full cap after a completed order (see `catalogue.eligible`, `catalogue.dailyCap` and `catalogue.remainingToday` on GET /me). Medias seen again the same day are free.

### Example

* Bearer Authentication (apiKey):

```python
import growwer
from growwer.models.list_flash_offers200_response import ListFlashOffers200Response
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
    api_instance = growwer.CatalogueApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The project.
    source = 'source_example' # str | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state. (optional)
    sort = 'sort_example' # str | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first. (optional)
    saved_filter_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, `source` or `sort`. A filter saved on the web that uses a filter the API does not support is refused with 422 `saved_filter_unsupported`. (optional)
    domain = 'domain_example' # str | Medias whose domain contains this text, 1 to 255 characters. (optional)
    website_type = 'website_type_example' # str | A comma-separated list of website types: `blog`, `press`. (optional)
    language = 'language_example' # str | A comma-separated list of language codes, as in GET /vocabulary. (optional)
    country = 'country_example' # str | A comma-separated list of country codes, as in GET /vocabulary. (optional)
    topics = 'topics_example' # str | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. (optional)
    not_banned_topics = True # bool | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise. (optional)
    min_traffic = 56 # int | Minimum monthly organic traffic. (optional)
    max_traffic = 56 # int | Maximum monthly organic traffic. (optional)
    traffic_trend_upward = True # bool | Medias whose traffic is growing. Only `true` applies it; omit it otherwise. (optional)
    min_domain_rating = 56 # int | Minimum domain rating, 0 to 100. (optional)
    max_domain_rating = 56 # int | Maximum domain rating, 0 to 100. (optional)
    min_linked_to_referring_ratio = 3.4 # float | Minimum ratio of linked domains to referring domains, such as 0.5. (optional)
    max_linked_to_referring_ratio = 3.4 # float | Maximum ratio of linked domains to referring domains, such as 1.5. (optional)
    min_post_price = 56 # int | Minimum post price, in cents. (optional)
    max_post_price = 56 # int | Maximum post price, in cents. (optional)
    post_link_type = 'post_link_type_example' # str | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`. (optional)
    promoted_social_network = 'promoted_social_network_example' # str | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`. (optional)
    without_advertising_label = True # bool | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise. (optional)
    homepage_listing = True # bool | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise. (optional)
    has_link_addition = True # bool | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise. (optional)
    min_link_addition_price = 56 # int | Minimum link addition price, in cents. (optional)
    max_link_addition_price = 56 # int | Maximum link addition price, in cents. (optional)
    link_addition_link_type = 'link_addition_link_type_example' # str | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`. (optional)
    recommended = True # bool | `true`: only the medias Growwer recommends for the project; `false`: only the others. (optional)
    favourite = True # bool | `true`: only your favourites for the project; `false`: leave them out. (optional)
    requested = True # bool | `true`: only the medias you requested for the project; `false`: leave them out. (optional)
    flash_offer = True # bool | `true`: only medias with a flash offer running; `false`: leave them out. (optional)
    bought = True # bool | `true`: only medias you bought for the project; `false`: leave them out. (optional)
    discarded = True # bool | `true`: only the medias you discarded for the project; `false`: leave them out. (optional)
    new = True # bool | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise. (optional)
    ranks_goal_keyword = 'ranks_goal_keyword_example' # str | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project. (optional)
    ranks_ai_keyword = 'ranks_ai_keyword_example' # str | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`. (optional)
    limit = 20 # int | Medias per page, 1 to 100. (optional) (default to 20)
    offset = 0 # int | Medias to skip, at most 99900. (optional) (default to 0)

    try:
        # Search the catalogue for a project
        api_response = api_instance.search_project_medias(id, source=source, sort=sort, saved_filter_id=saved_filter_id, domain=domain, website_type=website_type, language=language, country=country, topics=topics, not_banned_topics=not_banned_topics, min_traffic=min_traffic, max_traffic=max_traffic, traffic_trend_upward=traffic_trend_upward, min_domain_rating=min_domain_rating, max_domain_rating=max_domain_rating, min_linked_to_referring_ratio=min_linked_to_referring_ratio, max_linked_to_referring_ratio=max_linked_to_referring_ratio, min_post_price=min_post_price, max_post_price=max_post_price, post_link_type=post_link_type, promoted_social_network=promoted_social_network, without_advertising_label=without_advertising_label, homepage_listing=homepage_listing, has_link_addition=has_link_addition, min_link_addition_price=min_link_addition_price, max_link_addition_price=max_link_addition_price, link_addition_link_type=link_addition_link_type, recommended=recommended, favourite=favourite, requested=requested, flash_offer=flash_offer, bought=bought, discarded=discarded, new=new, ranks_goal_keyword=ranks_goal_keyword, ranks_ai_keyword=ranks_ai_keyword, limit=limit, offset=offset)
        print("The response of CatalogueApi->search_project_medias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogueApi->search_project_medias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The project. | 
 **source** | **str**| Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [optional] 
 **sort** | **str**| The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [optional] 
 **saved_filter_id** | **UUID**| Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, &#x60;source&#x60; or &#x60;sort&#x60;. A filter saved on the web that uses a filter the API does not support is refused with 422 &#x60;saved_filter_unsupported&#x60;. | [optional] 
 **domain** | **str**| Medias whose domain contains this text, 1 to 255 characters. | [optional] 
 **website_type** | **str**| A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [optional] 
 **language** | **str**| A comma-separated list of language codes, as in GET /vocabulary. | [optional] 
 **country** | **str**| A comma-separated list of country codes, as in GET /vocabulary. | [optional] 
 **topics** | **str**| A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [optional] 
 **not_banned_topics** | **bool**| Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **min_traffic** | **int**| Minimum monthly organic traffic. | [optional] 
 **max_traffic** | **int**| Maximum monthly organic traffic. | [optional] 
 **traffic_trend_upward** | **bool**| Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **min_domain_rating** | **int**| Minimum domain rating, 0 to 100. | [optional] 
 **max_domain_rating** | **int**| Maximum domain rating, 0 to 100. | [optional] 
 **min_linked_to_referring_ratio** | **float**| Minimum ratio of linked domains to referring domains, such as 0.5. | [optional] 
 **max_linked_to_referring_ratio** | **float**| Maximum ratio of linked domains to referring domains, such as 1.5. | [optional] 
 **min_post_price** | **int**| Minimum post price, in cents. | [optional] 
 **max_post_price** | **int**| Maximum post price, in cents. | [optional] 
 **post_link_type** | **str**| A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] 
 **promoted_social_network** | **str**| A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [optional] 
 **without_advertising_label** | **bool**| Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **homepage_listing** | **bool**| Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **has_link_addition** | **bool**| Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **min_link_addition_price** | **int**| Minimum link addition price, in cents. | [optional] 
 **max_link_addition_price** | **int**| Maximum link addition price, in cents. | [optional] 
 **link_addition_link_type** | **str**| A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] 
 **recommended** | **bool**| &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [optional] 
 **favourite** | **bool**| &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [optional] 
 **requested** | **bool**| &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [optional] 
 **flash_offer** | **bool**| &#x60;true&#x60;: only medias with a flash offer running; &#x60;false&#x60;: leave them out. | [optional] 
 **bought** | **bool**| &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [optional] 
 **discarded** | **bool**| &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [optional] 
 **new** | **bool**| Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] 
 **ranks_goal_keyword** | **str**| A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [optional] 
 **ranks_ai_keyword** | **str**| A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [optional] 
 **limit** | **int**| Medias per page, 1 to 100. | [optional] [default to 20]
 **offset** | **int**| Medias to skip, at most 99900. | [optional] [default to 0]

### Return type

[**ListFlashOffers200Response**](ListFlashOffers200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of matching medias and how many match in all. |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The catalogue is open to accounts with recent completed orders, as buyer or as seller, and to other accounts within a daily trial quota; this account has no such order and the trial quota is off (code &#x60;catalogue_requires_recent_order&#x60;). GET /me reports &#x60;catalogue.eligible&#x60; and &#x60;catalogue.dailyCap&#x60;. |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**422** | A parameter is not valid (code &#x60;validation_failed&#x60;; &#x60;details.fields&#x60; names it), or the saved filter uses a web filter the API does not support (code &#x60;saved_filter_unsupported&#x60;; &#x60;details.field&#x60; names it). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undiscard_media**
> undiscard_media(id, media_id, idempotency_key)

Restore a discarded media for a project

Restores a media you discarded for one of your projects. Restoring one that is not discarded changes nothing. It works for any media, even one the catalogue no longer shows.

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
    api_instance = growwer.CatalogueApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The project.
    media_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The media.
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

    try:
        # Restore a discarded media for a project
        api_instance.undiscard_media(id, media_id, idempotency_key)
    except Exception as e:
        print("Exception when calling CatalogueApi->undiscard_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The project. | 
 **media_id** | **UUID**| The media. | 
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
**204** | The media is not discarded for the project. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfavourite_media**
> unfavourite_media(id, media_id, idempotency_key)

Remove a media from the favourites of a project

Removes a media from the favourites of one of your projects. Removing one that is not a favourite changes nothing. It works for any media, even one the catalogue no longer shows.

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
    api_instance = growwer.CatalogueApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The project.
    media_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The media.
    idempotency_key = 'idempotency_key_example' # str | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

    try:
        # Remove a media from the favourites of a project
        api_instance.unfavourite_media(id, media_id, idempotency_key)
    except Exception as e:
        print("Exception when calling CatalogueApi->unfavourite_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The project. | 
 **media_id** | **UUID**| The media. | 
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
**204** | The media is not a favourite of the project. |  -  |
**400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
**401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
**403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
**404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
**409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
**429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
**500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
**503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

