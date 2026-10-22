# Growwer\Api\SellerWalletApi



All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**downloadSellerTransactionDocument()**](SellerWalletApi.md#downloadSellerTransactionDocument) | **GET** /api/v1/wallets/seller/transactions/{id}/document | Download the document of a seller wallet movement |
| [**downloadWithdrawalInvoice()**](SellerWalletApi.md#downloadWithdrawalInvoice) | **GET** /api/v1/withdrawals/{id}/invoice | Download the invoice of a withdrawal |
| [**getSellerWallet()**](SellerWalletApi.md#getSellerWallet) | **GET** /api/v1/wallets/seller | Get your seller wallet |
| [**listSellerTransactions()**](SellerWalletApi.md#listSellerTransactions) | **GET** /api/v1/wallets/seller/transactions | List your seller wallet movements |
| [**listWithdrawals()**](SellerWalletApi.md#listWithdrawals) | **GET** /api/v1/withdrawals | List your withdrawals |


## `downloadSellerTransactionDocument()`

```php
downloadSellerTransactionDocument($id): \SplFileObject
```

Download the document of a seller wallet movement

The document Growwer attached to a movement of your seller wallet. 404 when the movement has none (`hasDocument` is false) or the file cannot be read.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerWalletApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->downloadSellerTransactionDocument($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerWalletApi->downloadSellerTransactionDocument: ', $e->getMessage(), PHP_EOL;
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

## `downloadWithdrawalInvoice()`

```php
downloadWithdrawalInvoice($id): \SplFileObject
```

Download the invoice of a withdrawal

The invoice you uploaded for one of your withdrawals, named `withdrawal-{id}-invoice.pdf`. 404 when the withdrawal has none (`hasInvoice` is false); 503 `storage_unavailable` when the file cannot be read right now.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerWalletApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->downloadWithdrawalInvoice($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerWalletApi->downloadWithdrawalInvoice: ', $e->getMessage(), PHP_EOL;
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

## `getSellerWallet()`

```php
getSellerWallet(): \Growwer\Api\Model\GetSellerWallet200Response
```

Get your seller wallet

What your sales have earned: the balance you can withdraw now and what is held until orders settle. `restricted` is true while your seller account is restricted; the reason is not published here, and support can tell you more.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerWalletApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getSellerWallet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerWalletApi->getSellerWallet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\Growwer\Api\Model\GetSellerWallet200Response**](../Model/GetSellerWallet200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listSellerTransactions()`

```php
listSellerTransactions($limit, $offset): \Growwer\Api\Model\ListSellerTransactions200Response
```

List your seller wallet movements

Every movement of your seller wallet, newest first: earnings from orders, withdrawals and manual corrections. An earning names its order (`orderId`) and a withdrawal its request (`withdrawalId`).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerWalletApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$limit = 20; // int | Movements per page, 1 to 100.
$offset = 0; // int | Movements to skip.

try {
    $result = $apiInstance->listSellerTransactions($limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerWalletApi->listSellerTransactions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**| Movements per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Movements to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListSellerTransactions200Response**](../Model/ListSellerTransactions200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listWithdrawals()`

```php
listWithdrawals($state, $limit, $offset): \Growwer\Api\Model\ListWithdrawals200Response
```

List your withdrawals

The withdrawals you requested from your seller wallet, newest first. Requesting a withdrawal is not available through the API; use the seller wallet page.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerWalletApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$state = started; // string | Only the withdrawals in one of these states, comma-separated: `started`, `approved`, `rejected`. An unknown state is refused with 422.
$limit = 20; // int | Withdrawals per page, 1 to 100.
$offset = 0; // int | Withdrawals to skip.

try {
    $result = $apiInstance->listWithdrawals($state, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerWalletApi->listWithdrawals: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **state** | **string**| Only the withdrawals in one of these states, comma-separated: &#x60;started&#x60;, &#x60;approved&#x60;, &#x60;rejected&#x60;. An unknown state is refused with 422. | [optional] |
| **limit** | **int**| Withdrawals per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Withdrawals to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListWithdrawals200Response**](../Model/ListWithdrawals200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
