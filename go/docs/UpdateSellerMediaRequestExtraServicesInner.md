# UpdateSellerMediaRequestExtraServicesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**Cost** | [**Money**](Money.md) | What you are paid for the extra service. | 

## Methods

### NewUpdateSellerMediaRequestExtraServicesInner

`func NewUpdateSellerMediaRequestExtraServicesInner(name string, cost Money, ) *UpdateSellerMediaRequestExtraServicesInner`

NewUpdateSellerMediaRequestExtraServicesInner instantiates a new UpdateSellerMediaRequestExtraServicesInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateSellerMediaRequestExtraServicesInnerWithDefaults

`func NewUpdateSellerMediaRequestExtraServicesInnerWithDefaults() *UpdateSellerMediaRequestExtraServicesInner`

NewUpdateSellerMediaRequestExtraServicesInnerWithDefaults instantiates a new UpdateSellerMediaRequestExtraServicesInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *UpdateSellerMediaRequestExtraServicesInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateSellerMediaRequestExtraServicesInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpdateSellerMediaRequestExtraServicesInner) SetName(v string)`

SetName sets Name field to given value.


### GetCost

`func (o *UpdateSellerMediaRequestExtraServicesInner) GetCost() Money`

GetCost returns the Cost field if non-nil, zero value otherwise.

### GetCostOk

`func (o *UpdateSellerMediaRequestExtraServicesInner) GetCostOk() (*Money, bool)`

GetCostOk returns a tuple with the Cost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCost

`func (o *UpdateSellerMediaRequestExtraServicesInner) SetCost(v Money)`

SetCost sets Cost field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


