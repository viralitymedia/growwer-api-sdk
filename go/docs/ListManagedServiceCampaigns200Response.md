# ListManagedServiceCampaigns200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]ManagedServiceCampaign**](ManagedServiceCampaign.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewListManagedServiceCampaigns200Response

`func NewListManagedServiceCampaigns200Response(items []ManagedServiceCampaign, total int32, ) *ListManagedServiceCampaigns200Response`

NewListManagedServiceCampaigns200Response instantiates a new ListManagedServiceCampaigns200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListManagedServiceCampaigns200ResponseWithDefaults

`func NewListManagedServiceCampaigns200ResponseWithDefaults() *ListManagedServiceCampaigns200Response`

NewListManagedServiceCampaigns200ResponseWithDefaults instantiates a new ListManagedServiceCampaigns200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListManagedServiceCampaigns200Response) GetItems() []ManagedServiceCampaign`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListManagedServiceCampaigns200Response) GetItemsOk() (*[]ManagedServiceCampaign, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListManagedServiceCampaigns200Response) SetItems(v []ManagedServiceCampaign)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ListManagedServiceCampaigns200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListManagedServiceCampaigns200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListManagedServiceCampaigns200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


