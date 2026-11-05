# Growwer\Api\TestHelpersApi



All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**advanceTestOrder()**](TestHelpersApi.md#advanceTestOrder) | **POST** /api/v1/test-helpers/orders/{id}/advance | Advance a test order |
| [**resetTestData()**](TestHelpersApi.md#resetTestData) | **POST** /api/v1/test-helpers/reset | Reset your test data |
| [**topUpTestWallet()**](TestHelpersApi.md#topUpTestWallet) | **POST** /api/v1/test-helpers/wallet/top-up | Top up your test wallet |


## `advanceTestOrder()`

```php
advanceTestOrder($id, $idempotency_key, $advance_test_order_request): \Growwer\Api\Model\Order
```

Advance a test order

Test keys only. Moves one of your test orders at once to `to`, without waiting for the simulated seller: `accepted` or `rejected` (by the seller, from `pending_acceptance`), `draft_delivered` (the sample draft, from `pending_draft` or `pending_draft_update`), `draft_update_requested` (as if you sent the draft back, from `pending_draft_review`), `published` (delivered for your review, from `pending_order_delivery`, `scheduled` or `pending_order_delivery_update`), `update_requested` (as if you sent the delivery back, from `pending_order_delivery_review`) or `cancelled_by_growwer` (from any state that is not finished). The order and your test wallet change as that move changes them live, a rejection or a cancellation refunding the price, and the simulated seller carries on from the new state. A post with a future `scheduledPublicationDate` waits in `scheduled` until that date once the simulated seller delivers it; `published` skips the wait. A target its state does not allow answers 409 `invalid_transition` with the targets it allows. A live key gets 403 `test_mode_only`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\TestHelpersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$advance_test_order_request = new \Growwer\Api\Model\AdvanceTestOrderRequest(); // \Growwer\Api\Model\AdvanceTestOrderRequest

try {
    $result = $apiInstance->advanceTestOrder($id, $idempotency_key, $advance_test_order_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TestHelpersApi->advanceTestOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **advance_test_order_request** | [**\Growwer\Api\Model\AdvanceTestOrderRequest**](../Model/AdvanceTestOrderRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\Order**](../Model/Order.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `resetTestData()`

```php
resetTestData($idempotency_key)
```

Reset your test data

Test keys only. Deletes your test projects, orders and uploaded test files, and returns your test wallet to its opening balance of 1,000.00 EUR with no movements. Your API keys and webhook subscriptions stay, and nothing of your live account changes. It takes no body. A live key gets 403 `test_mode_only`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\TestHelpersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

try {
    $apiInstance->resetTestData($idempotency_key);
} catch (Exception $e) {
    echo 'Exception when calling TestHelpersApi->resetTestData: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |

### Return type

void (empty response body)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `topUpTestWallet()`

```php
topUpTestWallet($idempotency_key, $top_up_test_wallet_request): \Growwer\Api\Model\TopUpTestWallet200Response
```

Top up your test wallet

Test keys only. Credits your test wallet, the buyer wallet a test key spends from, with fictitious money: more than nothing and at most 10,000.00 EUR per call. It never touches your real wallets, takes no payment and issues no invoice; the movement shows in GET /wallets/buyer/transactions for a test key as a confirmed `deposit`. A live key gets 403 `test_mode_only`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\TestHelpersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$top_up_test_wallet_request = new \Growwer\Api\Model\TopUpTestWalletRequest(); // \Growwer\Api\Model\TopUpTestWalletRequest

try {
    $result = $apiInstance->topUpTestWallet($idempotency_key, $top_up_test_wallet_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TestHelpersApi->topUpTestWallet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **top_up_test_wallet_request** | [**\Growwer\Api\Model\TopUpTestWalletRequest**](../Model/TopUpTestWalletRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\TopUpTestWallet200Response**](../Model/TopUpTestWallet200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
