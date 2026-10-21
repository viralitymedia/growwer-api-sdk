# SellerOrderBriefing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Title** | **NullableString** |  | 
**Language** | **string** | The language code of the article. | 
**Links** | [**[]OrderLink**](OrderLink.md) |  | 
**ExtraServices** | **[]string** |  | 
**AdditionalInfo** | **NullableString** |  | 
**WrittenBy** | **string** | Who writes the article; &#x60;seller&#x60; means you do. | 
**HasProposedDraft** | **bool** | Whether the buyer attached a draft; GET /seller/orders/{id}/briefing downloads it. | 
**LinkingFrom** | **string** | The existing article of the media the link goes into. | 
**Link** | [**OrderLink**](OrderLink.md) |  | 

## Methods

### NewSellerOrderBriefing

`func NewSellerOrderBriefing(title NullableString, language string, links []OrderLink, extraServices []string, additionalInfo NullableString, writtenBy string, hasProposedDraft bool, linkingFrom string, link OrderLink, ) *SellerOrderBriefing`

NewSellerOrderBriefing instantiates a new SellerOrderBriefing object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerOrderBriefingWithDefaults

`func NewSellerOrderBriefingWithDefaults() *SellerOrderBriefing`

NewSellerOrderBriefingWithDefaults instantiates a new SellerOrderBriefing object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTitle

`func (o *SellerOrderBriefing) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *SellerOrderBriefing) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *SellerOrderBriefing) SetTitle(v string)`

SetTitle sets Title field to given value.


### SetTitleNil

`func (o *SellerOrderBriefing) SetTitleNil(b bool)`

 SetTitleNil sets the value for Title to be an explicit nil

### UnsetTitle
`func (o *SellerOrderBriefing) UnsetTitle()`

UnsetTitle ensures that no value is present for Title, not even an explicit nil
### GetLanguage

`func (o *SellerOrderBriefing) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *SellerOrderBriefing) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *SellerOrderBriefing) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetLinks

`func (o *SellerOrderBriefing) GetLinks() []OrderLink`

GetLinks returns the Links field if non-nil, zero value otherwise.

### GetLinksOk

`func (o *SellerOrderBriefing) GetLinksOk() (*[]OrderLink, bool)`

GetLinksOk returns a tuple with the Links field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinks

`func (o *SellerOrderBriefing) SetLinks(v []OrderLink)`

SetLinks sets Links field to given value.


### GetExtraServices

`func (o *SellerOrderBriefing) GetExtraServices() []string`

GetExtraServices returns the ExtraServices field if non-nil, zero value otherwise.

### GetExtraServicesOk

`func (o *SellerOrderBriefing) GetExtraServicesOk() (*[]string, bool)`

GetExtraServicesOk returns a tuple with the ExtraServices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtraServices

`func (o *SellerOrderBriefing) SetExtraServices(v []string)`

SetExtraServices sets ExtraServices field to given value.


### GetAdditionalInfo

`func (o *SellerOrderBriefing) GetAdditionalInfo() string`

GetAdditionalInfo returns the AdditionalInfo field if non-nil, zero value otherwise.

### GetAdditionalInfoOk

`func (o *SellerOrderBriefing) GetAdditionalInfoOk() (*string, bool)`

GetAdditionalInfoOk returns a tuple with the AdditionalInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalInfo

`func (o *SellerOrderBriefing) SetAdditionalInfo(v string)`

SetAdditionalInfo sets AdditionalInfo field to given value.


### SetAdditionalInfoNil

`func (o *SellerOrderBriefing) SetAdditionalInfoNil(b bool)`

 SetAdditionalInfoNil sets the value for AdditionalInfo to be an explicit nil

### UnsetAdditionalInfo
`func (o *SellerOrderBriefing) UnsetAdditionalInfo()`

UnsetAdditionalInfo ensures that no value is present for AdditionalInfo, not even an explicit nil
### GetWrittenBy

`func (o *SellerOrderBriefing) GetWrittenBy() string`

GetWrittenBy returns the WrittenBy field if non-nil, zero value otherwise.

### GetWrittenByOk

`func (o *SellerOrderBriefing) GetWrittenByOk() (*string, bool)`

GetWrittenByOk returns a tuple with the WrittenBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWrittenBy

`func (o *SellerOrderBriefing) SetWrittenBy(v string)`

SetWrittenBy sets WrittenBy field to given value.


### GetHasProposedDraft

`func (o *SellerOrderBriefing) GetHasProposedDraft() bool`

GetHasProposedDraft returns the HasProposedDraft field if non-nil, zero value otherwise.

### GetHasProposedDraftOk

`func (o *SellerOrderBriefing) GetHasProposedDraftOk() (*bool, bool)`

GetHasProposedDraftOk returns a tuple with the HasProposedDraft field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasProposedDraft

`func (o *SellerOrderBriefing) SetHasProposedDraft(v bool)`

SetHasProposedDraft sets HasProposedDraft field to given value.


### GetLinkingFrom

`func (o *SellerOrderBriefing) GetLinkingFrom() string`

GetLinkingFrom returns the LinkingFrom field if non-nil, zero value otherwise.

### GetLinkingFromOk

`func (o *SellerOrderBriefing) GetLinkingFromOk() (*string, bool)`

GetLinkingFromOk returns a tuple with the LinkingFrom field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkingFrom

`func (o *SellerOrderBriefing) SetLinkingFrom(v string)`

SetLinkingFrom sets LinkingFrom field to given value.


### GetLink

`func (o *SellerOrderBriefing) GetLink() OrderLink`

GetLink returns the Link field if non-nil, zero value otherwise.

### GetLinkOk

`func (o *SellerOrderBriefing) GetLinkOk() (*OrderLink, bool)`

GetLinkOk returns a tuple with the Link field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLink

`func (o *SellerOrderBriefing) SetLink(v OrderLink)`

SetLink sets Link field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


