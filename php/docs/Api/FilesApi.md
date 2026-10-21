# Growwer\Api\FilesApi

Files

All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**uploadFile()**](FilesApi.md#uploadFile) | **POST** /api/v1/files | Upload a file |


## `uploadFile()`

```php
uploadFile($idempotency_key, $file): \Growwer\Api\Model\UploadFile201Response
```

Upload a file

Uploads a document (odt, doc, docx or txt, up to 8 MB) for a later write to reference by its `id`. A file belongs to you, can be used by one write, and expires 24 hours after it was uploaded; an expired or used file is answered like an unknown one.

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
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
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
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
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
