# Balance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Available** | [**Money**](Money.md) | What can be spent, or withdrawn, now. | 
**Pending** | [**Money**](Money.md) | What is held until orders in progress settle. | 

## Methods

### NewBalance

`func NewBalance(available Money, pending Money, ) *Balance`

NewBalance instantiates a new Balance object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBalanceWithDefaults

`func NewBalanceWithDefaults() *Balance`

NewBalanceWithDefaults instantiates a new Balance object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAvailable

`func (o *Balance) GetAvailable() Money`

GetAvailable returns the Available field if non-nil, zero value otherwise.

### GetAvailableOk

`func (o *Balance) GetAvailableOk() (*Money, bool)`

GetAvailableOk returns a tuple with the Available field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvailable

`func (o *Balance) SetAvailable(v Money)`

SetAvailable sets Available field to given value.


### GetPending

`func (o *Balance) GetPending() Money`

GetPending returns the Pending field if non-nil, zero value otherwise.

### GetPendingOk

`func (o *Balance) GetPendingOk() (*Money, bool)`

GetPendingOk returns a tuple with the Pending field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPending

`func (o *Balance) SetPending(v Money)`

SetPending sets Pending field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


