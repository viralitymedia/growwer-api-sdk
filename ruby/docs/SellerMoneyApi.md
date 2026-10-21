# Growwer::SellerMoneyApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**download_seller_transaction_document**](SellerMoneyApi.md#download_seller_transaction_document) | **GET** /api/v1/wallets/seller/transactions/{id}/document | Download the document of a seller wallet movement |
| [**download_withdrawal_invoice**](SellerMoneyApi.md#download_withdrawal_invoice) | **GET** /api/v1/withdrawals/{id}/invoice | Download the invoice of a withdrawal |
| [**get_seller_wallet**](SellerMoneyApi.md#get_seller_wallet) | **GET** /api/v1/wallets/seller | Get your seller wallet |
| [**list_seller_transactions**](SellerMoneyApi.md#list_seller_transactions) | **GET** /api/v1/wallets/seller/transactions | List your seller wallet movements |
| [**list_withdrawals**](SellerMoneyApi.md#list_withdrawals) | **GET** /api/v1/withdrawals | List your withdrawals |


## download_seller_transaction_document

> File download_seller_transaction_document(id)

Download the document of a seller wallet movement

The document Growwer attached to a movement of your seller wallet. 404 when the movement has none (`hasDocument` is false) or the file cannot be read.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerMoneyApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Download the document of a seller wallet movement
  result = api_instance.download_seller_transaction_document(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerMoneyApi->download_seller_transaction_document: #{e}"
end
```

#### Using the download_seller_transaction_document_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(File, Integer, Hash)> download_seller_transaction_document_with_http_info(id)

```ruby
begin
  # Download the document of a seller wallet movement
  data, status_code, headers = api_instance.download_seller_transaction_document_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => File
rescue Growwer::ApiError => e
  puts "Error when calling SellerMoneyApi->download_seller_transaction_document_with_http_info: #{e}"
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


## download_withdrawal_invoice

> File download_withdrawal_invoice(id)

Download the invoice of a withdrawal

The invoice you uploaded for one of your withdrawals, named `withdrawal-{id}-invoice.pdf`. 404 when the withdrawal has none (`hasInvoice` is false); 503 `storage_unavailable` when the file cannot be read right now.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerMoneyApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Download the invoice of a withdrawal
  result = api_instance.download_withdrawal_invoice(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerMoneyApi->download_withdrawal_invoice: #{e}"
end
```

#### Using the download_withdrawal_invoice_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(File, Integer, Hash)> download_withdrawal_invoice_with_http_info(id)

```ruby
begin
  # Download the invoice of a withdrawal
  data, status_code, headers = api_instance.download_withdrawal_invoice_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => File
rescue Growwer::ApiError => e
  puts "Error when calling SellerMoneyApi->download_withdrawal_invoice_with_http_info: #{e}"
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


## get_seller_wallet

> <GetSellerWallet200Response> get_seller_wallet

Get your seller wallet

What your sales have earned: the balance you can withdraw now and what is held until orders settle. `restricted` is true while your seller account is restricted; the reason is not published here, and support can tell you more.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerMoneyApi.new

begin
  # Get your seller wallet
  result = api_instance.get_seller_wallet
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerMoneyApi->get_seller_wallet: #{e}"
end
```

#### Using the get_seller_wallet_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetSellerWallet200Response>, Integer, Hash)> get_seller_wallet_with_http_info

```ruby
begin
  # Get your seller wallet
  data, status_code, headers = api_instance.get_seller_wallet_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetSellerWallet200Response>
rescue Growwer::ApiError => e
  puts "Error when calling SellerMoneyApi->get_seller_wallet_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSellerWallet200Response**](GetSellerWallet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_seller_transactions

> <ListSellerTransactions200Response> list_seller_transactions(opts)

List your seller wallet movements

Every movement of your seller wallet, newest first: earnings from orders, withdrawals and manual corrections. An earning names its order (`orderId`) and a withdrawal its request (`withdrawalId`).

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerMoneyApi.new
opts = {
  limit: 56, # Integer | Movements per page, 1 to 100.
  offset: 56 # Integer | Movements to skip.
}

begin
  # List your seller wallet movements
  result = api_instance.list_seller_transactions(opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerMoneyApi->list_seller_transactions: #{e}"
end
```

#### Using the list_seller_transactions_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListSellerTransactions200Response>, Integer, Hash)> list_seller_transactions_with_http_info(opts)

```ruby
begin
  # List your seller wallet movements
  data, status_code, headers = api_instance.list_seller_transactions_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListSellerTransactions200Response>
rescue Growwer::ApiError => e
  puts "Error when calling SellerMoneyApi->list_seller_transactions_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **limit** | **Integer** | Movements per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Movements to skip. | [optional][default to 0] |

### Return type

[**ListSellerTransactions200Response**](ListSellerTransactions200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_withdrawals

> <ListWithdrawals200Response> list_withdrawals(opts)

List your withdrawals

The withdrawals you requested from your seller wallet, newest first. Requesting a withdrawal is not available through the API; use the seller wallet page.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SellerMoneyApi.new
opts = {
  state: 'started', # String | Only the withdrawals in one of these states, comma-separated: `started`, `approved`, `rejected`. An unknown state is refused with 422.
  limit: 56, # Integer | Withdrawals per page, 1 to 100.
  offset: 56 # Integer | Withdrawals to skip.
}

begin
  # List your withdrawals
  result = api_instance.list_withdrawals(opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SellerMoneyApi->list_withdrawals: #{e}"
end
```

#### Using the list_withdrawals_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListWithdrawals200Response>, Integer, Hash)> list_withdrawals_with_http_info(opts)

```ruby
begin
  # List your withdrawals
  data, status_code, headers = api_instance.list_withdrawals_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListWithdrawals200Response>
rescue Growwer::ApiError => e
  puts "Error when calling SellerMoneyApi->list_withdrawals_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **state** | **String** | Only the withdrawals in one of these states, comma-separated: &#x60;started&#x60;, &#x60;approved&#x60;, &#x60;rejected&#x60;. An unknown state is refused with 422. | [optional] |
| **limit** | **Integer** | Withdrawals per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Withdrawals to skip. | [optional][default to 0] |

### Return type

[**ListWithdrawals200Response**](ListWithdrawals200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

