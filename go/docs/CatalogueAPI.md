# \CatalogueAPI

All URIs are relative to *https://tool.growwer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DiscardMedia**](CatalogueAPI.md#DiscardMedia) | **Put** /api/v1/projects/{id}/discards/{mediaId} | Discard a media for a project
[**FavouriteMedia**](CatalogueAPI.md#FavouriteMedia) | **Put** /api/v1/projects/{id}/favourites/{mediaId} | Add a media to the favourites of a project
[**GetCatalogueMedia**](CatalogueAPI.md#GetCatalogueMedia) | **Get** /api/v1/medias/{id} | Get a media
[**ListFlashOffers**](CatalogueAPI.md#ListFlashOffers) | **Get** /api/v1/flash-offers | List flash offers
[**RequestMedias**](CatalogueAPI.md#RequestMedias) | **Post** /api/v1/projects/{id}/media-requests | Request specific medias for a project
[**SearchProjectMedias**](CatalogueAPI.md#SearchProjectMedias) | **Get** /api/v1/projects/{id}/medias | Search the catalogue for a project
[**UndiscardMedia**](CatalogueAPI.md#UndiscardMedia) | **Delete** /api/v1/projects/{id}/discards/{mediaId} | Restore a discarded media for a project
[**UnfavouriteMedia**](CatalogueAPI.md#UnfavouriteMedia) | **Delete** /api/v1/projects/{id}/favourites/{mediaId} | Remove a media from the favourites of a project



## DiscardMedia

> DiscardMedia(ctx, id, mediaId).IdempotencyKey(idempotencyKey).Execute()

Discard a media for a project



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The project.
	mediaId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The media.
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CatalogueAPI.DiscardMedia(context.Background(), id, mediaId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CatalogueAPI.DiscardMedia``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | The project. | 
**mediaId** | **string** | The media. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDiscardMediaRequest struct via the builder pattern


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


## FavouriteMedia

> FavouriteMedia(ctx, id, mediaId).IdempotencyKey(idempotencyKey).Execute()

Add a media to the favourites of a project



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The project.
	mediaId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The media.
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CatalogueAPI.FavouriteMedia(context.Background(), id, mediaId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CatalogueAPI.FavouriteMedia``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | The project. | 
**mediaId** | **string** | The media. | 

### Other Parameters

Other parameters are passed through a pointer to a apiFavouriteMediaRequest struct via the builder pattern


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


## GetCatalogueMedia

> CatalogueMedia GetCatalogueMedia(ctx, id).Execute()

Get a media



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The media.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CatalogueAPI.GetCatalogueMedia(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CatalogueAPI.GetCatalogueMedia``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCatalogueMedia`: CatalogueMedia
	fmt.Fprintf(os.Stdout, "Response from `CatalogueAPI.GetCatalogueMedia`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | The media. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetCatalogueMediaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CatalogueMedia**](CatalogueMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListFlashOffers

> ListFlashOffers200Response ListFlashOffers(ctx).ProjectId(projectId).Source(source).Sort(sort).Domain(domain).WebsiteType(websiteType).Language(language).Country(country).Topics(topics).NotBannedTopics(notBannedTopics).MinTraffic(minTraffic).MaxTraffic(maxTraffic).TrafficTrendUpward(trafficTrendUpward).MinDomainRating(minDomainRating).MaxDomainRating(maxDomainRating).MinLinkedToReferringRatio(minLinkedToReferringRatio).MaxLinkedToReferringRatio(maxLinkedToReferringRatio).MinPostPrice(minPostPrice).MaxPostPrice(maxPostPrice).PostLinkType(postLinkType).PromotedSocialNetwork(promotedSocialNetwork).WithoutAdvertisingLabel(withoutAdvertisingLabel).HomepageListing(homepageListing).HasLinkAddition(hasLinkAddition).MinLinkAdditionPrice(minLinkAdditionPrice).MaxLinkAdditionPrice(maxLinkAdditionPrice).LinkAdditionLinkType(linkAdditionLinkType).Recommended(recommended).Favourite(favourite).Requested(requested).Bought(bought).Discarded(discarded).New(new).RanksGoalKeyword(ranksGoalKeyword).RanksAiKeyword(ranksAiKeyword).Limit(limit).Offset(offset).Execute()

List flash offers



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
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The project to search flash offers for.
	source := "source_example" // string | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state. (optional)
	sort := "sort_example" // string | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first. (optional)
	domain := "domain_example" // string | Medias whose domain contains this text, 1 to 255 characters. (optional)
	websiteType := "websiteType_example" // string | A comma-separated list of website types: `blog`, `press`. (optional)
	language := "language_example" // string | A comma-separated list of language codes, as in GET /vocabulary. (optional)
	country := "country_example" // string | A comma-separated list of country codes, as in GET /vocabulary. (optional)
	topics := "topics_example" // string | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. (optional)
	notBannedTopics := true // bool | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise. (optional)
	minTraffic := int32(56) // int32 | Minimum monthly organic traffic. (optional)
	maxTraffic := int32(56) // int32 | Maximum monthly organic traffic. (optional)
	trafficTrendUpward := true // bool | Medias whose traffic is growing. Only `true` applies it; omit it otherwise. (optional)
	minDomainRating := int32(56) // int32 | Minimum domain rating, 0 to 100. (optional)
	maxDomainRating := int32(56) // int32 | Maximum domain rating, 0 to 100. (optional)
	minLinkedToReferringRatio := float32(8.14) // float32 | Minimum ratio of linked domains to referring domains, such as 0.5. (optional)
	maxLinkedToReferringRatio := float32(8.14) // float32 | Maximum ratio of linked domains to referring domains, such as 1.5. (optional)
	minPostPrice := int32(56) // int32 | Minimum post price, in cents. (optional)
	maxPostPrice := int32(56) // int32 | Maximum post price, in cents. (optional)
	postLinkType := "postLinkType_example" // string | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`. (optional)
	promotedSocialNetwork := "promotedSocialNetwork_example" // string | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`. (optional)
	withoutAdvertisingLabel := true // bool | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise. (optional)
	homepageListing := true // bool | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise. (optional)
	hasLinkAddition := true // bool | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise. (optional)
	minLinkAdditionPrice := int32(56) // int32 | Minimum link addition price, in cents. (optional)
	maxLinkAdditionPrice := int32(56) // int32 | Maximum link addition price, in cents. (optional)
	linkAdditionLinkType := "linkAdditionLinkType_example" // string | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`. (optional)
	recommended := true // bool | `true`: only the medias Growwer recommends for the project; `false`: only the others. (optional)
	favourite := true // bool | `true`: only your favourites for the project; `false`: leave them out. (optional)
	requested := true // bool | `true`: only the medias you requested for the project; `false`: leave them out. (optional)
	bought := true // bool | `true`: only medias you bought for the project; `false`: leave them out. (optional)
	discarded := true // bool | `true`: only the medias you discarded for the project; `false`: leave them out. (optional)
	new := true // bool | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise. (optional)
	ranksGoalKeyword := "ranksGoalKeyword_example" // string | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project. (optional)
	ranksAiKeyword := "ranksAiKeyword_example" // string | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`. (optional)
	limit := int32(56) // int32 | Medias per page, 1 to 100. (optional) (default to 20)
	offset := int32(56) // int32 | Medias to skip, at most 99900. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CatalogueAPI.ListFlashOffers(context.Background()).ProjectId(projectId).Source(source).Sort(sort).Domain(domain).WebsiteType(websiteType).Language(language).Country(country).Topics(topics).NotBannedTopics(notBannedTopics).MinTraffic(minTraffic).MaxTraffic(maxTraffic).TrafficTrendUpward(trafficTrendUpward).MinDomainRating(minDomainRating).MaxDomainRating(maxDomainRating).MinLinkedToReferringRatio(minLinkedToReferringRatio).MaxLinkedToReferringRatio(maxLinkedToReferringRatio).MinPostPrice(minPostPrice).MaxPostPrice(maxPostPrice).PostLinkType(postLinkType).PromotedSocialNetwork(promotedSocialNetwork).WithoutAdvertisingLabel(withoutAdvertisingLabel).HomepageListing(homepageListing).HasLinkAddition(hasLinkAddition).MinLinkAdditionPrice(minLinkAdditionPrice).MaxLinkAdditionPrice(maxLinkAdditionPrice).LinkAdditionLinkType(linkAdditionLinkType).Recommended(recommended).Favourite(favourite).Requested(requested).Bought(bought).Discarded(discarded).New(new).RanksGoalKeyword(ranksGoalKeyword).RanksAiKeyword(ranksAiKeyword).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CatalogueAPI.ListFlashOffers``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListFlashOffers`: ListFlashOffers200Response
	fmt.Fprintf(os.Stdout, "Response from `CatalogueAPI.ListFlashOffers`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListFlashOffersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **string** | The project to search flash offers for. | 
 **source** | **string** | Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | 
 **sort** | **string** | The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | 
 **domain** | **string** | Medias whose domain contains this text, 1 to 255 characters. | 
 **websiteType** | **string** | A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | 
 **language** | **string** | A comma-separated list of language codes, as in GET /vocabulary. | 
 **country** | **string** | A comma-separated list of country codes, as in GET /vocabulary. | 
 **topics** | **string** | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | 
 **notBannedTopics** | **bool** | Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **minTraffic** | **int32** | Minimum monthly organic traffic. | 
 **maxTraffic** | **int32** | Maximum monthly organic traffic. | 
 **trafficTrendUpward** | **bool** | Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **minDomainRating** | **int32** | Minimum domain rating, 0 to 100. | 
 **maxDomainRating** | **int32** | Maximum domain rating, 0 to 100. | 
 **minLinkedToReferringRatio** | **float32** | Minimum ratio of linked domains to referring domains, such as 0.5. | 
 **maxLinkedToReferringRatio** | **float32** | Maximum ratio of linked domains to referring domains, such as 1.5. | 
 **minPostPrice** | **int32** | Minimum post price, in cents. | 
 **maxPostPrice** | **int32** | Maximum post price, in cents. | 
 **postLinkType** | **string** | A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | 
 **promotedSocialNetwork** | **string** | A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | 
 **withoutAdvertisingLabel** | **bool** | Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **homepageListing** | **bool** | Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **hasLinkAddition** | **bool** | Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **minLinkAdditionPrice** | **int32** | Minimum link addition price, in cents. | 
 **maxLinkAdditionPrice** | **int32** | Maximum link addition price, in cents. | 
 **linkAdditionLinkType** | **string** | A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | 
 **recommended** | **bool** | &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | 
 **favourite** | **bool** | &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | 
 **requested** | **bool** | &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | 
 **bought** | **bool** | &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | 
 **discarded** | **bool** | &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | 
 **new** | **bool** | Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **ranksGoalKeyword** | **string** | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | 
 **ranksAiKeyword** | **string** | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | 
 **limit** | **int32** | Medias per page, 1 to 100. | [default to 20]
 **offset** | **int32** | Medias to skip, at most 99900. | [default to 0]

### Return type

[**ListFlashOffers200Response**](ListFlashOffers200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RequestMedias

> RequestMedias201Response RequestMedias(ctx, id).IdempotencyKey(idempotencyKey).RequestMediasRequest(requestMediasRequest).Execute()

Request specific medias for a project



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The project.
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
	requestMediasRequest := *openapiclient.NewRequestMediasRequest([]string{"example.com"}) // RequestMediasRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CatalogueAPI.RequestMedias(context.Background(), id).IdempotencyKey(idempotencyKey).RequestMediasRequest(requestMediasRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CatalogueAPI.RequestMedias``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RequestMedias`: RequestMedias201Response
	fmt.Fprintf(os.Stdout, "Response from `CatalogueAPI.RequestMedias`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | The project. | 

### Other Parameters

Other parameters are passed through a pointer to a apiRequestMediasRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. | 
 **requestMediasRequest** | [**RequestMediasRequest**](RequestMediasRequest.md) |  | 

### Return type

[**RequestMedias201Response**](RequestMedias201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SearchProjectMedias

> ListFlashOffers200Response SearchProjectMedias(ctx, id).Source(source).Sort(sort).SavedFilterId(savedFilterId).Domain(domain).WebsiteType(websiteType).Language(language).Country(country).Topics(topics).NotBannedTopics(notBannedTopics).MinTraffic(minTraffic).MaxTraffic(maxTraffic).TrafficTrendUpward(trafficTrendUpward).MinDomainRating(minDomainRating).MaxDomainRating(maxDomainRating).MinLinkedToReferringRatio(minLinkedToReferringRatio).MaxLinkedToReferringRatio(maxLinkedToReferringRatio).MinPostPrice(minPostPrice).MaxPostPrice(maxPostPrice).PostLinkType(postLinkType).PromotedSocialNetwork(promotedSocialNetwork).WithoutAdvertisingLabel(withoutAdvertisingLabel).HomepageListing(homepageListing).HasLinkAddition(hasLinkAddition).MinLinkAdditionPrice(minLinkAdditionPrice).MaxLinkAdditionPrice(maxLinkAdditionPrice).LinkAdditionLinkType(linkAdditionLinkType).Recommended(recommended).Favourite(favourite).Requested(requested).FlashOffer(flashOffer).Bought(bought).Discarded(discarded).New(new).RanksGoalKeyword(ranksGoalKeyword).RanksAiKeyword(ranksAiKeyword).Limit(limit).Offset(offset).Execute()

Search the catalogue for a project



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The project.
	source := "source_example" // string | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state. (optional)
	sort := "sort_example" // string | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first. (optional)
	savedFilterId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, `source` or `sort`. A filter saved on the web that uses a filter the API does not support is refused with 422 `saved_filter_unsupported`. (optional)
	domain := "domain_example" // string | Medias whose domain contains this text, 1 to 255 characters. (optional)
	websiteType := "websiteType_example" // string | A comma-separated list of website types: `blog`, `press`. (optional)
	language := "language_example" // string | A comma-separated list of language codes, as in GET /vocabulary. (optional)
	country := "country_example" // string | A comma-separated list of country codes, as in GET /vocabulary. (optional)
	topics := "topics_example" // string | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. (optional)
	notBannedTopics := true // bool | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise. (optional)
	minTraffic := int32(56) // int32 | Minimum monthly organic traffic. (optional)
	maxTraffic := int32(56) // int32 | Maximum monthly organic traffic. (optional)
	trafficTrendUpward := true // bool | Medias whose traffic is growing. Only `true` applies it; omit it otherwise. (optional)
	minDomainRating := int32(56) // int32 | Minimum domain rating, 0 to 100. (optional)
	maxDomainRating := int32(56) // int32 | Maximum domain rating, 0 to 100. (optional)
	minLinkedToReferringRatio := float32(8.14) // float32 | Minimum ratio of linked domains to referring domains, such as 0.5. (optional)
	maxLinkedToReferringRatio := float32(8.14) // float32 | Maximum ratio of linked domains to referring domains, such as 1.5. (optional)
	minPostPrice := int32(56) // int32 | Minimum post price, in cents. (optional)
	maxPostPrice := int32(56) // int32 | Maximum post price, in cents. (optional)
	postLinkType := "postLinkType_example" // string | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`. (optional)
	promotedSocialNetwork := "promotedSocialNetwork_example" // string | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`. (optional)
	withoutAdvertisingLabel := true // bool | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise. (optional)
	homepageListing := true // bool | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise. (optional)
	hasLinkAddition := true // bool | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise. (optional)
	minLinkAdditionPrice := int32(56) // int32 | Minimum link addition price, in cents. (optional)
	maxLinkAdditionPrice := int32(56) // int32 | Maximum link addition price, in cents. (optional)
	linkAdditionLinkType := "linkAdditionLinkType_example" // string | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`. (optional)
	recommended := true // bool | `true`: only the medias Growwer recommends for the project; `false`: only the others. (optional)
	favourite := true // bool | `true`: only your favourites for the project; `false`: leave them out. (optional)
	requested := true // bool | `true`: only the medias you requested for the project; `false`: leave them out. (optional)
	flashOffer := true // bool | `true`: only medias with a flash offer running; `false`: leave them out. (optional)
	bought := true // bool | `true`: only medias you bought for the project; `false`: leave them out. (optional)
	discarded := true // bool | `true`: only the medias you discarded for the project; `false`: leave them out. (optional)
	new := true // bool | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise. (optional)
	ranksGoalKeyword := "ranksGoalKeyword_example" // string | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project. (optional)
	ranksAiKeyword := "ranksAiKeyword_example" // string | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`. (optional)
	limit := int32(56) // int32 | Medias per page, 1 to 100. (optional) (default to 20)
	offset := int32(56) // int32 | Medias to skip, at most 99900. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CatalogueAPI.SearchProjectMedias(context.Background(), id).Source(source).Sort(sort).SavedFilterId(savedFilterId).Domain(domain).WebsiteType(websiteType).Language(language).Country(country).Topics(topics).NotBannedTopics(notBannedTopics).MinTraffic(minTraffic).MaxTraffic(maxTraffic).TrafficTrendUpward(trafficTrendUpward).MinDomainRating(minDomainRating).MaxDomainRating(maxDomainRating).MinLinkedToReferringRatio(minLinkedToReferringRatio).MaxLinkedToReferringRatio(maxLinkedToReferringRatio).MinPostPrice(minPostPrice).MaxPostPrice(maxPostPrice).PostLinkType(postLinkType).PromotedSocialNetwork(promotedSocialNetwork).WithoutAdvertisingLabel(withoutAdvertisingLabel).HomepageListing(homepageListing).HasLinkAddition(hasLinkAddition).MinLinkAdditionPrice(minLinkAdditionPrice).MaxLinkAdditionPrice(maxLinkAdditionPrice).LinkAdditionLinkType(linkAdditionLinkType).Recommended(recommended).Favourite(favourite).Requested(requested).FlashOffer(flashOffer).Bought(bought).Discarded(discarded).New(new).RanksGoalKeyword(ranksGoalKeyword).RanksAiKeyword(ranksAiKeyword).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CatalogueAPI.SearchProjectMedias``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SearchProjectMedias`: ListFlashOffers200Response
	fmt.Fprintf(os.Stdout, "Response from `CatalogueAPI.SearchProjectMedias`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | The project. | 

### Other Parameters

Other parameters are passed through a pointer to a apiSearchProjectMediasRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **source** | **string** | Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | 
 **sort** | **string** | The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | 
 **savedFilterId** | **string** | Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, &#x60;source&#x60; or &#x60;sort&#x60;. A filter saved on the web that uses a filter the API does not support is refused with 422 &#x60;saved_filter_unsupported&#x60;. | 
 **domain** | **string** | Medias whose domain contains this text, 1 to 255 characters. | 
 **websiteType** | **string** | A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | 
 **language** | **string** | A comma-separated list of language codes, as in GET /vocabulary. | 
 **country** | **string** | A comma-separated list of country codes, as in GET /vocabulary. | 
 **topics** | **string** | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | 
 **notBannedTopics** | **bool** | Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **minTraffic** | **int32** | Minimum monthly organic traffic. | 
 **maxTraffic** | **int32** | Maximum monthly organic traffic. | 
 **trafficTrendUpward** | **bool** | Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **minDomainRating** | **int32** | Minimum domain rating, 0 to 100. | 
 **maxDomainRating** | **int32** | Maximum domain rating, 0 to 100. | 
 **minLinkedToReferringRatio** | **float32** | Minimum ratio of linked domains to referring domains, such as 0.5. | 
 **maxLinkedToReferringRatio** | **float32** | Maximum ratio of linked domains to referring domains, such as 1.5. | 
 **minPostPrice** | **int32** | Minimum post price, in cents. | 
 **maxPostPrice** | **int32** | Maximum post price, in cents. | 
 **postLinkType** | **string** | A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | 
 **promotedSocialNetwork** | **string** | A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | 
 **withoutAdvertisingLabel** | **bool** | Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **homepageListing** | **bool** | Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **hasLinkAddition** | **bool** | Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **minLinkAdditionPrice** | **int32** | Minimum link addition price, in cents. | 
 **maxLinkAdditionPrice** | **int32** | Maximum link addition price, in cents. | 
 **linkAdditionLinkType** | **string** | A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | 
 **recommended** | **bool** | &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | 
 **favourite** | **bool** | &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | 
 **requested** | **bool** | &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | 
 **flashOffer** | **bool** | &#x60;true&#x60;: only medias with a flash offer running; &#x60;false&#x60;: leave them out. | 
 **bought** | **bool** | &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | 
 **discarded** | **bool** | &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | 
 **new** | **bool** | Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | 
 **ranksGoalKeyword** | **string** | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | 
 **ranksAiKeyword** | **string** | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | 
 **limit** | **int32** | Medias per page, 1 to 100. | [default to 20]
 **offset** | **int32** | Medias to skip, at most 99900. | [default to 0]

### Return type

[**ListFlashOffers200Response**](ListFlashOffers200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UndiscardMedia

> UndiscardMedia(ctx, id, mediaId).IdempotencyKey(idempotencyKey).Execute()

Restore a discarded media for a project



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The project.
	mediaId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The media.
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CatalogueAPI.UndiscardMedia(context.Background(), id, mediaId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CatalogueAPI.UndiscardMedia``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | The project. | 
**mediaId** | **string** | The media. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUndiscardMediaRequest struct via the builder pattern


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


## UnfavouriteMedia

> UnfavouriteMedia(ctx, id, mediaId).IdempotencyKey(idempotencyKey).Execute()

Remove a media from the favourites of a project



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The project.
	mediaId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The media.
	idempotencyKey := "idempotencyKey_example" // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CatalogueAPI.UnfavouriteMedia(context.Background(), id, mediaId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CatalogueAPI.UnfavouriteMedia``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | The project. | 
**mediaId** | **string** | The media. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUnfavouriteMediaRequest struct via the builder pattern


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

