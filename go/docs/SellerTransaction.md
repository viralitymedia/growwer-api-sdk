# SellerTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Type** | **string** | What moved the money, for example &#x60;credit_from_order&#x60; (an order you delivered), &#x60;credit_from_writing&#x60;, &#x60;withdrawal&#x60;, &#x60;manual_deposit&#x60; or &#x60;manual_charge&#x60;. | 
**State** | **string** | An order&#39;s earning stays &#x60;pending_confirmation&#x60; until the order settles. | 
**Direction** | **string** |  | 
**Amount** | [**Money**](Money.md) |  | 
**Description** | **NullableString** | The text the wallet page prints, or null when the movement points to an order or a withdrawal instead, or has no text. | 
**OrderId** | **NullableString** | Your order this earning came from, while it exists; GET /seller/orders/{id} reads it. | 
**WithdrawalId** | **NullableString** | Your withdrawal this debit paid; GET /withdrawals lists it. | 
**HasDocument** | **bool** | Whether GET /wallets/seller/transactions/{id}/document downloads a document for it. | 
**CreatedAt** | **time.Time** |  | 
**UpdatedAt** | **time.Time** |  | 

## Methods

### NewSellerTransaction

`func NewSellerTransaction(id string, type_ string, state string, direction string, amount Money, description NullableString, orderId NullableString, withdrawalId NullableString, hasDocument bool, createdAt time.Time, updatedAt time.Time, ) *SellerTransaction`

NewSellerTransaction instantiates a new SellerTransaction object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerTransactionWithDefaults

`func NewSellerTransactionWithDefaults() *SellerTransaction`

NewSellerTransactionWithDefaults instantiates a new SellerTransaction object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SellerTransaction) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SellerTransaction) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SellerTransaction) SetId(v string)`

SetId sets Id field to given value.


### GetType

`func (o *SellerTransaction) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SellerTransaction) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SellerTransaction) SetType(v string)`

SetType sets Type field to given value.


### GetState

`func (o *SellerTransaction) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *SellerTransaction) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *SellerTransaction) SetState(v string)`

SetState sets State field to given value.


### GetDirection

`func (o *SellerTransaction) GetDirection() string`

GetDirection returns the Direction field if non-nil, zero value otherwise.

### GetDirectionOk

`func (o *SellerTransaction) GetDirectionOk() (*string, bool)`

GetDirectionOk returns a tuple with the Direction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDirection

`func (o *SellerTransaction) SetDirection(v string)`

SetDirection sets Direction field to given value.


### GetAmount

`func (o *SellerTransaction) GetAmount() Money`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *SellerTransaction) GetAmountOk() (*Money, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *SellerTransaction) SetAmount(v Money)`

SetAmount sets Amount field to given value.


### GetDescription

`func (o *SellerTransaction) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SellerTransaction) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SellerTransaction) SetDescription(v string)`

SetDescription sets Description field to given value.


### SetDescriptionNil

`func (o *SellerTransaction) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *SellerTransaction) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetOrderId

`func (o *SellerTransaction) GetOrderId() string`

GetOrderId returns the OrderId field if non-nil, zero value otherwise.

### GetOrderIdOk

`func (o *SellerTransaction) GetOrderIdOk() (*string, bool)`

GetOrderIdOk returns a tuple with the OrderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderId

`func (o *SellerTransaction) SetOrderId(v string)`

SetOrderId sets OrderId field to given value.


### SetOrderIdNil

`func (o *SellerTransaction) SetOrderIdNil(b bool)`

 SetOrderIdNil sets the value for OrderId to be an explicit nil

### UnsetOrderId
`func (o *SellerTransaction) UnsetOrderId()`

UnsetOrderId ensures that no value is present for OrderId, not even an explicit nil
### GetWithdrawalId

`func (o *SellerTransaction) GetWithdrawalId() string`

GetWithdrawalId returns the WithdrawalId field if non-nil, zero value otherwise.

### GetWithdrawalIdOk

`func (o *SellerTransaction) GetWithdrawalIdOk() (*string, bool)`

GetWithdrawalIdOk returns a tuple with the WithdrawalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWithdrawalId

`func (o *SellerTransaction) SetWithdrawalId(v string)`

SetWithdrawalId sets WithdrawalId field to given value.


### SetWithdrawalIdNil

`func (o *SellerTransaction) SetWithdrawalIdNil(b bool)`

 SetWithdrawalIdNil sets the value for WithdrawalId to be an explicit nil

### UnsetWithdrawalId
`func (o *SellerTransaction) UnsetWithdrawalId()`

UnsetWithdrawalId ensures that no value is present for WithdrawalId, not even an explicit nil
### GetHasDocument

`func (o *SellerTransaction) GetHasDocument() bool`

GetHasDocument returns the HasDocument field if non-nil, zero value otherwise.

### GetHasDocumentOk

`func (o *SellerTransaction) GetHasDocumentOk() (*bool, bool)`

GetHasDocumentOk returns a tuple with the HasDocument field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasDocument

`func (o *SellerTransaction) SetHasDocument(v bool)`

SetHasDocument sets HasDocument field to given value.


### GetCreatedAt

`func (o *SellerTransaction) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SellerTransaction) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SellerTransaction) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *SellerTransaction) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *SellerTransaction) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *SellerTransaction) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


