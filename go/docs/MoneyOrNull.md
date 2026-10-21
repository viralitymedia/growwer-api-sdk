# MoneyOrNull

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Amount** | **int32** | Integer cents. | 
**Currency** | **string** | ISO 4217 currency code. | 

## Methods

### NewMoneyOrNull

`func NewMoneyOrNull(amount int32, currency string, ) *MoneyOrNull`

NewMoneyOrNull instantiates a new MoneyOrNull object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMoneyOrNullWithDefaults

`func NewMoneyOrNullWithDefaults() *MoneyOrNull`

NewMoneyOrNullWithDefaults instantiates a new MoneyOrNull object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAmount

`func (o *MoneyOrNull) GetAmount() int32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *MoneyOrNull) GetAmountOk() (*int32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *MoneyOrNull) SetAmount(v int32)`

SetAmount sets Amount field to given value.


### GetCurrency

`func (o *MoneyOrNull) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *MoneyOrNull) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *MoneyOrNull) SetCurrency(v string)`

SetCurrency sets Currency field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


