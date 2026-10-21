# ListManagedServiceProposals200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]ManagedServiceProposal**](ManagedServiceProposal.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewListManagedServiceProposals200Response

`func NewListManagedServiceProposals200Response(items []ManagedServiceProposal, total int32, ) *ListManagedServiceProposals200Response`

NewListManagedServiceProposals200Response instantiates a new ListManagedServiceProposals200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListManagedServiceProposals200ResponseWithDefaults

`func NewListManagedServiceProposals200ResponseWithDefaults() *ListManagedServiceProposals200Response`

NewListManagedServiceProposals200ResponseWithDefaults instantiates a new ListManagedServiceProposals200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListManagedServiceProposals200Response) GetItems() []ManagedServiceProposal`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListManagedServiceProposals200Response) GetItemsOk() (*[]ManagedServiceProposal, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListManagedServiceProposals200Response) SetItems(v []ManagedServiceProposal)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ListManagedServiceProposals200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListManagedServiceProposals200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListManagedServiceProposals200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


