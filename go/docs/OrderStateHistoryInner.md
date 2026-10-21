# OrderStateHistoryInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**State** | **string** |  | 
**Date** | **time.Time** |  | 
**Reason** | [**NullableOrderStateHistoryInnerReason**](OrderStateHistoryInnerReason.md) |  | 

## Methods

### NewOrderStateHistoryInner

`func NewOrderStateHistoryInner(state string, date time.Time, reason NullableOrderStateHistoryInnerReason, ) *OrderStateHistoryInner`

NewOrderStateHistoryInner instantiates a new OrderStateHistoryInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderStateHistoryInnerWithDefaults

`func NewOrderStateHistoryInnerWithDefaults() *OrderStateHistoryInner`

NewOrderStateHistoryInnerWithDefaults instantiates a new OrderStateHistoryInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetState

`func (o *OrderStateHistoryInner) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *OrderStateHistoryInner) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *OrderStateHistoryInner) SetState(v string)`

SetState sets State field to given value.


### GetDate

`func (o *OrderStateHistoryInner) GetDate() time.Time`

GetDate returns the Date field if non-nil, zero value otherwise.

### GetDateOk

`func (o *OrderStateHistoryInner) GetDateOk() (*time.Time, bool)`

GetDateOk returns a tuple with the Date field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDate

`func (o *OrderStateHistoryInner) SetDate(v time.Time)`

SetDate sets Date field to given value.


### GetReason

`func (o *OrderStateHistoryInner) GetReason() OrderStateHistoryInnerReason`

GetReason returns the Reason field if non-nil, zero value otherwise.

### GetReasonOk

`func (o *OrderStateHistoryInner) GetReasonOk() (*OrderStateHistoryInnerReason, bool)`

GetReasonOk returns a tuple with the Reason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReason

`func (o *OrderStateHistoryInner) SetReason(v OrderStateHistoryInnerReason)`

SetReason sets Reason field to given value.


### SetReasonNil

`func (o *OrderStateHistoryInner) SetReasonNil(b bool)`

 SetReasonNil sets the value for Reason to be an explicit nil

### UnsetReason
`func (o *OrderStateHistoryInner) UnsetReason()`

UnsetReason ensures that no value is present for Reason, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


