# OrderEstimate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Price** | [**Money**](Money.md) | What the order costs you. Send it as &#x60;expectedPrice&#x60;. | 
**AvailableBalance** | [**Money**](Money.md) | Your wallet&#39;s available balance. | 
**Missing** | [**Money**](Money.md) | How much the available balance falls short of the price; zero when it covers it. | 
**SufficientBalance** | **bool** | Whether the available balance covers the price. | 

## Methods

### NewOrderEstimate

`func NewOrderEstimate(price Money, availableBalance Money, missing Money, sufficientBalance bool, ) *OrderEstimate`

NewOrderEstimate instantiates a new OrderEstimate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderEstimateWithDefaults

`func NewOrderEstimateWithDefaults() *OrderEstimate`

NewOrderEstimateWithDefaults instantiates a new OrderEstimate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrice

`func (o *OrderEstimate) GetPrice() Money`

GetPrice returns the Price field if non-nil, zero value otherwise.

### GetPriceOk

`func (o *OrderEstimate) GetPriceOk() (*Money, bool)`

GetPriceOk returns a tuple with the Price field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrice

`func (o *OrderEstimate) SetPrice(v Money)`

SetPrice sets Price field to given value.


### GetAvailableBalance

`func (o *OrderEstimate) GetAvailableBalance() Money`

GetAvailableBalance returns the AvailableBalance field if non-nil, zero value otherwise.

### GetAvailableBalanceOk

`func (o *OrderEstimate) GetAvailableBalanceOk() (*Money, bool)`

GetAvailableBalanceOk returns a tuple with the AvailableBalance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvailableBalance

`func (o *OrderEstimate) SetAvailableBalance(v Money)`

SetAvailableBalance sets AvailableBalance field to given value.


### GetMissing

`func (o *OrderEstimate) GetMissing() Money`

GetMissing returns the Missing field if non-nil, zero value otherwise.

### GetMissingOk

`func (o *OrderEstimate) GetMissingOk() (*Money, bool)`

GetMissingOk returns a tuple with the Missing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMissing

`func (o *OrderEstimate) SetMissing(v Money)`

SetMissing sets Missing field to given value.


### GetSufficientBalance

`func (o *OrderEstimate) GetSufficientBalance() bool`

GetSufficientBalance returns the SufficientBalance field if non-nil, zero value otherwise.

### GetSufficientBalanceOk

`func (o *OrderEstimate) GetSufficientBalanceOk() (*bool, bool)`

GetSufficientBalanceOk returns a tuple with the SufficientBalance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSufficientBalance

`func (o *OrderEstimate) SetSufficientBalance(v bool)`

SetSufficientBalance sets SufficientBalance field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


