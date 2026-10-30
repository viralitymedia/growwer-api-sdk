# \SellerOrdersAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AcceptSellerOrder**](SellerOrdersAPI.md#AcceptSellerOrder) | **Post** /api/v1/seller/orders/{id}/accept | Accept an order
[**DeliverSellerOrder**](SellerOrdersAPI.md#DeliverSellerOrder) | **Post** /api/v1/seller/orders/{id}/deliver | Deliver an order
[**DeliverSellerOrderDraft**](SellerOrdersAPI.md#DeliverSellerOrderDraft) | **Post** /api/v1/seller/orders/{id}/deliver-draft | Deliver a draft
[**DeliverSellerOrderDraftUpdate**](SellerOrdersAPI.md#DeliverSellerOrderDraftUpdate) | **Post** /api/v1/seller/orders/{id}/deliver-draft-update | Deliver a draft update
[**DeliverSellerOrderUpdate**](SellerOrdersAPI.md#DeliverSellerOrderUpdate) | **Post** /api/v1/seller/orders/{id}/deliver-update | Deliver an update
[**DownloadSellerOrderBriefing**](SellerOrdersAPI.md#DownloadSellerOrderBriefing) | **Get** /api/v1/seller/orders/{id}/briefing | Download the draft the buyer attached to an order
[**DownloadSellerOrderDraft**](SellerOrdersAPI.md#DownloadSellerOrderDraft) | **Get** /api/v1/seller/orders/{id}/draft | Download the draft of an order you sell
[**GetSellerOrder**](SellerOrdersAPI.md#GetSellerOrder) | **Get** /api/v1/seller/orders/{id} | Get an order you sell
[**ListSellerOrders**](SellerOrdersAPI.md#ListSellerOrders) | **Get** /api/v1/seller/orders | List the orders you sell
[**RefuteSellerOrderDraftUpdate**](SellerOrdersAPI.md#RefuteSellerOrderDraftUpdate) | **Post** /api/v1/seller/orders/{id}/refute-draft-update | Refuse a draft update
[**RefuteSellerOrderUpdate**](SellerOrdersAPI.md#RefuteSellerOrderUpdate) | **Post** /api/v1/seller/orders/{id}/refute-update | Refuse an update
[**RejectSellerOrder**](SellerOrdersAPI.md#RejectSellerOrder) | **Post** /api/v1/seller/orders/{id}/reject | Reject an order



## AcceptSellerOrder

> SellerOrder AcceptSellerOrder(ctx, id).IdempotencyKey(idempotencyKey).Execute()

Accept an order



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.AcceptSellerOrder(context.Background(), id).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.AcceptSellerOrder``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AcceptSellerOrder`: SellerOrder
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.AcceptSellerOrder`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiAcceptSellerOrderRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeliverSellerOrder

> SellerOrder DeliverSellerOrder(ctx, id).IdempotencyKey(idempotencyKey).SellerOrderPostDelivery(sellerOrderPostDelivery).Execute()

Deliver an order



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	sellerOrderPostDelivery := *openapiclient.NewSellerOrderPostDelivery("Url_example", false) // SellerOrderPostDelivery |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.DeliverSellerOrder(context.Background(), id).IdempotencyKey(idempotencyKey).SellerOrderPostDelivery(sellerOrderPostDelivery).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.DeliverSellerOrder``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeliverSellerOrder`: SellerOrder
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.DeliverSellerOrder`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeliverSellerOrderRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **sellerOrderPostDelivery** | [**SellerOrderPostDelivery**](SellerOrderPostDelivery.md) |  | 

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeliverSellerOrderDraft

> SellerOrder DeliverSellerOrderDraft(ctx, id).IdempotencyKey(idempotencyKey).SellerOrderDraftFile(sellerOrderDraftFile).Execute()

Deliver a draft



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	sellerOrderDraftFile := *openapiclient.NewSellerOrderDraftFile("FileId_example") // SellerOrderDraftFile | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.DeliverSellerOrderDraft(context.Background(), id).IdempotencyKey(idempotencyKey).SellerOrderDraftFile(sellerOrderDraftFile).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.DeliverSellerOrderDraft``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeliverSellerOrderDraft`: SellerOrder
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.DeliverSellerOrderDraft`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeliverSellerOrderDraftRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **sellerOrderDraftFile** | [**SellerOrderDraftFile**](SellerOrderDraftFile.md) |  | 

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeliverSellerOrderDraftUpdate

> SellerOrder DeliverSellerOrderDraftUpdate(ctx, id).IdempotencyKey(idempotencyKey).SellerOrderDraftFile(sellerOrderDraftFile).Execute()

Deliver a draft update



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	sellerOrderDraftFile := *openapiclient.NewSellerOrderDraftFile("FileId_example") // SellerOrderDraftFile | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.DeliverSellerOrderDraftUpdate(context.Background(), id).IdempotencyKey(idempotencyKey).SellerOrderDraftFile(sellerOrderDraftFile).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.DeliverSellerOrderDraftUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeliverSellerOrderDraftUpdate`: SellerOrder
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.DeliverSellerOrderDraftUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeliverSellerOrderDraftUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **sellerOrderDraftFile** | [**SellerOrderDraftFile**](SellerOrderDraftFile.md) |  | 

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeliverSellerOrderUpdate

> SellerOrder DeliverSellerOrderUpdate(ctx, id).IdempotencyKey(idempotencyKey).SellerOrderPostDelivery(sellerOrderPostDelivery).Execute()

Deliver an update



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	sellerOrderPostDelivery := *openapiclient.NewSellerOrderPostDelivery("Url_example", false) // SellerOrderPostDelivery |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.DeliverSellerOrderUpdate(context.Background(), id).IdempotencyKey(idempotencyKey).SellerOrderPostDelivery(sellerOrderPostDelivery).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.DeliverSellerOrderUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeliverSellerOrderUpdate`: SellerOrder
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.DeliverSellerOrderUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeliverSellerOrderUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **sellerOrderPostDelivery** | [**SellerOrderPostDelivery**](SellerOrderPostDelivery.md) |  | 

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadSellerOrderBriefing

> *os.File DownloadSellerOrderBriefing(ctx, id).Execute()

Download the draft the buyer attached to an order



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.DownloadSellerOrderBriefing(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.DownloadSellerOrderBriefing``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadSellerOrderBriefing`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.DownloadSellerOrderBriefing`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadSellerOrderBriefingRequest struct via the builder pattern


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


## DownloadSellerOrderDraft

> *os.File DownloadSellerOrderDraft(ctx, id).Execute()

Download the draft of an order you sell



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.DownloadSellerOrderDraft(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.DownloadSellerOrderDraft``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadSellerOrderDraft`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.DownloadSellerOrderDraft`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadSellerOrderDraftRequest struct via the builder pattern


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


## GetSellerOrder

> SellerOrder GetSellerOrder(ctx, id).Execute()

Get an order you sell



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.GetSellerOrder(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.GetSellerOrder``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSellerOrder`: SellerOrder
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.GetSellerOrder`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSellerOrderRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSellerOrders

> ListSellerOrders200Response ListSellerOrders(ctx).MediaId(mediaId).State(state).UpdatedSince(updatedSince).Sort(sort).Limit(limit).Offset(offset).Execute()

List the orders you sell



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	mediaId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Only the orders on this media of yours. (optional)
	state := "pending_acceptance,pending_order_delivery" // string | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones. (optional)
	updatedSince := time.Now() // time.Time | Only the orders whose `updatedAt` is at or after this instant, an ISO-8601 date-time with its offset (send `+` as `%2B`). (optional)
	sort := "sort_example" // string | `-createdAt`, newest first, or `updatedAt`, least recently changed first. Orders of the same instant come in id order. (optional) (default to "-createdAt")
	limit := int32(56) // int32 | Orders per page, 1 to 100. (optional) (default to 20)
	offset := int32(56) // int32 | Orders to skip. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.ListSellerOrders(context.Background()).MediaId(mediaId).State(state).UpdatedSince(updatedSince).Sort(sort).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.ListSellerOrders``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSellerOrders`: ListSellerOrders200Response
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.ListSellerOrders`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListSellerOrdersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaId** | **string** | Only the orders on this media of yours. | 
 **state** | **string** | Only the orders in one of these states, comma-separated. An unknown state is refused with 422 and the list of valid ones. | 
 **updatedSince** | **time.Time** | Only the orders whose &#x60;updatedAt&#x60; is at or after this instant, an ISO-8601 date-time with its offset (send &#x60;+&#x60; as &#x60;%2B&#x60;). | 
 **sort** | **string** | &#x60;-createdAt&#x60;, newest first, or &#x60;updatedAt&#x60;, least recently changed first. Orders of the same instant come in id order. | [default to &quot;-createdAt&quot;]
 **limit** | **int32** | Orders per page, 1 to 100. | [default to 20]
 **offset** | **int32** | Orders to skip. | [default to 0]

### Return type

[**ListSellerOrders200Response**](ListSellerOrders200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RefuteSellerOrderDraftUpdate

> SellerOrder RefuteSellerOrderDraftUpdate(ctx, id).IdempotencyKey(idempotencyKey).SellerOrderRefutation(sellerOrderRefutation).Execute()

Refuse a draft update



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	sellerOrderRefutation := *openapiclient.NewSellerOrderRefutation("Reason_example") // SellerOrderRefutation | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.RefuteSellerOrderDraftUpdate(context.Background(), id).IdempotencyKey(idempotencyKey).SellerOrderRefutation(sellerOrderRefutation).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.RefuteSellerOrderDraftUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RefuteSellerOrderDraftUpdate`: SellerOrder
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.RefuteSellerOrderDraftUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRefuteSellerOrderDraftUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **sellerOrderRefutation** | [**SellerOrderRefutation**](SellerOrderRefutation.md) |  | 

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RefuteSellerOrderUpdate

> SellerOrder RefuteSellerOrderUpdate(ctx, id).IdempotencyKey(idempotencyKey).SellerOrderRefutation(sellerOrderRefutation).Execute()

Refuse an update



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	sellerOrderRefutation := *openapiclient.NewSellerOrderRefutation("Reason_example") // SellerOrderRefutation | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.RefuteSellerOrderUpdate(context.Background(), id).IdempotencyKey(idempotencyKey).SellerOrderRefutation(sellerOrderRefutation).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.RefuteSellerOrderUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RefuteSellerOrderUpdate`: SellerOrder
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.RefuteSellerOrderUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRefuteSellerOrderUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **sellerOrderRefutation** | [**SellerOrderRefutation**](SellerOrderRefutation.md) |  | 

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RejectSellerOrder

> SellerOrder RejectSellerOrder(ctx, id).IdempotencyKey(idempotencyKey).SellerOrderRejection(sellerOrderRejection).Execute()

Reject an order



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go/v2"
)

func main() {
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	sellerOrderRejection := *openapiclient.NewSellerOrderRejection(*openapiclient.NewSellerOrderRejectionReason("Name_example")) // SellerOrderRejection | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerOrdersAPI.RejectSellerOrder(context.Background(), id).IdempotencyKey(idempotencyKey).SellerOrderRejection(sellerOrderRejection).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerOrdersAPI.RejectSellerOrder``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RejectSellerOrder`: SellerOrder
	fmt.Fprintf(os.Stdout, "Response from `SellerOrdersAPI.RejectSellerOrder`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRejectSellerOrderRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **sellerOrderRejection** | [**SellerOrderRejection**](SellerOrderRejection.md) |  | 

### Return type

[**SellerOrder**](SellerOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

