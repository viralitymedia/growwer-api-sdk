# UpdateSellerMediaRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PostOffer** | Pointer to [**UpdateSellerMediaRequestPostOffer**](UpdateSellerMediaRequestPostOffer.md) |  | [optional] 
**LinkAdditionOffer** | Pointer to [**NullableUpdateSellerMediaRequestLinkAdditionOffer**](UpdateSellerMediaRequestLinkAdditionOffer.md) |  | [optional] 
**ExtraServices** | Pointer to [**[]UpdateSellerMediaRequestExtraServicesInner**](UpdateSellerMediaRequestExtraServicesInner.md) |  | [optional] 

## Methods

### NewUpdateSellerMediaRequest

`func NewUpdateSellerMediaRequest() *UpdateSellerMediaRequest`

NewUpdateSellerMediaRequest instantiates a new UpdateSellerMediaRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateSellerMediaRequestWithDefaults

`func NewUpdateSellerMediaRequestWithDefaults() *UpdateSellerMediaRequest`

NewUpdateSellerMediaRequestWithDefaults instantiates a new UpdateSellerMediaRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPostOffer

`func (o *UpdateSellerMediaRequest) GetPostOffer() UpdateSellerMediaRequestPostOffer`

GetPostOffer returns the PostOffer field if non-nil, zero value otherwise.

### GetPostOfferOk

`func (o *UpdateSellerMediaRequest) GetPostOfferOk() (*UpdateSellerMediaRequestPostOffer, bool)`

GetPostOfferOk returns a tuple with the PostOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostOffer

`func (o *UpdateSellerMediaRequest) SetPostOffer(v UpdateSellerMediaRequestPostOffer)`

SetPostOffer sets PostOffer field to given value.

### HasPostOffer

`func (o *UpdateSellerMediaRequest) HasPostOffer() bool`

HasPostOffer returns a boolean if a field has been set.

### GetLinkAdditionOffer

`func (o *UpdateSellerMediaRequest) GetLinkAdditionOffer() UpdateSellerMediaRequestLinkAdditionOffer`

GetLinkAdditionOffer returns the LinkAdditionOffer field if non-nil, zero value otherwise.

### GetLinkAdditionOfferOk

`func (o *UpdateSellerMediaRequest) GetLinkAdditionOfferOk() (*UpdateSellerMediaRequestLinkAdditionOffer, bool)`

GetLinkAdditionOfferOk returns a tuple with the LinkAdditionOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkAdditionOffer

`func (o *UpdateSellerMediaRequest) SetLinkAdditionOffer(v UpdateSellerMediaRequestLinkAdditionOffer)`

SetLinkAdditionOffer sets LinkAdditionOffer field to given value.

### HasLinkAdditionOffer

`func (o *UpdateSellerMediaRequest) HasLinkAdditionOffer() bool`

HasLinkAdditionOffer returns a boolean if a field has been set.

### SetLinkAdditionOfferNil

`func (o *UpdateSellerMediaRequest) SetLinkAdditionOfferNil(b bool)`

 SetLinkAdditionOfferNil sets the value for LinkAdditionOffer to be an explicit nil

### UnsetLinkAdditionOffer
`func (o *UpdateSellerMediaRequest) UnsetLinkAdditionOffer()`

UnsetLinkAdditionOffer ensures that no value is present for LinkAdditionOffer, not even an explicit nil
### GetExtraServices

`func (o *UpdateSellerMediaRequest) GetExtraServices() []UpdateSellerMediaRequestExtraServicesInner`

GetExtraServices returns the ExtraServices field if non-nil, zero value otherwise.

### GetExtraServicesOk

`func (o *UpdateSellerMediaRequest) GetExtraServicesOk() (*[]UpdateSellerMediaRequestExtraServicesInner, bool)`

GetExtraServicesOk returns a tuple with the ExtraServices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtraServices

`func (o *UpdateSellerMediaRequest) SetExtraServices(v []UpdateSellerMediaRequestExtraServicesInner)`

SetExtraServices sets ExtraServices field to given value.

### HasExtraServices

`func (o *UpdateSellerMediaRequest) HasExtraServices() bool`

HasExtraServices returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


