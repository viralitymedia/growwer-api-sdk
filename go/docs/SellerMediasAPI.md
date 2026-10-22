# \SellerMediasAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApplySellerMediaCompetitiveFees**](SellerMediasAPI.md#ApplySellerMediaCompetitiveFees) | **Post** /api/v1/seller/medias/{id}/apply-competitive-fees | Set the competitive fees Growwer suggests
[**GetSellerMedia**](SellerMediasAPI.md#GetSellerMedia) | **Get** /api/v1/seller/medias/{id} | Get a media you sell on
[**ListSellerMedias**](SellerMediasAPI.md#ListSellerMedias) | **Get** /api/v1/seller/medias | List the medias you sell on
[**UpdateSellerMedia**](SellerMediasAPI.md#UpdateSellerMedia) | **Patch** /api/v1/seller/medias/{id} | Edit the fees of a media you sell on



## ApplySellerMediaCompetitiveFees

> SellerMedia ApplySellerMediaCompetitiveFees(ctx, id).IdempotencyKey(idempotencyKey).Execute()

Set the competitive fees Growwer suggests



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
	resp, r, err := apiClient.SellerMediasAPI.ApplySellerMediaCompetitiveFees(context.Background(), id).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerMediasAPI.ApplySellerMediaCompetitiveFees``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ApplySellerMediaCompetitiveFees`: SellerMedia
	fmt.Fprintf(os.Stdout, "Response from `SellerMediasAPI.ApplySellerMediaCompetitiveFees`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiApplySellerMediaCompetitiveFeesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSellerMedia

> SellerMedia GetSellerMedia(ctx, id).Execute()

Get a media you sell on



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
	resp, r, err := apiClient.SellerMediasAPI.GetSellerMedia(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerMediasAPI.GetSellerMedia``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSellerMedia`: SellerMedia
	fmt.Fprintf(os.Stdout, "Response from `SellerMediasAPI.GetSellerMedia`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSellerMediaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSellerMedias

> ListSellerMedias200Response ListSellerMedias(ctx).State(state).Sort(sort).Limit(limit).Offset(offset).Execute()

List the medias you sell on



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
	state := "active,deactivated" // string | Only the medias in one of these states, comma-separated: `analyzing`, `pending_review`, `active`, `deactivated`. An unknown state is refused with 422. (optional)
	sort := "sort_example" // string | By creation date, number of published orders or publication rate; a leading `-` sorts descending. Medias with no publication rate come first ascending, last descending. Ties come in id order. (optional) (default to "-createdAt")
	limit := int32(56) // int32 | Medias per page, 1 to 100. (optional) (default to 20)
	offset := int32(56) // int32 | Medias to skip. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerMediasAPI.ListSellerMedias(context.Background()).State(state).Sort(sort).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerMediasAPI.ListSellerMedias``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSellerMedias`: ListSellerMedias200Response
	fmt.Fprintf(os.Stdout, "Response from `SellerMediasAPI.ListSellerMedias`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListSellerMediasRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **string** | Only the medias in one of these states, comma-separated: &#x60;analyzing&#x60;, &#x60;pending_review&#x60;, &#x60;active&#x60;, &#x60;deactivated&#x60;. An unknown state is refused with 422. | 
 **sort** | **string** | By creation date, number of published orders or publication rate; a leading &#x60;-&#x60; sorts descending. Medias with no publication rate come first ascending, last descending. Ties come in id order. | [default to &quot;-createdAt&quot;]
 **limit** | **int32** | Medias per page, 1 to 100. | [default to 20]
 **offset** | **int32** | Medias to skip. | [default to 0]

### Return type

[**ListSellerMedias200Response**](ListSellerMedias200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateSellerMedia

> SellerMedia UpdateSellerMedia(ctx, id).IdempotencyKey(idempotencyKey).UpdateSellerMediaRequest(updateSellerMediaRequest).Execute()

Edit the fees of a media you sell on



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
	updateSellerMediaRequest := *openapiclient.NewUpdateSellerMediaRequest() // UpdateSellerMediaRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerMediasAPI.UpdateSellerMedia(context.Background(), id).IdempotencyKey(idempotencyKey).UpdateSellerMediaRequest(updateSellerMediaRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerMediasAPI.UpdateSellerMedia``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateSellerMedia`: SellerMedia
	fmt.Fprintf(os.Stdout, "Response from `SellerMediasAPI.UpdateSellerMedia`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateSellerMediaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **updateSellerMediaRequest** | [**UpdateSellerMediaRequest**](UpdateSellerMediaRequest.md) |  | 

### Return type

[**SellerMedia**](SellerMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

