# Growwer\Api\SellerAccountApi



All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**putSellerHoliday()**](SellerAccountApi.md#putSellerHoliday) | **PUT** /api/v1/seller/holiday | Set your holiday |


## `putSellerHoliday()`

```php
putSellerHoliday($idempotency_key, $put_seller_holiday_request): \Growwer\Api\Model\PutSellerHoliday200Response
```

Set your holiday

Starts, changes or ends your holiday, as the holiday settings of your profile page do. While you are on holiday your medias take no orders. `endDate` is the day your holiday ends, at 00:00 of that day in Growwer's server time, and must be later than now; leave it out, or send null, for a holiday you end yourself. Ending the holiday takes no `endDate`.  A holiday that already is as you ask is answered 200 without a change. A restricted seller account stays on holiday until the restriction is lifted, so any change is refused. Your holiday is also in GET /me.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerAccountApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$put_seller_holiday_request = new \Growwer\Api\Model\PutSellerHolidayRequest(); // \Growwer\Api\Model\PutSellerHolidayRequest

try {
    $result = $apiInstance->putSellerHoliday($idempotency_key, $put_seller_holiday_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerAccountApi->putSellerHoliday: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **put_seller_holiday_request** | [**\Growwer\Api\Model\PutSellerHolidayRequest**](../Model/PutSellerHolidayRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\PutSellerHoliday200Response**](../Model/PutSellerHoliday200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
