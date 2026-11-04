# Growwer\Api\AccountApi

Your profile, balances and catalogue quota, and the codes and names the API uses.

All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getMe()**](AccountApi.md#getMe) | **GET** /api/v1/me | Your account |
| [**getVocabulary()**](AccountApi.md#getVocabulary) | **GET** /api/v1/vocabulary | Codes and names |


## `getMe()`

```php
getMe(): \Growwer\Api\Model\GetMe200Response
```

Your account

Profile basics, the buyer and seller balances, whether your seller account is restricted, whether the catalogue is open to you, whether you have a managed service, and whether the key you called with is live or test. A test key reads its test wallet as the buyer balance (1,000.00 EUR until test orders and top-ups move it), never your real balance, and no seller side.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\AccountApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getMe();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountApi->getMe: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\Growwer\Api\Model\GetMe200Response**](../Model/GetMe200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getVocabulary()`

```php
getVocabulary(): \Growwer\Api\Model\GetVocabulary200Response
```

Codes and names

The countries, languages, topics, product types, link types and order states that other operations take and return. Names are in English.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\AccountApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getVocabulary();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountApi->getVocabulary: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\Growwer\Api\Model\GetVocabulary200Response**](../Model/GetVocabulary200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
