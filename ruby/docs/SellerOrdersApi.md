# Growwer::SellerOrdersApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**accept_seller_order**](SellerOrdersApi.md#accept_seller_order) | **POST** /api/v1/seller/orders/{id}/accept | Accept an order |
| [**deliver_seller_order**](SellerOrdersApi.md#deliver_seller_order) | **POST** /api/v1/seller/orders/{id}/deliver | Deliver an order |
| [**deliver_seller_order_draft**](SellerOrdersApi.md#deliver_seller_order_draft) | **POST** /api/v1/seller/orders/{id}/deliver-draft | Deliver a draft |
| [**deliver_seller_order_draft_update**](SellerOrdersApi.md#deliver_seller_order_draft_update) | **POST** /api/v1/seller/orders/{id}/deliver-draft-update | Deliver a draft update |
| [**deliver_seller_order_update**](SellerOrdersApi.md#deliver_seller_order_update) | **POST** /api/v1/seller/orders/{id}/deliver-update | Deliver an update |
| [**download_seller_order_briefing**](SellerOrdersApi.md#download_seller_order_briefing) | **GET** /api/v1/seller/orders/{id}/briefing | Download the draft the buyer attached to an order |
| [**download_seller_order_draft**](SellerOrdersApi.md#download_seller_order_draft) | **GET** /api/v1/seller/orders/{id}/draft | Download the draft of an order you sell |
| [**get_seller_order**](SellerOrdersApi.md#get_seller_order) | **GET** /api/v1/seller/orders/{id} | Get an order you sell |
| [**list_seller_orders**](SellerOrdersApi.md#list_seller_orders) | **GET** /api/v1/seller/orders | List the orders you sell |
| [**refute_seller_order_draft_update**](SellerOrdersApi.md#refute_seller_order_draft_update) | **POST** /api/v1/seller/orders/{id}/refute-draft-update | Refuse a draft update |
| [**refute_seller_order_update**](SellerOrdersApi.md#refute_seller_order_update) | **POST** /api/v1/seller/orders/{id}/refute-update | Refuse an update |
| [**reject_seller_order**](SellerOrdersApi.md#reject_seller_order) | **POST** /api/v1/seller/orders/{id}/reject | Reject an order |


## accept_seller_order

> <SellerOrder> accept_seller_order(id, idempotency_key)

Accept an order

Accepts an order placed on one of your medias (`state` `pending_acceptance`), as the web does. A post order whose draft is still to be written (by you or by Growwer) moves to `pending_draft`; any other order moves to `pending_order_delivery`. The buyer is told. Takes no body.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

begin
  # Accept an order
  result = api_instance.accept_seller_order(id, idempotency_key)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->accept_seller_order: #{e}"
end
```

#### Using the accept_seller_order_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerOrder>, Integer, Hash)> accept_seller_order_with_http_info(id, idempotency_key)

```ruby
begin
  # Accept an order
  data, status_code, headers = api_instance.accept_seller_order_with_http_info(id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerOrder>
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->accept_seller_order_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deliver_seller_order

> <SellerOrder> deliver_seller_order(id, idempotency_key, opts)

Deliver an order

Delivers an order placed on one of your medias (`state` `pending_order_delivery`), as the web does. A post order takes the URL of the published post and the confirmation of its publication date; a link addition order takes no body, and any field is refused. The order moves to `pending_order_delivery_review` and the buyer is asked to review it, or, for a post order whose scheduled publication date is still to come, to `scheduled` without telling the buyer yet. The URL is checked to be a URL only, as the web does.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
opts = {
  seller_order_post_delivery: Growwer::SellerOrderPostDelivery.new({url: 'url_example', publication_date_confirmed: false}) # SellerOrderPostDelivery | 
}

begin
  # Deliver an order
  result = api_instance.deliver_seller_order(id, idempotency_key, opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->deliver_seller_order: #{e}"
end
```

#### Using the deliver_seller_order_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerOrder>, Integer, Hash)> deliver_seller_order_with_http_info(id, idempotency_key, opts)

```ruby
begin
  # Deliver an order
  data, status_code, headers = api_instance.deliver_seller_order_with_http_info(id, idempotency_key, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerOrder>
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->deliver_seller_order_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **seller_order_post_delivery** | [**SellerOrderPostDelivery**](SellerOrderPostDelivery.md) |  | [optional] |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deliver_seller_order_draft

> <SellerOrder> deliver_seller_order_draft(id, idempotency_key, seller_order_draft_file)

Deliver a draft

Delivers the draft of a post order placed on one of your medias whose draft you write (`state` `pending_draft`), as the web does, from a file you uploaded with POST /files. The order moves to `pending_draft_review` when the buyer reviews drafts, otherwise to `pending_order_delivery`. The file is used up once the draft is delivered; a refused request leaves it usable.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
seller_order_draft_file = Growwer::SellerOrderDraftFile.new({file_id: 'file_id_example'}) # SellerOrderDraftFile | 

begin
  # Deliver a draft
  result = api_instance.deliver_seller_order_draft(id, idempotency_key, seller_order_draft_file)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->deliver_seller_order_draft: #{e}"
end
```

#### Using the deliver_seller_order_draft_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerOrder>, Integer, Hash)> deliver_seller_order_draft_with_http_info(id, idempotency_key, seller_order_draft_file)

```ruby
begin
  # Deliver a draft
  data, status_code, headers = api_instance.deliver_seller_order_draft_with_http_info(id, idempotency_key, seller_order_draft_file)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerOrder>
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->deliver_seller_order_draft_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **seller_order_draft_file** | [**SellerOrderDraftFile**](SellerOrderDraftFile.md) |  |  |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deliver_seller_order_draft_update

> <SellerOrder> deliver_seller_order_draft_update(id, idempotency_key, seller_order_draft_file)

Deliver a draft update

Delivers the draft update the buyer asked for on a post order placed on one of your medias whose draft you write (`state` `pending_draft_update`), as the web does, from a file you uploaded with POST /files. The order moves back to `pending_draft_review`. The file is used up once the draft is delivered; a refused request leaves it usable.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
seller_order_draft_file = Growwer::SellerOrderDraftFile.new({file_id: 'file_id_example'}) # SellerOrderDraftFile | 

begin
  # Deliver a draft update
  result = api_instance.deliver_seller_order_draft_update(id, idempotency_key, seller_order_draft_file)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->deliver_seller_order_draft_update: #{e}"
end
```

#### Using the deliver_seller_order_draft_update_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerOrder>, Integer, Hash)> deliver_seller_order_draft_update_with_http_info(id, idempotency_key, seller_order_draft_file)

```ruby
begin
  # Deliver a draft update
  data, status_code, headers = api_instance.deliver_seller_order_draft_update_with_http_info(id, idempotency_key, seller_order_draft_file)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerOrder>
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->deliver_seller_order_draft_update_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **seller_order_draft_file** | [**SellerOrderDraftFile**](SellerOrderDraftFile.md) |  |  |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deliver_seller_order_update

> <SellerOrder> deliver_seller_order_update(id, idempotency_key, opts)

Deliver an update

Delivers the update the buyer asked for on an order placed on one of your medias (`state` `pending_order_delivery_update`), as the web does. A post order takes the URL of the published post, which may be the same as before, and the confirmation of its publication date; both must be sent. A link addition order takes no body, and any field is refused. The order moves back to `pending_order_delivery_review` and the buyer is asked to review it.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
opts = {
  seller_order_post_delivery: Growwer::SellerOrderPostDelivery.new({url: 'url_example', publication_date_confirmed: false}) # SellerOrderPostDelivery | 
}

begin
  # Deliver an update
  result = api_instance.deliver_seller_order_update(id, idempotency_key, opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->deliver_seller_order_update: #{e}"
end
```

#### Using the deliver_seller_order_update_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerOrder>, Integer, Hash)> deliver_seller_order_update_with_http_info(id, idempotency_key, opts)

```ruby
begin
  # Deliver an update
  data, status_code, headers = api_instance.deliver_seller_order_update_with_http_info(id, idempotency_key, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerOrder>
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->deliver_seller_order_update_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **seller_order_post_delivery** | [**SellerOrderPostDelivery**](SellerOrderPostDelivery.md) |  | [optional] |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## download_seller_order_briefing

> File download_seller_order_briefing(id)

Download the draft the buyer attached to an order

The file the buyer attached to the briefing of a post order you sell. 404 when the order has none (`briefing.hasProposedDraft` is false) or the file cannot be read.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Download the draft the buyer attached to an order
  result = api_instance.download_seller_order_briefing(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->download_seller_order_briefing: #{e}"
end
```

#### Using the download_seller_order_briefing_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(File, Integer, Hash)> download_seller_order_briefing_with_http_info(id)

```ruby
begin
  # Download the draft the buyer attached to an order
  data, status_code, headers = api_instance.download_seller_order_briefing_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => File
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->download_seller_order_briefing_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## download_seller_order_draft

> File download_seller_order_draft(id)

Download the draft of an order you sell

The file of the current draft of a post order you sell. 404 when the order has no draft file (`draft.hasFile` is false) or the file cannot be read. Earlier drafts are not available.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Download the draft of an order you sell
  result = api_instance.download_seller_order_draft(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->download_seller_order_draft: #{e}"
end
```

#### Using the download_seller_order_draft_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(File, Integer, Hash)> download_seller_order_draft_with_http_info(id)

```ruby
begin
  # Download the draft of an order you sell
  data, status_code, headers = api_instance.download_seller_order_draft_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => File
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->download_seller_order_draft_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## get_seller_order

> <SellerOrder> get_seller_order(id)

Get an order you sell

One order placed on one of your medias, with its briefing, its draft and its state history. An order you only bought is not found here; it is under GET /orders/{id}.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Get an order you sell
  result = api_instance.get_seller_order(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->get_seller_order: #{e}"
end
```

#### Using the get_seller_order_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerOrder>, Integer, Hash)> get_seller_order_with_http_info(id)

```ruby
begin
  # Get an order you sell
  data, status_code, headers = api_instance.get_seller_order_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerOrder>
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->get_seller_order_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_seller_orders

> <ListSellerOrders200Response> list_seller_orders(opts)

List the orders you sell

The orders placed on your medias, newest first by default. To follow them, poll with `sort=updatedAt` and `updatedSince` set to the `updatedAt` of the last order you saw: an order moves to the end of that list each time it changes state. The orders you bought are under GET /orders.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
opts = {
  media_id: '38400000-8cf0-11bd-b23e-10b96e4ef00d', # String | Only the orders on this media of yours.
  state: 'pending_acceptance,pending_order_delivery', # String | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones.
  updated_since: Time.parse('2013-10-20T19:20:30+01:00'), # Time | Only the orders whose `updatedAt` is at or after this instant, an ISO-8601 date-time with its offset (send `+` as `%2B`).
  sort: '-createdAt', # String | `-createdAt`, newest first, or `updatedAt`, least recently changed first. Orders of the same instant come in id order.
  limit: 56, # Integer | Orders per page, 1 to 100.
  offset: 56 # Integer | Orders to skip.
}

begin
  # List the orders you sell
  result = api_instance.list_seller_orders(opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->list_seller_orders: #{e}"
end
```

#### Using the list_seller_orders_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListSellerOrders200Response>, Integer, Hash)> list_seller_orders_with_http_info(opts)

```ruby
begin
  # List the orders you sell
  data, status_code, headers = api_instance.list_seller_orders_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListSellerOrders200Response>
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->list_seller_orders_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **media_id** | **String** | Only the orders on this media of yours. | [optional] |
| **state** | **String** | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones. | [optional] |
| **updated_since** | **Time** | Only the orders whose &#x60;updatedAt&#x60; is at or after this instant, an ISO-8601 date-time with its offset (send &#x60;+&#x60; as &#x60;%2B&#x60;). | [optional] |
| **sort** | **String** | &#x60;-createdAt&#x60;, newest first, or &#x60;updatedAt&#x60;, least recently changed first. Orders of the same instant come in id order. | [optional][default to &#39;-createdAt&#39;] |
| **limit** | **Integer** | Orders per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Orders to skip. | [optional][default to 0] |

### Return type

[**ListSellerOrders200Response**](ListSellerOrders200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## refute_seller_order_draft_update

> <SellerOrder> refute_seller_order_draft_update(id, idempotency_key, seller_order_refutation)

Refuse a draft update

Refuses the draft update the buyer asked for on a post order placed on one of your medias whose draft you write (`state` `pending_draft_update`), as the web does. The order moves back to `pending_draft_review` and the buyer is told your reason. A draft Growwer or the buyer writes cannot be refused here.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
seller_order_refutation = Growwer::SellerOrderRefutation.new({reason: 'reason_example'}) # SellerOrderRefutation | 

begin
  # Refuse a draft update
  result = api_instance.refute_seller_order_draft_update(id, idempotency_key, seller_order_refutation)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->refute_seller_order_draft_update: #{e}"
end
```

#### Using the refute_seller_order_draft_update_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerOrder>, Integer, Hash)> refute_seller_order_draft_update_with_http_info(id, idempotency_key, seller_order_refutation)

```ruby
begin
  # Refuse a draft update
  data, status_code, headers = api_instance.refute_seller_order_draft_update_with_http_info(id, idempotency_key, seller_order_refutation)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerOrder>
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->refute_seller_order_draft_update_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **seller_order_refutation** | [**SellerOrderRefutation**](SellerOrderRefutation.md) |  |  |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## refute_seller_order_update

> <SellerOrder> refute_seller_order_update(id, idempotency_key, seller_order_refutation)

Refuse an update

Refuses the update the buyer asked for on an order placed on one of your medias (`state` `pending_order_delivery_update`), as the web does. The order moves back to `pending_order_delivery_review` and the buyer is told your reason.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
seller_order_refutation = Growwer::SellerOrderRefutation.new({reason: 'reason_example'}) # SellerOrderRefutation | 

begin
  # Refuse an update
  result = api_instance.refute_seller_order_update(id, idempotency_key, seller_order_refutation)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->refute_seller_order_update: #{e}"
end
```

#### Using the refute_seller_order_update_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerOrder>, Integer, Hash)> refute_seller_order_update_with_http_info(id, idempotency_key, seller_order_refutation)

```ruby
begin
  # Refuse an update
  data, status_code, headers = api_instance.refute_seller_order_update_with_http_info(id, idempotency_key, seller_order_refutation)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerOrder>
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->refute_seller_order_update_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **seller_order_refutation** | [**SellerOrderRefutation**](SellerOrderRefutation.md) |  |  |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reject_seller_order

> <SellerOrder> reject_seller_order(id, idempotency_key, seller_order_rejection)

Reject an order

Rejects an order placed on one of your medias that you have not accepted yet (`state` `pending_acceptance`), as the web does. The order moves to `rejected_by_seller`, its price returns to the buyer, and the buyer is told your reason.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerOrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
seller_order_rejection = Growwer::SellerOrderRejection.new({reason: Growwer::SellerOrderRejectionReason.new({name: 'media_is_competition'})}) # SellerOrderRejection | 

begin
  # Reject an order
  result = api_instance.reject_seller_order(id, idempotency_key, seller_order_rejection)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->reject_seller_order: #{e}"
end
```

#### Using the reject_seller_order_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SellerOrder>, Integer, Hash)> reject_seller_order_with_http_info(id, idempotency_key, seller_order_rejection)

```ruby
begin
  # Reject an order
  data, status_code, headers = api_instance.reject_seller_order_with_http_info(id, idempotency_key, seller_order_rejection)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SellerOrder>
rescue Growwer::ApiError => e
  puts "Error when calling SellerOrdersApi->reject_seller_order_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **seller_order_rejection** | [**SellerOrderRejection**](SellerOrderRejection.md) |  |  |

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

