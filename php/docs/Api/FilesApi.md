# Growwer\Api\FilesApi

Upload the documents that a later write, such as an order&#39;s briefing, references.

All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**uploadFile()**](FilesApi.md#uploadFile) | **POST** /api/v1/files | Upload a file |


## `uploadFile()`

```php
uploadFile($idempotency_key, $file): \Growwer\Api\Model\UploadFile201Response
```

Upload a file

Uploads a document (odt, doc, docx or txt, up to 8 MB) for a later write to reference by its `id`. A file belongs to you, can be used by one write, and expires 24 hours after it was uploaded; an expired or used file is answered like an unknown one.  You may hold 20 files that no write has used yet and that have not expired. Past them it answers 429 `file_limit_reached`, with `details.limit` the number you may hold and `Retry-After` the seconds until the first of them expires; using one of them in a write frees its place at once. A file refused as invalid (422) is refused before they are counted, and a refused upload stores nothing.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\FilesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$file = '/path/to/file.txt'; // \SplFileObject

try {
    $result = $apiInstance->uploadFile($idempotency_key, $file);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FilesApi->uploadFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **file** | **\SplFileObject****\SplFileObject**|  | |

### Return type

[**\Growwer\Api\Model\UploadFile201Response**](../Model/UploadFile201Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
