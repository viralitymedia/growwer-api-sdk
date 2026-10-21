# ManagedServiceProposalsEstimate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AcceptedTotal** | [**Money**](Money.md) | The proposals already accepted and still awaiting their order. | 
**SelectedTotal** | [**Money**](Money.md) | The proposals named in &#x60;accept&#x60;. | 
**Total** | [**Money**](Money.md) | &#x60;acceptedTotal&#x60; plus &#x60;selectedTotal&#x60;. | 
**AvailableBalance** | [**Money**](Money.md) | Your wallet&#39;s available balance. | 
**Missing** | [**Money**](Money.md) | How much the available balance falls short of &#x60;total&#x60;; zero when it covers it. | 
**SufficientBalance** | **bool** | Whether the available balance covers &#x60;total&#x60;. | 

## Methods

### NewManagedServiceProposalsEstimate

`func NewManagedServiceProposalsEstimate(acceptedTotal Money, selectedTotal Money, total Money, availableBalance Money, missing Money, sufficientBalance bool, ) *ManagedServiceProposalsEstimate`

NewManagedServiceProposalsEstimate instantiates a new ManagedServiceProposalsEstimate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewManagedServiceProposalsEstimateWithDefaults

`func NewManagedServiceProposalsEstimateWithDefaults() *ManagedServiceProposalsEstimate`

NewManagedServiceProposalsEstimateWithDefaults instantiates a new ManagedServiceProposalsEstimate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAcceptedTotal

`func (o *ManagedServiceProposalsEstimate) GetAcceptedTotal() Money`

GetAcceptedTotal returns the AcceptedTotal field if non-nil, zero value otherwise.

### GetAcceptedTotalOk

`func (o *ManagedServiceProposalsEstimate) GetAcceptedTotalOk() (*Money, bool)`

GetAcceptedTotalOk returns a tuple with the AcceptedTotal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAcceptedTotal

`func (o *ManagedServiceProposalsEstimate) SetAcceptedTotal(v Money)`

SetAcceptedTotal sets AcceptedTotal field to given value.


### GetSelectedTotal

`func (o *ManagedServiceProposalsEstimate) GetSelectedTotal() Money`

GetSelectedTotal returns the SelectedTotal field if non-nil, zero value otherwise.

### GetSelectedTotalOk

`func (o *ManagedServiceProposalsEstimate) GetSelectedTotalOk() (*Money, bool)`

GetSelectedTotalOk returns a tuple with the SelectedTotal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelectedTotal

`func (o *ManagedServiceProposalsEstimate) SetSelectedTotal(v Money)`

SetSelectedTotal sets SelectedTotal field to given value.


### GetTotal

`func (o *ManagedServiceProposalsEstimate) GetTotal() Money`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ManagedServiceProposalsEstimate) GetTotalOk() (*Money, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ManagedServiceProposalsEstimate) SetTotal(v Money)`

SetTotal sets Total field to given value.


### GetAvailableBalance

`func (o *ManagedServiceProposalsEstimate) GetAvailableBalance() Money`

GetAvailableBalance returns the AvailableBalance field if non-nil, zero value otherwise.

### GetAvailableBalanceOk

`func (o *ManagedServiceProposalsEstimate) GetAvailableBalanceOk() (*Money, bool)`

GetAvailableBalanceOk returns a tuple with the AvailableBalance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvailableBalance

`func (o *ManagedServiceProposalsEstimate) SetAvailableBalance(v Money)`

SetAvailableBalance sets AvailableBalance field to given value.


### GetMissing

`func (o *ManagedServiceProposalsEstimate) GetMissing() Money`

GetMissing returns the Missing field if non-nil, zero value otherwise.

### GetMissingOk

`func (o *ManagedServiceProposalsEstimate) GetMissingOk() (*Money, bool)`

GetMissingOk returns a tuple with the Missing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMissing

`func (o *ManagedServiceProposalsEstimate) SetMissing(v Money)`

SetMissing sets Missing field to given value.


### GetSufficientBalance

`func (o *ManagedServiceProposalsEstimate) GetSufficientBalance() bool`

GetSufficientBalance returns the SufficientBalance field if non-nil, zero value otherwise.

### GetSufficientBalanceOk

`func (o *ManagedServiceProposalsEstimate) GetSufficientBalanceOk() (*bool, bool)`

GetSufficientBalanceOk returns a tuple with the SufficientBalance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSufficientBalance

`func (o *ManagedServiceProposalsEstimate) SetSufficientBalance(v bool)`

SetSufficientBalance sets SufficientBalance field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


