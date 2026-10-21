# Growwer::CatalogueApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**discard_media**](CatalogueApi.md#discard_media) | **PUT** /api/v1/projects/{id}/discards/{mediaId} | Discard a media for a project |
| [**favourite_media**](CatalogueApi.md#favourite_media) | **PUT** /api/v1/projects/{id}/favourites/{mediaId} | Add a media to the favourites of a project |
| [**get_catalogue_media**](CatalogueApi.md#get_catalogue_media) | **GET** /api/v1/medias/{id} | Get a media |
| [**list_flash_offers**](CatalogueApi.md#list_flash_offers) | **GET** /api/v1/flash-offers | List flash offers |
| [**request_medias**](CatalogueApi.md#request_medias) | **POST** /api/v1/projects/{id}/media-requests | Request specific medias for a project |
| [**search_project_medias**](CatalogueApi.md#search_project_medias) | **GET** /api/v1/projects/{id}/medias | Search the catalogue for a project |
| [**undiscard_media**](CatalogueApi.md#undiscard_media) | **DELETE** /api/v1/projects/{id}/discards/{mediaId} | Restore a discarded media for a project |
| [**unfavourite_media**](CatalogueApi.md#unfavourite_media) | **DELETE** /api/v1/projects/{id}/favourites/{mediaId} | Remove a media from the favourites of a project |


## discard_media

> discard_media(id, media_id, idempotency_key)

Discard a media for a project

Discards a media for one of your projects, as the web does. Discarding it again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::CatalogueApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The project.
media_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The media.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

begin
  # Discard a media for a project
  api_instance.discard_media(id, media_id, idempotency_key)
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->discard_media: #{e}"
end
```

#### Using the discard_media_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> discard_media_with_http_info(id, media_id, idempotency_key)

```ruby
begin
  # Discard a media for a project
  data, status_code, headers = api_instance.discard_media_with_http_info(id, media_id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->discard_media_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The project. |  |
| **media_id** | **String** | The media. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |

### Return type

nil (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## favourite_media

> favourite_media(id, media_id, idempotency_key)

Add a media to the favourites of a project

Marks a media as a favourite of one of your projects, as the heart on the web does. Adding a favourite again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::CatalogueApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The project.
media_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The media.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

begin
  # Add a media to the favourites of a project
  api_instance.favourite_media(id, media_id, idempotency_key)
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->favourite_media: #{e}"
end
```

#### Using the favourite_media_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> favourite_media_with_http_info(id, media_id, idempotency_key)

```ruby
begin
  # Add a media to the favourites of a project
  data, status_code, headers = api_instance.favourite_media_with_http_info(id, media_id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->favourite_media_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The project. |  |
| **media_id** | **String** | The media. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |

### Return type

nil (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_catalogue_media

> <CatalogueMedia> get_catalogue_media(id)

Get a media

One media of the catalogue: an active, public media. A media you have ordered is always readable, even if it has since left the catalogue, and is open to every account. Otherwise the catalogue is open to accounts with recent completed orders (see `catalogue.eligible` on GET /me), and the media counts towards the distinct medias the account may see per day (UTC). For the media's state in one of your projects, search the project with GET /projects/{id}/medias.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::CatalogueApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The media.

begin
  # Get a media
  result = api_instance.get_catalogue_media(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->get_catalogue_media: #{e}"
end
```

#### Using the get_catalogue_media_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CatalogueMedia>, Integer, Hash)> get_catalogue_media_with_http_info(id)

```ruby
begin
  # Get a media
  data, status_code, headers = api_instance.get_catalogue_media_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CatalogueMedia>
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->get_catalogue_media_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The media. |  |

### Return type

[**CatalogueMedia**](CatalogueMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_flash_offers

> <ListFlashOffers200Response> list_flash_offers(project_id, opts)

List flash offers

The medias on a flash offer, a time-limited discount, in the catalogue of one of your projects. It is GET /projects/{id}/medias with `flashOffer=true`, and takes the same parameters except `flashOffer` and `savedFilterId`. The catalogue access and the daily distinct-media limit of that operation apply.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::CatalogueApi.new
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The project to search flash offers for.
opts = {
  source: 'all', # String | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state.
  sort: '-growwerRank', # String | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first.
  domain: 'domain_example', # String | Medias whose domain contains this text, 1 to 255 characters.
  website_type: 'website_type_example', # String | A comma-separated list of website types: `blog`, `press`.
  language: 'language_example', # String | A comma-separated list of language codes, as in GET /vocabulary.
  country: 'country_example', # String | A comma-separated list of country codes, as in GET /vocabulary.
  topics: 'topics_example', # String | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them.
  not_banned_topics: true, # Boolean | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise.
  min_traffic: 56, # Integer | Minimum monthly organic traffic.
  max_traffic: 56, # Integer | Maximum monthly organic traffic.
  traffic_trend_upward: true, # Boolean | Medias whose traffic is growing. Only `true` applies it; omit it otherwise.
  min_domain_rating: 56, # Integer | Minimum domain rating, 0 to 100.
  max_domain_rating: 56, # Integer | Maximum domain rating, 0 to 100.
  min_linked_to_referring_ratio: 8.14, # Float | Minimum ratio of linked domains to referring domains, such as 0.5.
  max_linked_to_referring_ratio: 8.14, # Float | Maximum ratio of linked domains to referring domains, such as 1.5.
  min_post_price: 56, # Integer | Minimum post price, in cents.
  max_post_price: 56, # Integer | Maximum post price, in cents.
  post_link_type: 'post_link_type_example', # String | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`.
  promoted_social_network: 'promoted_social_network_example', # String | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`.
  without_advertising_label: true, # Boolean | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise.
  homepage_listing: true, # Boolean | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise.
  has_link_addition: true, # Boolean | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise.
  min_link_addition_price: 56, # Integer | Minimum link addition price, in cents.
  max_link_addition_price: 56, # Integer | Maximum link addition price, in cents.
  link_addition_link_type: 'link_addition_link_type_example', # String | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`.
  recommended: true, # Boolean | `true`: only the medias Growwer recommends for the project; `false`: only the others.
  favourite: true, # Boolean | `true`: only your favourites for the project; `false`: leave them out.
  requested: true, # Boolean | `true`: only the medias you requested for the project; `false`: leave them out.
  bought: true, # Boolean | `true`: only medias you bought for the project; `false`: leave them out.
  discarded: true, # Boolean | `true`: only the medias you discarded for the project; `false`: leave them out.
  new: true, # Boolean | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise.
  ranks_goal_keyword: 'ranks_goal_keyword_example', # String | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project.
  ranks_ai_keyword: 'ranks_ai_keyword_example', # String | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`.
  limit: 56, # Integer | Medias per page, 1 to 100.
  offset: 56 # Integer | Medias to skip, at most 99900.
}

begin
  # List flash offers
  result = api_instance.list_flash_offers(project_id, opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->list_flash_offers: #{e}"
end
```

#### Using the list_flash_offers_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListFlashOffers200Response>, Integer, Hash)> list_flash_offers_with_http_info(project_id, opts)

```ruby
begin
  # List flash offers
  data, status_code, headers = api_instance.list_flash_offers_with_http_info(project_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListFlashOffers200Response>
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->list_flash_offers_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | **String** | The project to search flash offers for. |  |
| **source** | **String** | Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [optional] |
| **sort** | **String** | The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [optional] |
| **domain** | **String** | Medias whose domain contains this text, 1 to 255 characters. | [optional] |
| **website_type** | **String** | A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [optional] |
| **language** | **String** | A comma-separated list of language codes, as in GET /vocabulary. | [optional] |
| **country** | **String** | A comma-separated list of country codes, as in GET /vocabulary. | [optional] |
| **topics** | **String** | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [optional] |
| **not_banned_topics** | **Boolean** | Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_traffic** | **Integer** | Minimum monthly organic traffic. | [optional] |
| **max_traffic** | **Integer** | Maximum monthly organic traffic. | [optional] |
| **traffic_trend_upward** | **Boolean** | Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_domain_rating** | **Integer** | Minimum domain rating, 0 to 100. | [optional] |
| **max_domain_rating** | **Integer** | Maximum domain rating, 0 to 100. | [optional] |
| **min_linked_to_referring_ratio** | **Float** | Minimum ratio of linked domains to referring domains, such as 0.5. | [optional] |
| **max_linked_to_referring_ratio** | **Float** | Maximum ratio of linked domains to referring domains, such as 1.5. | [optional] |
| **min_post_price** | **Integer** | Minimum post price, in cents. | [optional] |
| **max_post_price** | **Integer** | Maximum post price, in cents. | [optional] |
| **post_link_type** | **String** | A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **promoted_social_network** | **String** | A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [optional] |
| **without_advertising_label** | **Boolean** | Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **homepage_listing** | **Boolean** | Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **has_link_addition** | **Boolean** | Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_link_addition_price** | **Integer** | Minimum link addition price, in cents. | [optional] |
| **max_link_addition_price** | **Integer** | Maximum link addition price, in cents. | [optional] |
| **link_addition_link_type** | **String** | A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **recommended** | **Boolean** | &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [optional] |
| **favourite** | **Boolean** | &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **requested** | **Boolean** | &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **bought** | **Boolean** | &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **discarded** | **Boolean** | &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **new** | **Boolean** | Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **ranks_goal_keyword** | **String** | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [optional] |
| **ranks_ai_keyword** | **String** | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [optional] |
| **limit** | **Integer** | Medias per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Medias to skip, at most 99900. | [optional][default to 0] |

### Return type

[**ListFlashOffers200Response**](ListFlashOffers200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## request_medias

> <RequestMedias201Response> request_medias(id, idempotency_key, request_medias_request)

Request specific medias for a project

Asks Growwer to find the medias of these domains for one of your projects, as the \"request specific domains\" form on the web does. Each entry may be a domain or a URL; it is read as its full domain, lowercased. Repeated domains are requested once, and a domain already requested changes nothing. Up to 200 distinct domains per call. They then appear in the project's catalogue with `project.requested` true (`requested=true` on GET /projects/{id}/medias) once Growwer lists them.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::CatalogueApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The project.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
request_medias_request = Growwer::RequestMediasRequest.new({domains: ['example.com']}) # RequestMediasRequest | 

begin
  # Request specific medias for a project
  result = api_instance.request_medias(id, idempotency_key, request_medias_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->request_medias: #{e}"
end
```

#### Using the request_medias_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<RequestMedias201Response>, Integer, Hash)> request_medias_with_http_info(id, idempotency_key, request_medias_request)

```ruby
begin
  # Request specific medias for a project
  data, status_code, headers = api_instance.request_medias_with_http_info(id, idempotency_key, request_medias_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <RequestMedias201Response>
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->request_medias_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The project. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |
| **request_medias_request** | [**RequestMediasRequest**](RequestMediasRequest.md) |  |  |

### Return type

[**RequestMedias201Response**](RequestMedias201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## search_project_medias

> <ListFlashOffers200Response> search_project_medias(id, opts)

Search the catalogue for a project

The medias the catalogue offers for one of your projects, as the web lists them, with each media's state in the project. Filter with the parameters below, which all combine, or apply one of your saved filters with `savedFilterId` alone. The catalogue is open to accounts with recent completed orders (see `catalogue.eligible` on GET /me), and each account can see a limited number of distinct medias per day (UTC) across the catalogue operations; medias seen again the same day are free.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::CatalogueApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The project.
opts = {
  source: 'all', # String | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state.
  sort: '-growwerRank', # String | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first.
  saved_filter_id: '38400000-8cf0-11bd-b23e-10b96e4ef00d', # String | Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, `source` or `sort`. A filter saved on the web that uses a filter the API does not support is refused with 422 `saved_filter_unsupported`.
  domain: 'domain_example', # String | Medias whose domain contains this text, 1 to 255 characters.
  website_type: 'website_type_example', # String | A comma-separated list of website types: `blog`, `press`.
  language: 'language_example', # String | A comma-separated list of language codes, as in GET /vocabulary.
  country: 'country_example', # String | A comma-separated list of country codes, as in GET /vocabulary.
  topics: 'topics_example', # String | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them.
  not_banned_topics: true, # Boolean | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise.
  min_traffic: 56, # Integer | Minimum monthly organic traffic.
  max_traffic: 56, # Integer | Maximum monthly organic traffic.
  traffic_trend_upward: true, # Boolean | Medias whose traffic is growing. Only `true` applies it; omit it otherwise.
  min_domain_rating: 56, # Integer | Minimum domain rating, 0 to 100.
  max_domain_rating: 56, # Integer | Maximum domain rating, 0 to 100.
  min_linked_to_referring_ratio: 8.14, # Float | Minimum ratio of linked domains to referring domains, such as 0.5.
  max_linked_to_referring_ratio: 8.14, # Float | Maximum ratio of linked domains to referring domains, such as 1.5.
  min_post_price: 56, # Integer | Minimum post price, in cents.
  max_post_price: 56, # Integer | Maximum post price, in cents.
  post_link_type: 'post_link_type_example', # String | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`.
  promoted_social_network: 'promoted_social_network_example', # String | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`.
  without_advertising_label: true, # Boolean | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise.
  homepage_listing: true, # Boolean | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise.
  has_link_addition: true, # Boolean | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise.
  min_link_addition_price: 56, # Integer | Minimum link addition price, in cents.
  max_link_addition_price: 56, # Integer | Maximum link addition price, in cents.
  link_addition_link_type: 'link_addition_link_type_example', # String | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`.
  recommended: true, # Boolean | `true`: only the medias Growwer recommends for the project; `false`: only the others.
  favourite: true, # Boolean | `true`: only your favourites for the project; `false`: leave them out.
  requested: true, # Boolean | `true`: only the medias you requested for the project; `false`: leave them out.
  flash_offer: true, # Boolean | `true`: only medias with a flash offer running; `false`: leave them out.
  bought: true, # Boolean | `true`: only medias you bought for the project; `false`: leave them out.
  discarded: true, # Boolean | `true`: only the medias you discarded for the project; `false`: leave them out.
  new: true, # Boolean | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise.
  ranks_goal_keyword: 'ranks_goal_keyword_example', # String | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project.
  ranks_ai_keyword: 'ranks_ai_keyword_example', # String | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`.
  limit: 56, # Integer | Medias per page, 1 to 100.
  offset: 56 # Integer | Medias to skip, at most 99900.
}

begin
  # Search the catalogue for a project
  result = api_instance.search_project_medias(id, opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->search_project_medias: #{e}"
end
```

#### Using the search_project_medias_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListFlashOffers200Response>, Integer, Hash)> search_project_medias_with_http_info(id, opts)

```ruby
begin
  # Search the catalogue for a project
  data, status_code, headers = api_instance.search_project_medias_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListFlashOffers200Response>
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->search_project_medias_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The project. |  |
| **source** | **String** | Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [optional] |
| **sort** | **String** | The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [optional] |
| **saved_filter_id** | **String** | Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, &#x60;source&#x60; or &#x60;sort&#x60;. A filter saved on the web that uses a filter the API does not support is refused with 422 &#x60;saved_filter_unsupported&#x60;. | [optional] |
| **domain** | **String** | Medias whose domain contains this text, 1 to 255 characters. | [optional] |
| **website_type** | **String** | A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [optional] |
| **language** | **String** | A comma-separated list of language codes, as in GET /vocabulary. | [optional] |
| **country** | **String** | A comma-separated list of country codes, as in GET /vocabulary. | [optional] |
| **topics** | **String** | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [optional] |
| **not_banned_topics** | **Boolean** | Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_traffic** | **Integer** | Minimum monthly organic traffic. | [optional] |
| **max_traffic** | **Integer** | Maximum monthly organic traffic. | [optional] |
| **traffic_trend_upward** | **Boolean** | Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_domain_rating** | **Integer** | Minimum domain rating, 0 to 100. | [optional] |
| **max_domain_rating** | **Integer** | Maximum domain rating, 0 to 100. | [optional] |
| **min_linked_to_referring_ratio** | **Float** | Minimum ratio of linked domains to referring domains, such as 0.5. | [optional] |
| **max_linked_to_referring_ratio** | **Float** | Maximum ratio of linked domains to referring domains, such as 1.5. | [optional] |
| **min_post_price** | **Integer** | Minimum post price, in cents. | [optional] |
| **max_post_price** | **Integer** | Maximum post price, in cents. | [optional] |
| **post_link_type** | **String** | A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **promoted_social_network** | **String** | A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [optional] |
| **without_advertising_label** | **Boolean** | Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **homepage_listing** | **Boolean** | Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **has_link_addition** | **Boolean** | Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_link_addition_price** | **Integer** | Minimum link addition price, in cents. | [optional] |
| **max_link_addition_price** | **Integer** | Maximum link addition price, in cents. | [optional] |
| **link_addition_link_type** | **String** | A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **recommended** | **Boolean** | &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [optional] |
| **favourite** | **Boolean** | &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **requested** | **Boolean** | &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **flash_offer** | **Boolean** | &#x60;true&#x60;: only medias with a flash offer running; &#x60;false&#x60;: leave them out. | [optional] |
| **bought** | **Boolean** | &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **discarded** | **Boolean** | &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **new** | **Boolean** | Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **ranks_goal_keyword** | **String** | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [optional] |
| **ranks_ai_keyword** | **String** | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [optional] |
| **limit** | **Integer** | Medias per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Medias to skip, at most 99900. | [optional][default to 0] |

### Return type

[**ListFlashOffers200Response**](ListFlashOffers200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## undiscard_media

> undiscard_media(id, media_id, idempotency_key)

Restore a discarded media for a project

Restores a media you discarded for one of your projects. Restoring one that is not discarded changes nothing. It works for any media, even one the catalogue no longer shows.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::CatalogueApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The project.
media_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The media.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

begin
  # Restore a discarded media for a project
  api_instance.undiscard_media(id, media_id, idempotency_key)
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->undiscard_media: #{e}"
end
```

#### Using the undiscard_media_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> undiscard_media_with_http_info(id, media_id, idempotency_key)

```ruby
begin
  # Restore a discarded media for a project
  data, status_code, headers = api_instance.undiscard_media_with_http_info(id, media_id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->undiscard_media_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The project. |  |
| **media_id** | **String** | The media. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |

### Return type

nil (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unfavourite_media

> unfavourite_media(id, media_id, idempotency_key)

Remove a media from the favourites of a project

Removes a media from the favourites of one of your projects. Removing one that is not a favourite changes nothing. It works for any media, even one the catalogue no longer shows.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::CatalogueApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The project.
media_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The media.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

begin
  # Remove a media from the favourites of a project
  api_instance.unfavourite_media(id, media_id, idempotency_key)
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->unfavourite_media: #{e}"
end
```

#### Using the unfavourite_media_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> unfavourite_media_with_http_info(id, media_id, idempotency_key)

```ruby
begin
  # Remove a media from the favourites of a project
  data, status_code, headers = api_instance.unfavourite_media_with_http_info(id, media_id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Growwer::ApiError => e
  puts "Error when calling CatalogueApi->unfavourite_media_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The project. |  |
| **media_id** | **String** | The media. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |

### Return type

nil (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

