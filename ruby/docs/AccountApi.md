# Growwer::AccountApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_me**](AccountApi.md#get_me) | **GET** /api/v1/me | Your account |
| [**get_vocabulary**](AccountApi.md#get_vocabulary) | **GET** /api/v1/vocabulary | Codes and names |


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

