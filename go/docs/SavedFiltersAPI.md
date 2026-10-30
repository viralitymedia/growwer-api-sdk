# \SavedFiltersAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CountSavedFilterMedias**](SavedFiltersAPI.md#CountSavedFilterMedias) | **Get** /api/v1/projects/{id}/saved-filters/{filterId}/media-count | Count the medias of a saved filter
[**CreateSavedFilter**](SavedFiltersAPI.md#CreateSavedFilter) | **Post** /api/v1/projects/{id}/saved-filters | Save a filter
[**DeleteSavedFilter**](SavedFiltersAPI.md#DeleteSavedFilter) | **Delete** /api/v1/projects/{id}/saved-filters/{filterId} | Delete a saved filter
[**ListSavedFilters**](SavedFiltersAPI.md#ListSavedFilters) | **Get** /api/v1/projects/{id}/saved-filters | List the saved filters of a project



## CountSavedFilterMedias

> CountSavedFilterMedias200Response CountSavedFilterMedias(ctx, id, filterId).Execute()

Count the medias of a saved filter



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The project.
	filterId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The saved filter.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SavedFiltersAPI.CountSavedFilterMedias(context.Background(), id, filterId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SavedFiltersAPI.CountSavedFilterMedias``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CountSavedFilterMedias`: CountSavedFilterMedias200Response
	fmt.Fprintf(os.Stdout, "Response from `SavedFiltersAPI.CountSavedFilterMedias`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | The project. | 
**filterId** | **string** | The saved filter. | 

### Other Parameters

Other parameters are passed through a pointer to a apiCountSavedFilterMediasRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**CountSavedFilterMedias200Response**](CountSavedFilterMedias200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateSavedFilter

> SavedFilter CreateSavedFilter(ctx, id).IdempotencyKey(idempotencyKey).CreateSavedFilterRequest(createSavedFilterRequest).Execute()

Save a filter



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The project.
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	createSavedFilterRequest := *openapiclient.NewCreateSavedFilterRequest("Name_example", map[string]interface{}{"key": interface{}(123)}) // CreateSavedFilterRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SavedFiltersAPI.CreateSavedFilter(context.Background(), id).IdempotencyKey(idempotencyKey).CreateSavedFilterRequest(createSavedFilterRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SavedFiltersAPI.CreateSavedFilter``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateSavedFilter`: SavedFilter
	fmt.Fprintf(os.Stdout, "Response from `SavedFiltersAPI.CreateSavedFilter`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | The project. | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateSavedFilterRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **createSavedFilterRequest** | [**CreateSavedFilterRequest**](CreateSavedFilterRequest.md) |  | 

### Return type

[**SavedFilter**](SavedFilter.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteSavedFilter

> DeleteSavedFilter(ctx, id, filterId).IdempotencyKey(idempotencyKey).Execute()

Delete a saved filter



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The project.
	filterId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The saved filter.
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.SavedFiltersAPI.DeleteSavedFilter(context.Background(), id, filterId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SavedFiltersAPI.DeleteSavedFilter``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | The project. | 
**filterId** | **string** | The saved filter. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteSavedFilterRequest struct via the builder pattern


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


## ListSavedFilters

> ListSavedFilters200Response ListSavedFilters(ctx, id).Execute()

List the saved filters of a project



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The project.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SavedFiltersAPI.ListSavedFilters(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SavedFiltersAPI.ListSavedFilters``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSavedFilters`: ListSavedFilters200Response
	fmt.Fprintf(os.Stdout, "Response from `SavedFiltersAPI.ListSavedFilters`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | The project. | 

### Other Parameters

Other parameters are passed through a pointer to a apiListSavedFiltersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ListSavedFilters200Response**](ListSavedFilters200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

