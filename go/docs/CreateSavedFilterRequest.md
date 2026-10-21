# CreateSavedFilterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | 1 to 255 characters. | 
**Filters** | **map[string]interface{}** | At least one filter parameter of GET /projects/{id}/medias, or &#x60;source&#x60;, by name. | 
**NotificationFrequency** | Pointer to **string** | Email new matching medias this often. Omit it for no emails. | [optional] 

## Methods

### NewCreateSavedFilterRequest

`func NewCreateSavedFilterRequest(name string, filters map[string]interface{}, ) *CreateSavedFilterRequest`

NewCreateSavedFilterRequest instantiates a new CreateSavedFilterRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateSavedFilterRequestWithDefaults

`func NewCreateSavedFilterRequestWithDefaults() *CreateSavedFilterRequest`

NewCreateSavedFilterRequestWithDefaults instantiates a new CreateSavedFilterRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateSavedFilterRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateSavedFilterRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateSavedFilterRequest) SetName(v string)`

SetName sets Name field to given value.


### GetFilters

`func (o *CreateSavedFilterRequest) GetFilters() map[string]interface{}`

GetFilters returns the Filters field if non-nil, zero value otherwise.

### GetFiltersOk

`func (o *CreateSavedFilterRequest) GetFiltersOk() (*map[string]interface{}, bool)`

GetFiltersOk returns a tuple with the Filters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFilters

`func (o *CreateSavedFilterRequest) SetFilters(v map[string]interface{})`

SetFilters sets Filters field to given value.


### GetNotificationFrequency

`func (o *CreateSavedFilterRequest) GetNotificationFrequency() string`

GetNotificationFrequency returns the NotificationFrequency field if non-nil, zero value otherwise.

### GetNotificationFrequencyOk

`func (o *CreateSavedFilterRequest) GetNotificationFrequencyOk() (*string, bool)`

GetNotificationFrequencyOk returns a tuple with the NotificationFrequency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotificationFrequency

`func (o *CreateSavedFilterRequest) SetNotificationFrequency(v string)`

SetNotificationFrequency sets NotificationFrequency field to given value.

### HasNotificationFrequency

`func (o *CreateSavedFilterRequest) HasNotificationFrequency() bool`

HasNotificationFrequency returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


