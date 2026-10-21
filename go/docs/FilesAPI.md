# \FilesAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**UploadFile**](FilesAPI.md#UploadFile) | **Post** /api/v1/files | Upload a file



## UploadFile

> UploadFile201Response UploadFile(ctx).IdempotencyKey(idempotencyKey).File(file).Execute()

Upload a file



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
	file := os.NewFile(1234, "some_file") // *os.File | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FilesAPI.UploadFile(context.Background()).IdempotencyKey(idempotencyKey).File(file).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FilesAPI.UploadFile``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UploadFile`: UploadFile201Response
	fmt.Fprintf(os.Stdout, "Response from `FilesAPI.UploadFile`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUploadFileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | 
 **file** | ***os.File** |  | 

### Return type

[**UploadFile201Response**](UploadFile201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

