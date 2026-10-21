# Growwer::SavedFiltersApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**count_saved_filter_medias**](SavedFiltersApi.md#count_saved_filter_medias) | **GET** /api/v1/projects/{id}/saved-filters/{filterId}/media-count | Count the medias of a saved filter |
| [**create_saved_filter**](SavedFiltersApi.md#create_saved_filter) | **POST** /api/v1/projects/{id}/saved-filters | Save a filter |
| [**delete_saved_filter**](SavedFiltersApi.md#delete_saved_filter) | **DELETE** /api/v1/projects/{id}/saved-filters/{filterId} | Delete a saved filter |
| [**list_saved_filters**](SavedFiltersApi.md#list_saved_filters) | **GET** /api/v1/projects/{id}/saved-filters | List the saved filters of a project |


## count_saved_filter_medias

> <CountSavedFilterMedias200Response> count_saved_filter_medias(id, filter_id)

Count the medias of a saved filter

How many medias of the project's catalogue one of your saved filters matches: the `total` of GET /projects/{id}/medias with its `savedFilterId`. The number is cached for up to 24 hours, and it can differ from the count the web shows, which is not limited to the project's catalogue. A filter saved on the web that uses a filter the API does not support is refused with 422 `saved_filter_unsupported`.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SavedFiltersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The project.
filter_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The saved filter.

begin
  # Count the medias of a saved filter
  result = api_instance.count_saved_filter_medias(id, filter_id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SavedFiltersApi->count_saved_filter_medias: #{e}"
end
```

#### Using the count_saved_filter_medias_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CountSavedFilterMedias200Response>, Integer, Hash)> count_saved_filter_medias_with_http_info(id, filter_id)

```ruby
begin
  # Count the medias of a saved filter
  data, status_code, headers = api_instance.count_saved_filter_medias_with_http_info(id, filter_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CountSavedFilterMedias200Response>
rescue Growwer::ApiError => e
  puts "Error when calling SavedFiltersApi->count_saved_filter_medias_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The project. |  |
| **filter_id** | **String** | The saved filter. |  |

### Return type

[**CountSavedFilterMedias200Response**](CountSavedFilterMedias200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## create_saved_filter

> <SavedFilter> create_saved_filter(id, idempotency_key, create_saved_filter_request)

Save a filter

Saves a catalogue search of one of your projects, which then also appears on the web. `filters` takes the filter parameters of GET /projects/{id}/medias, and `source`, with the same values; lists may be JSON arrays and flags JSON booleans. With `notificationFrequency`, Growwer emails you new medias that match. A project has at most 100 saved filters and an account 500.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SavedFiltersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The project.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
create_saved_filter_request = Growwer::CreateSavedFilterRequest.new({name: 'name_example', filters: { key: 3.56}}) # CreateSavedFilterRequest | 

begin
  # Save a filter
  result = api_instance.create_saved_filter(id, idempotency_key, create_saved_filter_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SavedFiltersApi->create_saved_filter: #{e}"
end
```

#### Using the create_saved_filter_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SavedFilter>, Integer, Hash)> create_saved_filter_with_http_info(id, idempotency_key, create_saved_filter_request)

```ruby
begin
  # Save a filter
  data, status_code, headers = api_instance.create_saved_filter_with_http_info(id, idempotency_key, create_saved_filter_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SavedFilter>
rescue Growwer::ApiError => e
  puts "Error when calling SavedFiltersApi->create_saved_filter_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The project. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |
| **create_saved_filter_request** | [**CreateSavedFilterRequest**](CreateSavedFilterRequest.md) |  |  |

### Return type

[**SavedFilter**](SavedFilter.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_saved_filter

> delete_saved_filter(id, filter_id, idempotency_key)

Delete a saved filter

Deletes one of your saved filters of one of your projects, including one saved on the web. Its notifications stop.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SavedFiltersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The project.
filter_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The saved filter.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

begin
  # Delete a saved filter
  api_instance.delete_saved_filter(id, filter_id, idempotency_key)
rescue Growwer::ApiError => e
  puts "Error when calling SavedFiltersApi->delete_saved_filter: #{e}"
end
```

#### Using the delete_saved_filter_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_saved_filter_with_http_info(id, filter_id, idempotency_key)

```ruby
begin
  # Delete a saved filter
  data, status_code, headers = api_instance.delete_saved_filter_with_http_info(id, filter_id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Growwer::ApiError => e
  puts "Error when calling SavedFiltersApi->delete_saved_filter_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The project. |  |
| **filter_id** | **String** | The saved filter. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |

### Return type

nil (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_saved_filters

> <ListSavedFilters200Response> list_saved_filters(id)

List the saved filters of a project

Your saved filters of one of your projects, newest first, including those saved on the web. A project has at most 100. Apply one with `savedFilterId` on GET /projects/{id}/medias.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::SavedFiltersApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The project.

begin
  # List the saved filters of a project
  result = api_instance.list_saved_filters(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling SavedFiltersApi->list_saved_filters: #{e}"
end
```

#### Using the list_saved_filters_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListSavedFilters200Response>, Integer, Hash)> list_saved_filters_with_http_info(id)

```ruby
begin
  # List the saved filters of a project
  data, status_code, headers = api_instance.list_saved_filters_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListSavedFilters200Response>
rescue Growwer::ApiError => e
  puts "Error when calling SavedFiltersApi->list_saved_filters_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The project. |  |

### Return type

[**ListSavedFilters200Response**](ListSavedFilters200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

