# SavedFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | **string** |  | 
**ActiveFilterCount** | **int32** | How many filters it applies. | 
**Notifications** | [**SavedFilterNotifications**](SavedFilterNotifications.md) |  | 
**CreatedAt** | **time.Time** |  | 

## Methods

### NewSavedFilter

`func NewSavedFilter(id string, name string, activeFilterCount int32, notifications SavedFilterNotifications, createdAt time.Time, ) *SavedFilter`

NewSavedFilter instantiates a new SavedFilter object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSavedFilterWithDefaults

`func NewSavedFilterWithDefaults() *SavedFilter`

NewSavedFilterWithDefaults instantiates a new SavedFilter object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SavedFilter) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SavedFilter) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SavedFilter) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *SavedFilter) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SavedFilter) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SavedFilter) SetName(v string)`

SetName sets Name field to given value.


### GetActiveFilterCount

`func (o *SavedFilter) GetActiveFilterCount() int32`

GetActiveFilterCount returns the ActiveFilterCount field if non-nil, zero value otherwise.

### GetActiveFilterCountOk

`func (o *SavedFilter) GetActiveFilterCountOk() (*int32, bool)`

GetActiveFilterCountOk returns a tuple with the ActiveFilterCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActiveFilterCount

`func (o *SavedFilter) SetActiveFilterCount(v int32)`

SetActiveFilterCount sets ActiveFilterCount field to given value.


### GetNotifications

`func (o *SavedFilter) GetNotifications() SavedFilterNotifications`

GetNotifications returns the Notifications field if non-nil, zero value otherwise.

### GetNotificationsOk

`func (o *SavedFilter) GetNotificationsOk() (*SavedFilterNotifications, bool)`

GetNotificationsOk returns a tuple with the Notifications field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotifications

`func (o *SavedFilter) SetNotifications(v SavedFilterNotifications)`

SetNotifications sets Notifications field to given value.


### GetCreatedAt

`func (o *SavedFilter) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SavedFilter) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SavedFilter) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


