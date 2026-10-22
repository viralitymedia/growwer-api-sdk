# ManagedServicesApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**estimateManagedServiceProposals**](ManagedServicesApi.md#estimatemanagedserviceproposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/estimate | Estimate accepting proposals |
| [**getManagedServiceCampaign**](ManagedServicesApi.md#getmanagedservicecampaign) | **GET** /api/v1/managed-service/campaigns/{id} | Get a managed service campaign |
| [**getManagedServiceProposalsSummary**](ManagedServicesApi.md#getmanagedserviceproposalssummary) | **GET** /api/v1/managed-service/campaigns/{id}/proposals-summary | Download the summary of a campaign\&#39;s proposals |
| [**listManagedServiceCampaigns**](ManagedServicesApi.md#listmanagedservicecampaigns) | **GET** /api/v1/managed-service/campaigns | List your managed service campaigns |
| [**listManagedServiceProposals**](ManagedServicesApi.md#listmanagedserviceproposals) | **GET** /api/v1/managed-service/campaigns/{id}/proposals | List the proposals of a campaign |
| [**requestManagedServiceCampaign**](ManagedServicesApi.md#requestmanagedservicecampaign) | **POST** /api/v1/managed-service/campaign-requests | Request a new campaign |
| [**requestManagedServiceInfo**](ManagedServicesApi.md#requestmanagedserviceinfo) | **POST** /api/v1/managed-service/info-requests | Ask about the managed service |
| [**reviewManagedServiceProposals**](ManagedServicesApi.md#reviewmanagedserviceproposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/review | Accept or reject proposals |



## estimateManagedServiceProposals

> ManagedServiceProposalsEstimate estimateManagedServiceProposals(id, managedServiceProposalsEstimateRequest)

Estimate accepting proposals

Totals the campaign\&#39;s accepted proposals that still await their order and the &#x60;proposed&#x60; ones you name in &#x60;accept&#x60;, and compares the total with your wallet\&#39;s available balance. Each proposal counts at its &#x60;currentPrice&#x60;, or at its &#x60;proposedPrice&#x60; when the media no longer offers the service. Nothing is accepted, charged or reserved, so a read-only key may call it and it takes no Idempotency-Key.  The estimate is advisory: accepting a proposal charges nothing. The team charges your wallet when it places the order for an accepted proposal, and the same balance pays for the orders you place yourself.

### Example

```ts
import {
  Configuration,
  ManagedServicesApi,
} from '@growwer/api';
import type { EstimateManagedServiceProposalsRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ManagedServicesApi(config);

  const body = {
    // string
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // ManagedServiceProposalsEstimateRequest (optional)
    managedServiceProposalsEstimateRequest: ...,
  } satisfies EstimateManagedServiceProposalsRequest;

  try {
    const data = await api.estimateManagedServiceProposals(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` |  | [Defaults to `undefined`] |
| **managedServiceProposalsEstimateRequest** | [ManagedServiceProposalsEstimateRequest](ManagedServiceProposalsEstimateRequest.md) |  | [Optional] |

### Return type

[**ManagedServiceProposalsEstimate**](ManagedServiceProposalsEstimate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The totals and how your wallet covers them. |  -  |
| **400** | The body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The campaign is not yours, or a proposal named in &#x60;accept&#x60; is not one of the campaign\&#39;s (code &#x60;not_found&#x60;, with &#x60;details.proposalId&#x60;). |  -  |
| **409** | A proposal named in &#x60;accept&#x60; is not awaiting your review (code &#x60;invalid_state&#x60;, with &#x60;details.proposalIds&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getManagedServiceCampaign

> ManagedServiceCampaign getManagedServiceCampaign(id)

Get a managed service campaign

### Example

```ts
import {
  Configuration,
  ManagedServicesApi,
} from '@growwer/api';
import type { GetManagedServiceCampaignRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ManagedServicesApi(config);

  const body = {
    // string
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetManagedServiceCampaignRequest;

  try {
    const data = await api.getManagedServiceCampaign(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ManagedServiceCampaign**](ManagedServiceCampaign.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The campaign. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getManagedServiceProposalsSummary

> Blob getManagedServiceProposalsSummary(id, extended)

Download the summary of a campaign\&#39;s proposals

The PDF the campaign page offers: the proposals awaiting your review, accepted or being published, newest first, in your language. With &#x60;extended&#x3D;true&#x60; it also shows each proposal\&#39;s price, the price it was proposed at (&#x60;proposedPrice&#x60;).

### Example

```ts
import {
  Configuration,
  ManagedServicesApi,
} from '@growwer/api';
import type { GetManagedServiceProposalsSummaryRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ManagedServicesApi(config);

  const body = {
    // string
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // 'true' | 'false' | Whether to show the prices. (optional)
    extended: extended_example,
  } satisfies GetManagedServiceProposalsSummaryRequest;

  try {
    const data = await api.getManagedServiceProposalsSummary(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` |  | [Defaults to `undefined`] |
| **extended** | `true`, `false` | Whether to show the prices. | [Optional] [Defaults to `&#39;false&#39;`] [Enum: true, false] |

### Return type

**Blob**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/pdf`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The summary. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listManagedServiceCampaigns

> ListManagedServiceCampaigns200Response listManagedServiceCampaigns(limit, offset)

List your managed service campaigns

The campaigns your managed service runs for you, newest first. Without a managed service the list is empty: GET /me says whether you have one.

### Example

```ts
import {
  Configuration,
  ManagedServicesApi,
} from '@growwer/api';
import type { ListManagedServiceCampaignsRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ManagedServicesApi(config);

  const body = {
    // number | Campaigns per page, 1 to 100. (optional)
    limit: 56,
    // number | Campaigns to skip. (optional)
    offset: 56,
  } satisfies ListManagedServiceCampaignsRequest;

  try {
    const data = await api.listManagedServiceCampaigns(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | `number` | Campaigns per page, 1 to 100. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Campaigns to skip. | [Optional] [Defaults to `0`] |

### Return type

[**ListManagedServiceCampaigns200Response**](ListManagedServiceCampaigns200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of your campaigns and how many you have in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listManagedServiceProposals

> ListManagedServiceProposals200Response listManagedServiceProposals(id, state, limit, offset)

List the proposals of a campaign

The medias the team proposes for the campaign, newest first. Those &#x60;proposed&#x60; await your review (POST /managed-service/campaigns/{id}/proposals/review).

### Example

```ts
import {
  Configuration,
  ManagedServicesApi,
} from '@growwer/api';
import type { ListManagedServiceProposalsRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ManagedServicesApi(config);

  const body = {
    // string
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Only proposals in these states, comma-separated: `proposed`, `accepted`, `cancelled`, `purchase_started`, `purchase_finished`. (optional)
    state: proposed,accepted,
    // number | Proposals per page, 1 to 100. (optional)
    limit: 56,
    // number | Proposals to skip. (optional)
    offset: 56,
  } satisfies ListManagedServiceProposalsRequest;

  try {
    const data = await api.listManagedServiceProposals(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` |  | [Defaults to `undefined`] |
| **state** | `string` | Only proposals in these states, comma-separated: &#x60;proposed&#x60;, &#x60;accepted&#x60;, &#x60;cancelled&#x60;, &#x60;purchase_started&#x60;, &#x60;purchase_finished&#x60;. | [Optional] [Defaults to `undefined`] |
| **limit** | `number` | Proposals per page, 1 to 100. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Proposals to skip. | [Optional] [Defaults to `0`] |

### Return type

[**ListManagedServiceProposals200Response**](ListManagedServiceProposals200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of the campaign\&#39;s proposals and how many match in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## requestManagedServiceCampaign

> ManagedServiceRequestSent requestManagedServiceCampaign(idempotencyKey, managedServiceRequest)

Request a new campaign

Asks your account manager for a new campaign, as the managed service page does: the team emails you to agree on it. For accounts with a managed service (GET /me &#x60;managedService.active&#x60;); without one, POST /managed-service/info-requests asks about the service.  You may send 5 such requests per UTC day through the API. Past them it answers 429 &#x60;managed_service_request_limit_reached&#x60;, with &#x60;Retry-After&#x60; the time to the next UTC midnight. A request that is refused (4xx) does not count; one that fails on the server (5xx) does, as it may have been sent.

### Example

```ts
import {
  Configuration,
  ManagedServicesApi,
} from '@growwer/api';
import type { RequestManagedServiceCampaignRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ManagedServicesApi(config);

  const body = {
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
    // ManagedServiceRequest
    managedServiceRequest: ...,
  } satisfies RequestManagedServiceCampaignRequest;

  try {
    const data = await api.requestManagedServiceCampaign(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |
| **managedServiceRequest** | [ManagedServiceRequest](ManagedServiceRequest.md) |  | |

### Return type

[**ManagedServiceRequestSent**](ManagedServiceRequestSent.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request was sent. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **409** | You have no managed service yet (code &#x60;managed_service_required&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## requestManagedServiceInfo

> ManagedServiceRequestSent requestManagedServiceInfo(idempotencyKey, managedServiceRequest)

Ask about the managed service

Asks the team about the managed service for your website, as the managed service landing page does: the team contacts you. For accounts without a managed service (GET /me &#x60;managedService.active&#x60;); with one, POST /managed-service/campaign-requests requests a new campaign.  You may send 5 such requests per UTC day through the API. Past them it answers 429 &#x60;managed_service_request_limit_reached&#x60;, with &#x60;Retry-After&#x60; the time to the next UTC midnight. A request that is refused (4xx) does not count; one that fails on the server (5xx) does, as it may have been sent.

### Example

```ts
import {
  Configuration,
  ManagedServicesApi,
} from '@growwer/api';
import type { RequestManagedServiceInfoRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ManagedServicesApi(config);

  const body = {
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
    // ManagedServiceRequest
    managedServiceRequest: ...,
  } satisfies RequestManagedServiceInfoRequest;

  try {
    const data = await api.requestManagedServiceInfo(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |
| **managedServiceRequest** | [ManagedServiceRequest](ManagedServiceRequest.md) |  | |

### Return type

[**ManagedServiceRequestSent**](ManagedServiceRequestSent.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request was sent. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **409** | You already have a managed service (code &#x60;managed_service_exists&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## reviewManagedServiceProposals

> ManagedServiceProposalReview reviewManagedServiceProposals(id, idempotencyKey, managedServiceProposalReviewRequest)

Accept or reject proposals

Decides on every proposal of the campaign that awaits your review (&#x60;state&#x60; &#x60;proposed&#x60;), as the campaign page does: name each one once, with &#x60;accept&#x60; or &#x60;reject&#x60;, and a comment for the team to reject one. Their order in the body does not matter. Accepting charges nothing: the team places the orders for the accepted proposals and your wallet pays for them then. POST /managed-service/campaigns/{id}/proposals/estimate says what they would cost.  When every proposal is accepted the campaign moves to &#x60;proposal_accepted&#x60;; when one is rejected the team is told and prepares others. A proposal someone else moved on the campaign page while the request ran is answered in the state it reached.

### Example

```ts
import {
  Configuration,
  ManagedServicesApi,
} from '@growwer/api';
import type { ReviewManagedServiceProposalsRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ManagedServicesApi(config);

  const body = {
    // string
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
    idempotencyKey: idempotencyKey_example,
    // ManagedServiceProposalReviewRequest
    managedServiceProposalReviewRequest: ...,
  } satisfies ReviewManagedServiceProposalsRequest;

  try {
    const data = await api.reviewManagedServiceProposals(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | [Defaults to `undefined`] |
| **managedServiceProposalReviewRequest** | [ManagedServiceProposalReviewRequest](ManagedServiceProposalReviewRequest.md) |  | |

### Return type

[**ManagedServiceProposalReview**](ManagedServiceProposalReview.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The campaign and the proposals you reviewed, as they now are. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters without spaces (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;). |  -  |
| **404** | The campaign is not yours, or a proposal named is not one of the campaign\&#39;s (code &#x60;not_found&#x60;, with &#x60;details.proposalId&#x60;). |  -  |
| **409** | No proposal of the campaign awaits your review (code &#x60;no_pending_proposals&#x60;), or a proposal named does not (code &#x60;invalid_state&#x60;, with &#x60;details.proposalIds&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The body is invalid (code &#x60;validation_failed&#x60;), or it leaves out proposals awaiting your review (code &#x60;review_incomplete&#x60;, with &#x60;details.missingProposalIds&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

