# SellerMediaCompetitiveFeesByLinkTypeInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LinkType** | **string** |  | 
**FeeWhenSellerWritesPost** | [**NullableMoneyOrNull**](MoneyOrNull.md) | The fee the apply sets for a post you write on this link type, or null when it keeps your fee on that side. | 
**FeeWhenSellerDoesNotWritePost** | [**NullableMoneyOrNull**](MoneyOrNull.md) | The fee the apply sets for a post the buyer or Growwer writes on this link type, or null when it keeps your fee on that side. | 

## Methods

### NewSellerMediaCompetitiveFeesByLinkTypeInner

`func NewSellerMediaCompetitiveFeesByLinkTypeInner(linkType string, feeWhenSellerWritesPost NullableMoneyOrNull, feeWhenSellerDoesNotWritePost NullableMoneyOrNull, ) *SellerMediaCompetitiveFeesByLinkTypeInner`

NewSellerMediaCompetitiveFeesByLinkTypeInner instantiates a new SellerMediaCompetitiveFeesByLinkTypeInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerMediaCompetitiveFeesByLinkTypeInnerWithDefaults

`func NewSellerMediaCompetitiveFeesByLinkTypeInnerWithDefaults() *SellerMediaCompetitiveFeesByLinkTypeInner`

NewSellerMediaCompetitiveFeesByLinkTypeInnerWithDefaults instantiates a new SellerMediaCompetitiveFeesByLinkTypeInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLinkType

`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) GetLinkType() string`

GetLinkType returns the LinkType field if non-nil, zero value otherwise.

### GetLinkTypeOk

`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) GetLinkTypeOk() (*string, bool)`

GetLinkTypeOk returns a tuple with the LinkType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkType

`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) SetLinkType(v string)`

SetLinkType sets LinkType field to given value.


### GetFeeWhenSellerWritesPost

`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) GetFeeWhenSellerWritesPost() MoneyOrNull`

GetFeeWhenSellerWritesPost returns the FeeWhenSellerWritesPost field if non-nil, zero value otherwise.

### GetFeeWhenSellerWritesPostOk

`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) GetFeeWhenSellerWritesPostOk() (*MoneyOrNull, bool)`

GetFeeWhenSellerWritesPostOk returns a tuple with the FeeWhenSellerWritesPost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeeWhenSellerWritesPost

`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) SetFeeWhenSellerWritesPost(v MoneyOrNull)`

SetFeeWhenSellerWritesPost sets FeeWhenSellerWritesPost field to given value.


### SetFeeWhenSellerWritesPostNil

`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) SetFeeWhenSellerWritesPostNil(b bool)`

 SetFeeWhenSellerWritesPostNil sets the value for FeeWhenSellerWritesPost to be an explicit nil

### UnsetFeeWhenSellerWritesPost
`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) UnsetFeeWhenSellerWritesPost()`

UnsetFeeWhenSellerWritesPost ensures that no value is present for FeeWhenSellerWritesPost, not even an explicit nil
### GetFeeWhenSellerDoesNotWritePost

`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) GetFeeWhenSellerDoesNotWritePost() MoneyOrNull`

GetFeeWhenSellerDoesNotWritePost returns the FeeWhenSellerDoesNotWritePost field if non-nil, zero value otherwise.

### GetFeeWhenSellerDoesNotWritePostOk

`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) GetFeeWhenSellerDoesNotWritePostOk() (*MoneyOrNull, bool)`

GetFeeWhenSellerDoesNotWritePostOk returns a tuple with the FeeWhenSellerDoesNotWritePost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeeWhenSellerDoesNotWritePost

`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) SetFeeWhenSellerDoesNotWritePost(v MoneyOrNull)`

SetFeeWhenSellerDoesNotWritePost sets FeeWhenSellerDoesNotWritePost field to given value.


### SetFeeWhenSellerDoesNotWritePostNil

`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) SetFeeWhenSellerDoesNotWritePostNil(b bool)`

 SetFeeWhenSellerDoesNotWritePostNil sets the value for FeeWhenSellerDoesNotWritePost to be an explicit nil

### UnsetFeeWhenSellerDoesNotWritePost
`func (o *SellerMediaCompetitiveFeesByLinkTypeInner) UnsetFeeWhenSellerDoesNotWritePost()`

UnsetFeeWhenSellerDoesNotWritePost ensures that no value is present for FeeWhenSellerDoesNotWritePost, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


