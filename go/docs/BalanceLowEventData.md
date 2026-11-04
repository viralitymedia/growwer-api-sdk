# BalanceLowEventData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Wallet** | [**BalanceLowEventDataWallet**](BalanceLowEventDataWallet.md) |  | 
**Threshold** | [**Money**](Money.md) | The subscription&#39;s &#x60;lowBalanceThreshold&#x60; that the balance dropped below. | 

## Methods

### NewBalanceLowEventData

`func NewBalanceLowEventData(wallet BalanceLowEventDataWallet, threshold Money, ) *BalanceLowEventData`

NewBalanceLowEventData instantiates a new BalanceLowEventData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBalanceLowEventDataWithDefaults

`func NewBalanceLowEventDataWithDefaults() *BalanceLowEventData`

NewBalanceLowEventDataWithDefaults instantiates a new BalanceLowEventData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWallet

`func (o *BalanceLowEventData) GetWallet() BalanceLowEventDataWallet`

GetWallet returns the Wallet field if non-nil, zero value otherwise.

### GetWalletOk

`func (o *BalanceLowEventData) GetWalletOk() (*BalanceLowEventDataWallet, bool)`

GetWalletOk returns a tuple with the Wallet field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWallet

`func (o *BalanceLowEventData) SetWallet(v BalanceLowEventDataWallet)`

SetWallet sets Wallet field to given value.


### GetThreshold

`func (o *BalanceLowEventData) GetThreshold() Money`

GetThreshold returns the Threshold field if non-nil, zero value otherwise.

### GetThresholdOk

`func (o *BalanceLowEventData) GetThresholdOk() (*Money, bool)`

GetThresholdOk returns a tuple with the Threshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreshold

`func (o *BalanceLowEventData) SetThreshold(v Money)`

SetThreshold sets Threshold field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


