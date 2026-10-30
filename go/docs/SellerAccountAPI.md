# \SellerAccountAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**PutSellerHoliday**](SellerAccountAPI.md#PutSellerHoliday) | **Put** /api/v1/seller/holiday | Set your holiday



## PutSellerHoliday

> PutSellerHoliday200Response PutSellerHoliday(ctx).IdempotencyKey(idempotencyKey).PutSellerHolidayRequest(putSellerHolidayRequest).Execute()

Set your holiday



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
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	putSellerHolidayRequest := *openapiclient.NewPutSellerHolidayRequest(false) // PutSellerHolidayRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerAccountAPI.PutSellerHoliday(context.Background()).IdempotencyKey(idempotencyKey).PutSellerHolidayRequest(putSellerHolidayRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerAccountAPI.PutSellerHoliday``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PutSellerHoliday`: PutSellerHoliday200Response
	fmt.Fprintf(os.Stdout, "Response from `SellerAccountAPI.PutSellerHoliday`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPutSellerHolidayRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **putSellerHolidayRequest** | [**PutSellerHolidayRequest**](PutSellerHolidayRequest.md) |  | 

### Return type

[**PutSellerHoliday200Response**](PutSellerHoliday200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

