# Growwer\Api\ProjectsApi

Create, edit and delete the projects you buy for.

All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createProject()**](ProjectsApi.md#createProject) | **POST** /api/v1/projects | Create a project |
| [**deleteProject()**](ProjectsApi.md#deleteProject) | **DELETE** /api/v1/projects/{id} | Delete a project |
| [**getProject()**](ProjectsApi.md#getProject) | **GET** /api/v1/projects/{id} | Get a project |
| [**listProjects()**](ProjectsApi.md#listProjects) | **GET** /api/v1/projects | List your projects |
| [**updateProject()**](ProjectsApi.md#updateProject) | **PATCH** /api/v1/projects/{id} | Edit a project |


## `createProject()`

```php
createProject($idempotency_key, $create_project_request): \Growwer\Api\Model\Project
```

Create a project

Creates a project for a website, as the web's project creation does. Growwer then analyses it in the background to recommend media: the project is answered with `state: analyzing` and turns `finished` when the analysis ends. Analysis can take hours, and it never finishes when no medium matches the project, so poll GET /projects/{id} with backoff and use `createdAt` to decide when to stop.  Every value is validated as on the web: `topics`, `language` and `country` take the identifiers GET /vocabulary publishes.  Creating a project also categorises its website through an external service, as the web does. When that service fails the answer is 500, although the project may already be saved, and a retry under the same Idempotency-Key answers 409 `idempotency_outcome_unknown`. After either, list your projects (GET /projects) before retrying with a new key, or you may create a duplicate.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$create_project_request = new \Growwer\Api\Model\CreateProjectRequest(); // \Growwer\Api\Model\CreateProjectRequest

try {
    $result = $apiInstance->createProject($idempotency_key, $create_project_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->createProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **create_project_request** | [**\Growwer\Api\Model\CreateProjectRequest**](../Model/CreateProjectRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\Project**](../Model/Project.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteProject()`

```php
deleteProject($id, $idempotency_key)
```

Delete a project

Deletes one of your projects. A project with an order in progress cannot be deleted until its orders finish.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

try {
    $apiInstance->deleteProject($id, $idempotency_key);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->deleteProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
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

## `getProject()`

```php
getProject($id): \Growwer\Api\Model\Project
```

Get a project

One of your projects. Poll it to follow `state` after creating the project.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->getProject($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->getProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |

### Return type

[**\Growwer\Api\Model\Project**](../Model/Project.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listProjects()`

```php
listProjects($limit, $offset): \Growwer\Api\Model\ListProjects200Response
```

List your projects

Your projects, newest first.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$limit = 20; // int | Projects per page, 1 to 100.
$offset = 0; // int | Projects to skip.

try {
    $result = $apiInstance->listProjects($limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->listProjects: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**| Projects per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Projects to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListProjects200Response**](../Model/ListProjects200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateProject()`

```php
updateProject($id, $idempotency_key, $update_project_request): \Growwer\Api\Model\Project
```

Edit a project

Changes only the fields you send. `rootUrl` cannot be changed; any field not listed here is refused. Changing `language`, `country`, `promotedProducts` or `topics` makes Growwer categorise the project and work out its target keywords again, in the background.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$update_project_request = new \Growwer\Api\Model\UpdateProjectRequest(); // \Growwer\Api\Model\UpdateProjectRequest

try {
    $result = $apiInstance->updateProject($id, $idempotency_key, $update_project_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->updateProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **update_project_request** | [**\Growwer\Api\Model\UpdateProjectRequest**](../Model/UpdateProjectRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\Project**](../Model/Project.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
