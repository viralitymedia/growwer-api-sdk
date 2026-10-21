# ListOrders200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]Order**](Order.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewListOrders200Response

`func NewListOrders200Response(items []Order, total int32, ) *ListOrders200Response`

NewListOrders200Response instantiates a new ListOrders200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListOrders200ResponseWithDefaults

`func NewListOrders200ResponseWithDefaults() *ListOrders200Response`

NewListOrders200ResponseWithDefaults instantiates a new ListOrders200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListOrders200Response) GetItems() []Order`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListOrders200Response) GetItemsOk() (*[]Order, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListOrders200Response) SetItems(v []Order)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ListOrders200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListOrders200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListOrders200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


