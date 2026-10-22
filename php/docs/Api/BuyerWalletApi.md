# Growwer\Api\BuyerWalletApi



All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**downloadBuyerTransactionDocument()**](BuyerWalletApi.md#downloadBuyerTransactionDocument) | **GET** /api/v1/wallets/buyer/transactions/{id}/document | Download the document of a wallet movement |
| [**getBuyerWallet()**](BuyerWalletApi.md#getBuyerWallet) | **GET** /api/v1/wallets/buyer | Get your buyer wallet |
| [**getInvoicePdf()**](BuyerWalletApi.md#getInvoicePdf) | **GET** /api/v1/invoices/{id}/pdf | Download an invoice |
| [**listBuyerTransactions()**](BuyerWalletApi.md#listBuyerTransactions) | **GET** /api/v1/wallets/buyer/transactions | List your buyer wallet movements |
| [**listInvoices()**](BuyerWalletApi.md#listInvoices) | **GET** /api/v1/invoices | List your invoices |


## `downloadBuyerTransactionDocument()`

```php
downloadBuyerTransactionDocument($id): \SplFileObject
```

Download the document of a wallet movement

The document Growwer attached to a movement of your buyer wallet. 404 when the movement has none (`hasDocument` is false) or the file cannot be read.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\BuyerWalletApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->downloadBuyerTransactionDocument($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BuyerWalletApi->downloadBuyerTransactionDocument: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |

### Return type

**\SplFileObject**

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`, `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getBuyerWallet()`

```php
getBuyerWallet(): \Growwer\Api\Model\GetBuyerWallet200Response
```

Get your buyer wallet

The balance you buy with, and the page where you top it up.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\BuyerWalletApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getBuyerWallet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BuyerWalletApi->getBuyerWallet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\Growwer\Api\Model\GetBuyerWallet200Response**](../Model/GetBuyerWallet200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getInvoicePdf()`

```php
getInvoicePdf($id): \SplFileObject
```

Download an invoice

The PDF of one of your invoices.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\BuyerWalletApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->getInvoicePdf($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BuyerWalletApi->getInvoicePdf: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |

### Return type

**\SplFileObject**

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/pdf`, `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listBuyerTransactions()`

```php
listBuyerTransactions($limit, $offset): \Growwer\Api\Model\ListBuyerTransactions200Response
```

List your buyer wallet movements

Every movement of your buyer wallet, newest first: top-ups, order debits and their refunds, gifts and manual corrections.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\BuyerWalletApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$limit = 20; // int | Movements per page, 1 to 100.
$offset = 0; // int | Movements to skip.

try {
    $result = $apiInstance->listBuyerTransactions($limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BuyerWalletApi->listBuyerTransactions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**| Movements per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Movements to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListBuyerTransactions200Response**](../Model/ListBuyerTransactions200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listInvoices()`

```php
listInvoices($limit, $offset): \Growwer\Api\Model\ListInvoices200Response
```

List your invoices

The invoices of your top-ups, newest first.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\BuyerWalletApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$limit = 20; // int | Invoices per page, 1 to 100.
$offset = 0; // int | Invoices to skip.

try {
    $result = $apiInstance->listInvoices($limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BuyerWalletApi->listInvoices: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**| Invoices per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Invoices to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListInvoices200Response**](../Model/ListInvoices200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
