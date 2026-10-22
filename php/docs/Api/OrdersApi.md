# Growwer\Api\OrdersApi

Orders

All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**approveOrder()**](OrdersApi.md#approveOrder) | **POST** /api/v1/orders/{id}/approve | Approve an order&#39;s delivery |
| [**approveOrderDraft()**](OrdersApi.md#approveOrderDraft) | **POST** /api/v1/orders/{id}/approve-draft | Approve a draft |
| [**cancelOrder()**](OrdersApi.md#cancelOrder) | **POST** /api/v1/orders/{id}/cancel | Cancel an order |
| [**createOrder()**](OrdersApi.md#createOrder) | **POST** /api/v1/orders | Place an order |
| [**downloadOrderBriefing()**](OrdersApi.md#downloadOrderBriefing) | **GET** /api/v1/orders/{id}/briefing | Download the draft you attached to an order |
| [**downloadOrderDraft()**](OrdersApi.md#downloadOrderDraft) | **GET** /api/v1/orders/{id}/draft | Download the draft of an order |
| [**estimateOrder()**](OrdersApi.md#estimateOrder) | **POST** /api/v1/orders/estimate | Estimate an order |
| [**getOrder()**](OrdersApi.md#getOrder) | **GET** /api/v1/orders/{id} | Get an order |
| [**listOrders()**](OrdersApi.md#listOrders) | **GET** /api/v1/orders | List your orders |
| [**requestOrderDraftUpdate()**](OrdersApi.md#requestOrderDraftUpdate) | **POST** /api/v1/orders/{id}/request-draft-update | Request changes to a draft |
| [**requestOrderUpdate()**](OrdersApi.md#requestOrderUpdate) | **POST** /api/v1/orders/{id}/request-update | Request changes to a delivery |


## `approveOrder()`

```php
approveOrder($id, $idempotency_key): \Growwer\Api\Model\Order
```

Approve an order's delivery

Approves the delivery of an order whose `pendingAction` is yours to review the delivery, as the web does. The order finishes and the seller is paid. It takes no body.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

try {
    $result = $apiInstance->approveOrder($id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->approveOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |

### Return type

[**\Growwer\Api\Model\Order**](../Model/Order.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `approveOrderDraft()`

```php
approveOrderDraft($id, $idempotency_key): \Growwer\Api\Model\Order
```

Approve a draft

Approves the draft of a post order whose `pendingAction` is yours to review the draft (GET /orders/{id}/draft downloads it), as the web does. The seller then publishes it. It takes no body.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

try {
    $result = $apiInstance->approveOrderDraft($id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->approveOrderDraft: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |

### Return type

[**\Growwer\Api\Model\Order**](../Model/Order.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `cancelOrder()`

```php
cancelOrder($id, $idempotency_key, $order_action_reason): \Growwer\Api\Model\Order
```

Cancel an order

Cancels an order the seller has not accepted yet (`state` `pending_acceptance`), as the web does. Its price returns to your wallet's available balance, and the seller is told your reason.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$order_action_reason = new \Growwer\Api\Model\OrderActionReason(); // \Growwer\Api\Model\OrderActionReason

try {
    $result = $apiInstance->cancelOrder($id, $idempotency_key, $order_action_reason);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->cancelOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **order_action_reason** | [**\Growwer\Api\Model\OrderActionReason**](../Model/OrderActionReason.md)|  | |

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

## `createOrder()`

```php
createOrder($idempotency_key, $order_create_request): \Growwer\Api\Model\Order
```

Place an order

Places an order on a media for one of your projects and pays its price from your wallet's available balance, as ordering on the web does. Estimate the order first (POST /orders/estimate) and send the price it answers as `expectedPrice`: the order is placed only at that price.  Placing the same order (same project, media, type and price) again within 5 seconds of one still in progress is refused with `duplicate_order`. Its `details.orderId` is the earlier order, or null when that order has finished or was deleted since.  A proposed draft (`proposedDraftFileId`, from POST /files) is used up when the order is placed. If the order is then refused because another request changed your balance, the media or its price, or placed the same order, the file is used up all the same and the refusal's message says so: upload it again before retrying.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$order_create_request = new \Growwer\Api\Model\OrderCreateRequest(); // \Growwer\Api\Model\OrderCreateRequest

try {
    $result = $apiInstance->createOrder($idempotency_key, $order_create_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->createOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **order_create_request** | [**\Growwer\Api\Model\OrderCreateRequest**](../Model/OrderCreateRequest.md)|  | |

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

## `downloadOrderBriefing()`

```php
downloadOrderBriefing($id): \SplFileObject
```

Download the draft you attached to an order

The file you attached to the briefing of a post order. 404 when the order has none (`briefing.hasProposedDraft` is false) or the file cannot be read.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->downloadOrderBriefing($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->downloadOrderBriefing: ', $e->getMessage(), PHP_EOL;
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

## `downloadOrderDraft()`

```php
downloadOrderDraft($id): \SplFileObject
```

Download the draft of an order

The file of the current draft of a post order. 404 when the order has no draft file (`draft.hasFile` is false) or the file cannot be read.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->downloadOrderDraft($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->downloadOrderDraft: ', $e->getMessage(), PHP_EOL;
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

## `estimateOrder()`

```php
estimateOrder($order_estimate_request): \Growwer\Api\Model\OrderEstimate
```

Estimate an order

Checks and prices the order POST /orders would place with the same body, without `expectedPrice`, and compares the price with your wallet's available balance. Nothing is placed, charged or used up, so a read-only key may call it and it takes no Idempotency-Key. Send the `price` it answers as `expectedPrice` when you place the order.  The estimate is refused for the same reasons as the order itself, except a balance that does not cover the price: that is answered here with `sufficientBalance: false` and the `missing` amount.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$order_estimate_request = new \Growwer\Api\Model\OrderEstimateRequest(); // \Growwer\Api\Model\OrderEstimateRequest

try {
    $result = $apiInstance->estimateOrder($order_estimate_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->estimateOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **order_estimate_request** | [**\Growwer\Api\Model\OrderEstimateRequest**](../Model/OrderEstimateRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\OrderEstimate**](../Model/OrderEstimate.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getOrder()`

```php
getOrder($id): \Growwer\Api\Model\Order
```

Get an order

One order you bought, with its briefing, its draft and its state history.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->getOrder($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->getOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |

### Return type

[**\Growwer\Api\Model\Order**](../Model/Order.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listOrders()`

```php
listOrders($project_id, $media_id, $state, $updated_since, $sort, $limit, $offset): \Growwer\Api\Model\ListOrders200Response
```

List your orders

The orders you bought, newest first by default. To follow your orders, poll with `sort=updatedAt` and `updatedSince` set to the `updatedAt` of the last order you saw: an order moves to the end of that list each time it changes state.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$project_id = 'project_id_example'; // string | Only the orders of this project of yours.
$media_id = 'media_id_example'; // string | Only the orders on this media.
$state = pending_acceptance,pending_order_delivery; // string | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones.
$updated_since = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Only the orders whose `updatedAt` is at or after this instant, an ISO-8601 date-time with its offset (send `+` as `%2B`).
$sort = '-createdAt'; // string | `-createdAt`, newest first, or `updatedAt`, least recently changed first. Orders of the same instant come in id order.
$limit = 20; // int | Orders per page, 1 to 100.
$offset = 0; // int | Orders to skip.

try {
    $result = $apiInstance->listOrders($project_id, $media_id, $state, $updated_since, $sort, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->listOrders: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**| Only the orders of this project of yours. | [optional] |
| **media_id** | **string**| Only the orders on this media. | [optional] |
| **state** | **string**| Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones. | [optional] |
| **updated_since** | **\DateTime**| Only the orders whose &#x60;updatedAt&#x60; is at or after this instant, an ISO-8601 date-time with its offset (send &#x60;+&#x60; as &#x60;%2B&#x60;). | [optional] |
| **sort** | **string**| &#x60;-createdAt&#x60;, newest first, or &#x60;updatedAt&#x60;, least recently changed first. Orders of the same instant come in id order. | [optional] [default to &#39;-createdAt&#39;] |
| **limit** | **int**| Orders per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Orders to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListOrders200Response**](../Model/ListOrders200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `requestOrderDraftUpdate()`

```php
requestOrderDraftUpdate($id, $idempotency_key, $order_action_reason): \Growwer\Api\Model\Order
```

Request changes to a draft

Asks the seller to change the draft of a post order whose `pendingAction` is yours to review the draft, as the web does. The seller is told your reason.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$order_action_reason = new \Growwer\Api\Model\OrderActionReason(); // \Growwer\Api\Model\OrderActionReason

try {
    $result = $apiInstance->requestOrderDraftUpdate($id, $idempotency_key, $order_action_reason);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->requestOrderDraftUpdate: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **order_action_reason** | [**\Growwer\Api\Model\OrderActionReason**](../Model/OrderActionReason.md)|  | |

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

## `requestOrderUpdate()`

```php
requestOrderUpdate($id, $idempotency_key, $order_action_reason): \Growwer\Api\Model\Order
```

Request changes to a delivery

Asks the seller to change the delivery of an order whose `pendingAction` is yours to review the delivery, as the web does. The seller is told your reason.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$order_action_reason = new \Growwer\Api\Model\OrderActionReason(); // \Growwer\Api\Model\OrderActionReason

try {
    $result = $apiInstance->requestOrderUpdate($id, $idempotency_key, $order_action_reason);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->requestOrderUpdate: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **order_action_reason** | [**\Growwer\Api\Model\OrderActionReason**](../Model/OrderActionReason.md)|  | |

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
