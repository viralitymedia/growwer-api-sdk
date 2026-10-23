# ProjectCatalogueMediaAllOfProject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Favourite** | **bool** |  | 
**Discarded** | **bool** |  | 
**Requested** | **bool** |  | 
**Recommended** | **bool** | Growwer recommends the media for the project. | 
**Bought** | **bool** | You have ordered on the media for the project. | 
**New** | **bool** | Growwer matched the media with the project recently. | 
**AiKeywords** | [**[]ProjectCatalogueMediaAllOfProjectAiKeywords**](ProjectCatalogueMediaAllOfProjectAiKeywords.md) | The AI keywords the web lists for the media in this project, one entry per keyword of each stored source, empty when there are none. Keywords an AI answer gave without referencing any domain may be listed for every media of the project, so an entry does not mean that the engine cited the media. Entries keep their order within an engine, and a keyword listed by two engines appears once for each; the order of the engines is not promised. | 

## Methods

### NewProjectCatalogueMediaAllOfProject

`func NewProjectCatalogueMediaAllOfProject(favourite bool, discarded bool, requested bool, recommended bool, bought bool, new bool, aiKeywords []ProjectCatalogueMediaAllOfProjectAiKeywords, ) *ProjectCatalogueMediaAllOfProject`

NewProjectCatalogueMediaAllOfProject instantiates a new ProjectCatalogueMediaAllOfProject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectCatalogueMediaAllOfProjectWithDefaults

`func NewProjectCatalogueMediaAllOfProjectWithDefaults() *ProjectCatalogueMediaAllOfProject`

NewProjectCatalogueMediaAllOfProjectWithDefaults instantiates a new ProjectCatalogueMediaAllOfProject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFavourite

`func (o *ProjectCatalogueMediaAllOfProject) GetFavourite() bool`

GetFavourite returns the Favourite field if non-nil, zero value otherwise.

### GetFavouriteOk

`func (o *ProjectCatalogueMediaAllOfProject) GetFavouriteOk() (*bool, bool)`

GetFavouriteOk returns a tuple with the Favourite field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFavourite

`func (o *ProjectCatalogueMediaAllOfProject) SetFavourite(v bool)`

SetFavourite sets Favourite field to given value.


### GetDiscarded

`func (o *ProjectCatalogueMediaAllOfProject) GetDiscarded() bool`

GetDiscarded returns the Discarded field if non-nil, zero value otherwise.

### GetDiscardedOk

`func (o *ProjectCatalogueMediaAllOfProject) GetDiscardedOk() (*bool, bool)`

GetDiscardedOk returns a tuple with the Discarded field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiscarded

`func (o *ProjectCatalogueMediaAllOfProject) SetDiscarded(v bool)`

SetDiscarded sets Discarded field to given value.


### GetRequested

`func (o *ProjectCatalogueMediaAllOfProject) GetRequested() bool`

GetRequested returns the Requested field if non-nil, zero value otherwise.

### GetRequestedOk

`func (o *ProjectCatalogueMediaAllOfProject) GetRequestedOk() (*bool, bool)`

GetRequestedOk returns a tuple with the Requested field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequested

`func (o *ProjectCatalogueMediaAllOfProject) SetRequested(v bool)`

SetRequested sets Requested field to given value.


### GetRecommended

`func (o *ProjectCatalogueMediaAllOfProject) GetRecommended() bool`

GetRecommended returns the Recommended field if non-nil, zero value otherwise.

### GetRecommendedOk

`func (o *ProjectCatalogueMediaAllOfProject) GetRecommendedOk() (*bool, bool)`

GetRecommendedOk returns a tuple with the Recommended field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecommended

`func (o *ProjectCatalogueMediaAllOfProject) SetRecommended(v bool)`

SetRecommended sets Recommended field to given value.


### GetBought

`func (o *ProjectCatalogueMediaAllOfProject) GetBought() bool`

GetBought returns the Bought field if non-nil, zero value otherwise.

### GetBoughtOk

`func (o *ProjectCatalogueMediaAllOfProject) GetBoughtOk() (*bool, bool)`

GetBoughtOk returns a tuple with the Bought field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBought

`func (o *ProjectCatalogueMediaAllOfProject) SetBought(v bool)`

SetBought sets Bought field to given value.


### GetNew

`func (o *ProjectCatalogueMediaAllOfProject) GetNew() bool`

GetNew returns the New field if non-nil, zero value otherwise.

### GetNewOk

`func (o *ProjectCatalogueMediaAllOfProject) GetNewOk() (*bool, bool)`

GetNewOk returns a tuple with the New field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNew

`func (o *ProjectCatalogueMediaAllOfProject) SetNew(v bool)`

SetNew sets New field to given value.


### GetAiKeywords

`func (o *ProjectCatalogueMediaAllOfProject) GetAiKeywords() []ProjectCatalogueMediaAllOfProjectAiKeywords`

GetAiKeywords returns the AiKeywords field if non-nil, zero value otherwise.

### GetAiKeywordsOk

`func (o *ProjectCatalogueMediaAllOfProject) GetAiKeywordsOk() (*[]ProjectCatalogueMediaAllOfProjectAiKeywords, bool)`

GetAiKeywordsOk returns a tuple with the AiKeywords field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAiKeywords

`func (o *ProjectCatalogueMediaAllOfProject) SetAiKeywords(v []ProjectCatalogueMediaAllOfProjectAiKeywords)`

SetAiKeywords sets AiKeywords field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


