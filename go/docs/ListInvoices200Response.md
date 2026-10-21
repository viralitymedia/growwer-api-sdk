# ListInvoices200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]Invoice**](Invoice.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewListInvoices200Response

`func NewListInvoices200Response(items []Invoice, total int32, ) *ListInvoices200Response`

NewListInvoices200Response instantiates a new ListInvoices200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListInvoices200ResponseWithDefaults

`func NewListInvoices200ResponseWithDefaults() *ListInvoices200Response`

NewListInvoices200ResponseWithDefaults instantiates a new ListInvoices200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListInvoices200Response) GetItems() []Invoice`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListInvoices200Response) GetItemsOk() (*[]Invoice, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListInvoices200Response) SetItems(v []Invoice)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ListInvoices200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListInvoices200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListInvoices200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


