# SellerPostOrderBriefing

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

## Methods

### NewSellerPostOrderBriefing

`func NewSellerPostOrderBriefing(title NullableString, language string, links []OrderLink, extraServices []string, additionalInfo NullableString, writtenBy string, hasProposedDraft bool, ) *SellerPostOrderBriefing`

NewSellerPostOrderBriefing instantiates a new SellerPostOrderBriefing object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerPostOrderBriefingWithDefaults

`func NewSellerPostOrderBriefingWithDefaults() *SellerPostOrderBriefing`

NewSellerPostOrderBriefingWithDefaults instantiates a new SellerPostOrderBriefing object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTitle

`func (o *SellerPostOrderBriefing) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *SellerPostOrderBriefing) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *SellerPostOrderBriefing) SetTitle(v string)`

SetTitle sets Title field to given value.


### SetTitleNil

`func (o *SellerPostOrderBriefing) SetTitleNil(b bool)`

 SetTitleNil sets the value for Title to be an explicit nil

### UnsetTitle
`func (o *SellerPostOrderBriefing) UnsetTitle()`

UnsetTitle ensures that no value is present for Title, not even an explicit nil
### GetLanguage

`func (o *SellerPostOrderBriefing) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *SellerPostOrderBriefing) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *SellerPostOrderBriefing) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetLinks

`func (o *SellerPostOrderBriefing) GetLinks() []OrderLink`

GetLinks returns the Links field if non-nil, zero value otherwise.

### GetLinksOk

`func (o *SellerPostOrderBriefing) GetLinksOk() (*[]OrderLink, bool)`

GetLinksOk returns a tuple with the Links field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinks

`func (o *SellerPostOrderBriefing) SetLinks(v []OrderLink)`

SetLinks sets Links field to given value.


### GetExtraServices

`func (o *SellerPostOrderBriefing) GetExtraServices() []string`

GetExtraServices returns the ExtraServices field if non-nil, zero value otherwise.

### GetExtraServicesOk

`func (o *SellerPostOrderBriefing) GetExtraServicesOk() (*[]string, bool)`

GetExtraServicesOk returns a tuple with the ExtraServices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtraServices

`func (o *SellerPostOrderBriefing) SetExtraServices(v []string)`

SetExtraServices sets ExtraServices field to given value.


### GetAdditionalInfo

`func (o *SellerPostOrderBriefing) GetAdditionalInfo() string`

GetAdditionalInfo returns the AdditionalInfo field if non-nil, zero value otherwise.

### GetAdditionalInfoOk

`func (o *SellerPostOrderBriefing) GetAdditionalInfoOk() (*string, bool)`

GetAdditionalInfoOk returns a tuple with the AdditionalInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalInfo

`func (o *SellerPostOrderBriefing) SetAdditionalInfo(v string)`

SetAdditionalInfo sets AdditionalInfo field to given value.


### SetAdditionalInfoNil

`func (o *SellerPostOrderBriefing) SetAdditionalInfoNil(b bool)`

 SetAdditionalInfoNil sets the value for AdditionalInfo to be an explicit nil

### UnsetAdditionalInfo
`func (o *SellerPostOrderBriefing) UnsetAdditionalInfo()`

UnsetAdditionalInfo ensures that no value is present for AdditionalInfo, not even an explicit nil
### GetWrittenBy

`func (o *SellerPostOrderBriefing) GetWrittenBy() string`

GetWrittenBy returns the WrittenBy field if non-nil, zero value otherwise.

### GetWrittenByOk

`func (o *SellerPostOrderBriefing) GetWrittenByOk() (*string, bool)`

GetWrittenByOk returns a tuple with the WrittenBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWrittenBy

`func (o *SellerPostOrderBriefing) SetWrittenBy(v string)`

SetWrittenBy sets WrittenBy field to given value.


### GetHasProposedDraft

`func (o *SellerPostOrderBriefing) GetHasProposedDraft() bool`

GetHasProposedDraft returns the HasProposedDraft field if non-nil, zero value otherwise.

### GetHasProposedDraftOk

`func (o *SellerPostOrderBriefing) GetHasProposedDraftOk() (*bool, bool)`

GetHasProposedDraftOk returns a tuple with the HasProposedDraft field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasProposedDraft

`func (o *SellerPostOrderBriefing) SetHasProposedDraft(v bool)`

SetHasProposedDraft sets HasProposedDraft field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


