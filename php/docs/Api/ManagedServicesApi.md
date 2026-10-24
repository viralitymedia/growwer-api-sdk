# Growwer\Api\ManagedServicesApi



All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**estimateManagedServiceProposals()**](ManagedServicesApi.md#estimateManagedServiceProposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/estimate | Estimate accepting proposals |
| [**getManagedServiceCampaign()**](ManagedServicesApi.md#getManagedServiceCampaign) | **GET** /api/v1/managed-service/campaigns/{id} | Get a managed service campaign |
| [**getManagedServiceProposalsSummary()**](ManagedServicesApi.md#getManagedServiceProposalsSummary) | **GET** /api/v1/managed-service/campaigns/{id}/proposals-summary | Download the summary of a campaign&#39;s proposals |
| [**listManagedServiceCampaigns()**](ManagedServicesApi.md#listManagedServiceCampaigns) | **GET** /api/v1/managed-service/campaigns | List your managed service campaigns |
| [**listManagedServiceProposals()**](ManagedServicesApi.md#listManagedServiceProposals) | **GET** /api/v1/managed-service/campaigns/{id}/proposals | List the proposals of a campaign |
| [**requestManagedServiceCampaign()**](ManagedServicesApi.md#requestManagedServiceCampaign) | **POST** /api/v1/managed-service/campaign-requests | Request a new campaign |
| [**requestManagedServiceInfo()**](ManagedServicesApi.md#requestManagedServiceInfo) | **POST** /api/v1/managed-service/info-requests | Ask about the managed service |
| [**reviewManagedServiceProposals()**](ManagedServicesApi.md#reviewManagedServiceProposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/review | Accept or reject proposals |


## `estimateManagedServiceProposals()`

```php
estimateManagedServiceProposals($id, $managed_service_proposals_estimate_request): \Growwer\Api\Model\ManagedServiceProposalsEstimate
```

Estimate accepting proposals

Totals the campaign's accepted proposals that still await their order and the `proposed` ones you name in `accept`, and compares the total with your wallet's available balance. Each proposal counts at its `currentPrice`, or at its `proposedPrice` when the media no longer offers the service. Nothing is accepted, charged or reserved, so a read-only key may call it and it takes no Idempotency-Key.  The estimate is advisory: accepting a proposal charges nothing. The team charges your wallet when it places the order for an accepted proposal, and the same balance pays for the orders you place yourself.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ManagedServicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$managed_service_proposals_estimate_request = new \Growwer\Api\Model\ManagedServiceProposalsEstimateRequest(); // \Growwer\Api\Model\ManagedServiceProposalsEstimateRequest

try {
    $result = $apiInstance->estimateManagedServiceProposals($id, $managed_service_proposals_estimate_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ManagedServicesApi->estimateManagedServiceProposals: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **managed_service_proposals_estimate_request** | [**\Growwer\Api\Model\ManagedServiceProposalsEstimateRequest**](../Model/ManagedServiceProposalsEstimateRequest.md)|  | [optional] |

### Return type

[**\Growwer\Api\Model\ManagedServiceProposalsEstimate**](../Model/ManagedServiceProposalsEstimate.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getManagedServiceCampaign()`

```php
getManagedServiceCampaign($id): \Growwer\Api\Model\ManagedServiceCampaign
```

Get a managed service campaign

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ManagedServicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string

try {
    $result = $apiInstance->getManagedServiceCampaign($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ManagedServicesApi->getManagedServiceCampaign: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |

### Return type

[**\Growwer\Api\Model\ManagedServiceCampaign**](../Model/ManagedServiceCampaign.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getManagedServiceProposalsSummary()`

```php
getManagedServiceProposalsSummary($id, $extended): \SplFileObject
```

Download the summary of a campaign's proposals

The PDF the campaign page offers: the proposals awaiting your review, accepted or being published, newest first, in your language. With `extended=true` it also shows each proposal's price, the price it was proposed at (`proposedPrice`). One summary of yours is rendered at a time: a request while another is being rendered gets 429 `proposals_summary_in_progress`, to retry after the `Retry-After` header.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ManagedServicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$extended = 'false'; // string | Whether to show the prices.

try {
    $result = $apiInstance->getManagedServiceProposalsSummary($id, $extended);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ManagedServicesApi->getManagedServiceProposalsSummary: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **extended** | **string**| Whether to show the prices. | [optional] [default to &#39;false&#39;] |

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

## `listManagedServiceCampaigns()`

```php
listManagedServiceCampaigns($limit, $offset): \Growwer\Api\Model\ListManagedServiceCampaigns200Response
```

List your managed service campaigns

The campaigns your managed service runs for you, newest first. Without a managed service the list is empty: GET /me says whether you have one.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ManagedServicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$limit = 20; // int | Campaigns per page, 1 to 100.
$offset = 0; // int | Campaigns to skip.

try {
    $result = $apiInstance->listManagedServiceCampaigns($limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ManagedServicesApi->listManagedServiceCampaigns: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**| Campaigns per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Campaigns to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListManagedServiceCampaigns200Response**](../Model/ListManagedServiceCampaigns200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listManagedServiceProposals()`

```php
listManagedServiceProposals($id, $state, $limit, $offset): \Growwer\Api\Model\ListManagedServiceProposals200Response
```

List the proposals of a campaign

The medias the team proposes for the campaign, newest first. Those `proposed` await your review (POST /managed-service/campaigns/{id}/proposals/review).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ManagedServicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$state = proposed,accepted; // string | Only proposals in these states, comma-separated: `proposed`, `accepted`, `cancelled`, `purchase_started`, `purchase_finished`.
$limit = 20; // int | Proposals per page, 1 to 100.
$offset = 0; // int | Proposals to skip.

try {
    $result = $apiInstance->listManagedServiceProposals($id, $state, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ManagedServicesApi->listManagedServiceProposals: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **state** | **string**| Only proposals in these states, comma-separated: &#x60;proposed&#x60;, &#x60;accepted&#x60;, &#x60;cancelled&#x60;, &#x60;purchase_started&#x60;, &#x60;purchase_finished&#x60;. | [optional] |
| **limit** | **int**| Proposals per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Proposals to skip. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListManagedServiceProposals200Response**](../Model/ListManagedServiceProposals200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `requestManagedServiceCampaign()`

```php
requestManagedServiceCampaign($idempotency_key, $managed_service_request): \Growwer\Api\Model\ManagedServiceRequestSent
```

Request a new campaign

Asks your account manager for a new campaign, as the managed service page does: the team emails you to agree on it. For accounts with a managed service (GET /me `managedService.active`); without one, POST /managed-service/info-requests asks about the service.  The API admits a limited number of such requests per user and UTC day (5 by default; the refusal message states the current limit). Past it, it answers 429 `managed_service_request_limit_reached`, with `Retry-After` the time to the next UTC midnight. A request that is refused (4xx) does not count; one that fails on the server (5xx) does, as it may have been sent.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ManagedServicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$managed_service_request = new \Growwer\Api\Model\ManagedServiceRequest(); // \Growwer\Api\Model\ManagedServiceRequest

try {
    $result = $apiInstance->requestManagedServiceCampaign($idempotency_key, $managed_service_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ManagedServicesApi->requestManagedServiceCampaign: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **managed_service_request** | [**\Growwer\Api\Model\ManagedServiceRequest**](../Model/ManagedServiceRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\ManagedServiceRequestSent**](../Model/ManagedServiceRequestSent.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `requestManagedServiceInfo()`

```php
requestManagedServiceInfo($idempotency_key, $managed_service_request): \Growwer\Api\Model\ManagedServiceRequestSent
```

Ask about the managed service

Asks the team about the managed service for your website, as the managed service landing page does: the team contacts you. For accounts without a managed service (GET /me `managedService.active`); with one, POST /managed-service/campaign-requests requests a new campaign.  The API admits a limited number of such requests per user and UTC day (5 by default; the refusal message states the current limit). Past it, it answers 429 `managed_service_request_limit_reached`, with `Retry-After` the time to the next UTC midnight. A request that is refused (4xx) does not count; one that fails on the server (5xx) does, as it may have been sent.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ManagedServicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$managed_service_request = new \Growwer\Api\Model\ManagedServiceRequest(); // \Growwer\Api\Model\ManagedServiceRequest

try {
    $result = $apiInstance->requestManagedServiceInfo($idempotency_key, $managed_service_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ManagedServicesApi->requestManagedServiceInfo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **managed_service_request** | [**\Growwer\Api\Model\ManagedServiceRequest**](../Model/ManagedServiceRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\ManagedServiceRequestSent**](../Model/ManagedServiceRequestSent.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `reviewManagedServiceProposals()`

```php
reviewManagedServiceProposals($id, $idempotency_key, $managed_service_proposal_review_request): \Growwer\Api\Model\ManagedServiceProposalReview
```

Accept or reject proposals

Decides on every proposal of the campaign that awaits your review (`state` `proposed`), as the campaign page does: name each one once, with `accept` or `reject`, and a comment for the team to reject one. Their order in the body does not matter. Accepting charges nothing: the team places the orders for the accepted proposals and your wallet pays for them then. POST /managed-service/campaigns/{id}/proposals/estimate says what they would cost.  When every proposal is accepted the campaign moves to `proposal_accepted`; when one is rejected the team is told and prepares others. A proposal someone else moved on the campaign page while the request ran is answered in the state it reached.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\ManagedServicesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
$managed_service_proposal_review_request = new \Growwer\Api\Model\ManagedServiceProposalReviewRequest(); // \Growwer\Api\Model\ManagedServiceProposalReviewRequest

try {
    $result = $apiInstance->reviewManagedServiceProposals($id, $idempotency_key, $managed_service_proposal_review_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ManagedServicesApi->reviewManagedServiceProposals: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**|  | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | |
| **managed_service_proposal_review_request** | [**\Growwer\Api\Model\ManagedServiceProposalReviewRequest**](../Model/ManagedServiceProposalReviewRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\ManagedServiceProposalReview**](../Model/ManagedServiceProposalReview.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
