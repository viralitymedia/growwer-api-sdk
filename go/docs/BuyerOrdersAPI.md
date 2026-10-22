# \BuyerOrdersAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApproveOrder**](BuyerOrdersAPI.md#ApproveOrder) | **Post** /api/v1/orders/{id}/approve | Approve an order&#39;s delivery
[**ApproveOrderDraft**](BuyerOrdersAPI.md#ApproveOrderDraft) | **Post** /api/v1/orders/{id}/approve-draft | Approve a draft
[**CancelOrder**](BuyerOrdersAPI.md#CancelOrder) | **Post** /api/v1/orders/{id}/cancel | Cancel an order
[**CreateOrder**](BuyerOrdersAPI.md#CreateOrder) | **Post** /api/v1/orders | Place an order
[**DownloadOrderBriefing**](BuyerOrdersAPI.md#DownloadOrderBriefing) | **Get** /api/v1/orders/{id}/briefing | Download the draft you attached to an order
[**DownloadOrderDraft**](BuyerOrdersAPI.md#DownloadOrderDraft) | **Get** /api/v1/orders/{id}/draft | Download the draft of an order
[**EstimateOrder**](BuyerOrdersAPI.md#EstimateOrder) | **Post** /api/v1/orders/estimate | Estimate an order
[**GetOrder**](BuyerOrdersAPI.md#GetOrder) | **Get** /api/v1/orders/{id} | Get an order
[**ListOrders**](BuyerOrdersAPI.md#ListOrders) | **Get** /api/v1/orders | List your orders
[**RequestOrderDraftUpdate**](BuyerOrdersAPI.md#RequestOrderDraftUpdate) | **Post** /api/v1/orders/{id}/request-draft-update | Request changes to a draft
[**RequestOrderUpdate**](BuyerOrdersAPI.md#RequestOrderUpdate) | **Post** /api/v1/orders/{id}/request-update | Request changes to a delivery



## ApproveOrder

> Order ApproveOrder(ctx, id).IdempotencyKey(idempotencyKey).Execute()

Approve an order's delivery



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerOrdersAPI.ApproveOrder(context.Background(), id).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerOrdersAPI.ApproveOrder``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ApproveOrder`: Order
	fmt.Fprintf(os.Stdout, "Response from `BuyerOrdersAPI.ApproveOrder`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiApproveOrderRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ApproveOrderDraft

> Order ApproveOrderDraft(ctx, id).IdempotencyKey(idempotencyKey).Execute()

Approve a draft



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerOrdersAPI.ApproveOrderDraft(context.Background(), id).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerOrdersAPI.ApproveOrderDraft``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ApproveOrderDraft`: Order
	fmt.Fprintf(os.Stdout, "Response from `BuyerOrdersAPI.ApproveOrderDraft`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiApproveOrderDraftRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 

### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CancelOrder

> Order CancelOrder(ctx, id).IdempotencyKey(idempotencyKey).OrderActionReason(orderActionReason).Execute()

Cancel an order



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	orderActionReason := *openapiclient.NewOrderActionReason("Reason_example") // OrderActionReason | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerOrdersAPI.CancelOrder(context.Background(), id).IdempotencyKey(idempotencyKey).OrderActionReason(orderActionReason).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerOrdersAPI.CancelOrder``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CancelOrder`: Order
	fmt.Fprintf(os.Stdout, "Response from `BuyerOrdersAPI.CancelOrder`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCancelOrderRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **orderActionReason** | [**OrderActionReason**](OrderActionReason.md) |  | 

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


## CreateOrder

> Order CreateOrder(ctx).IdempotencyKey(idempotencyKey).OrderCreateRequest(orderCreateRequest).Execute()

Place an order



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	orderCreateRequest := *openapiclient.NewOrderCreateRequest("Type_example", "ProjectId_example", "MediaId_example", openapiclient.OrderEstimateRequest_briefing{LinkAdditionOrderBriefingRequest: openapiclient.NewLinkAdditionOrderBriefingRequest("LinkingFrom_example", *openapiclient.NewOrderLinkRequest("Type_example"))}, *openapiclient.NewMoney(int32(12500), "EUR")) // OrderCreateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerOrdersAPI.CreateOrder(context.Background()).IdempotencyKey(idempotencyKey).OrderCreateRequest(orderCreateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerOrdersAPI.CreateOrder``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateOrder`: Order
	fmt.Fprintf(os.Stdout, "Response from `BuyerOrdersAPI.CreateOrder`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateOrderRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **orderCreateRequest** | [**OrderCreateRequest**](OrderCreateRequest.md) |  | 

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


## DownloadOrderBriefing

> *os.File DownloadOrderBriefing(ctx, id).Execute()

Download the draft you attached to an order



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerOrdersAPI.DownloadOrderBriefing(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerOrdersAPI.DownloadOrderBriefing``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadOrderBriefing`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `BuyerOrdersAPI.DownloadOrderBriefing`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadOrderBriefingRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[***os.File**](*os.File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadOrderDraft

> *os.File DownloadOrderDraft(ctx, id).Execute()

Download the draft of an order



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerOrdersAPI.DownloadOrderDraft(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerOrdersAPI.DownloadOrderDraft``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadOrderDraft`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `BuyerOrdersAPI.DownloadOrderDraft`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadOrderDraftRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[***os.File**](*os.File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## EstimateOrder

> OrderEstimate EstimateOrder(ctx).OrderEstimateRequest(orderEstimateRequest).Execute()

Estimate an order



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	orderEstimateRequest := *openapiclient.NewOrderEstimateRequest("Type_example", "ProjectId_example", "MediaId_example", openapiclient.OrderEstimateRequest_briefing{LinkAdditionOrderBriefingRequest: openapiclient.NewLinkAdditionOrderBriefingRequest("LinkingFrom_example", *openapiclient.NewOrderLinkRequest("Type_example"))}) // OrderEstimateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerOrdersAPI.EstimateOrder(context.Background()).OrderEstimateRequest(orderEstimateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerOrdersAPI.EstimateOrder``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `EstimateOrder`: OrderEstimate
	fmt.Fprintf(os.Stdout, "Response from `BuyerOrdersAPI.EstimateOrder`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiEstimateOrderRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderEstimateRequest** | [**OrderEstimateRequest**](OrderEstimateRequest.md) |  | 

### Return type

[**OrderEstimate**](OrderEstimate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetOrder

> Order GetOrder(ctx, id).Execute()

Get an order



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerOrdersAPI.GetOrder(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerOrdersAPI.GetOrder``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetOrder`: Order
	fmt.Fprintf(os.Stdout, "Response from `BuyerOrdersAPI.GetOrder`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetOrderRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Order**](Order.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListOrders

> ListOrders200Response ListOrders(ctx).ProjectId(projectId).MediaId(mediaId).State(state).UpdatedSince(updatedSince).Sort(sort).Limit(limit).Offset(offset).Execute()

List your orders



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Only the orders of this project of yours. (optional)
	mediaId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Only the orders on this media. (optional)
	state := "pending_acceptance,pending_order_delivery" // string | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones. (optional)
	updatedSince := time.Now() // time.Time | Only the orders whose `updatedAt` is at or after this instant, an ISO-8601 date-time with its offset (send `+` as `%2B`). (optional)
	sort := "sort_example" // string | `-createdAt`, newest first, or `updatedAt`, least recently changed first. Orders of the same instant come in id order. (optional) (default to "-createdAt")
	limit := int32(56) // int32 | Orders per page, 1 to 100. (optional) (default to 20)
	offset := int32(56) // int32 | Orders to skip. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerOrdersAPI.ListOrders(context.Background()).ProjectId(projectId).MediaId(mediaId).State(state).UpdatedSince(updatedSince).Sort(sort).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerOrdersAPI.ListOrders``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListOrders`: ListOrders200Response
	fmt.Fprintf(os.Stdout, "Response from `BuyerOrdersAPI.ListOrders`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListOrdersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **string** | Only the orders of this project of yours. | 
 **mediaId** | **string** | Only the orders on this media. | 
 **state** | **string** | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones. | 
 **updatedSince** | **time.Time** | Only the orders whose &#x60;updatedAt&#x60; is at or after this instant, an ISO-8601 date-time with its offset (send &#x60;+&#x60; as &#x60;%2B&#x60;). | 
 **sort** | **string** | &#x60;-createdAt&#x60;, newest first, or &#x60;updatedAt&#x60;, least recently changed first. Orders of the same instant come in id order. | [default to &quot;-createdAt&quot;]
 **limit** | **int32** | Orders per page, 1 to 100. | [default to 20]
 **offset** | **int32** | Orders to skip. | [default to 0]

### Return type

[**ListOrders200Response**](ListOrders200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RequestOrderDraftUpdate

> Order RequestOrderDraftUpdate(ctx, id).IdempotencyKey(idempotencyKey).OrderActionReason(orderActionReason).Execute()

Request changes to a draft



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	orderActionReason := *openapiclient.NewOrderActionReason("Reason_example") // OrderActionReason | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerOrdersAPI.RequestOrderDraftUpdate(context.Background(), id).IdempotencyKey(idempotencyKey).OrderActionReason(orderActionReason).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerOrdersAPI.RequestOrderDraftUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RequestOrderDraftUpdate`: Order
	fmt.Fprintf(os.Stdout, "Response from `BuyerOrdersAPI.RequestOrderDraftUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRequestOrderDraftUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **orderActionReason** | [**OrderActionReason**](OrderActionReason.md) |  | 

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


## RequestOrderUpdate

> Order RequestOrderUpdate(ctx, id).IdempotencyKey(idempotencyKey).OrderActionReason(orderActionReason).Execute()

Request changes to a delivery



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	orderActionReason := *openapiclient.NewOrderActionReason("Reason_example") // OrderActionReason | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerOrdersAPI.RequestOrderUpdate(context.Background(), id).IdempotencyKey(idempotencyKey).OrderActionReason(orderActionReason).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerOrdersAPI.RequestOrderUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RequestOrderUpdate`: Order
	fmt.Fprintf(os.Stdout, "Response from `BuyerOrdersAPI.RequestOrderUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRequestOrderUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **orderActionReason** | [**OrderActionReason**](OrderActionReason.md) |  | 

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

