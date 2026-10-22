# Growwer\Api\SellerMediasApi



All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**applySellerMediaCompetitiveFees()**](SellerMediasApi.md#applySellerMediaCompetitiveFees) | **POST** /api/v1/seller/medias/{id}/apply-competitive-fees | Set the competitive fees Growwer suggests |
| [**getSellerMedia()**](SellerMediasApi.md#getSellerMedia) | **GET** /api/v1/seller/medias/{id} | Get a media you sell on |
| [**listSellerMedias()**](SellerMediasApi.md#listSellerMedias) | **GET** /api/v1/seller/medias | List the medias you sell on |
| [**updateSellerMedia()**](SellerMediasApi.md#updateSellerMedia) | **PATCH** /api/v1/seller/medias/{id} | Edit the fees of a media you sell on |


## `applySellerMediaCompetitiveFees()`

```php
applySellerMediaCompetitiveFees($id, $idempotency_key): \Growwer\Api\Model\SellerMedia
```

Set the competitive fees Growwer suggests

Sets your post fees for the media to the competitive fees Growwer suggests, the `competitiveFees` of GET /seller/medias/{id}, as the button on the media edit page does. Each link type you offer gets the suggested fee on each side it already has a fee for; no link type gains a side it did not offer.  Two differences from the page: a side Growwer has no suggestion for keeps your fee (the page clears it), and the fixed fee the page falls back to when it cannot find a competitive one is never applied (the page applies it). When neither side has a suggestion, nothing changes and the answer is 409 `no_competitive_fees`. When your fees already are the suggested ones, or the suggestion is only for a side none of your link types offers, nothing changes and the answer is 200.  The fees set are your base fees: a running flash offer keeps discounting them. As with a fee edit, a change of the price may cancel the managed-service proposals accepted for the media whose price it changes. Send no body, or an empty object.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerMediasApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

try {
    $result = $apiInstance->applySellerMediaCompetitiveFees($id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerMediasApi->applySellerMediaCompetitiveFees: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |

### Return type

[**\Growwer\Api\Model\SellerMedia**](../Model/SellerMedia.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getSellerMedia()`

```php
getSellerMedia($id): \Growwer\Api\Model\SellerMedia
```

Get a media you sell on

One of your medias, with your fees, its extras, the competitive fees Growwer suggests and how it performs. Another seller's media is not found.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerMediasApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->getSellerMedia($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerMediasApi->getSellerMedia: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |

### Return type

[**\Growwer\Api\Model\SellerMedia**](../Model/SellerMedia.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listSellerMedias()`

```php
listSellerMedias($state, $sort, $limit, $offset): \Growwer\Api\Model\ListSellerMedias200Response
```

List the medias you sell on

Your medias in every state, with your fees and how they perform, newest first by default.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerMediasApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$state = active,deactivated; // string | Only the medias in one of these states, comma-separated: `analyzing`, `pending_review`, `active`, `deactivated`. An unknown state is refused with 422.
$sort = '-createdAt'; // string | By creation date, number of published orders or publication rate; a leading `-` sorts descending. Medias with no publication rate come first ascending, last descending. Ties come in id order.
$limit = 20; // int | Medias per page, 1 to 100.
$offset = 0; // int | Medias to skip.

try {
    $result = $apiInstance->listSellerMedias($state, $sort, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerMediasApi->listSellerMedias: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **state** | **string**| Only the medias in one of these states, comma-separated: &#x60;analyzing&#x60;, &#x60;pending_review&#x60;, &#x60;active&#x60;, &#x60;deactivated&#x60;. An unknown state is refused with 422. | [optional] |
| **sort** | **string**| By creation date, number of published orders or publication rate; a leading &#x60;-&#x60; sorts descending. Medias with no publication rate come first ascending, last descending. Ties come in id order. | [optional] [default to &#39;-createdAt&#39;] |
| **limit** | **int**| Medias per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Medias to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListSellerMedias200Response**](../Model/ListSellerMedias200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateSellerMedia()`

```php
updateSellerMedia($id, $idempotency_key, $update_seller_media_request): \Growwer\Api\Model\SellerMedia
```

Edit the fees of a media you sell on

Sets the fees of one of your medias, as the media edit page saves them. Send only the sections you change: a section you send replaces that section wholly, a section you leave out stays as it is.  - `postOffer.pricingOptions` lists every link type you offer for sponsored posts, at least one. A link type you leave out is no longer offered. Each option needs at least one fee, and every option must offer the same sides (written by you, written by the buyer or Growwer), as the page requires. Each fee is at least 1 EUR. - `linkAdditionOffer.pricingOptions` lists the link types you offer for adding a link to an existing article; `null` or an empty list stops offering link additions. - `extraServices` is the full list of extra services you offer; an empty list removes them all.  The fees are your base fees, the ones GET /seller/medias/{id} returns: while a flash offer runs, its discount keeps applying on top of them, and `currentCost` shows the result. `currentCost` may be sent back as read and is ignored. Characteristics, topics and comments are not edited here.  As on the page, a change of the post offer's price may cancel the managed-service proposals accepted for the media whose price it changes, and raising the price above the best competitor's tells Growwer's support team. A restricted seller account may edit its fees.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SellerMediasApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$update_seller_media_request = {"postOffer":{"pricingOptions":[{"linkType":"dofollow","feeWhenSellerWritesPost":{"amount":12000,"currency":"EUR"},"feeWhenSellerDoesNotWritePost":{"amount":10000,"currency":"EUR"}},{"linkType":"nofollow","feeWhenSellerWritesPost":{"amount":9000,"currency":"EUR"},"feeWhenSellerDoesNotWritePost":{"amount":7000,"currency":"EUR"}}]},"linkAdditionOffer":null,"extraServices":[{"name":"list_on_homepage","cost":{"amount":5000,"currency":"EUR"}}]}; // \Growwer\Api\Model\UpdateSellerMediaRequest

try {
    $result = $apiInstance->updateSellerMedia($id, $idempotency_key, $update_seller_media_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SellerMediasApi->updateSellerMedia: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **update_seller_media_request** | [**\Growwer\Api\Model\UpdateSellerMediaRequest**](../Model/UpdateSellerMediaRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\SellerMedia**](../Model/SellerMedia.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
