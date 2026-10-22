# SellerWalletApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadSellerTransactionDocument**](SellerWalletApi.md#downloadsellertransactiondocument) | **GET** /api/v1/wallets/seller/transactions/{id}/document | Download the document of a seller wallet movement |
| [**downloadWithdrawalInvoice**](SellerWalletApi.md#downloadwithdrawalinvoice) | **GET** /api/v1/withdrawals/{id}/invoice | Download the invoice of a withdrawal |
| [**getSellerWallet**](SellerWalletApi.md#getsellerwallet) | **GET** /api/v1/wallets/seller | Get your seller wallet |
| [**listSellerTransactions**](SellerWalletApi.md#listsellertransactions) | **GET** /api/v1/wallets/seller/transactions | List your seller wallet movements |
| [**listWithdrawals**](SellerWalletApi.md#listwithdrawals) | **GET** /api/v1/withdrawals | List your withdrawals |



## downloadSellerTransactionDocument

> Blob downloadSellerTransactionDocument(id)

Download the document of a seller wallet movement

The document Growwer attached to a movement of your seller wallet. 404 when the movement has none (&#x60;hasDocument&#x60; is false) or the file cannot be read.

### Example

```ts
import {
  Configuration,
  SellerWalletApi,
} from '@growwer/api';
import type { DownloadSellerTransactionDocumentRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SellerWalletApi(config);

  const body = {
    // string
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DownloadSellerTransactionDocumentRequest;

  try {
    const data = await api.downloadSellerTransactionDocument(body);
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

**Blob**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document, with its own content type and name. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadWithdrawalInvoice

> Blob downloadWithdrawalInvoice(id)

Download the invoice of a withdrawal

The invoice you uploaded for one of your withdrawals, named &#x60;withdrawal-{id}-invoice.pdf&#x60;. 404 when the withdrawal has none (&#x60;hasInvoice&#x60; is false); 503 &#x60;storage_unavailable&#x60; when the file cannot be read right now.

### Example

```ts
import {
  Configuration,
  SellerWalletApi,
} from '@growwer/api';
import type { DownloadWithdrawalInvoiceRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SellerWalletApi(config);

  const body = {
    // string
    id: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DownloadWithdrawalInvoiceRequest;

  try {
    const data = await api.downloadWithdrawalInvoice(body);
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

**Blob**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The invoice file. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getSellerWallet

> GetSellerWallet200Response getSellerWallet()

Get your seller wallet

What your sales have earned: the balance you can withdraw now and what is held until orders settle. &#x60;restricted&#x60; is true while your seller account is restricted; the reason is not published here, and support can tell you more.

### Example

```ts
import {
  Configuration,
  SellerWalletApi,
} from '@growwer/api';
import type { GetSellerWalletRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SellerWalletApi(config);

  try {
    const data = await api.getSellerWallet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSellerWallet200Response**](GetSellerWallet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your seller wallet. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSellerTransactions

> ListSellerTransactions200Response listSellerTransactions(limit, offset)

List your seller wallet movements

Every movement of your seller wallet, newest first: earnings from orders, withdrawals and manual corrections. An earning names its order (&#x60;orderId&#x60;) and a withdrawal its request (&#x60;withdrawalId&#x60;).

### Example

```ts
import {
  Configuration,
  SellerWalletApi,
} from '@growwer/api';
import type { ListSellerTransactionsRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SellerWalletApi(config);

  const body = {
    // number | Movements per page, 1 to 100. (optional)
    limit: 56,
    // number | Movements to skip. (optional)
    offset: 56,
  } satisfies ListSellerTransactionsRequest;

  try {
    const data = await api.listSellerTransactions(body);
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
| **limit** | `number` | Movements per page, 1 to 100. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Movements to skip. | [Optional] [Defaults to `0`] |

### Return type

[**ListSellerTransactions200Response**](ListSellerTransactions200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of your movements and how many there are in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listWithdrawals

> ListWithdrawals200Response listWithdrawals(state, limit, offset)

List your withdrawals

The withdrawals you requested from your seller wallet, newest first. Requesting a withdrawal is not available through the API; use the seller wallet page.

### Example

```ts
import {
  Configuration,
  SellerWalletApi,
} from '@growwer/api';
import type { ListWithdrawalsRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SellerWalletApi(config);

  const body = {
    // string | Only the withdrawals in one of these states, comma-separated: `started`, `approved`, `rejected`. An unknown state is refused with 422. (optional)
    state: started,
    // number | Withdrawals per page, 1 to 100. (optional)
    limit: 56,
    // number | Withdrawals to skip. (optional)
    offset: 56,
  } satisfies ListWithdrawalsRequest;

  try {
    const data = await api.listWithdrawals(body);
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
| **state** | `string` | Only the withdrawals in one of these states, comma-separated: &#x60;started&#x60;, &#x60;approved&#x60;, &#x60;rejected&#x60;. An unknown state is refused with 422. | [Optional] [Defaults to `undefined`] |
| **limit** | `number` | Withdrawals per page, 1 to 100. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Withdrawals to skip. | [Optional] [Defaults to `0`] |

### Return type

[**ListWithdrawals200Response**](ListWithdrawals200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of your withdrawals and how many match in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications (code &#x60;too_many_failed_authentications&#x60;): with this key from this address, or from this address with any key; a valid key is never refused for it. On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;details.limit&#x60; is the daily cap that applies and &#x60;details.tier&#x60; is &#x60;full&#x60;, or &#x60;trial&#x60; for an account without a recent completed order, whose quota rises to the full cap after one; &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

