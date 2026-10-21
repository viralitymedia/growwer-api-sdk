# SellerOrderRejectionReason

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Why you reject the order, as the seller order page offers it. | 
**AdditionalInfo** | Pointer to **NullableString** | More about the reason, which the buyer is told, 10 to 2000 characters. Required with &#x60;other_reasons&#x60;. | [optional] 

## Methods

### NewSellerOrderRejectionReason

`func NewSellerOrderRejectionReason(name string, ) *SellerOrderRejectionReason`

NewSellerOrderRejectionReason instantiates a new SellerOrderRejectionReason object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerOrderRejectionReasonWithDefaults

`func NewSellerOrderRejectionReasonWithDefaults() *SellerOrderRejectionReason`

NewSellerOrderRejectionReasonWithDefaults instantiates a new SellerOrderRejectionReason object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *SellerOrderRejectionReason) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SellerOrderRejectionReason) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SellerOrderRejectionReason) SetName(v string)`

SetName sets Name field to given value.


### GetAdditionalInfo

`func (o *SellerOrderRejectionReason) GetAdditionalInfo() string`

GetAdditionalInfo returns the AdditionalInfo field if non-nil, zero value otherwise.

### GetAdditionalInfoOk

`func (o *SellerOrderRejectionReason) GetAdditionalInfoOk() (*string, bool)`

GetAdditionalInfoOk returns a tuple with the AdditionalInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalInfo

`func (o *SellerOrderRejectionReason) SetAdditionalInfo(v string)`

SetAdditionalInfo sets AdditionalInfo field to given value.

### HasAdditionalInfo

`func (o *SellerOrderRejectionReason) HasAdditionalInfo() bool`

HasAdditionalInfo returns a boolean if a field has been set.

### SetAdditionalInfoNil

`func (o *SellerOrderRejectionReason) SetAdditionalInfoNil(b bool)`

 SetAdditionalInfoNil sets the value for AdditionalInfo to be an explicit nil

### UnsetAdditionalInfo
`func (o *SellerOrderRejectionReason) UnsetAdditionalInfo()`

UnsetAdditionalInfo ensures that no value is present for AdditionalInfo, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


