# ManagedServiceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectUrl** | **string** | The website the campaign is for. | 
**Goal** | **string** |  | 
**Country** | **string** | ISO 3166-1 alpha-2 code of the target country. | 
**Duration** | **string** |  | 
**EstimatedBudget** | [**Money**](Money.md) | At least 500 EUR. Only EUR is accepted. | 
**AdditionalInfo** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewManagedServiceRequest

`func NewManagedServiceRequest(projectUrl string, goal string, country string, duration string, estimatedBudget Money, ) *ManagedServiceRequest`

NewManagedServiceRequest instantiates a new ManagedServiceRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewManagedServiceRequestWithDefaults

`func NewManagedServiceRequestWithDefaults() *ManagedServiceRequest`

NewManagedServiceRequestWithDefaults instantiates a new ManagedServiceRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProjectUrl

`func (o *ManagedServiceRequest) GetProjectUrl() string`

GetProjectUrl returns the ProjectUrl field if non-nil, zero value otherwise.

### GetProjectUrlOk

`func (o *ManagedServiceRequest) GetProjectUrlOk() (*string, bool)`

GetProjectUrlOk returns a tuple with the ProjectUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectUrl

`func (o *ManagedServiceRequest) SetProjectUrl(v string)`

SetProjectUrl sets ProjectUrl field to given value.


### GetGoal

`func (o *ManagedServiceRequest) GetGoal() string`

GetGoal returns the Goal field if non-nil, zero value otherwise.

### GetGoalOk

`func (o *ManagedServiceRequest) GetGoalOk() (*string, bool)`

GetGoalOk returns a tuple with the Goal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoal

`func (o *ManagedServiceRequest) SetGoal(v string)`

SetGoal sets Goal field to given value.


### GetCountry

`func (o *ManagedServiceRequest) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *ManagedServiceRequest) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *ManagedServiceRequest) SetCountry(v string)`

SetCountry sets Country field to given value.


### GetDuration

`func (o *ManagedServiceRequest) GetDuration() string`

GetDuration returns the Duration field if non-nil, zero value otherwise.

### GetDurationOk

`func (o *ManagedServiceRequest) GetDurationOk() (*string, bool)`

GetDurationOk returns a tuple with the Duration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDuration

`func (o *ManagedServiceRequest) SetDuration(v string)`

SetDuration sets Duration field to given value.


### GetEstimatedBudget

`func (o *ManagedServiceRequest) GetEstimatedBudget() Money`

GetEstimatedBudget returns the EstimatedBudget field if non-nil, zero value otherwise.

### GetEstimatedBudgetOk

`func (o *ManagedServiceRequest) GetEstimatedBudgetOk() (*Money, bool)`

GetEstimatedBudgetOk returns a tuple with the EstimatedBudget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEstimatedBudget

`func (o *ManagedServiceRequest) SetEstimatedBudget(v Money)`

SetEstimatedBudget sets EstimatedBudget field to given value.


### GetAdditionalInfo

`func (o *ManagedServiceRequest) GetAdditionalInfo() string`

GetAdditionalInfo returns the AdditionalInfo field if non-nil, zero value otherwise.

### GetAdditionalInfoOk

`func (o *ManagedServiceRequest) GetAdditionalInfoOk() (*string, bool)`

GetAdditionalInfoOk returns a tuple with the AdditionalInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalInfo

`func (o *ManagedServiceRequest) SetAdditionalInfo(v string)`

SetAdditionalInfo sets AdditionalInfo field to given value.

### HasAdditionalInfo

`func (o *ManagedServiceRequest) HasAdditionalInfo() bool`

HasAdditionalInfo returns a boolean if a field has been set.

### SetAdditionalInfoNil

`func (o *ManagedServiceRequest) SetAdditionalInfoNil(b bool)`

 SetAdditionalInfoNil sets the value for AdditionalInfo to be an explicit nil

### UnsetAdditionalInfo
`func (o *ManagedServiceRequest) UnsetAdditionalInfo()`

UnsetAdditionalInfo ensures that no value is present for AdditionalInfo, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


