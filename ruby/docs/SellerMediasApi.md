# Growwer::SellerMediasApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**apply_seller_media_competitive_fees**](SellerMediasApi.md#apply_seller_media_competitive_fees) | **POST** /api/v1/seller/medias/{id}/apply-competitive-fees | Set the competitive fees Growwer suggests |
| [**create_seller_media**](SellerMediasApi.md#create_seller_media) | **POST** /api/v1/seller/medias | Register a media you sell on |
| [**delete_seller_media**](SellerMediasApi.md#delete_seller_media) | **DELETE** /api/v1/seller/medias/{id} | Delete a media you sell on |
| [**get_seller_media**](SellerMediasApi.md#get_seller_media) | **GET** /api/v1/seller/medias/{id} | Get a media you sell on |
| [**list_seller_medias**](SellerMediasApi.md#list_seller_medias) | **GET** /api/v1/seller/medias | List the medias you sell on |
| [**update_seller_media**](SellerMediasApi.md#update_seller_media) | **PATCH** /api/v1/seller/medias/{id} | Edit the offer of a media you sell on |


## apply_seller_media_competitive_fees

> <SellerMedia> apply_seller_media_competitive_fees(id, idempotency_key)

Set the competitive fees Growwer suggests

Sets your post fees for the media to the competitive fees Growwer suggests, the `competitiveFees` of GET /seller/medias/{id}, as the button on the media edit page does. Each link type you offer gets the suggested fee on each side it already has a fee for; no link type gains a side it did not offer.  Two differences from the page: a side Growwer has no suggestion for keeps your fee (the page clears it), and the fixed fee the page falls back to when it cannot find a competitive one is never applied (the page applies it). When neither side has a suggestion, nothing changes and the answer is 409 `no_competitive_fees`. When your fees already are the suggested ones, or the suggestion is only for a side none of your link types offers, nothing changes and the answer is 200.  The fees set are your base fees: a running flash offer keeps discounting them. As with a fee edit, a change of the price may cancel the managed-service proposals accepted for the media whose price it changes. Send no body, or an empty object.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerMediasApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

begin
  # Set the competitive fees Growwer suggests
  result = api_instance.apply_seller_media_competitive_fees(id, idempotency_key)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->apply_seller_media_competitive_fees: #{e}"
end
```

#### Using the apply_seller_media_competitive_fees_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerMedia>, Integer, Hash)> apply_seller_media_competitive_fees_with_http_info(id, idempotency_key)

```ruby
begin
  # Set the competitive fees Growwer suggests
  data, status_code, headers = api_instance.apply_seller_media_competitive_fees_with_http_info(id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerMedia>
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->apply_seller_media_competitive_fees_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## create_seller_media

> <SellerMedia> create_seller_media(idempotency_key, create_seller_media_request)

Register a media you sell on

Registers one of your medias, as the media create page does. The media is created with `state: pending_review` and Growwer reviews it in the background, as for a media registered on the web; GET /seller/medias/{id} shows its state.  - `rootUrl` is the media's root URL; `typology` is `blog` or `press`. - `country` and `language` take the codes GET /vocabulary publishes; `topics` and `bannedTopics` take its topic ids, at most 100 each, and no topic may be both; `bannedTopics` left out bans none. - `postOffer.pricingOptions` lists every link type you offer for sponsored posts, at least one. Each option needs at least one fee, and every option must offer the same sides (written by you, written by the buyer or Growwer), as the page requires. Each fee is at least 1 EUR, sent in cents. - `postOffer.maximumLinks` is how many links a sponsored post may hold, 1 to 4; `postOffer.advertisingLabellingPolicy` whether posts are labelled as advertising, `never` when left out; `postOffer.promotedSocialNetworks` the social networks posts are promoted on, none when left out. - `linkAdditionOffer.pricingOptions` lists the link types you offer for adding a link to an existing article; left out, `null` or an empty list offers none. - `extraServices` lists the extra services you offer, none when left out. It is sent at the top level, although GET /seller/medias/{id} reads it inside `postOffer`. - `acceptMediaPublishingTerms` and `declareMediaOwnership` must be `true`: they accept the media publishing terms and declare that you own or manage the media, as the page's checkboxes do, and are recorded as your consents for the media.  A media registered already, by you or by anyone else, is refused with 409 `media_already_registered`, and each such refusal counts toward a daily limit of refusals (429 `media_duplicate_limit_reached` once reached); medias not registered yet are never limited by it.  To register many medias, call this operation once per media, each call with its own `Idempotency-Key` and its own answer (201, 409, 422 or 429); there is no batch operation. The request limits apply to the loop as to any calls (600 requests per minute per user and 300 per key), and each 409 `media_already_registered` counts toward the daily limit of refusals as it does for a single call. Retry a call that got no answer with its same `Idempotency-Key`, as for any write.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerMediasApi.new
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
create_seller_media_request = Growwer::CreateSellerMediaRequest.new({root_url: 'https://www.example.com', typology: 'blog', country: 'ES', language: 'es', topics: [37], post_offer: Growwer::CreateSellerMediaRequestPostOffer.new({pricing_options: [Growwer::UpdateSellerMediaRequestPostOfferPricingOptionsInner.new({link_type: 'dofollow'})], maximum_links: 37}), accept_media_publishing_terms: false, declare_media_ownership: false}) # CreateSellerMediaRequest | 

begin
  # Register a media you sell on
  result = api_instance.create_seller_media(idempotency_key, create_seller_media_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->create_seller_media: #{e}"
end
```

#### Using the create_seller_media_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerMedia>, Integer, Hash)> create_seller_media_with_http_info(idempotency_key, create_seller_media_request)

```ruby
begin
  # Register a media you sell on
  data, status_code, headers = api_instance.create_seller_media_with_http_info(idempotency_key, create_seller_media_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerMedia>
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->create_seller_media_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **create_seller_media_request** | [**CreateSellerMediaRequest**](CreateSellerMediaRequest.md) |  |  |

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_seller_media

> delete_seller_media(id, idempotency_key)

Delete a media you sell on

Deletes one of your medias, in any state, as the media delete button does. The media must have no order in progress: close or reject its orders first. The API never cancels an order for you, and an order placed while the delete runs is refused, never cancelled.  What goes with the media, as on the web:  - A running flash offer ends with it, and its managed-service proposals are deleted. - Its finished orders stay, with the media's URL; they read `media.id` null. - Buyers' favourites and discards of the domain stay, as they are kept by domain. - The catalogue search drops the media shortly after the 204, as the search index updates asynchronously.  Repeating the call with the same `Idempotency-Key` answers the same 204 with `Idempotent-Replayed: true`; a new key after the delete answers 404.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerMediasApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

begin
  # Delete a media you sell on
  api_instance.delete_seller_media(id, idempotency_key)
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->delete_seller_media: #{e}"
end
```

#### Using the delete_seller_media_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_seller_media_with_http_info(id, idempotency_key)

```ruby
begin
  # Delete a media you sell on
  data, status_code, headers = api_instance.delete_seller_media_with_http_info(id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->delete_seller_media_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

nil (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_seller_media

> <SellerMedia> get_seller_media(id)

Get a media you sell on

One of your medias, with your fees, its extras, the competitive fees Growwer suggests and how it performs. Another seller's media is not found.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerMediasApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Get a media you sell on
  result = api_instance.get_seller_media(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->get_seller_media: #{e}"
end
```

#### Using the get_seller_media_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerMedia>, Integer, Hash)> get_seller_media_with_http_info(id)

```ruby
begin
  # Get a media you sell on
  data, status_code, headers = api_instance.get_seller_media_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerMedia>
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->get_seller_media_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_seller_medias

> <ListSellerMedias200Response> list_seller_medias(opts)

List the medias you sell on

Your medias in every state, with your fees and how they perform, newest first by default.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerMediasApi.new
opts = {
  state: 'active,deactivated', # String | Only the medias in one of these states, comma-separated: `analyzing`, `pending_review`, `active`, `deactivated`. An unknown state is refused with 422.
  sort: '-createdAt', # String | By creation date, number of published orders or publication rate; a leading `-` sorts descending. Medias with no publication rate come first ascending, last descending. Ties come in id order.
  limit: 56, # Integer | Medias per page, 1 to 100.
  offset: 56 # Integer | Medias to skip.
}

begin
  # List the medias you sell on
  result = api_instance.list_seller_medias(opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->list_seller_medias: #{e}"
end
```

#### Using the list_seller_medias_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListSellerMedias200Response>, Integer, Hash)> list_seller_medias_with_http_info(opts)

```ruby
begin
  # List the medias you sell on
  data, status_code, headers = api_instance.list_seller_medias_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListSellerMedias200Response>
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->list_seller_medias_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **state** | **String** | Only the medias in one of these states, comma-separated: &#x60;analyzing&#x60;, &#x60;pending_review&#x60;, &#x60;active&#x60;, &#x60;deactivated&#x60;. An unknown state is refused with 422. | [optional] |
| **sort** | **String** | By creation date, number of published orders or publication rate; a leading &#x60;-&#x60; sorts descending. Medias with no publication rate come first ascending, last descending. Ties come in id order. | [optional][default to &#39;-createdAt&#39;] |
| **limit** | **Integer** | Medias per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Medias to skip. | [optional][default to 0] |

### Return type

[**ListSellerMedias200Response**](ListSellerMedias200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_seller_media

> <SellerMedia> update_seller_media(id, idempotency_key, update_seller_media_request)

Edit the offer of a media you sell on

Sets the fees, extra services, typology and post offer characteristics of one of your medias, as the media edit page saves them. Send only the fields you change: a field you send replaces that field wholly, a field you leave out stays as it is, inside `postOffer` too (sending only `postOffer.maximumLinks` keeps your fees).  - `typology` is `blog` or `press`. - `postOffer.pricingOptions` lists every link type you offer for sponsored posts, at least one. A link type you leave out is no longer offered. Each option needs at least one fee, and every option must offer the same sides (written by you, written by the buyer or Growwer), as the page requires. Each fee is at least 1 EUR. - `postOffer.maximumLinks` is how many links a sponsored post may hold, 1 to 4; `postOffer.advertisingLabellingPolicy` whether posts are labelled as advertising (`always` or `never`); `postOffer.promotedSocialNetworks` the full list of social networks posts are promoted on, each once (an empty list for none). - `linkAdditionOffer.pricingOptions` lists the link types you offer for adding a link to an existing article; `null` or an empty list stops offering link additions. - `extraServices` is the full list of extra services you offer; an empty list removes them all. It is sent at the top level, although GET /seller/medias/{id} reads it inside `postOffer`.  The fees are your base fees, the ones GET /seller/medias/{id} returns: while a flash offer runs, its discount keeps applying on top of them, and `currentCost` shows the result. `currentCost` may be sent back as read and is ignored. Country, language, topics and comments are not edited here.  As on the page, a change of the post offer's price may cancel the managed-service proposals accepted for the media whose price it changes, and raising the price above the best competitor's tells Growwer's support team. A restricted seller account may edit its offer.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerMediasApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
update_seller_media_request = Growwer::UpdateSellerMediaRequest.new # UpdateSellerMediaRequest | 

begin
  # Edit the offer of a media you sell on
  result = api_instance.update_seller_media(id, idempotency_key, update_seller_media_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->update_seller_media: #{e}"
end
```

#### Using the update_seller_media_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerMedia>, Integer, Hash)> update_seller_media_with_http_info(id, idempotency_key, update_seller_media_request)

```ruby
begin
  # Edit the offer of a media you sell on
  data, status_code, headers = api_instance.update_seller_media_with_http_info(id, idempotency_key, update_seller_media_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerMedia>
rescue Growwer::ApiError => e
  puts "Error when calling SellerMediasApi->update_seller_media_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **update_seller_media_request** | [**UpdateSellerMediaRequest**](UpdateSellerMediaRequest.md) |  |  |

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

