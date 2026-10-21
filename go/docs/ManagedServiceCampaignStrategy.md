# ManagedServiceCampaignStrategy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Goal** | **string** |  | 
**Countries** | **[]string** | ISO 3166-1 alpha-2 codes. | 
**Languages** | **[]string** |  | 
**Topics** | **[]int32** | Topic ids, as GET /vocabulary lists them. | 
**Definition** | **string** |  | 

## Methods

### NewManagedServiceCampaignStrategy

`func NewManagedServiceCampaignStrategy(goal string, countries []string, languages []string, topics []int32, definition string, ) *ManagedServiceCampaignStrategy`

NewManagedServiceCampaignStrategy instantiates a new ManagedServiceCampaignStrategy object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewManagedServiceCampaignStrategyWithDefaults

`func NewManagedServiceCampaignStrategyWithDefaults() *ManagedServiceCampaignStrategy`

NewManagedServiceCampaignStrategyWithDefaults instantiates a new ManagedServiceCampaignStrategy object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGoal

`func (o *ManagedServiceCampaignStrategy) GetGoal() string`

GetGoal returns the Goal field if non-nil, zero value otherwise.

### GetGoalOk

`func (o *ManagedServiceCampaignStrategy) GetGoalOk() (*string, bool)`

GetGoalOk returns a tuple with the Goal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoal

`func (o *ManagedServiceCampaignStrategy) SetGoal(v string)`

SetGoal sets Goal field to given value.


### GetCountries

`func (o *ManagedServiceCampaignStrategy) GetCountries() []string`

GetCountries returns the Countries field if non-nil, zero value otherwise.

### GetCountriesOk

`func (o *ManagedServiceCampaignStrategy) GetCountriesOk() (*[]string, bool)`

GetCountriesOk returns a tuple with the Countries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountries

`func (o *ManagedServiceCampaignStrategy) SetCountries(v []string)`

SetCountries sets Countries field to given value.


### GetLanguages

`func (o *ManagedServiceCampaignStrategy) GetLanguages() []string`

GetLanguages returns the Languages field if non-nil, zero value otherwise.

### GetLanguagesOk

`func (o *ManagedServiceCampaignStrategy) GetLanguagesOk() (*[]string, bool)`

GetLanguagesOk returns a tuple with the Languages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguages

`func (o *ManagedServiceCampaignStrategy) SetLanguages(v []string)`

SetLanguages sets Languages field to given value.


### GetTopics

`func (o *ManagedServiceCampaignStrategy) GetTopics() []int32`

GetTopics returns the Topics field if non-nil, zero value otherwise.

### GetTopicsOk

`func (o *ManagedServiceCampaignStrategy) GetTopicsOk() (*[]int32, bool)`

GetTopicsOk returns a tuple with the Topics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopics

`func (o *ManagedServiceCampaignStrategy) SetTopics(v []int32)`

SetTopics sets Topics field to given value.


### GetDefinition

`func (o *ManagedServiceCampaignStrategy) GetDefinition() string`

GetDefinition returns the Definition field if non-nil, zero value otherwise.

### GetDefinitionOk

`func (o *ManagedServiceCampaignStrategy) GetDefinitionOk() (*string, bool)`

GetDefinitionOk returns a tuple with the Definition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinition

`func (o *ManagedServiceCampaignStrategy) SetDefinition(v string)`

SetDefinition sets Definition field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


