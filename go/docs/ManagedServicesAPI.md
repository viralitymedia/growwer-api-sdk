# \ManagedServicesAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**EstimateManagedServiceProposals**](ManagedServicesAPI.md#EstimateManagedServiceProposals) | **Post** /api/v1/managed-service/campaigns/{id}/proposals/estimate | Estimate accepting proposals
[**GetManagedServiceCampaign**](ManagedServicesAPI.md#GetManagedServiceCampaign) | **Get** /api/v1/managed-service/campaigns/{id} | Get a managed service campaign
[**GetManagedServiceProposalsSummary**](ManagedServicesAPI.md#GetManagedServiceProposalsSummary) | **Get** /api/v1/managed-service/campaigns/{id}/proposals-summary | Download the summary of a campaign&#39;s proposals
[**ListManagedServiceCampaigns**](ManagedServicesAPI.md#ListManagedServiceCampaigns) | **Get** /api/v1/managed-service/campaigns | List your managed service campaigns
[**ListManagedServiceProposals**](ManagedServicesAPI.md#ListManagedServiceProposals) | **Get** /api/v1/managed-service/campaigns/{id}/proposals | List the proposals of a campaign
[**RequestManagedServiceCampaign**](ManagedServicesAPI.md#RequestManagedServiceCampaign) | **Post** /api/v1/managed-service/campaign-requests | Request a new campaign
[**RequestManagedServiceInfo**](ManagedServicesAPI.md#RequestManagedServiceInfo) | **Post** /api/v1/managed-service/info-requests | Ask about the managed service
[**ReviewManagedServiceProposals**](ManagedServicesAPI.md#ReviewManagedServiceProposals) | **Post** /api/v1/managed-service/campaigns/{id}/proposals/review | Accept or reject proposals



## EstimateManagedServiceProposals

> ManagedServiceProposalsEstimate EstimateManagedServiceProposals(ctx, id).ManagedServiceProposalsEstimateRequest(managedServiceProposalsEstimateRequest).Execute()

Estimate accepting proposals



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
	managedServiceProposalsEstimateRequest := *openapiclient.NewManagedServiceProposalsEstimateRequest() // ManagedServiceProposalsEstimateRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ManagedServicesAPI.EstimateManagedServiceProposals(context.Background(), id).ManagedServiceProposalsEstimateRequest(managedServiceProposalsEstimateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManagedServicesAPI.EstimateManagedServiceProposals``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `EstimateManagedServiceProposals`: ManagedServiceProposalsEstimate
	fmt.Fprintf(os.Stdout, "Response from `ManagedServicesAPI.EstimateManagedServiceProposals`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiEstimateManagedServiceProposalsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **managedServiceProposalsEstimateRequest** | [**ManagedServiceProposalsEstimateRequest**](ManagedServiceProposalsEstimateRequest.md) |  | 

### Return type

[**ManagedServiceProposalsEstimate**](ManagedServiceProposalsEstimate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetManagedServiceCampaign

> ManagedServiceCampaign GetManagedServiceCampaign(ctx, id).Execute()

Get a managed service campaign

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
	resp, r, err := apiClient.ManagedServicesAPI.GetManagedServiceCampaign(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManagedServicesAPI.GetManagedServiceCampaign``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetManagedServiceCampaign`: ManagedServiceCampaign
	fmt.Fprintf(os.Stdout, "Response from `ManagedServicesAPI.GetManagedServiceCampaign`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetManagedServiceCampaignRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ManagedServiceCampaign**](ManagedServiceCampaign.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetManagedServiceProposalsSummary

> *os.File GetManagedServiceProposalsSummary(ctx, id).Extended(extended).Execute()

Download the summary of a campaign's proposals



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
	extended := "extended_example" // string | Whether to show the prices. (optional) (default to "false")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ManagedServicesAPI.GetManagedServiceProposalsSummary(context.Background(), id).Extended(extended).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManagedServicesAPI.GetManagedServiceProposalsSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetManagedServiceProposalsSummary`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `ManagedServicesAPI.GetManagedServiceProposalsSummary`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetManagedServiceProposalsSummaryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **extended** | **string** | Whether to show the prices. | [default to &quot;false&quot;]

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


## ListManagedServiceCampaigns

> ListManagedServiceCampaigns200Response ListManagedServiceCampaigns(ctx).Limit(limit).Offset(offset).Execute()

List your managed service campaigns



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
	limit := int32(56) // int32 | Campaigns per page, 1 to 100. (optional) (default to 20)
	offset := int32(56) // int32 | Campaigns to skip. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ManagedServicesAPI.ListManagedServiceCampaigns(context.Background()).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManagedServicesAPI.ListManagedServiceCampaigns``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListManagedServiceCampaigns`: ListManagedServiceCampaigns200Response
	fmt.Fprintf(os.Stdout, "Response from `ManagedServicesAPI.ListManagedServiceCampaigns`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListManagedServiceCampaignsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Campaigns per page, 1 to 100. | [default to 20]
 **offset** | **int32** | Campaigns to skip. | [default to 0]

### Return type

[**ListManagedServiceCampaigns200Response**](ListManagedServiceCampaigns200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListManagedServiceProposals

> ListManagedServiceProposals200Response ListManagedServiceProposals(ctx, id).State(state).Limit(limit).Offset(offset).Execute()

List the proposals of a campaign



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
	state := "proposed,accepted" // string | Only proposals in these states, comma-separated: `proposed`, `accepted`, `cancelled`, `purchase_started`, `purchase_finished`. (optional)
	limit := int32(56) // int32 | Proposals per page, 1 to 100. (optional) (default to 20)
	offset := int32(56) // int32 | Proposals to skip. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ManagedServicesAPI.ListManagedServiceProposals(context.Background(), id).State(state).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManagedServicesAPI.ListManagedServiceProposals``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListManagedServiceProposals`: ListManagedServiceProposals200Response
	fmt.Fprintf(os.Stdout, "Response from `ManagedServicesAPI.ListManagedServiceProposals`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListManagedServiceProposalsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **state** | **string** | Only proposals in these states, comma-separated: &#x60;proposed&#x60;, &#x60;accepted&#x60;, &#x60;cancelled&#x60;, &#x60;purchase_started&#x60;, &#x60;purchase_finished&#x60;. | 
 **limit** | **int32** | Proposals per page, 1 to 100. | [default to 20]
 **offset** | **int32** | Proposals to skip. | [default to 0]

### Return type

[**ListManagedServiceProposals200Response**](ListManagedServiceProposals200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RequestManagedServiceCampaign

> ManagedServiceRequestSent RequestManagedServiceCampaign(ctx).IdempotencyKey(idempotencyKey).ManagedServiceRequest(managedServiceRequest).Execute()

Request a new campaign



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
	managedServiceRequest := *openapiclient.NewManagedServiceRequest("ProjectUrl_example", "Goal_example", "Country_example", "Duration_example", *openapiclient.NewMoney(int32(12500), "EUR")) // ManagedServiceRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ManagedServicesAPI.RequestManagedServiceCampaign(context.Background()).IdempotencyKey(idempotencyKey).ManagedServiceRequest(managedServiceRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManagedServicesAPI.RequestManagedServiceCampaign``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RequestManagedServiceCampaign`: ManagedServiceRequestSent
	fmt.Fprintf(os.Stdout, "Response from `ManagedServicesAPI.RequestManagedServiceCampaign`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRequestManagedServiceCampaignRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **managedServiceRequest** | [**ManagedServiceRequest**](ManagedServiceRequest.md) |  | 

### Return type

[**ManagedServiceRequestSent**](ManagedServiceRequestSent.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RequestManagedServiceInfo

> ManagedServiceRequestSent RequestManagedServiceInfo(ctx).IdempotencyKey(idempotencyKey).ManagedServiceRequest(managedServiceRequest).Execute()

Ask about the managed service



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
	managedServiceRequest := *openapiclient.NewManagedServiceRequest("ProjectUrl_example", "Goal_example", "Country_example", "Duration_example", *openapiclient.NewMoney(int32(12500), "EUR")) // ManagedServiceRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ManagedServicesAPI.RequestManagedServiceInfo(context.Background()).IdempotencyKey(idempotencyKey).ManagedServiceRequest(managedServiceRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManagedServicesAPI.RequestManagedServiceInfo``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RequestManagedServiceInfo`: ManagedServiceRequestSent
	fmt.Fprintf(os.Stdout, "Response from `ManagedServicesAPI.RequestManagedServiceInfo`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRequestManagedServiceInfoRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **managedServiceRequest** | [**ManagedServiceRequest**](ManagedServiceRequest.md) |  | 

### Return type

[**ManagedServiceRequestSent**](ManagedServiceRequestSent.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ReviewManagedServiceProposals

> ManagedServiceProposalReview ReviewManagedServiceProposals(ctx, id).IdempotencyKey(idempotencyKey).ManagedServiceProposalReviewRequest(managedServiceProposalReviewRequest).Execute()

Accept or reject proposals



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
	managedServiceProposalReviewRequest := *openapiclient.NewManagedServiceProposalReviewRequest([]openapiclient.ManagedServiceProposalReviewRequestReviewsInner{*openapiclient.NewManagedServiceProposalReviewRequestReviewsInner("ProposalId_example", "Decision_example")}) // ManagedServiceProposalReviewRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ManagedServicesAPI.ReviewManagedServiceProposals(context.Background(), id).IdempotencyKey(idempotencyKey).ManagedServiceProposalReviewRequest(managedServiceProposalReviewRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManagedServicesAPI.ReviewManagedServiceProposals``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ReviewManagedServiceProposals`: ManagedServiceProposalReview
	fmt.Fprintf(os.Stdout, "Response from `ManagedServicesAPI.ReviewManagedServiceProposals`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiReviewManagedServiceProposalsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **managedServiceProposalReviewRequest** | [**ManagedServiceProposalReviewRequest**](ManagedServiceProposalReviewRequest.md) |  | 

### Return type

[**ManagedServiceProposalReview**](ManagedServiceProposalReview.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

