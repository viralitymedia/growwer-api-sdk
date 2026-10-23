# CreateSellerMediaRequestPostOffer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PricingOptions** | [**[]UpdateSellerMediaRequestPostOfferPricingOptionsInner**](UpdateSellerMediaRequestPostOfferPricingOptionsInner.md) |  | 
**MaximumLinks** | **int32** |  | 
**AdvertisingLabellingPolicy** | Pointer to **string** |  | [optional] 
**PromotedSocialNetworks** | Pointer to **[]string** |  | [optional] 

## Methods

### NewCreateSellerMediaRequestPostOffer

`func NewCreateSellerMediaRequestPostOffer(pricingOptions []UpdateSellerMediaRequestPostOfferPricingOptionsInner, maximumLinks int32, ) *CreateSellerMediaRequestPostOffer`

NewCreateSellerMediaRequestPostOffer instantiates a new CreateSellerMediaRequestPostOffer object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateSellerMediaRequestPostOfferWithDefaults

`func NewCreateSellerMediaRequestPostOfferWithDefaults() *CreateSellerMediaRequestPostOffer`

NewCreateSellerMediaRequestPostOfferWithDefaults instantiates a new CreateSellerMediaRequestPostOffer object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPricingOptions

`func (o *CreateSellerMediaRequestPostOffer) GetPricingOptions() []UpdateSellerMediaRequestPostOfferPricingOptionsInner`

GetPricingOptions returns the PricingOptions field if non-nil, zero value otherwise.

### GetPricingOptionsOk

`func (o *CreateSellerMediaRequestPostOffer) GetPricingOptionsOk() (*[]UpdateSellerMediaRequestPostOfferPricingOptionsInner, bool)`

GetPricingOptionsOk returns a tuple with the PricingOptions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPricingOptions

`func (o *CreateSellerMediaRequestPostOffer) SetPricingOptions(v []UpdateSellerMediaRequestPostOfferPricingOptionsInner)`

SetPricingOptions sets PricingOptions field to given value.


### GetMaximumLinks

`func (o *CreateSellerMediaRequestPostOffer) GetMaximumLinks() int32`

GetMaximumLinks returns the MaximumLinks field if non-nil, zero value otherwise.

### GetMaximumLinksOk

`func (o *CreateSellerMediaRequestPostOffer) GetMaximumLinksOk() (*int32, bool)`

GetMaximumLinksOk returns a tuple with the MaximumLinks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaximumLinks

`func (o *CreateSellerMediaRequestPostOffer) SetMaximumLinks(v int32)`

SetMaximumLinks sets MaximumLinks field to given value.


### GetAdvertisingLabellingPolicy

`func (o *CreateSellerMediaRequestPostOffer) GetAdvertisingLabellingPolicy() string`

GetAdvertisingLabellingPolicy returns the AdvertisingLabellingPolicy field if non-nil, zero value otherwise.

### GetAdvertisingLabellingPolicyOk

`func (o *CreateSellerMediaRequestPostOffer) GetAdvertisingLabellingPolicyOk() (*string, bool)`

GetAdvertisingLabellingPolicyOk returns a tuple with the AdvertisingLabellingPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdvertisingLabellingPolicy

`func (o *CreateSellerMediaRequestPostOffer) SetAdvertisingLabellingPolicy(v string)`

SetAdvertisingLabellingPolicy sets AdvertisingLabellingPolicy field to given value.

### HasAdvertisingLabellingPolicy

`func (o *CreateSellerMediaRequestPostOffer) HasAdvertisingLabellingPolicy() bool`

HasAdvertisingLabellingPolicy returns a boolean if a field has been set.

### GetPromotedSocialNetworks

`func (o *CreateSellerMediaRequestPostOffer) GetPromotedSocialNetworks() []string`

GetPromotedSocialNetworks returns the PromotedSocialNetworks field if non-nil, zero value otherwise.

### GetPromotedSocialNetworksOk

`func (o *CreateSellerMediaRequestPostOffer) GetPromotedSocialNetworksOk() (*[]string, bool)`

GetPromotedSocialNetworksOk returns a tuple with the PromotedSocialNetworks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPromotedSocialNetworks

`func (o *CreateSellerMediaRequestPostOffer) SetPromotedSocialNetworks(v []string)`

SetPromotedSocialNetworks sets PromotedSocialNetworks field to given value.

### HasPromotedSocialNetworks

`func (o *CreateSellerMediaRequestPostOffer) HasPromotedSocialNetworks() bool`

HasPromotedSocialNetworks returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


