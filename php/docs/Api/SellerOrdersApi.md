# Growwer\Api\SellerOrdersApi



All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**acceptSellerOrder()**](SellerOrdersApi.md#acceptSellerOrder) | **POST** /api/v1/seller/orders/{id}/accept | Accept an order |
| [**deliverSellerOrder()**](SellerOrdersApi.md#deliverSellerOrder) | **POST** /api/v1/seller/orders/{id}/deliver | Deliver an order |
| [**deliverSellerOrderDraft()**](SellerOrdersApi.md#deliverSellerOrderDraft) | **POST** /api/v1/seller/orders/{id}/deliver-draft | Deliver a draft |
| [**deliverSellerOrderDraftUpdate()**](SellerOrdersApi.md#deliverSellerOrderDraftUpdate) | **POST** /api/v1/seller/orders/{id}/deliver-draft-update | Deliver a draft update |
| [**deliverSellerOrderUpdate()**](SellerOrdersApi.md#deliverSellerOrderUpdate) | **POST** /api/v1/seller/orders/{id}/deliver-update | Deliver an update |
| [**downloadSellerOrderBriefing()**](SellerOrdersApi.md#downloadSellerOrderBriefing) | **GET** /api/v1/seller/orders/{id}/briefing | Download the draft the buyer attached to an order |
| [**downloadSellerOrderDraft()**](SellerOrdersApi.md#downloadSellerOrderDraft) | **GET** /api/v1/seller/orders/{id}/draft | Download the draft of an order you sell |
| [**getSellerOrder()**](SellerOrdersApi.md#getSellerOrder) | **GET** /api/v1/seller/orders/{id} | Get an order you sell |
| [**listSellerOrders()**](SellerOrdersApi.md#listSellerOrders) | **GET** /api/v1/seller/orders | List the orders you sell |
| [**refuteSellerOrderDraftUpdate()**](SellerOrdersApi.md#refuteSellerOrderDraftUpdate) | **POST** /api/v1/seller/orders/{id}/refute-draft-update | Refuse a draft update |
| [**refuteSellerOrderUpdate()**](SellerOrdersApi.md#refuteSellerOrderUpdate) | **POST** /api/v1/seller/orders/{id}/refute-update | Refuse an update |
| [**rejectSellerOrder()**](SellerOrdersApi.md#rejectSellerOrder) | **POST** /api/v1/seller/orders/{id}/reject | Reject an order |


## `acceptSellerOrder()`

```php
acceptSellerOrder($id, $idempotency_key): \Growwer\Api\Model\SellerOrder
```

Accept an order

Accepts an order placed on one of your medias (`state` `pending_acceptance`), as the web does. A post order whose draft is still to be written (by you or by Growwer) moves to `pending_draft`; any other order moves to `pending_order_delivery`. The buyer is told. Takes no body.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

try {
    $result = $apiInstance->acceptSellerOrder($id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->acceptSellerOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |

### Return type

[**\Growwer\Api\Model\SellerOrder**](../Model/SellerOrder.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deliverSellerOrder()`

```php
deliverSellerOrder($id, $idempotency_key, $seller_order_post_delivery): \Growwer\Api\Model\SellerOrder
```

Deliver an order

Delivers an order placed on one of your medias (`state` `pending_order_delivery`), as the web does. A post order takes the URL of the published post and the confirmation of its publication date; a link addition order takes no body, and any field is refused. The order moves to `pending_order_delivery_review` and the buyer is asked to review it, or, for a post order whose scheduled publication date is still to come, to `scheduled` without telling the buyer yet. The URL is checked to be a URL only, as the web does.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
$seller_order_post_delivery = new \Growwer\Api\Model\SellerOrderPostDelivery(); // \Growwer\Api\Model\SellerOrderPostDelivery

try {
    $result = $apiInstance->deliverSellerOrder($id, $idempotency_key, $seller_order_post_delivery);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->deliverSellerOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **seller_order_post_delivery** | [**\Growwer\Api\Model\SellerOrderPostDelivery**](../Model/SellerOrderPostDelivery.md)|  | [optional] |

### Return type

[**\Growwer\Api\Model\SellerOrder**](../Model/SellerOrder.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deliverSellerOrderDraft()`

```php
deliverSellerOrderDraft($id, $idempotency_key, $seller_order_draft_file): \Growwer\Api\Model\SellerOrder
```

Deliver a draft

Delivers the draft of a post order placed on one of your medias whose draft you write (`state` `pending_draft`), as the web does, from a file you uploaded with POST /files. The order moves to `pending_draft_review` when the buyer reviews drafts, otherwise to `pending_order_delivery`. The file is used up once the draft is delivered; a refused request leaves it usable.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
$seller_order_draft_file = new \Growwer\Api\Model\SellerOrderDraftFile(); // \Growwer\Api\Model\SellerOrderDraftFile

try {
    $result = $apiInstance->deliverSellerOrderDraft($id, $idempotency_key, $seller_order_draft_file);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->deliverSellerOrderDraft: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **seller_order_draft_file** | [**\Growwer\Api\Model\SellerOrderDraftFile**](../Model/SellerOrderDraftFile.md)|  | |

### Return type

[**\Growwer\Api\Model\SellerOrder**](../Model/SellerOrder.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deliverSellerOrderDraftUpdate()`

```php
deliverSellerOrderDraftUpdate($id, $idempotency_key, $seller_order_draft_file): \Growwer\Api\Model\SellerOrder
```

Deliver a draft update

Delivers the draft update the buyer asked for on a post order placed on one of your medias whose draft you write (`state` `pending_draft_update`), as the web does, from a file you uploaded with POST /files. The order moves back to `pending_draft_review`. The file is used up once the draft is delivered; a refused request leaves it usable.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
$seller_order_draft_file = new \Growwer\Api\Model\SellerOrderDraftFile(); // \Growwer\Api\Model\SellerOrderDraftFile

try {
    $result = $apiInstance->deliverSellerOrderDraftUpdate($id, $idempotency_key, $seller_order_draft_file);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->deliverSellerOrderDraftUpdate: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **seller_order_draft_file** | [**\Growwer\Api\Model\SellerOrderDraftFile**](../Model/SellerOrderDraftFile.md)|  | |

### Return type

[**\Growwer\Api\Model\SellerOrder**](../Model/SellerOrder.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deliverSellerOrderUpdate()`

```php
deliverSellerOrderUpdate($id, $idempotency_key, $seller_order_post_delivery): \Growwer\Api\Model\SellerOrder
```

Deliver an update

Delivers the update the buyer asked for on an order placed on one of your medias (`state` `pending_order_delivery_update`), as the web does. A post order takes the URL of the published post, which may be the same as before, and the confirmation of its publication date; both must be sent. A link addition order takes no body, and any field is refused. The order moves back to `pending_order_delivery_review` and the buyer is asked to review it.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
$seller_order_post_delivery = new \Growwer\Api\Model\SellerOrderPostDelivery(); // \Growwer\Api\Model\SellerOrderPostDelivery

try {
    $result = $apiInstance->deliverSellerOrderUpdate($id, $idempotency_key, $seller_order_post_delivery);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->deliverSellerOrderUpdate: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **seller_order_post_delivery** | [**\Growwer\Api\Model\SellerOrderPostDelivery**](../Model/SellerOrderPostDelivery.md)|  | [optional] |

### Return type

[**\Growwer\Api\Model\SellerOrder**](../Model/SellerOrder.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `downloadSellerOrderBriefing()`

```php
downloadSellerOrderBriefing($id): \SplFileObject
```

Download the draft the buyer attached to an order

The file the buyer attached to the briefing of a post order you sell. 404 when the order has none (`briefing.hasProposedDraft` is false) or the file cannot be read.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->downloadSellerOrderBriefing($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->downloadSellerOrderBriefing: ', $e->getMessage(), PHP_EOL;
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

## `downloadSellerOrderDraft()`

```php
downloadSellerOrderDraft($id): \SplFileObject
```

Download the draft of an order you sell

The file of the current draft of a post order you sell. 404 when the order has no draft file (`draft.hasFile` is false) or the file cannot be read. Earlier drafts are not available.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->downloadSellerOrderDraft($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->downloadSellerOrderDraft: ', $e->getMessage(), PHP_EOL;
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

## `getSellerOrder()`

```php
getSellerOrder($id): \Growwer\Api\Model\SellerOrder
```

Get an order you sell

One order placed on one of your medias, with its briefing, its draft and its state history. An order you only bought is not found here; it is under GET /orders/{id}.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->getSellerOrder($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->getSellerOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |

### Return type

[**\Growwer\Api\Model\SellerOrder**](../Model/SellerOrder.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listSellerOrders()`

```php
listSellerOrders($media_id, $state, $updated_since, $sort, $limit, $offset): \Growwer\Api\Model\ListSellerOrders200Response
```

List the orders you sell

The orders placed on your medias, newest first by default. To follow them, poll with `sort=updatedAt` and `updatedSince` set to the `updatedAt` of the last order you saw: an order moves to the end of that list each time it changes state. The orders you bought are under GET /orders.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$media_id = 'media_id_example'; // string | Only the orders on this media of yours.
$state = pending_acceptance,pending_order_delivery; // string | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones.
$updated_since = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Only the orders whose `updatedAt` is at or after this instant, an ISO-8601 date-time with its offset (send `+` as `%2B`).
$sort = '-createdAt'; // string | `-createdAt`, newest first, or `updatedAt`, least recently changed first. Orders of the same instant come in id order.
$limit = 20; // int | Orders per page, 1 to 100.
$offset = 0; // int | Orders to skip.

try {
    $result = $apiInstance->listSellerOrders($media_id, $state, $updated_since, $sort, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->listSellerOrders: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **media_id** | **string**| Only the orders on this media of yours. | [optional] |
| **state** | **string**| Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones. | [optional] |
| **updated_since** | **\DateTime**| Only the orders whose &#x60;updatedAt&#x60; is at or after this instant, an ISO-8601 date-time with its offset (send &#x60;+&#x60; as &#x60;%2B&#x60;). | [optional] |
| **sort** | **string**| &#x60;-createdAt&#x60;, newest first, or &#x60;updatedAt&#x60;, least recently changed first. Orders of the same instant come in id order. | [optional] [default to &#39;-createdAt&#39;] |
| **limit** | **int**| Orders per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Orders to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListSellerOrders200Response**](../Model/ListSellerOrders200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `refuteSellerOrderDraftUpdate()`

```php
refuteSellerOrderDraftUpdate($id, $idempotency_key, $seller_order_refutation): \Growwer\Api\Model\SellerOrder
```

Refuse a draft update

Refuses the draft update the buyer asked for on a post order placed on one of your medias whose draft you write (`state` `pending_draft_update`), as the web does. The order moves back to `pending_draft_review` and the buyer is told your reason. A draft Growwer or the buyer writes cannot be refused here.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
$seller_order_refutation = new \Growwer\Api\Model\SellerOrderRefutation(); // \Growwer\Api\Model\SellerOrderRefutation

try {
    $result = $apiInstance->refuteSellerOrderDraftUpdate($id, $idempotency_key, $seller_order_refutation);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->refuteSellerOrderDraftUpdate: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **seller_order_refutation** | [**\Growwer\Api\Model\SellerOrderRefutation**](../Model/SellerOrderRefutation.md)|  | |

### Return type

[**\Growwer\Api\Model\SellerOrder**](../Model/SellerOrder.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `refuteSellerOrderUpdate()`

```php
refuteSellerOrderUpdate($id, $idempotency_key, $seller_order_refutation): \Growwer\Api\Model\SellerOrder
```

Refuse an update

Refuses the update the buyer asked for on an order placed on one of your medias (`state` `pending_order_delivery_update`), as the web does. The order moves back to `pending_order_delivery_review` and the buyer is told your reason.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
$seller_order_refutation = new \Growwer\Api\Model\SellerOrderRefutation(); // \Growwer\Api\Model\SellerOrderRefutation

try {
    $result = $apiInstance->refuteSellerOrderUpdate($id, $idempotency_key, $seller_order_refutation);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->refuteSellerOrderUpdate: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **seller_order_refutation** | [**\Growwer\Api\Model\SellerOrderRefutation**](../Model/SellerOrderRefutation.md)|  | |

### Return type

[**\Growwer\Api\Model\SellerOrder**](../Model/SellerOrder.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `rejectSellerOrder()`

```php
rejectSellerOrder($id, $idempotency_key, $seller_order_rejection): \Growwer\Api\Model\SellerOrder
```

Reject an order

Rejects an order placed on one of your medias that you have not accepted yet (`state` `pending_acceptance`), as the web does. The order moves to `rejected_by_seller`, its price returns to the buyer, and the buyer is told your reason.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerOrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
$seller_order_rejection = new \Growwer\Api\Model\SellerOrderRejection(); // \Growwer\Api\Model\SellerOrderRejection

try {
    $result = $apiInstance->rejectSellerOrder($id, $idempotency_key, $seller_order_rejection);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerOrdersApi->rejectSellerOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **seller_order_rejection** | [**\Growwer\Api\Model\SellerOrderRejection**](../Model/SellerOrderRejection.md)|  | |

### Return type

[**\Growwer\Api\Model\SellerOrder**](../Model/SellerOrder.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
