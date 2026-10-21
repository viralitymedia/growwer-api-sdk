# SellerMediaLinkAdditionOfferPricingOptionsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LinkType** | **string** |  | 
**Fee** | [**Money**](Money.md) | Your base fee for the link type. | 
**CurrentCost** | [**NullableMoneyOrNull**](MoneyOrNull.md) | What you are paid now for the link type, flash offer discount included; read-only. | 

## Methods

### NewSellerMediaLinkAdditionOfferPricingOptionsInner

`func NewSellerMediaLinkAdditionOfferPricingOptionsInner(linkType string, fee Money, currentCost NullableMoneyOrNull, ) *SellerMediaLinkAdditionOfferPricingOptionsInner`

NewSellerMediaLinkAdditionOfferPricingOptionsInner instantiates a new SellerMediaLinkAdditionOfferPricingOptionsInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerMediaLinkAdditionOfferPricingOptionsInnerWithDefaults

`func NewSellerMediaLinkAdditionOfferPricingOptionsInnerWithDefaults() *SellerMediaLinkAdditionOfferPricingOptionsInner`

NewSellerMediaLinkAdditionOfferPricingOptionsInnerWithDefaults instantiates a new SellerMediaLinkAdditionOfferPricingOptionsInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLinkType

`func (o *SellerMediaLinkAdditionOfferPricingOptionsInner) GetLinkType() string`

GetLinkType returns the LinkType field if non-nil, zero value otherwise.

### GetLinkTypeOk

`func (o *SellerMediaLinkAdditionOfferPricingOptionsInner) GetLinkTypeOk() (*string, bool)`

GetLinkTypeOk returns a tuple with the LinkType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkType

`func (o *SellerMediaLinkAdditionOfferPricingOptionsInner) SetLinkType(v string)`

SetLinkType sets LinkType field to given value.


### GetFee

`func (o *SellerMediaLinkAdditionOfferPricingOptionsInner) GetFee() Money`

GetFee returns the Fee field if non-nil, zero value otherwise.

### GetFeeOk

`func (o *SellerMediaLinkAdditionOfferPricingOptionsInner) GetFeeOk() (*Money, bool)`

GetFeeOk returns a tuple with the Fee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFee

`func (o *SellerMediaLinkAdditionOfferPricingOptionsInner) SetFee(v Money)`

SetFee sets Fee field to given value.


### GetCurrentCost

`func (o *SellerMediaLinkAdditionOfferPricingOptionsInner) GetCurrentCost() MoneyOrNull`

GetCurrentCost returns the CurrentCost field if non-nil, zero value otherwise.

### GetCurrentCostOk

`func (o *SellerMediaLinkAdditionOfferPricingOptionsInner) GetCurrentCostOk() (*MoneyOrNull, bool)`

GetCurrentCostOk returns a tuple with the CurrentCost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentCost

`func (o *SellerMediaLinkAdditionOfferPricingOptionsInner) SetCurrentCost(v MoneyOrNull)`

SetCurrentCost sets CurrentCost field to given value.


### SetCurrentCostNil

`func (o *SellerMediaLinkAdditionOfferPricingOptionsInner) SetCurrentCostNil(b bool)`

 SetCurrentCostNil sets the value for CurrentCost to be an explicit nil

### UnsetCurrentCost
`func (o *SellerMediaLinkAdditionOfferPricingOptionsInner) UnsetCurrentCost()`

UnsetCurrentCost ensures that no value is present for CurrentCost, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


