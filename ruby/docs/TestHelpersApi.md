# Growwer::TestHelpersApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**advance_test_order**](TestHelpersApi.md#advance_test_order) | **POST** /api/v1/test-helpers/orders/{id}/advance | Advance a test order |
| [**reset_test_data**](TestHelpersApi.md#reset_test_data) | **POST** /api/v1/test-helpers/reset | Reset your test data |
| [**top_up_test_wallet**](TestHelpersApi.md#top_up_test_wallet) | **POST** /api/v1/test-helpers/wallet/top-up | Top up your test wallet |


## advance_test_order

> <Order> advance_test_order(id, idempotency_key, advance_test_order_request)

Advance a test order

Test keys only. Moves one of your test orders at once to `to`, without waiting for the simulated seller: `accepted` or `rejected` (by the seller, from `pending_acceptance`), `draft_delivered` (the sample draft, from `pending_draft` or `pending_draft_update`), `draft_update_requested` (as if you sent the draft back, from `pending_draft_review`), `published` (delivered for your review, from `pending_order_delivery`, `scheduled` or `pending_order_delivery_update`), `update_requested` (as if you sent the delivery back, from `pending_order_delivery_review`) or `cancelled_by_growwer` (from any state that is not finished). The order and your test wallet change as that move changes them live, a rejection or a cancellation refunding the price, and the simulated seller carries on from the new state. A post with a future `scheduledPublicationDate` waits in `scheduled` until that date once the simulated seller delivers it; `published` skips the wait. A target its state does not allow answers 409 `invalid_transition` with the targets it allows. A live key gets 403 `test_mode_only`.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::TestHelpersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
advance_test_order_request = Growwer::AdvanceTestOrderRequest.new({to: 'accepted'}) # AdvanceTestOrderRequest | 

begin
  # Advance a test order
  result = api_instance.advance_test_order(id, idempotency_key, advance_test_order_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling TestHelpersApi->advance_test_order: #{e}"
end
```

#### Using the advance_test_order_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Order>, Integer, Hash)> advance_test_order_with_http_info(id, idempotency_key, advance_test_order_request)

```ruby
begin
  # Advance a test order
  data, status_code, headers = api_instance.advance_test_order_with_http_info(id, idempotency_key, advance_test_order_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Order>
rescue Growwer::ApiError => e
  puts "Error when calling TestHelpersApi->advance_test_order_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **advance_test_order_request** | [**AdvanceTestOrderRequest**](AdvanceTestOrderRequest.md) |  |  |

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reset_test_data

> reset_test_data(idempotency_key)

Reset your test data

Test keys only. Deletes your test projects, orders and uploaded test files, and returns your test wallet to its opening balance of 1,000.00 EUR with no movements. Your API keys and webhook subscriptions stay, and nothing of your live account changes. It takes no body. A live key gets 403 `test_mode_only`.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::TestHelpersApi.new
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

begin
  # Reset your test data
  api_instance.reset_test_data(idempotency_key)
rescue Growwer::ApiError => e
  puts "Error when calling TestHelpersApi->reset_test_data: #{e}"
end
```

#### Using the reset_test_data_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> reset_test_data_with_http_info(idempotency_key)

```ruby
begin
  # Reset your test data
  data, status_code, headers = api_instance.reset_test_data_with_http_info(idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Growwer::ApiError => e
  puts "Error when calling TestHelpersApi->reset_test_data_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

nil (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## top_up_test_wallet

> <TopUpTestWallet200Response> top_up_test_wallet(idempotency_key, top_up_test_wallet_request)

Top up your test wallet

Test keys only. Credits your test wallet, the buyer wallet a test key spends from, with fictitious money: more than nothing and at most 10,000.00 EUR per call. It never touches your real wallets, takes no payment and issues no invoice; the movement shows in GET /wallets/buyer/transactions for a test key as a confirmed `deposit`. A live key gets 403 `test_mode_only`.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::TestHelpersApi.new
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
top_up_test_wallet_request = Growwer::TopUpTestWalletRequest.new({amount: Growwer::Money.new({amount: 12500, currency: 'EUR'})}) # TopUpTestWalletRequest | 

begin
  # Top up your test wallet
  result = api_instance.top_up_test_wallet(idempotency_key, top_up_test_wallet_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling TestHelpersApi->top_up_test_wallet: #{e}"
end
```

#### Using the top_up_test_wallet_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TopUpTestWallet200Response>, Integer, Hash)> top_up_test_wallet_with_http_info(idempotency_key, top_up_test_wallet_request)

```ruby
begin
  # Top up your test wallet
  data, status_code, headers = api_instance.top_up_test_wallet_with_http_info(idempotency_key, top_up_test_wallet_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TopUpTestWallet200Response>
rescue Growwer::ApiError => e
  puts "Error when calling TestHelpersApi->top_up_test_wallet_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **top_up_test_wallet_request** | [**TopUpTestWalletRequest**](TopUpTestWalletRequest.md) |  |  |

### Return type

[**TopUpTestWallet200Response**](TopUpTestWallet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

