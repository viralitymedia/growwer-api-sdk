# Growwer::OrdersApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**approve_order**](OrdersApi.md#approve_order) | **POST** /api/v1/orders/{id}/approve | Approve an order&#39;s delivery |
| [**approve_order_draft**](OrdersApi.md#approve_order_draft) | **POST** /api/v1/orders/{id}/approve-draft | Approve a draft |
| [**cancel_order**](OrdersApi.md#cancel_order) | **POST** /api/v1/orders/{id}/cancel | Cancel an order |
| [**create_order**](OrdersApi.md#create_order) | **POST** /api/v1/orders | Place an order |
| [**download_order_briefing**](OrdersApi.md#download_order_briefing) | **GET** /api/v1/orders/{id}/briefing | Download the draft you attached to an order |
| [**download_order_draft**](OrdersApi.md#download_order_draft) | **GET** /api/v1/orders/{id}/draft | Download the draft of an order |
| [**estimate_order**](OrdersApi.md#estimate_order) | **POST** /api/v1/orders/estimate | Estimate an order |
| [**get_order**](OrdersApi.md#get_order) | **GET** /api/v1/orders/{id} | Get an order |
| [**list_orders**](OrdersApi.md#list_orders) | **GET** /api/v1/orders | List your orders |
| [**request_order_draft_update**](OrdersApi.md#request_order_draft_update) | **POST** /api/v1/orders/{id}/request-draft-update | Request changes to a draft |
| [**request_order_update**](OrdersApi.md#request_order_update) | **POST** /api/v1/orders/{id}/request-update | Request changes to a delivery |


## approve_order

> <Order> approve_order(id, idempotency_key)

Approve an order's delivery

Approves the delivery of an order whose `pendingAction` is yours to review the delivery, as the web does. The order finishes and the seller is paid. It takes no body.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::OrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

begin
  # Approve an order's delivery
  result = api_instance.approve_order(id, idempotency_key)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->approve_order: #{e}"
end
```

#### Using the approve_order_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Order>, Integer, Hash)> approve_order_with_http_info(id, idempotency_key)

```ruby
begin
  # Approve an order's delivery
  data, status_code, headers = api_instance.approve_order_with_http_info(id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Order>
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->approve_order_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## approve_order_draft

> <Order> approve_order_draft(id, idempotency_key)

Approve a draft

Approves the draft of a post order whose `pendingAction` is yours to review the draft (GET /orders/{id}/draft downloads it), as the web does. The seller then publishes it. It takes no body.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::OrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

begin
  # Approve a draft
  result = api_instance.approve_order_draft(id, idempotency_key)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->approve_order_draft: #{e}"
end
```

#### Using the approve_order_draft_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Order>, Integer, Hash)> approve_order_draft_with_http_info(id, idempotency_key)

```ruby
begin
  # Approve a draft
  data, status_code, headers = api_instance.approve_order_draft_with_http_info(id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Order>
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->approve_order_draft_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cancel_order

> <Order> cancel_order(id, idempotency_key, order_action_reason)

Cancel an order

Cancels an order the seller has not accepted yet (`state` `pending_acceptance`), as the web does. Its price returns to your wallet's available balance, and the seller is told your reason.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::OrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
order_action_reason = Growwer::OrderActionReason.new({reason: 'reason_example'}) # OrderActionReason | 

begin
  # Cancel an order
  result = api_instance.cancel_order(id, idempotency_key, order_action_reason)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->cancel_order: #{e}"
end
```

#### Using the cancel_order_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Order>, Integer, Hash)> cancel_order_with_http_info(id, idempotency_key, order_action_reason)

```ruby
begin
  # Cancel an order
  data, status_code, headers = api_instance.cancel_order_with_http_info(id, idempotency_key, order_action_reason)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Order>
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->cancel_order_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |
| **order_action_reason** | [**OrderActionReason**](OrderActionReason.md) |  |  |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_order

> <Order> create_order(idempotency_key, order_create_request)

Place an order

Places an order on a media for one of your projects and pays its price from your wallet's available balance, as ordering on the web does. Estimate the order first (POST /orders/estimate) and send the price it answers as `expectedPrice`: the order is placed only at that price.  Placing the same order (same project, media, type and price) again within 5 seconds of one still in progress is refused with `duplicate_order`. Its `details.orderId` is the earlier order, or null when that order has finished or was deleted since.  A proposed draft (`proposedDraftFileId`, from POST /files) is used up when the order is placed. If the order is then refused because another request changed your balance, the media or its price, or placed the same order, the file is used up all the same and the refusal's message says so: upload it again before retrying.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::OrdersApi.new
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
order_create_request = Growwer::OrderCreateRequest.new({type: 'post', project_id: 'project_id_example', media_id: 'media_id_example', briefing: Growwer::LinkAdditionOrderBriefingRequest.new({linking_from: 'linking_from_example', link: Growwer::OrderLinkRequest.new({type: 'dofollow'})}), expected_price: Growwer::Money.new({amount: 12500, currency: 'EUR'})}) # OrderCreateRequest | 

begin
  # Place an order
  result = api_instance.create_order(idempotency_key, order_create_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->create_order: #{e}"
end
```

#### Using the create_order_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Order>, Integer, Hash)> create_order_with_http_info(idempotency_key, order_create_request)

```ruby
begin
  # Place an order
  data, status_code, headers = api_instance.create_order_with_http_info(idempotency_key, order_create_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Order>
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->create_order_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |
| **order_create_request** | [**OrderCreateRequest**](OrderCreateRequest.md) |  |  |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## download_order_briefing

> File download_order_briefing(id)

Download the draft you attached to an order

The file you attached to the briefing of a post order. 404 when the order has none (`briefing.hasProposedDraft` is false) or the file cannot be read.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::OrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Download the draft you attached to an order
  result = api_instance.download_order_briefing(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->download_order_briefing: #{e}"
end
```

#### Using the download_order_briefing_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(File, Integer, Hash)> download_order_briefing_with_http_info(id)

```ruby
begin
  # Download the draft you attached to an order
  data, status_code, headers = api_instance.download_order_briefing_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => File
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->download_order_briefing_with_http_info: #{e}"
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


## download_order_draft

> File download_order_draft(id)

Download the draft of an order

The file of the current draft of a post order. 404 when the order has no draft file (`draft.hasFile` is false) or the file cannot be read.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::OrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Download the draft of an order
  result = api_instance.download_order_draft(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->download_order_draft: #{e}"
end
```

#### Using the download_order_draft_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(File, Integer, Hash)> download_order_draft_with_http_info(id)

```ruby
begin
  # Download the draft of an order
  data, status_code, headers = api_instance.download_order_draft_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => File
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->download_order_draft_with_http_info: #{e}"
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


## estimate_order

> <OrderEstimate> estimate_order(order_estimate_request)

Estimate an order

Checks and prices the order POST /orders would place with the same body, without `expectedPrice`, and compares the price with your wallet's available balance. Nothing is placed, charged or used up, so a read-only key may call it and it takes no Idempotency-Key. Send the `price` it answers as `expectedPrice` when you place the order.  The estimate is refused for the same reasons as the order itself, except a balance that does not cover the price: that is answered here with `sufficientBalance: false` and the `missing` amount.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::OrdersApi.new
order_estimate_request = Growwer::OrderEstimateRequest.new({type: 'post', project_id: 'project_id_example', media_id: 'media_id_example', briefing: Growwer::LinkAdditionOrderBriefingRequest.new({linking_from: 'linking_from_example', link: Growwer::OrderLinkRequest.new({type: 'dofollow'})})}) # OrderEstimateRequest | 

begin
  # Estimate an order
  result = api_instance.estimate_order(order_estimate_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->estimate_order: #{e}"
end
```

#### Using the estimate_order_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<OrderEstimate>, Integer, Hash)> estimate_order_with_http_info(order_estimate_request)

```ruby
begin
  # Estimate an order
  data, status_code, headers = api_instance.estimate_order_with_http_info(order_estimate_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <OrderEstimate>
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->estimate_order_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **order_estimate_request** | [**OrderEstimateRequest**](OrderEstimateRequest.md) |  |  |

### Return type

[**OrderEstimate**](OrderEstimate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_order

> <Order> get_order(id)

Get an order

One order you bought, with its briefing, its draft and its state history.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::OrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Get an order
  result = api_instance.get_order(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->get_order: #{e}"
end
```

#### Using the get_order_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Order>, Integer, Hash)> get_order_with_http_info(id)

```ruby
begin
  # Get an order
  data, status_code, headers = api_instance.get_order_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Order>
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->get_order_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_orders

> <ListOrders200Response> list_orders(opts)

List your orders

The orders you bought, newest first by default. To follow your orders, poll with `sort=updatedAt` and `updatedSince` set to the `updatedAt` of the last order you saw: an order moves to the end of that list each time it changes state.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::OrdersApi.new
opts = {
  project_id: '38400000-8cf0-11bd-b23e-10b96e4ef00d', # String | Only the orders of this project of yours.
  media_id: '38400000-8cf0-11bd-b23e-10b96e4ef00d', # String | Only the orders on this media.
  state: 'pending_acceptance,pending_order_delivery', # String | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones.
  updated_since: Time.parse('2013-10-20T19:20:30+01:00'), # Time | Only the orders whose `updatedAt` is at or after this instant, an ISO-8601 date-time with its offset (send `+` as `%2B`).
  sort: '-createdAt', # String | `-createdAt`, newest first, or `updatedAt`, least recently changed first. Orders of the same instant come in id order.
  limit: 56, # Integer | Orders per page, 1 to 100.
  offset: 56 # Integer | Orders to skip.
}

begin
  # List your orders
  result = api_instance.list_orders(opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->list_orders: #{e}"
end
```

#### Using the list_orders_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListOrders200Response>, Integer, Hash)> list_orders_with_http_info(opts)

```ruby
begin
  # List your orders
  data, status_code, headers = api_instance.list_orders_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListOrders200Response>
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->list_orders_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | **String** | Only the orders of this project of yours. | [optional] |
| **media_id** | **String** | Only the orders on this media. | [optional] |
| **state** | **String** | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones. | [optional] |
| **updated_since** | **Time** | Only the orders whose &#x60;updatedAt&#x60; is at or after this instant, an ISO-8601 date-time with its offset (send &#x60;+&#x60; as &#x60;%2B&#x60;). | [optional] |
| **sort** | **String** | &#x60;-createdAt&#x60;, newest first, or &#x60;updatedAt&#x60;, least recently changed first. Orders of the same instant come in id order. | [optional][default to &#39;-createdAt&#39;] |
| **limit** | **Integer** | Orders per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Orders to skip. | [optional][default to 0] |

### Return type

[**ListOrders200Response**](ListOrders200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## request_order_draft_update

> <Order> request_order_draft_update(id, idempotency_key, order_action_reason)

Request changes to a draft

Asks the seller to change the draft of a post order whose `pendingAction` is yours to review the draft, as the web does. The seller is told your reason.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::OrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
order_action_reason = Growwer::OrderActionReason.new({reason: 'reason_example'}) # OrderActionReason | 

begin
  # Request changes to a draft
  result = api_instance.request_order_draft_update(id, idempotency_key, order_action_reason)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->request_order_draft_update: #{e}"
end
```

#### Using the request_order_draft_update_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Order>, Integer, Hash)> request_order_draft_update_with_http_info(id, idempotency_key, order_action_reason)

```ruby
begin
  # Request changes to a draft
  data, status_code, headers = api_instance.request_order_draft_update_with_http_info(id, idempotency_key, order_action_reason)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Order>
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->request_order_draft_update_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |
| **order_action_reason** | [**OrderActionReason**](OrderActionReason.md) |  |  |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## request_order_update

> <Order> request_order_update(id, idempotency_key, order_action_reason)

Request changes to a delivery

Asks the seller to change the delivery of an order whose `pendingAction` is yours to review the delivery, as the web does. The seller is told your reason.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::OrdersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
order_action_reason = Growwer::OrderActionReason.new({reason: 'reason_example'}) # OrderActionReason | 

begin
  # Request changes to a delivery
  result = api_instance.request_order_update(id, idempotency_key, order_action_reason)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->request_order_update: #{e}"
end
```

#### Using the request_order_update_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Order>, Integer, Hash)> request_order_update_with_http_info(id, idempotency_key, order_action_reason)

```ruby
begin
  # Request changes to a delivery
  data, status_code, headers = api_instance.request_order_update_with_http_info(id, idempotency_key, order_action_reason)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Order>
rescue Growwer::ApiError => e
  puts "Error when calling OrdersApi->request_order_update_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |
| **order_action_reason** | [**OrderActionReason**](OrderActionReason.md) |  |  |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

