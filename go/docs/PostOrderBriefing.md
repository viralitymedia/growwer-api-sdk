# PostOrderBriefing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Title** | **NullableString** |  | 
**Language** | **string** | The language code of the article. | 
**Links** | [**[]OrderLink**](OrderLink.md) |  | 
**ExtraServices** | **[]string** |  | 
**AdditionalInfo** | **NullableString** |  | 
**HasProposedDraft** | **bool** | Whether you attached your own draft; GET /orders/{id}/briefing downloads it. | 

## Methods

### NewPostOrderBriefing

`func NewPostOrderBriefing(title NullableString, language string, links []OrderLink, extraServices []string, additionalInfo NullableString, hasProposedDraft bool, ) *PostOrderBriefing`

NewPostOrderBriefing instantiates a new PostOrderBriefing object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPostOrderBriefingWithDefaults

`func NewPostOrderBriefingWithDefaults() *PostOrderBriefing`

NewPostOrderBriefingWithDefaults instantiates a new PostOrderBriefing object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTitle

`func (o *PostOrderBriefing) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *PostOrderBriefing) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *PostOrderBriefing) SetTitle(v string)`

SetTitle sets Title field to given value.


### SetTitleNil

`func (o *PostOrderBriefing) SetTitleNil(b bool)`

 SetTitleNil sets the value for Title to be an explicit nil

### UnsetTitle
`func (o *PostOrderBriefing) UnsetTitle()`

UnsetTitle ensures that no value is present for Title, not even an explicit nil
### GetLanguage

`func (o *PostOrderBriefing) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *PostOrderBriefing) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *PostOrderBriefing) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetLinks

`func (o *PostOrderBriefing) GetLinks() []OrderLink`

GetLinks returns the Links field if non-nil, zero value otherwise.

### GetLinksOk

`func (o *PostOrderBriefing) GetLinksOk() (*[]OrderLink, bool)`

GetLinksOk returns a tuple with the Links field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinks

`func (o *PostOrderBriefing) SetLinks(v []OrderLink)`

SetLinks sets Links field to given value.


### GetExtraServices

`func (o *PostOrderBriefing) GetExtraServices() []string`

GetExtraServices returns the ExtraServices field if non-nil, zero value otherwise.

### GetExtraServicesOk

`func (o *PostOrderBriefing) GetExtraServicesOk() (*[]string, bool)`

GetExtraServicesOk returns a tuple with the ExtraServices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtraServices

`func (o *PostOrderBriefing) SetExtraServices(v []string)`

SetExtraServices sets ExtraServices field to given value.


### GetAdditionalInfo

`func (o *PostOrderBriefing) GetAdditionalInfo() string`

GetAdditionalInfo returns the AdditionalInfo field if non-nil, zero value otherwise.

### GetAdditionalInfoOk

`func (o *PostOrderBriefing) GetAdditionalInfoOk() (*string, bool)`

GetAdditionalInfoOk returns a tuple with the AdditionalInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalInfo

`func (o *PostOrderBriefing) SetAdditionalInfo(v string)`

SetAdditionalInfo sets AdditionalInfo field to given value.


### SetAdditionalInfoNil

`func (o *PostOrderBriefing) SetAdditionalInfoNil(b bool)`

 SetAdditionalInfoNil sets the value for AdditionalInfo to be an explicit nil

### UnsetAdditionalInfo
`func (o *PostOrderBriefing) UnsetAdditionalInfo()`

UnsetAdditionalInfo ensures that no value is present for AdditionalInfo, not even an explicit nil
### GetHasProposedDraft

`func (o *PostOrderBriefing) GetHasProposedDraft() bool`

GetHasProposedDraft returns the HasProposedDraft field if non-nil, zero value otherwise.

### GetHasProposedDraftOk

`func (o *PostOrderBriefing) GetHasProposedDraftOk() (*bool, bool)`

GetHasProposedDraftOk returns a tuple with the HasProposedDraft field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasProposedDraft

`func (o *PostOrderBriefing) SetHasProposedDraft(v bool)`

SetHasProposedDraft sets HasProposedDraft field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


