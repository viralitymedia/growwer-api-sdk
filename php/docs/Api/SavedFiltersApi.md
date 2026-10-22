# Growwer\Api\SavedFiltersApi



All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**countSavedFilterMedias()**](SavedFiltersApi.md#countSavedFilterMedias) | **GET** /api/v1/projects/{id}/saved-filters/{filterId}/media-count | Count the medias of a saved filter |
| [**createSavedFilter()**](SavedFiltersApi.md#createSavedFilter) | **POST** /api/v1/projects/{id}/saved-filters | Save a filter |
| [**deleteSavedFilter()**](SavedFiltersApi.md#deleteSavedFilter) | **DELETE** /api/v1/projects/{id}/saved-filters/{filterId} | Delete a saved filter |
| [**listSavedFilters()**](SavedFiltersApi.md#listSavedFilters) | **GET** /api/v1/projects/{id}/saved-filters | List the saved filters of a project |


## `countSavedFilterMedias()`

```php
countSavedFilterMedias($id, $filter_id): \Growwer\Api\Model\CountSavedFilterMedias200Response
```

Count the medias of a saved filter

How many medias of the project's catalogue one of your saved filters matches: the `total` of GET /projects/{id}/medias with its `savedFilterId`. The number is cached for up to 24 hours, and it can differ from the count the web shows, which is not limited to the project's catalogue. A filter saved on the web that uses a filter the API does not support is refused with 422 `saved_filter_unsupported`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SavedFiltersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The project.
$filter_id = 'filter_id_example'; // string | The saved filter.

try {
    $result = $apiInstance->countSavedFilterMedias($id, $filter_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SavedFiltersApi->countSavedFilterMedias: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The project. | |
| **filter_id** | **string**| The saved filter. | |

### Return type

[**\Growwer\Api\Model\CountSavedFilterMedias200Response**](../Model/CountSavedFilterMedias200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createSavedFilter()`

```php
createSavedFilter($id, $idempotency_key, $create_saved_filter_request): \Growwer\Api\Model\SavedFilter
```

Save a filter

Saves a catalogue search of one of your projects, which then also appears on the web. `filters` takes the filter parameters of GET /projects/{id}/medias, and `source`, with the same values; lists may be JSON arrays and flags JSON booleans. With `notificationFrequency`, Growwer emails you new medias that match. A project has at most 100 saved filters and an account 500.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SavedFiltersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The project.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$create_saved_filter_request = new \Growwer\Api\Model\CreateSavedFilterRequest(); // \Growwer\Api\Model\CreateSavedFilterRequest

try {
    $result = $apiInstance->createSavedFilter($id, $idempotency_key, $create_saved_filter_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SavedFiltersApi->createSavedFilter: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The project. | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **create_saved_filter_request** | [**\Growwer\Api\Model\CreateSavedFilterRequest**](../Model/CreateSavedFilterRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\SavedFilter**](../Model/SavedFilter.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteSavedFilter()`

```php
deleteSavedFilter($id, $filter_id, $idempotency_key)
```

Delete a saved filter

Deletes one of your saved filters of one of your projects, including one saved on the web. Its notifications stop.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SavedFiltersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The project.
$filter_id = 'filter_id_example'; // string | The saved filter.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

try {
    $apiInstance->deleteSavedFilter($id, $filter_id, $idempotency_key);
} catch (Exception $e) {
    echo 'Exception when calling SavedFiltersApi->deleteSavedFilter: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The project. | |
| **filter_id** | **string**| The saved filter. | |
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

## `listSavedFilters()`

```php
listSavedFilters($id): \Growwer\Api\Model\ListSavedFilters200Response
```

List the saved filters of a project

Your saved filters of one of your projects, newest first, including those saved on the web. A project has at most 100. Apply one with `savedFilterId` on GET /projects/{id}/medias.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\SavedFiltersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The project.

try {
    $result = $apiInstance->listSavedFilters($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SavedFiltersApi->listSavedFilters: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The project. | |

### Return type

[**\Growwer\Api\Model\ListSavedFilters200Response**](../Model/ListSavedFilters200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
