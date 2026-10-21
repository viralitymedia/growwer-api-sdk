# Invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Number** | **string** |  | 
**IssuedAt** | **time.Time** |  | 
**Total** | [**Money**](Money.md) | The invoice total, taxes included. | 

## Methods

### NewInvoice

`func NewInvoice(id string, number string, issuedAt time.Time, total Money, ) *Invoice`

NewInvoice instantiates a new Invoice object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInvoiceWithDefaults

`func NewInvoiceWithDefaults() *Invoice`

NewInvoiceWithDefaults instantiates a new Invoice object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Invoice) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Invoice) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Invoice) SetId(v string)`

SetId sets Id field to given value.


### GetNumber

`func (o *Invoice) GetNumber() string`

GetNumber returns the Number field if non-nil, zero value otherwise.

### GetNumberOk

`func (o *Invoice) GetNumberOk() (*string, bool)`

GetNumberOk returns a tuple with the Number field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumber

`func (o *Invoice) SetNumber(v string)`

SetNumber sets Number field to given value.


### GetIssuedAt

`func (o *Invoice) GetIssuedAt() time.Time`

GetIssuedAt returns the IssuedAt field if non-nil, zero value otherwise.

### GetIssuedAtOk

`func (o *Invoice) GetIssuedAtOk() (*time.Time, bool)`

GetIssuedAtOk returns a tuple with the IssuedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssuedAt

`func (o *Invoice) SetIssuedAt(v time.Time)`

SetIssuedAt sets IssuedAt field to given value.


### GetTotal

`func (o *Invoice) GetTotal() Money`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *Invoice) GetTotalOk() (*Money, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *Invoice) SetTotal(v Money)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


