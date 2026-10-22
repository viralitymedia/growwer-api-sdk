# \SellerWalletAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DownloadSellerTransactionDocument**](SellerWalletAPI.md#DownloadSellerTransactionDocument) | **Get** /api/v1/wallets/seller/transactions/{id}/document | Download the document of a seller wallet movement
[**DownloadWithdrawalInvoice**](SellerWalletAPI.md#DownloadWithdrawalInvoice) | **Get** /api/v1/withdrawals/{id}/invoice | Download the invoice of a withdrawal
[**GetSellerWallet**](SellerWalletAPI.md#GetSellerWallet) | **Get** /api/v1/wallets/seller | Get your seller wallet
[**ListSellerTransactions**](SellerWalletAPI.md#ListSellerTransactions) | **Get** /api/v1/wallets/seller/transactions | List your seller wallet movements
[**ListWithdrawals**](SellerWalletAPI.md#ListWithdrawals) | **Get** /api/v1/withdrawals | List your withdrawals



## DownloadSellerTransactionDocument

> *os.File DownloadSellerTransactionDocument(ctx, id).Execute()

Download the document of a seller wallet movement



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
	resp, r, err := apiClient.SellerWalletAPI.DownloadSellerTransactionDocument(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerWalletAPI.DownloadSellerTransactionDocument``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadSellerTransactionDocument`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `SellerWalletAPI.DownloadSellerTransactionDocument`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadSellerTransactionDocumentRequest struct via the builder pattern


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


## DownloadWithdrawalInvoice

> *os.File DownloadWithdrawalInvoice(ctx, id).Execute()

Download the invoice of a withdrawal



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
	resp, r, err := apiClient.SellerWalletAPI.DownloadWithdrawalInvoice(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerWalletAPI.DownloadWithdrawalInvoice``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadWithdrawalInvoice`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `SellerWalletAPI.DownloadWithdrawalInvoice`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadWithdrawalInvoiceRequest struct via the builder pattern


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


## GetSellerWallet

> GetSellerWallet200Response GetSellerWallet(ctx).Execute()

Get your seller wallet



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
	resp, r, err := apiClient.SellerWalletAPI.GetSellerWallet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerWalletAPI.GetSellerWallet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSellerWallet`: GetSellerWallet200Response
	fmt.Fprintf(os.Stdout, "Response from `SellerWalletAPI.GetSellerWallet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetSellerWalletRequest struct via the builder pattern


### Return type

[**GetSellerWallet200Response**](GetSellerWallet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSellerTransactions

> ListSellerTransactions200Response ListSellerTransactions(ctx).Limit(limit).Offset(offset).Execute()

List your seller wallet movements



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
	limit := int32(56) // int32 | Movements per page, 1 to 100. (optional) (default to 20)
	offset := int32(56) // int32 | Movements to skip. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerWalletAPI.ListSellerTransactions(context.Background()).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerWalletAPI.ListSellerTransactions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSellerTransactions`: ListSellerTransactions200Response
	fmt.Fprintf(os.Stdout, "Response from `SellerWalletAPI.ListSellerTransactions`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListSellerTransactionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Movements per page, 1 to 100. | [default to 20]
 **offset** | **int32** | Movements to skip. | [default to 0]

### Return type

[**ListSellerTransactions200Response**](ListSellerTransactions200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListWithdrawals

> ListWithdrawals200Response ListWithdrawals(ctx).State(state).Limit(limit).Offset(offset).Execute()

List your withdrawals



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
	state := "started" // string | Only the withdrawals in one of these states, comma-separated: `started`, `approved`, `rejected`. An unknown state is refused with 422. (optional)
	limit := int32(56) // int32 | Withdrawals per page, 1 to 100. (optional) (default to 20)
	offset := int32(56) // int32 | Withdrawals to skip. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SellerWalletAPI.ListWithdrawals(context.Background()).State(state).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SellerWalletAPI.ListWithdrawals``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListWithdrawals`: ListWithdrawals200Response
	fmt.Fprintf(os.Stdout, "Response from `SellerWalletAPI.ListWithdrawals`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListWithdrawalsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **string** | Only the withdrawals in one of these states, comma-separated: &#x60;started&#x60;, &#x60;approved&#x60;, &#x60;rejected&#x60;. An unknown state is refused with 422. | 
 **limit** | **int32** | Withdrawals per page, 1 to 100. | [default to 20]
 **offset** | **int32** | Withdrawals to skip. | [default to 0]

### Return type

[**ListWithdrawals200Response**](ListWithdrawals200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

