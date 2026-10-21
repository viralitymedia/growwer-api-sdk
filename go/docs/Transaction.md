# Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Type** | **string** | What moved the money, for example &#x60;deposit&#x60; (a top-up), &#x60;debit_from_order&#x60; (an order), &#x60;gift&#x60; or &#x60;manual_charge&#x60;. | 
**State** | **string** | An order&#39;s debit stays &#x60;pending_confirmation&#x60; until the order settles, and is &#x60;cancelled&#x60; when the order is refunded. | 
**Direction** | **string** |  | 
**Amount** | [**Money**](Money.md) |  | 
**Description** | **NullableString** | The text the wallet page prints as it is, or null where it prints a translated label instead (then see &#x60;descriptionCode&#x60;). | 
**DescriptionCode** | **NullableString** | A stable code for the label the wallet page translates: a payment method for a top-up, or &#x60;affiliate_promo&#x60;. Null otherwise. | 
**OrderId** | **NullableString** | The order this transaction paid for or refunded, while it exists. | 
**InvoiceId** | **NullableString** | The invoice of this transaction, if any; GET /invoices/{id}/pdf downloads it. | 
**HasDocument** | **bool** | Whether GET /wallets/buyer/transactions/{id}/document downloads a document for it. | 
**CreatedAt** | **time.Time** |  | 
**UpdatedAt** | **time.Time** |  | 

## Methods

### NewTransaction

`func NewTransaction(id string, type_ string, state string, direction string, amount Money, description NullableString, descriptionCode NullableString, orderId NullableString, invoiceId NullableString, hasDocument bool, createdAt time.Time, updatedAt time.Time, ) *Transaction`

NewTransaction instantiates a new Transaction object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTransactionWithDefaults

`func NewTransactionWithDefaults() *Transaction`

NewTransactionWithDefaults instantiates a new Transaction object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Transaction) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Transaction) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Transaction) SetId(v string)`

SetId sets Id field to given value.


### GetType

`func (o *Transaction) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Transaction) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Transaction) SetType(v string)`

SetType sets Type field to given value.


### GetState

`func (o *Transaction) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *Transaction) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *Transaction) SetState(v string)`

SetState sets State field to given value.


### GetDirection

`func (o *Transaction) GetDirection() string`

GetDirection returns the Direction field if non-nil, zero value otherwise.

### GetDirectionOk

`func (o *Transaction) GetDirectionOk() (*string, bool)`

GetDirectionOk returns a tuple with the Direction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDirection

`func (o *Transaction) SetDirection(v string)`

SetDirection sets Direction field to given value.


### GetAmount

`func (o *Transaction) GetAmount() Money`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *Transaction) GetAmountOk() (*Money, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *Transaction) SetAmount(v Money)`

SetAmount sets Amount field to given value.


### GetDescription

`func (o *Transaction) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Transaction) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Transaction) SetDescription(v string)`

SetDescription sets Description field to given value.


### SetDescriptionNil

`func (o *Transaction) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Transaction) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetDescriptionCode

`func (o *Transaction) GetDescriptionCode() string`

GetDescriptionCode returns the DescriptionCode field if non-nil, zero value otherwise.

### GetDescriptionCodeOk

`func (o *Transaction) GetDescriptionCodeOk() (*string, bool)`

GetDescriptionCodeOk returns a tuple with the DescriptionCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescriptionCode

`func (o *Transaction) SetDescriptionCode(v string)`

SetDescriptionCode sets DescriptionCode field to given value.


### SetDescriptionCodeNil

`func (o *Transaction) SetDescriptionCodeNil(b bool)`

 SetDescriptionCodeNil sets the value for DescriptionCode to be an explicit nil

### UnsetDescriptionCode
`func (o *Transaction) UnsetDescriptionCode()`

UnsetDescriptionCode ensures that no value is present for DescriptionCode, not even an explicit nil
### GetOrderId

`func (o *Transaction) GetOrderId() string`

GetOrderId returns the OrderId field if non-nil, zero value otherwise.

### GetOrderIdOk

`func (o *Transaction) GetOrderIdOk() (*string, bool)`

GetOrderIdOk returns a tuple with the OrderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderId

`func (o *Transaction) SetOrderId(v string)`

SetOrderId sets OrderId field to given value.


### SetOrderIdNil

`func (o *Transaction) SetOrderIdNil(b bool)`

 SetOrderIdNil sets the value for OrderId to be an explicit nil

### UnsetOrderId
`func (o *Transaction) UnsetOrderId()`

UnsetOrderId ensures that no value is present for OrderId, not even an explicit nil
### GetInvoiceId

`func (o *Transaction) GetInvoiceId() string`

GetInvoiceId returns the InvoiceId field if non-nil, zero value otherwise.

### GetInvoiceIdOk

`func (o *Transaction) GetInvoiceIdOk() (*string, bool)`

GetInvoiceIdOk returns a tuple with the InvoiceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInvoiceId

`func (o *Transaction) SetInvoiceId(v string)`

SetInvoiceId sets InvoiceId field to given value.


### SetInvoiceIdNil

`func (o *Transaction) SetInvoiceIdNil(b bool)`

 SetInvoiceIdNil sets the value for InvoiceId to be an explicit nil

### UnsetInvoiceId
`func (o *Transaction) UnsetInvoiceId()`

UnsetInvoiceId ensures that no value is present for InvoiceId, not even an explicit nil
### GetHasDocument

`func (o *Transaction) GetHasDocument() bool`

GetHasDocument returns the HasDocument field if non-nil, zero value otherwise.

### GetHasDocumentOk

`func (o *Transaction) GetHasDocumentOk() (*bool, bool)`

GetHasDocumentOk returns a tuple with the HasDocument field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasDocument

`func (o *Transaction) SetHasDocument(v bool)`

SetHasDocument sets HasDocument field to given value.


### GetCreatedAt

`func (o *Transaction) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Transaction) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Transaction) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *Transaction) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Transaction) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Transaction) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


