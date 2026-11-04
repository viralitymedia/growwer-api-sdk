# BalanceLowEventDataWallet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AvailableBalance** | [**Money**](Money.md) |  | 
**Currency** | **string** | The currency of the wallet. | 

## Methods

### NewBalanceLowEventDataWallet

`func NewBalanceLowEventDataWallet(availableBalance Money, currency string, ) *BalanceLowEventDataWallet`

NewBalanceLowEventDataWallet instantiates a new BalanceLowEventDataWallet object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBalanceLowEventDataWalletWithDefaults

`func NewBalanceLowEventDataWalletWithDefaults() *BalanceLowEventDataWallet`

NewBalanceLowEventDataWalletWithDefaults instantiates a new BalanceLowEventDataWallet object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAvailableBalance

`func (o *BalanceLowEventDataWallet) GetAvailableBalance() Money`

GetAvailableBalance returns the AvailableBalance field if non-nil, zero value otherwise.

### GetAvailableBalanceOk

`func (o *BalanceLowEventDataWallet) GetAvailableBalanceOk() (*Money, bool)`

GetAvailableBalanceOk returns a tuple with the AvailableBalance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvailableBalance

`func (o *BalanceLowEventDataWallet) SetAvailableBalance(v Money)`

SetAvailableBalance sets AvailableBalance field to given value.


### GetCurrency

`func (o *BalanceLowEventDataWallet) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *BalanceLowEventDataWallet) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *BalanceLowEventDataWallet) SetCurrency(v string)`

SetCurrency sets Currency field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


