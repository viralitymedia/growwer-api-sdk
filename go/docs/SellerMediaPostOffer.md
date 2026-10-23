# SellerMediaPostOffer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PricingOptions** | [**[]SellerMediaPostOfferPricingOptionsInner**](SellerMediaPostOfferPricingOptionsInner.md) | One entry per link type you offer. | 
**MaximumLinks** | **int32** | How many links a sponsored post may hold, 1 to 4. | 
**AdvertisingLabellingPolicy** | **string** | Whether sponsored posts are labelled as advertising. | 
**PromotedSocialNetworks** | **[]string** | The social networks sponsored posts are promoted on. | 
**ExtraServices** | [**[]UpdateSellerMediaRequestExtraServicesInner**](UpdateSellerMediaRequestExtraServicesInner.md) | Read here, but PATCH /seller/medias/{id} and POST /seller/medias take it at the top level of the body. | 

## Methods

### NewSellerMediaPostOffer

`func NewSellerMediaPostOffer(pricingOptions []SellerMediaPostOfferPricingOptionsInner, maximumLinks int32, advertisingLabellingPolicy string, promotedSocialNetworks []string, extraServices []UpdateSellerMediaRequestExtraServicesInner, ) *SellerMediaPostOffer`

NewSellerMediaPostOffer instantiates a new SellerMediaPostOffer object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerMediaPostOfferWithDefaults

`func NewSellerMediaPostOfferWithDefaults() *SellerMediaPostOffer`

NewSellerMediaPostOfferWithDefaults instantiates a new SellerMediaPostOffer object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPricingOptions

`func (o *SellerMediaPostOffer) GetPricingOptions() []SellerMediaPostOfferPricingOptionsInner`

GetPricingOptions returns the PricingOptions field if non-nil, zero value otherwise.

### GetPricingOptionsOk

`func (o *SellerMediaPostOffer) GetPricingOptionsOk() (*[]SellerMediaPostOfferPricingOptionsInner, bool)`

GetPricingOptionsOk returns a tuple with the PricingOptions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPricingOptions

`func (o *SellerMediaPostOffer) SetPricingOptions(v []SellerMediaPostOfferPricingOptionsInner)`

SetPricingOptions sets PricingOptions field to given value.


### GetMaximumLinks

`func (o *SellerMediaPostOffer) GetMaximumLinks() int32`

GetMaximumLinks returns the MaximumLinks field if non-nil, zero value otherwise.

### GetMaximumLinksOk

`func (o *SellerMediaPostOffer) GetMaximumLinksOk() (*int32, bool)`

GetMaximumLinksOk returns a tuple with the MaximumLinks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaximumLinks

`func (o *SellerMediaPostOffer) SetMaximumLinks(v int32)`

SetMaximumLinks sets MaximumLinks field to given value.


### GetAdvertisingLabellingPolicy

`func (o *SellerMediaPostOffer) GetAdvertisingLabellingPolicy() string`

GetAdvertisingLabellingPolicy returns the AdvertisingLabellingPolicy field if non-nil, zero value otherwise.

### GetAdvertisingLabellingPolicyOk

`func (o *SellerMediaPostOffer) GetAdvertisingLabellingPolicyOk() (*string, bool)`

GetAdvertisingLabellingPolicyOk returns a tuple with the AdvertisingLabellingPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdvertisingLabellingPolicy

`func (o *SellerMediaPostOffer) SetAdvertisingLabellingPolicy(v string)`

SetAdvertisingLabellingPolicy sets AdvertisingLabellingPolicy field to given value.


### GetPromotedSocialNetworks

`func (o *SellerMediaPostOffer) GetPromotedSocialNetworks() []string`

GetPromotedSocialNetworks returns the PromotedSocialNetworks field if non-nil, zero value otherwise.

### GetPromotedSocialNetworksOk

`func (o *SellerMediaPostOffer) GetPromotedSocialNetworksOk() (*[]string, bool)`

GetPromotedSocialNetworksOk returns a tuple with the PromotedSocialNetworks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPromotedSocialNetworks

`func (o *SellerMediaPostOffer) SetPromotedSocialNetworks(v []string)`

SetPromotedSocialNetworks sets PromotedSocialNetworks field to given value.


### GetExtraServices

`func (o *SellerMediaPostOffer) GetExtraServices() []UpdateSellerMediaRequestExtraServicesInner`

GetExtraServices returns the ExtraServices field if non-nil, zero value otherwise.

### GetExtraServicesOk

`func (o *SellerMediaPostOffer) GetExtraServicesOk() (*[]UpdateSellerMediaRequestExtraServicesInner, bool)`

GetExtraServicesOk returns a tuple with the ExtraServices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtraServices

`func (o *SellerMediaPostOffer) SetExtraServices(v []UpdateSellerMediaRequestExtraServicesInner)`

SetExtraServices sets ExtraServices field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


