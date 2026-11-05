# TopUpTestWalletRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Amount** | [**Money**](Money.md) | What to credit, in EUR: from 1 to 1000000 cents. | 

## Methods

### NewTopUpTestWalletRequest

`func NewTopUpTestWalletRequest(amount Money, ) *TopUpTestWalletRequest`

NewTopUpTestWalletRequest instantiates a new TopUpTestWalletRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTopUpTestWalletRequestWithDefaults

`func NewTopUpTestWalletRequestWithDefaults() *TopUpTestWalletRequest`

NewTopUpTestWalletRequestWithDefaults instantiates a new TopUpTestWalletRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAmount

`func (o *TopUpTestWalletRequest) GetAmount() Money`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *TopUpTestWalletRequest) GetAmountOk() (*Money, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *TopUpTestWalletRequest) SetAmount(v Money)`

SetAmount sets Amount field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


