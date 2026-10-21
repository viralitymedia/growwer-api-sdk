# ListSavedFilters200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]SavedFilter**](SavedFilter.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewListSavedFilters200Response

`func NewListSavedFilters200Response(items []SavedFilter, total int32, ) *ListSavedFilters200Response`

NewListSavedFilters200Response instantiates a new ListSavedFilters200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListSavedFilters200ResponseWithDefaults

`func NewListSavedFilters200ResponseWithDefaults() *ListSavedFilters200Response`

NewListSavedFilters200ResponseWithDefaults instantiates a new ListSavedFilters200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListSavedFilters200Response) GetItems() []SavedFilter`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListSavedFilters200Response) GetItemsOk() (*[]SavedFilter, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListSavedFilters200Response) SetItems(v []SavedFilter)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ListSavedFilters200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListSavedFilters200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListSavedFilters200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


