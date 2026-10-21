# ListBuyerTransactions200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]Transaction**](Transaction.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewListBuyerTransactions200Response

`func NewListBuyerTransactions200Response(items []Transaction, total int32, ) *ListBuyerTransactions200Response`

NewListBuyerTransactions200Response instantiates a new ListBuyerTransactions200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListBuyerTransactions200ResponseWithDefaults

`func NewListBuyerTransactions200ResponseWithDefaults() *ListBuyerTransactions200Response`

NewListBuyerTransactions200ResponseWithDefaults instantiates a new ListBuyerTransactions200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListBuyerTransactions200Response) GetItems() []Transaction`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListBuyerTransactions200Response) GetItemsOk() (*[]Transaction, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListBuyerTransactions200Response) SetItems(v []Transaction)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ListBuyerTransactions200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListBuyerTransactions200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListBuyerTransactions200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


