# SavedFilterNotifications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | **bool** |  | 
**Frequency** | **NullableString** | How often Growwer emails new matching medias, or null when it does not. | 

## Methods

### NewSavedFilterNotifications

`func NewSavedFilterNotifications(enabled bool, frequency NullableString, ) *SavedFilterNotifications`

NewSavedFilterNotifications instantiates a new SavedFilterNotifications object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSavedFilterNotificationsWithDefaults

`func NewSavedFilterNotificationsWithDefaults() *SavedFilterNotifications`

NewSavedFilterNotificationsWithDefaults instantiates a new SavedFilterNotifications object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *SavedFilterNotifications) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *SavedFilterNotifications) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *SavedFilterNotifications) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.


### GetFrequency

`func (o *SavedFilterNotifications) GetFrequency() string`

GetFrequency returns the Frequency field if non-nil, zero value otherwise.

### GetFrequencyOk

`func (o *SavedFilterNotifications) GetFrequencyOk() (*string, bool)`

GetFrequencyOk returns a tuple with the Frequency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrequency

`func (o *SavedFilterNotifications) SetFrequency(v string)`

SetFrequency sets Frequency field to given value.


### SetFrequencyNil

`func (o *SavedFilterNotifications) SetFrequencyNil(b bool)`

 SetFrequencyNil sets the value for Frequency to be an explicit nil

### UnsetFrequency
`func (o *SavedFilterNotifications) UnsetFrequency()`

UnsetFrequency ensures that no value is present for Frequency, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


