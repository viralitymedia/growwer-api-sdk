# Growwer::BuyerWalletApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**download_buyer_transaction_document**](BuyerWalletApi.md#download_buyer_transaction_document) | **GET** /api/v1/wallets/buyer/transactions/{id}/document | Download the document of a wallet movement |
| [**get_buyer_wallet**](BuyerWalletApi.md#get_buyer_wallet) | **GET** /api/v1/wallets/buyer | Get your buyer wallet |
| [**get_invoice_pdf**](BuyerWalletApi.md#get_invoice_pdf) | **GET** /api/v1/invoices/{id}/pdf | Download an invoice |
| [**list_buyer_transactions**](BuyerWalletApi.md#list_buyer_transactions) | **GET** /api/v1/wallets/buyer/transactions | List your buyer wallet movements |
| [**list_invoices**](BuyerWalletApi.md#list_invoices) | **GET** /api/v1/invoices | List your invoices |


## download_buyer_transaction_document

> File download_buyer_transaction_document(id)

Download the document of a wallet movement

The document Growwer attached to a movement of your buyer wallet. 404 when the movement has none (`hasDocument` is false) or the file cannot be read.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::BuyerWalletApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Download the document of a wallet movement
  result = api_instance.download_buyer_transaction_document(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling BuyerWalletApi->download_buyer_transaction_document: #{e}"
end
```

#### Using the download_buyer_transaction_document_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(File, Integer, Hash)> download_buyer_transaction_document_with_http_info(id)

```ruby
begin
  # Download the document of a wallet movement
  data, status_code, headers = api_instance.download_buyer_transaction_document_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => File
rescue Growwer::ApiError => e
  puts "Error when calling BuyerWalletApi->download_buyer_transaction_document_with_http_info: #{e}"
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


## get_buyer_wallet

> <GetBuyerWallet200Response> get_buyer_wallet

Get your buyer wallet

The balance you buy with, and the page where you top it up.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::BuyerWalletApi.new

begin
  # Get your buyer wallet
  result = api_instance.get_buyer_wallet
  p result
rescue Growwer::ApiError => e
  puts "Error when calling BuyerWalletApi->get_buyer_wallet: #{e}"
end
```

#### Using the get_buyer_wallet_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetBuyerWallet200Response>, Integer, Hash)> get_buyer_wallet_with_http_info

```ruby
begin
  # Get your buyer wallet
  data, status_code, headers = api_instance.get_buyer_wallet_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetBuyerWallet200Response>
rescue Growwer::ApiError => e
  puts "Error when calling BuyerWalletApi->get_buyer_wallet_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetBuyerWallet200Response**](GetBuyerWallet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_invoice_pdf

> File get_invoice_pdf(id)

Download an invoice

The PDF of one of your invoices.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::BuyerWalletApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Download an invoice
  result = api_instance.get_invoice_pdf(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling BuyerWalletApi->get_invoice_pdf: #{e}"
end
```

#### Using the get_invoice_pdf_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(File, Integer, Hash)> get_invoice_pdf_with_http_info(id)

```ruby
begin
  # Download an invoice
  data, status_code, headers = api_instance.get_invoice_pdf_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => File
rescue Growwer::ApiError => e
  puts "Error when calling BuyerWalletApi->get_invoice_pdf_with_http_info: #{e}"
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
- **Accept**: application/pdf, application/json


## list_buyer_transactions

> <ListBuyerTransactions200Response> list_buyer_transactions(opts)

List your buyer wallet movements

Every movement of your buyer wallet, newest first: top-ups, order debits and their refunds, gifts and manual corrections.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::BuyerWalletApi.new
opts = {
  limit: 56, # Integer | Movements per page, 1 to 100.
  offset: 56 # Integer | Movements to skip.
}

begin
  # List your buyer wallet movements
  result = api_instance.list_buyer_transactions(opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling BuyerWalletApi->list_buyer_transactions: #{e}"
end
```

#### Using the list_buyer_transactions_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListBuyerTransactions200Response>, Integer, Hash)> list_buyer_transactions_with_http_info(opts)

```ruby
begin
  # List your buyer wallet movements
  data, status_code, headers = api_instance.list_buyer_transactions_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListBuyerTransactions200Response>
rescue Growwer::ApiError => e
  puts "Error when calling BuyerWalletApi->list_buyer_transactions_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **limit** | **Integer** | Movements per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Movements to skip. | [optional][default to 0] |

### Return type

[**ListBuyerTransactions200Response**](ListBuyerTransactions200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_invoices

> <ListInvoices200Response> list_invoices(opts)

List your invoices

The invoices of your top-ups, newest first.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::BuyerWalletApi.new
opts = {
  limit: 56, # Integer | Invoices per page, 1 to 100.
  offset: 56 # Integer | Invoices to skip.
}

begin
  # List your invoices
  result = api_instance.list_invoices(opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling BuyerWalletApi->list_invoices: #{e}"
end
```

#### Using the list_invoices_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListInvoices200Response>, Integer, Hash)> list_invoices_with_http_info(opts)

```ruby
begin
  # List your invoices
  data, status_code, headers = api_instance.list_invoices_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListInvoices200Response>
rescue Growwer::ApiError => e
  puts "Error when calling BuyerWalletApi->list_invoices_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **limit** | **Integer** | Invoices per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Invoices to skip. | [optional][default to 0] |

### Return type

[**ListInvoices200Response**](ListInvoices200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

