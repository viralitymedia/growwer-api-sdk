# Growwer::SellerMediasApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**apply_seller_media_competitive_fees**](SellerMediasApi.md#apply_seller_media_competitive_fees) | **POST** /api/v1/seller/medias/{id}/apply-competitive-fees | Set the competitive fees Growwer suggests |
| [**get_seller_media**](SellerMediasApi.md#get_seller_media) | **GET** /api/v1/seller/medias/{id} | Get a media you sell on |
| [**list_seller_medias**](SellerMediasApi.md#list_seller_medias) | **GET** /api/v1/seller/medias | List the medias you sell on |
| [**update_seller_media**](SellerMediasApi.md#update_seller_media) | **PATCH** /api/v1/seller/medias/{id} | Edit the fees of a media you sell on |


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

Edit the fees of a media you sell on

Sets the fees of one of your medias, as the media edit page saves them. Send only the sections you change: a section you send replaces that section wholly, a section you leave out stays as it is.  - `postOffer.pricingOptions` lists every link type you offer for sponsored posts, at least one. A link type you leave out is no longer offered. Each option needs at least one fee, and every option must offer the same sides (written by you, written by the buyer or Growwer), as the page requires. Each fee is at least 1 EUR. - `linkAdditionOffer.pricingOptions` lists the link types you offer for adding a link to an existing article; `null` or an empty list stops offering link additions. - `extraServices` is the full list of extra services you offer; an empty list removes them all.  The fees are your base fees, the ones GET /seller/medias/{id} returns: while a flash offer runs, its discount keeps applying on top of them, and `currentCost` shows the result. `currentCost` may be sent back as read and is ignored. Characteristics, topics and comments are not edited here.  As on the page, a change of the post offer's price may cancel the managed-service proposals accepted for the media whose price it changes, and raising the price above the best competitor's tells Growwer's support team. A restricted seller account may edit its fees.

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
  # Edit the fees of a media you sell on
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
  # Edit the fees of a media you sell on
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

