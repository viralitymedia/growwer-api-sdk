# ListSellerOrders200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]SellerOrder**](SellerOrder.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewListSellerOrders200Response

`func NewListSellerOrders200Response(items []SellerOrder, total int32, ) *ListSellerOrders200Response`

NewListSellerOrders200Response instantiates a new ListSellerOrders200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListSellerOrders200ResponseWithDefaults

`func NewListSellerOrders200ResponseWithDefaults() *ListSellerOrders200Response`

NewListSellerOrders200ResponseWithDefaults instantiates a new ListSellerOrders200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListSellerOrders200Response) GetItems() []SellerOrder`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListSellerOrders200Response) GetItemsOk() (*[]SellerOrder, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListSellerOrders200Response) SetItems(v []SellerOrder)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ListSellerOrders200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListSellerOrders200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListSellerOrders200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


