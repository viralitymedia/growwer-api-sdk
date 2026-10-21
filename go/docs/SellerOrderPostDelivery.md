# SellerOrderPostDelivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | **string** | The URL of the published post. It is checked to be a URL only, as the web does; whether the post carries the links is not checked here. | 
**PublicationDateConfirmed** | **bool** | Must be true. Confirms the post is live, or for an order with a scheduled publication date, that it will be published on that date. | 

## Methods

### NewSellerOrderPostDelivery

`func NewSellerOrderPostDelivery(url string, publicationDateConfirmed bool, ) *SellerOrderPostDelivery`

NewSellerOrderPostDelivery instantiates a new SellerOrderPostDelivery object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerOrderPostDeliveryWithDefaults

`func NewSellerOrderPostDeliveryWithDefaults() *SellerOrderPostDelivery`

NewSellerOrderPostDeliveryWithDefaults instantiates a new SellerOrderPostDelivery object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUrl

`func (o *SellerOrderPostDelivery) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *SellerOrderPostDelivery) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *SellerOrderPostDelivery) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetPublicationDateConfirmed

`func (o *SellerOrderPostDelivery) GetPublicationDateConfirmed() bool`

GetPublicationDateConfirmed returns the PublicationDateConfirmed field if non-nil, zero value otherwise.

### GetPublicationDateConfirmedOk

`func (o *SellerOrderPostDelivery) GetPublicationDateConfirmedOk() (*bool, bool)`

GetPublicationDateConfirmedOk returns a tuple with the PublicationDateConfirmed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicationDateConfirmed

`func (o *SellerOrderPostDelivery) SetPublicationDateConfirmed(v bool)`

SetPublicationDateConfirmed sets PublicationDateConfirmed field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


