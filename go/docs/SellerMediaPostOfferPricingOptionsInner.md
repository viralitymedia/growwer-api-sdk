# SellerMediaPostOfferPricingOptionsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FeeWhenSellerWritesPost** | [**NullableMoneyOrNull**](MoneyOrNull.md) | What you are paid for a post you write, or null when you do not offer it. | 
**FeeWhenSellerDoesNotWritePost** | [**NullableMoneyOrNull**](MoneyOrNull.md) | What you are paid for a post the buyer or Growwer writes, or null when you do not offer it. | 
**LinkType** | **string** |  | 
**CurrentCost** | [**NullableMoneyOrNull**](MoneyOrNull.md) | What you are paid now for the link type, flash offer discount included; read-only. Null when the link type has no current pricing. | 

## Methods

### NewSellerMediaPostOfferPricingOptionsInner

`func NewSellerMediaPostOfferPricingOptionsInner(feeWhenSellerWritesPost NullableMoneyOrNull, feeWhenSellerDoesNotWritePost NullableMoneyOrNull, linkType string, currentCost NullableMoneyOrNull, ) *SellerMediaPostOfferPricingOptionsInner`

NewSellerMediaPostOfferPricingOptionsInner instantiates a new SellerMediaPostOfferPricingOptionsInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerMediaPostOfferPricingOptionsInnerWithDefaults

`func NewSellerMediaPostOfferPricingOptionsInnerWithDefaults() *SellerMediaPostOfferPricingOptionsInner`

NewSellerMediaPostOfferPricingOptionsInnerWithDefaults instantiates a new SellerMediaPostOfferPricingOptionsInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFeeWhenSellerWritesPost

`func (o *SellerMediaPostOfferPricingOptionsInner) GetFeeWhenSellerWritesPost() MoneyOrNull`

GetFeeWhenSellerWritesPost returns the FeeWhenSellerWritesPost field if non-nil, zero value otherwise.

### GetFeeWhenSellerWritesPostOk

`func (o *SellerMediaPostOfferPricingOptionsInner) GetFeeWhenSellerWritesPostOk() (*MoneyOrNull, bool)`

GetFeeWhenSellerWritesPostOk returns a tuple with the FeeWhenSellerWritesPost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeeWhenSellerWritesPost

`func (o *SellerMediaPostOfferPricingOptionsInner) SetFeeWhenSellerWritesPost(v MoneyOrNull)`

SetFeeWhenSellerWritesPost sets FeeWhenSellerWritesPost field to given value.


### SetFeeWhenSellerWritesPostNil

`func (o *SellerMediaPostOfferPricingOptionsInner) SetFeeWhenSellerWritesPostNil(b bool)`

 SetFeeWhenSellerWritesPostNil sets the value for FeeWhenSellerWritesPost to be an explicit nil

### UnsetFeeWhenSellerWritesPost
`func (o *SellerMediaPostOfferPricingOptionsInner) UnsetFeeWhenSellerWritesPost()`

UnsetFeeWhenSellerWritesPost ensures that no value is present for FeeWhenSellerWritesPost, not even an explicit nil
### GetFeeWhenSellerDoesNotWritePost

`func (o *SellerMediaPostOfferPricingOptionsInner) GetFeeWhenSellerDoesNotWritePost() MoneyOrNull`

GetFeeWhenSellerDoesNotWritePost returns the FeeWhenSellerDoesNotWritePost field if non-nil, zero value otherwise.

### GetFeeWhenSellerDoesNotWritePostOk

`func (o *SellerMediaPostOfferPricingOptionsInner) GetFeeWhenSellerDoesNotWritePostOk() (*MoneyOrNull, bool)`

GetFeeWhenSellerDoesNotWritePostOk returns a tuple with the FeeWhenSellerDoesNotWritePost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeeWhenSellerDoesNotWritePost

`func (o *SellerMediaPostOfferPricingOptionsInner) SetFeeWhenSellerDoesNotWritePost(v MoneyOrNull)`

SetFeeWhenSellerDoesNotWritePost sets FeeWhenSellerDoesNotWritePost field to given value.


### SetFeeWhenSellerDoesNotWritePostNil

`func (o *SellerMediaPostOfferPricingOptionsInner) SetFeeWhenSellerDoesNotWritePostNil(b bool)`

 SetFeeWhenSellerDoesNotWritePostNil sets the value for FeeWhenSellerDoesNotWritePost to be an explicit nil

### UnsetFeeWhenSellerDoesNotWritePost
`func (o *SellerMediaPostOfferPricingOptionsInner) UnsetFeeWhenSellerDoesNotWritePost()`

UnsetFeeWhenSellerDoesNotWritePost ensures that no value is present for FeeWhenSellerDoesNotWritePost, not even an explicit nil
### GetLinkType

`func (o *SellerMediaPostOfferPricingOptionsInner) GetLinkType() string`

GetLinkType returns the LinkType field if non-nil, zero value otherwise.

### GetLinkTypeOk

`func (o *SellerMediaPostOfferPricingOptionsInner) GetLinkTypeOk() (*string, bool)`

GetLinkTypeOk returns a tuple with the LinkType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkType

`func (o *SellerMediaPostOfferPricingOptionsInner) SetLinkType(v string)`

SetLinkType sets LinkType field to given value.


### GetCurrentCost

`func (o *SellerMediaPostOfferPricingOptionsInner) GetCurrentCost() MoneyOrNull`

GetCurrentCost returns the CurrentCost field if non-nil, zero value otherwise.

### GetCurrentCostOk

`func (o *SellerMediaPostOfferPricingOptionsInner) GetCurrentCostOk() (*MoneyOrNull, bool)`

GetCurrentCostOk returns a tuple with the CurrentCost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentCost

`func (o *SellerMediaPostOfferPricingOptionsInner) SetCurrentCost(v MoneyOrNull)`

SetCurrentCost sets CurrentCost field to given value.


### SetCurrentCostNil

`func (o *SellerMediaPostOfferPricingOptionsInner) SetCurrentCostNil(b bool)`

 SetCurrentCostNil sets the value for CurrentCost to be an explicit nil

### UnsetCurrentCost
`func (o *SellerMediaPostOfferPricingOptionsInner) UnsetCurrentCost()`

UnsetCurrentCost ensures that no value is present for CurrentCost, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


