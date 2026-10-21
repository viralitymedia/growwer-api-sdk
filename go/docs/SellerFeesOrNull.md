# SellerFeesOrNull

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FeeWhenSellerWritesPost** | [**NullableMoneyOrNull**](MoneyOrNull.md) | What you are paid for a post you write, or null when you do not offer it. | 
**FeeWhenSellerDoesNotWritePost** | [**NullableMoneyOrNull**](MoneyOrNull.md) | What you are paid for a post the buyer or Growwer writes, or null when you do not offer it. | 

## Methods

### NewSellerFeesOrNull

`func NewSellerFeesOrNull(feeWhenSellerWritesPost NullableMoneyOrNull, feeWhenSellerDoesNotWritePost NullableMoneyOrNull, ) *SellerFeesOrNull`

NewSellerFeesOrNull instantiates a new SellerFeesOrNull object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerFeesOrNullWithDefaults

`func NewSellerFeesOrNullWithDefaults() *SellerFeesOrNull`

NewSellerFeesOrNullWithDefaults instantiates a new SellerFeesOrNull object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFeeWhenSellerWritesPost

`func (o *SellerFeesOrNull) GetFeeWhenSellerWritesPost() MoneyOrNull`

GetFeeWhenSellerWritesPost returns the FeeWhenSellerWritesPost field if non-nil, zero value otherwise.

### GetFeeWhenSellerWritesPostOk

`func (o *SellerFeesOrNull) GetFeeWhenSellerWritesPostOk() (*MoneyOrNull, bool)`

GetFeeWhenSellerWritesPostOk returns a tuple with the FeeWhenSellerWritesPost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeeWhenSellerWritesPost

`func (o *SellerFeesOrNull) SetFeeWhenSellerWritesPost(v MoneyOrNull)`

SetFeeWhenSellerWritesPost sets FeeWhenSellerWritesPost field to given value.


### SetFeeWhenSellerWritesPostNil

`func (o *SellerFeesOrNull) SetFeeWhenSellerWritesPostNil(b bool)`

 SetFeeWhenSellerWritesPostNil sets the value for FeeWhenSellerWritesPost to be an explicit nil

### UnsetFeeWhenSellerWritesPost
`func (o *SellerFeesOrNull) UnsetFeeWhenSellerWritesPost()`

UnsetFeeWhenSellerWritesPost ensures that no value is present for FeeWhenSellerWritesPost, not even an explicit nil
### GetFeeWhenSellerDoesNotWritePost

`func (o *SellerFeesOrNull) GetFeeWhenSellerDoesNotWritePost() MoneyOrNull`

GetFeeWhenSellerDoesNotWritePost returns the FeeWhenSellerDoesNotWritePost field if non-nil, zero value otherwise.

### GetFeeWhenSellerDoesNotWritePostOk

`func (o *SellerFeesOrNull) GetFeeWhenSellerDoesNotWritePostOk() (*MoneyOrNull, bool)`

GetFeeWhenSellerDoesNotWritePostOk returns a tuple with the FeeWhenSellerDoesNotWritePost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeeWhenSellerDoesNotWritePost

`func (o *SellerFeesOrNull) SetFeeWhenSellerDoesNotWritePost(v MoneyOrNull)`

SetFeeWhenSellerDoesNotWritePost sets FeeWhenSellerDoesNotWritePost field to given value.


### SetFeeWhenSellerDoesNotWritePostNil

`func (o *SellerFeesOrNull) SetFeeWhenSellerDoesNotWritePostNil(b bool)`

 SetFeeWhenSellerDoesNotWritePostNil sets the value for FeeWhenSellerDoesNotWritePost to be an explicit nil

### UnsetFeeWhenSellerDoesNotWritePost
`func (o *SellerFeesOrNull) UnsetFeeWhenSellerDoesNotWritePost()`

UnsetFeeWhenSellerDoesNotWritePost ensures that no value is present for FeeWhenSellerDoesNotWritePost, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


