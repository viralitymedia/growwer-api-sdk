# Growwer::FilesApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**upload_file**](FilesApi.md#upload_file) | **POST** /api/v1/files | Upload a file |


## upload_file

> <UploadFile201Response> upload_file(idempotency_key, file)

Upload a file

Uploads a document (odt, doc, docx or txt, up to 8 MB) for a later write to reference by its `id`. A file belongs to you, can be used by one write, and expires 24 hours after it was uploaded; an expired or used file is answered like an unknown one.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::FilesApi.new
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
file = File.new('/path/to/some/file') # File | 

begin
  # Upload a file
  result = api_instance.upload_file(idempotency_key, file)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling FilesApi->upload_file: #{e}"
end
```

#### Using the upload_file_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<UploadFile201Response>, Integer, Hash)> upload_file_with_http_info(idempotency_key, file)

```ruby
begin
  # Upload a file
  data, status_code, headers = api_instance.upload_file_with_http_info(idempotency_key, file)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <UploadFile201Response>
rescue Growwer::ApiError => e
  puts "Error when calling FilesApi->upload_file_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |
| **file** | **File** |  |  |

### Return type

[**UploadFile201Response**](UploadFile201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

