# Growwer::AccountApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_me**](AccountApi.md#get_me) | **GET** /api/v1/me | Your account |
| [**get_vocabulary**](AccountApi.md#get_vocabulary) | **GET** /api/v1/vocabulary | Codes and names |
| [**put_seller_holiday**](AccountApi.md#put_seller_holiday) | **PUT** /api/v1/seller/holiday | Set your holiday |


## get_me

> <GetMe200Response> get_me

Your account

Profile basics, the buyer and seller balances, whether your seller account is restricted, whether the catalogue is open to you, and whether you have a managed service.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::AccountApi.new

begin
  # Your account
  result = api_instance.get_me
  p result
rescue Growwer::ApiError => e
  puts "Error when calling AccountApi->get_me: #{e}"
end
```

#### Using the get_me_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetMe200Response>, Integer, Hash)> get_me_with_http_info

```ruby
begin
  # Your account
  data, status_code, headers = api_instance.get_me_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetMe200Response>
rescue Growwer::ApiError => e
  puts "Error when calling AccountApi->get_me_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMe200Response**](GetMe200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_vocabulary

> <GetVocabulary200Response> get_vocabulary

Codes and names

The countries, languages, topics, product types, link types and order states that other operations take and return. Names are in English.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::AccountApi.new

begin
  # Codes and names
  result = api_instance.get_vocabulary
  p result
rescue Growwer::ApiError => e
  puts "Error when calling AccountApi->get_vocabulary: #{e}"
end
```

#### Using the get_vocabulary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetVocabulary200Response>, Integer, Hash)> get_vocabulary_with_http_info

```ruby
begin
  # Codes and names
  data, status_code, headers = api_instance.get_vocabulary_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetVocabulary200Response>
rescue Growwer::ApiError => e
  puts "Error when calling AccountApi->get_vocabulary_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetVocabulary200Response**](GetVocabulary200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## put_seller_holiday

> <PutSellerHoliday200Response> put_seller_holiday(idempotency_key, put_seller_holiday_request)

Set your holiday

Starts, changes or ends your holiday, as the holiday settings of your profile page do. While you are on holiday your medias take no orders. `endDate` is the day your holiday ends, at 00:00 of that day in Growwer's server time, and must be later than now; leave it out, or send null, for a holiday you end yourself. Ending the holiday takes no `endDate`.  A holiday that already is as you ask is answered 200 without a change. A restricted seller account stays on holiday until the restriction is lifted, so any change is refused. Your holiday is also in GET /me.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::AccountApi.new
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
put_seller_holiday_request = Growwer::PutSellerHolidayRequest.new({on_holiday: false}) # PutSellerHolidayRequest | 

begin
  # Set your holiday
  result = api_instance.put_seller_holiday(idempotency_key, put_seller_holiday_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling AccountApi->put_seller_holiday: #{e}"
end
```

#### Using the put_seller_holiday_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PutSellerHoliday200Response>, Integer, Hash)> put_seller_holiday_with_http_info(idempotency_key, put_seller_holiday_request)

```ruby
begin
  # Set your holiday
  data, status_code, headers = api_instance.put_seller_holiday_with_http_info(idempotency_key, put_seller_holiday_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PutSellerHoliday200Response>
rescue Growwer::ApiError => e
  puts "Error when calling AccountApi->put_seller_holiday_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **put_seller_holiday_request** | [**PutSellerHolidayRequest**](PutSellerHolidayRequest.md) |  |  |

### Return type

[**PutSellerHoliday200Response**](PutSellerHoliday200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

