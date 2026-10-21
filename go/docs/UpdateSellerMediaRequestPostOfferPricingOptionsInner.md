# UpdateSellerMediaRequestPostOfferPricingOptionsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LinkType** | **string** |  | 
**FeeWhenSellerWritesPost** | Pointer to [**NullableMoneyOrNull**](MoneyOrNull.md) | What you are paid for a post you write; null or left out when you do not offer it. | [optional] 
**FeeWhenSellerDoesNotWritePost** | Pointer to [**NullableMoneyOrNull**](MoneyOrNull.md) | What you are paid for a post the buyer or Growwer writes; null or left out when you do not offer it. | [optional] 

## Methods

### NewUpdateSellerMediaRequestPostOfferPricingOptionsInner

`func NewUpdateSellerMediaRequestPostOfferPricingOptionsInner(linkType string, ) *UpdateSellerMediaRequestPostOfferPricingOptionsInner`

NewUpdateSellerMediaRequestPostOfferPricingOptionsInner instantiates a new UpdateSellerMediaRequestPostOfferPricingOptionsInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateSellerMediaRequestPostOfferPricingOptionsInnerWithDefaults

`func NewUpdateSellerMediaRequestPostOfferPricingOptionsInnerWithDefaults() *UpdateSellerMediaRequestPostOfferPricingOptionsInner`

NewUpdateSellerMediaRequestPostOfferPricingOptionsInnerWithDefaults instantiates a new UpdateSellerMediaRequestPostOfferPricingOptionsInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLinkType

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) GetLinkType() string`

GetLinkType returns the LinkType field if non-nil, zero value otherwise.

### GetLinkTypeOk

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) GetLinkTypeOk() (*string, bool)`

GetLinkTypeOk returns a tuple with the LinkType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkType

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) SetLinkType(v string)`

SetLinkType sets LinkType field to given value.


### GetFeeWhenSellerWritesPost

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) GetFeeWhenSellerWritesPost() MoneyOrNull`

GetFeeWhenSellerWritesPost returns the FeeWhenSellerWritesPost field if non-nil, zero value otherwise.

### GetFeeWhenSellerWritesPostOk

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) GetFeeWhenSellerWritesPostOk() (*MoneyOrNull, bool)`

GetFeeWhenSellerWritesPostOk returns a tuple with the FeeWhenSellerWritesPost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeeWhenSellerWritesPost

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) SetFeeWhenSellerWritesPost(v MoneyOrNull)`

SetFeeWhenSellerWritesPost sets FeeWhenSellerWritesPost field to given value.

### HasFeeWhenSellerWritesPost

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) HasFeeWhenSellerWritesPost() bool`

HasFeeWhenSellerWritesPost returns a boolean if a field has been set.

### SetFeeWhenSellerWritesPostNil

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) SetFeeWhenSellerWritesPostNil(b bool)`

 SetFeeWhenSellerWritesPostNil sets the value for FeeWhenSellerWritesPost to be an explicit nil

### UnsetFeeWhenSellerWritesPost
`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) UnsetFeeWhenSellerWritesPost()`

UnsetFeeWhenSellerWritesPost ensures that no value is present for FeeWhenSellerWritesPost, not even an explicit nil
### GetFeeWhenSellerDoesNotWritePost

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) GetFeeWhenSellerDoesNotWritePost() MoneyOrNull`

GetFeeWhenSellerDoesNotWritePost returns the FeeWhenSellerDoesNotWritePost field if non-nil, zero value otherwise.

### GetFeeWhenSellerDoesNotWritePostOk

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) GetFeeWhenSellerDoesNotWritePostOk() (*MoneyOrNull, bool)`

GetFeeWhenSellerDoesNotWritePostOk returns a tuple with the FeeWhenSellerDoesNotWritePost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeeWhenSellerDoesNotWritePost

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) SetFeeWhenSellerDoesNotWritePost(v MoneyOrNull)`

SetFeeWhenSellerDoesNotWritePost sets FeeWhenSellerDoesNotWritePost field to given value.

### HasFeeWhenSellerDoesNotWritePost

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) HasFeeWhenSellerDoesNotWritePost() bool`

HasFeeWhenSellerDoesNotWritePost returns a boolean if a field has been set.

### SetFeeWhenSellerDoesNotWritePostNil

`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) SetFeeWhenSellerDoesNotWritePostNil(b bool)`

 SetFeeWhenSellerDoesNotWritePostNil sets the value for FeeWhenSellerDoesNotWritePost to be an explicit nil

### UnsetFeeWhenSellerDoesNotWritePost
`func (o *UpdateSellerMediaRequestPostOfferPricingOptionsInner) UnsetFeeWhenSellerDoesNotWritePost()`

UnsetFeeWhenSellerDoesNotWritePost ensures that no value is present for FeeWhenSellerDoesNotWritePost, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


