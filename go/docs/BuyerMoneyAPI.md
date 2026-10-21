# \BuyerMoneyAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DownloadBuyerTransactionDocument**](BuyerMoneyAPI.md#DownloadBuyerTransactionDocument) | **Get** /api/v1/wallets/buyer/transactions/{id}/document | Download the document of a wallet movement
[**GetBuyerWallet**](BuyerMoneyAPI.md#GetBuyerWallet) | **Get** /api/v1/wallets/buyer | Get your buyer wallet
[**GetInvoicePdf**](BuyerMoneyAPI.md#GetInvoicePdf) | **Get** /api/v1/invoices/{id}/pdf | Download an invoice
[**ListBuyerTransactions**](BuyerMoneyAPI.md#ListBuyerTransactions) | **Get** /api/v1/wallets/buyer/transactions | List your buyer wallet movements
[**ListInvoices**](BuyerMoneyAPI.md#ListInvoices) | **Get** /api/v1/invoices | List your invoices



## DownloadBuyerTransactionDocument

> *os.File DownloadBuyerTransactionDocument(ctx, id).Execute()

Download the document of a wallet movement



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
	resp, r, err := apiClient.BuyerMoneyAPI.DownloadBuyerTransactionDocument(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerMoneyAPI.DownloadBuyerTransactionDocument``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadBuyerTransactionDocument`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `BuyerMoneyAPI.DownloadBuyerTransactionDocument`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadBuyerTransactionDocumentRequest struct via the builder pattern


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


## GetBuyerWallet

> GetBuyerWallet200Response GetBuyerWallet(ctx).Execute()

Get your buyer wallet



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
	resp, r, err := apiClient.BuyerMoneyAPI.GetBuyerWallet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerMoneyAPI.GetBuyerWallet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBuyerWallet`: GetBuyerWallet200Response
	fmt.Fprintf(os.Stdout, "Response from `BuyerMoneyAPI.GetBuyerWallet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetBuyerWalletRequest struct via the builder pattern


### Return type

[**GetBuyerWallet200Response**](GetBuyerWallet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetInvoicePdf

> *os.File GetInvoicePdf(ctx, id).Execute()

Download an invoice



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
	resp, r, err := apiClient.BuyerMoneyAPI.GetInvoicePdf(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerMoneyAPI.GetInvoicePdf``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetInvoicePdf`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `BuyerMoneyAPI.GetInvoicePdf`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetInvoicePdfRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[***os.File**](*os.File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListBuyerTransactions

> ListBuyerTransactions200Response ListBuyerTransactions(ctx).Limit(limit).Offset(offset).Execute()

List your buyer wallet movements



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
	resp, r, err := apiClient.BuyerMoneyAPI.ListBuyerTransactions(context.Background()).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerMoneyAPI.ListBuyerTransactions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListBuyerTransactions`: ListBuyerTransactions200Response
	fmt.Fprintf(os.Stdout, "Response from `BuyerMoneyAPI.ListBuyerTransactions`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListBuyerTransactionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Movements per page, 1 to 100. | [default to 20]
 **offset** | **int32** | Movements to skip. | [default to 0]

### Return type

[**ListBuyerTransactions200Response**](ListBuyerTransactions200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListInvoices

> ListInvoices200Response ListInvoices(ctx).Limit(limit).Offset(offset).Execute()

List your invoices



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
	limit := int32(56) // int32 | Invoices per page, 1 to 100. (optional) (default to 20)
	offset := int32(56) // int32 | Invoices to skip. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BuyerMoneyAPI.ListInvoices(context.Background()).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BuyerMoneyAPI.ListInvoices``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListInvoices`: ListInvoices200Response
	fmt.Fprintf(os.Stdout, "Response from `BuyerMoneyAPI.ListInvoices`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListInvoicesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Invoices per page, 1 to 100. | [default to 20]
 **offset** | **int32** | Invoices to skip. | [default to 0]

### Return type

[**ListInvoices200Response**](ListInvoices200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

