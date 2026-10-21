# ListSellerMedias200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]SellerMedia**](SellerMedia.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewListSellerMedias200Response

`func NewListSellerMedias200Response(items []SellerMedia, total int32, ) *ListSellerMedias200Response`

NewListSellerMedias200Response instantiates a new ListSellerMedias200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListSellerMedias200ResponseWithDefaults

`func NewListSellerMedias200ResponseWithDefaults() *ListSellerMedias200Response`

NewListSellerMedias200ResponseWithDefaults instantiates a new ListSellerMedias200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListSellerMedias200Response) GetItems() []SellerMedia`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListSellerMedias200Response) GetItemsOk() (*[]SellerMedia, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListSellerMedias200Response) SetItems(v []SellerMedia)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ListSellerMedias200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListSellerMedias200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListSellerMedias200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


