# Withdrawal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**State** | **string** |  | 
**Amount** | [**Money**](Money.md) | What you withdraw. | 
**Method** | **string** |  | 
**HasInvoice** | **bool** | Whether you uploaded an invoice; GET /withdrawals/{id}/invoice downloads it. | 
**CreatedAt** | **time.Time** |  | 

## Methods

### NewWithdrawal

`func NewWithdrawal(id string, state string, amount Money, method string, hasInvoice bool, createdAt time.Time, ) *Withdrawal`

NewWithdrawal instantiates a new Withdrawal object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWithdrawalWithDefaults

`func NewWithdrawalWithDefaults() *Withdrawal`

NewWithdrawalWithDefaults instantiates a new Withdrawal object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Withdrawal) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Withdrawal) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Withdrawal) SetId(v string)`

SetId sets Id field to given value.


### GetState

`func (o *Withdrawal) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *Withdrawal) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *Withdrawal) SetState(v string)`

SetState sets State field to given value.


### GetAmount

`func (o *Withdrawal) GetAmount() Money`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *Withdrawal) GetAmountOk() (*Money, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *Withdrawal) SetAmount(v Money)`

SetAmount sets Amount field to given value.


### GetMethod

`func (o *Withdrawal) GetMethod() string`

GetMethod returns the Method field if non-nil, zero value otherwise.

### GetMethodOk

`func (o *Withdrawal) GetMethodOk() (*string, bool)`

GetMethodOk returns a tuple with the Method field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMethod

`func (o *Withdrawal) SetMethod(v string)`

SetMethod sets Method field to given value.


### GetHasInvoice

`func (o *Withdrawal) GetHasInvoice() bool`

GetHasInvoice returns the HasInvoice field if non-nil, zero value otherwise.

### GetHasInvoiceOk

`func (o *Withdrawal) GetHasInvoiceOk() (*bool, bool)`

GetHasInvoiceOk returns a tuple with the HasInvoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasInvoice

`func (o *Withdrawal) SetHasInvoice(v bool)`

SetHasInvoice sets HasInvoice field to given value.


### GetCreatedAt

`func (o *Withdrawal) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Withdrawal) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Withdrawal) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


