# ListSellerTransactions200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]SellerTransaction**](SellerTransaction.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewListSellerTransactions200Response

`func NewListSellerTransactions200Response(items []SellerTransaction, total int32, ) *ListSellerTransactions200Response`

NewListSellerTransactions200Response instantiates a new ListSellerTransactions200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListSellerTransactions200ResponseWithDefaults

`func NewListSellerTransactions200ResponseWithDefaults() *ListSellerTransactions200Response`

NewListSellerTransactions200ResponseWithDefaults instantiates a new ListSellerTransactions200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListSellerTransactions200Response) GetItems() []SellerTransaction`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListSellerTransactions200Response) GetItemsOk() (*[]SellerTransaction, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListSellerTransactions200Response) SetItems(v []SellerTransaction)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ListSellerTransactions200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListSellerTransactions200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListSellerTransactions200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


