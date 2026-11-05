# Growwer\Api\WebhooksApi

Subscribe your endpoints to events, rotate their secrets and follow their deliveries.

All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createWebhook()**](WebhooksApi.md#createWebhook) | **POST** /api/v1/webhooks | Create a webhook subscription |
| [**deleteWebhook()**](WebhooksApi.md#deleteWebhook) | **DELETE** /api/v1/webhooks/{id} | Delete a webhook subscription |
| [**getWebhook()**](WebhooksApi.md#getWebhook) | **GET** /api/v1/webhooks/{id} | Get a webhook subscription |
| [**listWebhookDeliveries()**](WebhooksApi.md#listWebhookDeliveries) | **GET** /api/v1/webhooks/{id}/deliveries | List the deliveries of a webhook subscription |
| [**listWebhooks()**](WebhooksApi.md#listWebhooks) | **GET** /api/v1/webhooks | List your webhook subscriptions |
| [**redeliverWebhook()**](WebhooksApi.md#redeliverWebhook) | **POST** /api/v1/webhooks/{id}/deliveries/{deliveryId}/redeliver | Redeliver a webhook event |
| [**rotateWebhookSecret()**](WebhooksApi.md#rotateWebhookSecret) | **POST** /api/v1/webhooks/{id}/rotate-secret | Rotate a webhook secret |
| [**sendWebhookTest()**](WebhooksApi.md#sendWebhookTest) | **POST** /api/v1/webhooks/{id}/test | Send a test event |
| [**updateWebhook()**](WebhooksApi.md#updateWebhook) | **PATCH** /api/v1/webhooks/{id} | Edit a webhook subscription |


## `createWebhook()`

```php
createWebhook($idempotency_key, $create_webhook_request): \Growwer\Api\Model\WebhookWithSecret
```

Create a webhook subscription

Subscribes an HTTPS URL to the events you list. Growwer then POSTs each event to it, signed as Standard Webhooks signs (`webhook-id`, `webhook-timestamp`, `webhook-signature`) with the `secret` this answer carries. The secret is shown only here and on POST /webhooks/{id}/rotate-secret: store it now. A replay of this request under its `Idempotency-Key` answers the subscription without it.  The URL must be HTTPS and its host must resolve to public addresses only: a loopback, private, link-local, multicast or metadata address is refused with 422 `webhook_url_not_public`, a host that does not resolve with 422 `webhook_url_unresolvable`. `lowBalanceThreshold` is required with `balance.low` and refused without it. An account has at most 20 subscriptions per mode. Test keys get 403 `not_available_in_test_mode` for now.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\WebhooksApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$create_webhook_request = new \Growwer\Api\Model\CreateWebhookRequest(); // \Growwer\Api\Model\CreateWebhookRequest

try {
    $result = $apiInstance->createWebhook($idempotency_key, $create_webhook_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->createWebhook: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **create_webhook_request** | [**\Growwer\Api\Model\CreateWebhookRequest**](../Model/CreateWebhookRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\WebhookWithSecret**](../Model/WebhookWithSecret.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteWebhook()`

```php
deleteWebhook($id, $idempotency_key)
```

Delete a webhook subscription

Deletes one of your webhook subscriptions and its delivery log. Deliveries still pending are not sent.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\WebhooksApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The subscription.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

try {
    $apiInstance->deleteWebhook($id, $idempotency_key);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->deleteWebhook: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The subscription. | |
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

## `getWebhook()`

```php
getWebhook($id): \Growwer\Api\Model\Webhook
```

Get a webhook subscription

One of your webhook subscriptions, without its secret. A subscription of the other mode is not found.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\WebhooksApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The subscription.

try {
    $result = $apiInstance->getWebhook($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->getWebhook: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The subscription. | |

### Return type

[**\Growwer\Api\Model\Webhook**](../Model/Webhook.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listWebhookDeliveries()`

```php
listWebhookDeliveries($id, $limit, $offset): \Growwer\Api\Model\ListWebhookDeliveries200Response
```

List the deliveries of a webhook subscription

The events sent to the subscription in the last 30 days, newest first, each with its status and its latest 10 attempts: when, the status code your endpoint answered, how long it took and the start of its response body. Older deliveries are deleted.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\WebhooksApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The subscription.
$limit = 20; // int | Deliveries per page, 1 to 100.
$offset = 0; // int | Deliveries to skip.

try {
    $result = $apiInstance->listWebhookDeliveries($id, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->listWebhookDeliveries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The subscription. | |
| **limit** | **int**| Deliveries per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Deliveries to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListWebhookDeliveries200Response**](../Model/ListWebhookDeliveries200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listWebhooks()`

```php
listWebhooks($limit, $offset): \Growwer\Api\Model\ListWebhooks200Response
```

List your webhook subscriptions

Your webhook subscriptions in the mode of the key, newest first, disabled ones included. A live key lists the live ones and a test key the test ones.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\WebhooksApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$limit = 20; // int | Subscriptions per page, 1 to 100.
$offset = 0; // int | Subscriptions to skip.

try {
    $result = $apiInstance->listWebhooks($limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->listWebhooks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**| Subscriptions per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Subscriptions to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListWebhooks200Response**](../Model/ListWebhooks200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `redeliverWebhook()`

```php
redeliverWebhook($id, $delivery_id, $idempotency_key): \Growwer\Api\Model\WebhookDelivery
```

Redeliver a webhook event

Queues a delivery that has succeeded or failed again, in a new round of retries, and answers it. It sends the same event with the same `webhook-id`, so a consumer that dedupes by it handles it once. Deliveries are kept 30 days. A delivery still pending, being sent or waiting for its next retry, answers 409 `webhook_delivery_pending` and takes none of the hour's sends; so does a redelivery while the subscription has 10 test events and redeliveries pending, its limit for a redelivery, given in `details.limit`. The pending deliveries of events never redelivered do not count. A subscription takes at most 10 test events and redeliveries an hour: past them it answers 429 `webhook_send_limit_reached` with `Retry-After`. A disabled subscription answers 409 `webhook_disabled`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\WebhooksApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The subscription.
$delivery_id = 'delivery_id_example'; // string | The delivery.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

try {
    $result = $apiInstance->redeliverWebhook($id, $delivery_id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->redeliverWebhook: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The subscription. | |
| **delivery_id** | **string**| The delivery. | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |

### Return type

[**\Growwer\Api\Model\WebhookDelivery**](../Model/WebhookDelivery.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `rotateWebhookSecret()`

```php
rotateWebhookSecret($id, $idempotency_key): \Growwer\Api\Model\WebhookWithSecret
```

Rotate a webhook secret

Gives the subscription a new signing secret and answers it: it is shown only here, so store it now. For 24 hours, until `previousSecretExpiresAt`, every delivery carries two signatures in `webhook-signature`, one with each secret, so you can switch without missing an event; after that only the new secret signs. A replay of this request under its `Idempotency-Key` answers the subscription without the secret.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\WebhooksApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The subscription.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

try {
    $result = $apiInstance->rotateWebhookSecret($id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->rotateWebhookSecret: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The subscription. | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |

### Return type

[**\Growwer\Api\Model\WebhookWithSecret**](../Model/WebhookWithSecret.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `sendWebhookTest()`

```php
sendWebhookTest($id, $idempotency_key): \Growwer\Api\Model\WebhookDelivery
```

Send a test event

Queues a `webhook.test` event for the subscription, whatever events it lists, and answers its delivery: follow it on GET /webhooks/{id}/deliveries. It is signed, retried and logged as any event. It normally supersedes the subscription's earlier test events still pending: their deliveries fail and are not retried, so a test right after fixing the endpoint does not wait behind them; one that cannot be failed then is failed by the next test. A subscription takes at most 10 test events and redeliveries an hour: past them it answers 429 `webhook_send_limit_reached` with `Retry-After`. A disabled subscription answers 409 `webhook_disabled`. A test event that cannot be recorded answers 503 `webhook_test_unavailable`: nothing was sent, the attempt counts toward the hourly limit, and a retry needs a new `Idempotency-Key`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\WebhooksApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The subscription.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

try {
    $result = $apiInstance->sendWebhookTest($id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->sendWebhookTest: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The subscription. | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |

### Return type

[**\Growwer\Api\Model\WebhookDelivery**](../Model/WebhookDelivery.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateWebhook()`

```php
updateWebhook($id, $idempotency_key, $update_webhook_request): \Growwer\Api\Model\Webhook
```

Edit a webhook subscription

Changes only the fields you send. A new `url` is checked as on create. Dropping `balance.low` from `events` drops the threshold with it. `enabled: false` disables the subscription, which then gets no events; `enabled: true` enables it again, including one Growwer disabled because its endpoint answered 410 or failed for 5 days, and forgets its failures.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\WebhooksApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The subscription.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$update_webhook_request = new \Growwer\Api\Model\UpdateWebhookRequest(); // \Growwer\Api\Model\UpdateWebhookRequest

try {
    $result = $apiInstance->updateWebhook($id, $idempotency_key, $update_webhook_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling WebhooksApi->updateWebhook: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The subscription. | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **update_webhook_request** | [**\Growwer\Api\Model\UpdateWebhookRequest**](../Model/UpdateWebhookRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\Webhook**](../Model/Webhook.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
