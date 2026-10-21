# OrderBriefing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Title** | **NullableString** |  | 
**Language** | **string** | The language code of the article. | 
**Links** | [**[]OrderLink**](OrderLink.md) |  | 
**ExtraServices** | **[]string** |  | 
**AdditionalInfo** | **NullableString** |  | 
**HasProposedDraft** | **bool** | Whether you attached your own draft; GET /orders/{id}/briefing downloads it. | 
**LinkingFrom** | **string** | The existing article of the media the link goes into. | 
**Link** | [**OrderLink**](OrderLink.md) |  | 

## Methods

### NewOrderBriefing

`func NewOrderBriefing(title NullableString, language string, links []OrderLink, extraServices []string, additionalInfo NullableString, hasProposedDraft bool, linkingFrom string, link OrderLink, ) *OrderBriefing`

NewOrderBriefing instantiates a new OrderBriefing object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderBriefingWithDefaults

`func NewOrderBriefingWithDefaults() *OrderBriefing`

NewOrderBriefingWithDefaults instantiates a new OrderBriefing object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTitle

`func (o *OrderBriefing) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *OrderBriefing) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *OrderBriefing) SetTitle(v string)`

SetTitle sets Title field to given value.


### SetTitleNil

`func (o *OrderBriefing) SetTitleNil(b bool)`

 SetTitleNil sets the value for Title to be an explicit nil

### UnsetTitle
`func (o *OrderBriefing) UnsetTitle()`

UnsetTitle ensures that no value is present for Title, not even an explicit nil
### GetLanguage

`func (o *OrderBriefing) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *OrderBriefing) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *OrderBriefing) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetLinks

`func (o *OrderBriefing) GetLinks() []OrderLink`

GetLinks returns the Links field if non-nil, zero value otherwise.

### GetLinksOk

`func (o *OrderBriefing) GetLinksOk() (*[]OrderLink, bool)`

GetLinksOk returns a tuple with the Links field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinks

`func (o *OrderBriefing) SetLinks(v []OrderLink)`

SetLinks sets Links field to given value.


### GetExtraServices

`func (o *OrderBriefing) GetExtraServices() []string`

GetExtraServices returns the ExtraServices field if non-nil, zero value otherwise.

### GetExtraServicesOk

`func (o *OrderBriefing) GetExtraServicesOk() (*[]string, bool)`

GetExtraServicesOk returns a tuple with the ExtraServices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtraServices

`func (o *OrderBriefing) SetExtraServices(v []string)`

SetExtraServices sets ExtraServices field to given value.


### GetAdditionalInfo

`func (o *OrderBriefing) GetAdditionalInfo() string`

GetAdditionalInfo returns the AdditionalInfo field if non-nil, zero value otherwise.

### GetAdditionalInfoOk

`func (o *OrderBriefing) GetAdditionalInfoOk() (*string, bool)`

GetAdditionalInfoOk returns a tuple with the AdditionalInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalInfo

`func (o *OrderBriefing) SetAdditionalInfo(v string)`

SetAdditionalInfo sets AdditionalInfo field to given value.


### SetAdditionalInfoNil

`func (o *OrderBriefing) SetAdditionalInfoNil(b bool)`

 SetAdditionalInfoNil sets the value for AdditionalInfo to be an explicit nil

### UnsetAdditionalInfo
`func (o *OrderBriefing) UnsetAdditionalInfo()`

UnsetAdditionalInfo ensures that no value is present for AdditionalInfo, not even an explicit nil
### GetHasProposedDraft

`func (o *OrderBriefing) GetHasProposedDraft() bool`

GetHasProposedDraft returns the HasProposedDraft field if non-nil, zero value otherwise.

### GetHasProposedDraftOk

`func (o *OrderBriefing) GetHasProposedDraftOk() (*bool, bool)`

GetHasProposedDraftOk returns a tuple with the HasProposedDraft field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasProposedDraft

`func (o *OrderBriefing) SetHasProposedDraft(v bool)`

SetHasProposedDraft sets HasProposedDraft field to given value.


### GetLinkingFrom

`func (o *OrderBriefing) GetLinkingFrom() string`

GetLinkingFrom returns the LinkingFrom field if non-nil, zero value otherwise.

### GetLinkingFromOk

`func (o *OrderBriefing) GetLinkingFromOk() (*string, bool)`

GetLinkingFromOk returns a tuple with the LinkingFrom field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkingFrom

`func (o *OrderBriefing) SetLinkingFrom(v string)`

SetLinkingFrom sets LinkingFrom field to given value.


### GetLink

`func (o *OrderBriefing) GetLink() OrderLink`

GetLink returns the Link field if non-nil, zero value otherwise.

### GetLinkOk

`func (o *OrderBriefing) GetLinkOk() (*OrderLink, bool)`

GetLinkOk returns a tuple with the Link field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLink

`func (o *OrderBriefing) SetLink(v OrderLink)`

SetLink sets Link field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


