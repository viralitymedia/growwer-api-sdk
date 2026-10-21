# \AccountAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetMe**](AccountAPI.md#GetMe) | **Get** /api/v1/me | Your account
[**GetVocabulary**](AccountAPI.md#GetVocabulary) | **Get** /api/v1/vocabulary | Codes and names
[**PutSellerHoliday**](AccountAPI.md#PutSellerHoliday) | **Put** /api/v1/seller/holiday | Set your holiday



## GetMe

> GetMe200Response GetMe(ctx).Execute()

Your account



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AccountAPI.GetMe(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccountAPI.GetMe``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMe`: GetMe200Response
	fmt.Fprintf(os.Stdout, "Response from `AccountAPI.GetMe`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetMeRequest struct via the builder pattern


### Return type

[**GetMe200Response**](GetMe200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetVocabulary

> GetVocabulary200Response GetVocabulary(ctx).Execute()

Codes and names



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AccountAPI.GetVocabulary(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccountAPI.GetVocabulary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetVocabulary`: GetVocabulary200Response
	fmt.Fprintf(os.Stdout, "Response from `AccountAPI.GetVocabulary`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetVocabularyRequest struct via the builder pattern


### Return type

[**GetVocabulary200Response**](GetVocabulary200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


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
	openapiclient "github.com/viralitymedia/growwer-api-sdk/go"
)

func main() {
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
	putSellerHolidayRequest := *openapiclient.NewPutSellerHolidayRequest(false) // PutSellerHolidayRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AccountAPI.PutSellerHoliday(context.Background()).IdempotencyKey(idempotencyKey).PutSellerHolidayRequest(putSellerHolidayRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccountAPI.PutSellerHoliday``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PutSellerHoliday`: PutSellerHoliday200Response
	fmt.Fprintf(os.Stdout, "Response from `AccountAPI.PutSellerHoliday`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPutSellerHolidayRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | 
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

