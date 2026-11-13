# \TestHelpersAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AdvanceTestOrder**](TestHelpersAPI.md#AdvanceTestOrder) | **Post** /api/v1/test-helpers/orders/{id}/advance | Advance a test order
[**ResetTestData**](TestHelpersAPI.md#ResetTestData) | **Post** /api/v1/test-helpers/reset | Reset your test data
[**TopUpTestWallet**](TestHelpersAPI.md#TopUpTestWallet) | **Post** /api/v1/test-helpers/wallet/top-up | Top up your test wallet



## AdvanceTestOrder

> Order AdvanceTestOrder(ctx, id).IdempotencyKey(idempotencyKey).AdvanceTestOrderRequest(advanceTestOrderRequest).Execute()

Advance a test order



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v3"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	advanceTestOrderRequest := *openapiclient.NewAdvanceTestOrderRequest("To_example") // AdvanceTestOrderRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TestHelpersAPI.AdvanceTestOrder(context.Background(), id).IdempotencyKey(idempotencyKey).AdvanceTestOrderRequest(advanceTestOrderRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TestHelpersAPI.AdvanceTestOrder``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AdvanceTestOrder`: Order
	fmt.Fprintf(os.Stdout, "Response from `TestHelpersAPI.AdvanceTestOrder`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiAdvanceTestOrderRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **advanceTestOrderRequest** | [**AdvanceTestOrderRequest**](AdvanceTestOrderRequest.md) |  | 

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ResetTestData

> ResetTestData(ctx).IdempotencyKey(idempotencyKey).Execute()

Reset your test data



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v3"
)

func main() {
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TestHelpersAPI.ResetTestData(context.Background()).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TestHelpersAPI.ResetTestData``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiResetTestDataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 

### Return type

 (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TopUpTestWallet

> TopUpTestWallet200Response TopUpTestWallet(ctx).IdempotencyKey(idempotencyKey).TopUpTestWalletRequest(topUpTestWalletRequest).Execute()

Top up your test wallet



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v3"
)

func main() {
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	topUpTestWalletRequest := *openapiclient.NewTopUpTestWalletRequest(*openapiclient.NewMoney(int32(12500), "EUR")) // TopUpTestWalletRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TestHelpersAPI.TopUpTestWallet(context.Background()).IdempotencyKey(idempotencyKey).TopUpTestWalletRequest(topUpTestWalletRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TestHelpersAPI.TopUpTestWallet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TopUpTestWallet`: TopUpTestWallet200Response
	fmt.Fprintf(os.Stdout, "Response from `TestHelpersAPI.TopUpTestWallet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTopUpTestWalletRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **topUpTestWalletRequest** | [**TopUpTestWalletRequest**](TopUpTestWalletRequest.md) |  | 

### Return type

[**TopUpTestWallet200Response**](TopUpTestWallet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

