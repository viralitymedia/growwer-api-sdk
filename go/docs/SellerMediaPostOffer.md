# SellerMediaPostOffer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PricingOptions** | [**[]SellerMediaPostOfferPricingOptionsInner**](SellerMediaPostOfferPricingOptionsInner.md) | One entry per link type you offer. | 
**ExtraServices** | [**[]UpdateSellerMediaRequestExtraServicesInner**](UpdateSellerMediaRequestExtraServicesInner.md) |  | 

## Methods

### NewSellerMediaPostOffer

`func NewSellerMediaPostOffer(pricingOptions []SellerMediaPostOfferPricingOptionsInner, extraServices []UpdateSellerMediaRequestExtraServicesInner, ) *SellerMediaPostOffer`

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


