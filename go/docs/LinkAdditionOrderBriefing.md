# LinkAdditionOrderBriefing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LinkingFrom** | **string** | The existing article of the media the link goes into. | 
**Link** | [**OrderLink**](OrderLink.md) |  | 
**AdditionalInfo** | **NullableString** |  | 

## Methods

### NewLinkAdditionOrderBriefing

`func NewLinkAdditionOrderBriefing(linkingFrom string, link OrderLink, additionalInfo NullableString, ) *LinkAdditionOrderBriefing`

NewLinkAdditionOrderBriefing instantiates a new LinkAdditionOrderBriefing object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLinkAdditionOrderBriefingWithDefaults

`func NewLinkAdditionOrderBriefingWithDefaults() *LinkAdditionOrderBriefing`

NewLinkAdditionOrderBriefingWithDefaults instantiates a new LinkAdditionOrderBriefing object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLinkingFrom

`func (o *LinkAdditionOrderBriefing) GetLinkingFrom() string`

GetLinkingFrom returns the LinkingFrom field if non-nil, zero value otherwise.

### GetLinkingFromOk

`func (o *LinkAdditionOrderBriefing) GetLinkingFromOk() (*string, bool)`

GetLinkingFromOk returns a tuple with the LinkingFrom field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkingFrom

`func (o *LinkAdditionOrderBriefing) SetLinkingFrom(v string)`

SetLinkingFrom sets LinkingFrom field to given value.


### GetLink

`func (o *LinkAdditionOrderBriefing) GetLink() OrderLink`

GetLink returns the Link field if non-nil, zero value otherwise.

### GetLinkOk

`func (o *LinkAdditionOrderBriefing) GetLinkOk() (*OrderLink, bool)`

GetLinkOk returns a tuple with the Link field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLink

`func (o *LinkAdditionOrderBriefing) SetLink(v OrderLink)`

SetLink sets Link field to given value.


### GetAdditionalInfo

`func (o *LinkAdditionOrderBriefing) GetAdditionalInfo() string`

GetAdditionalInfo returns the AdditionalInfo field if non-nil, zero value otherwise.

### GetAdditionalInfoOk

`func (o *LinkAdditionOrderBriefing) GetAdditionalInfoOk() (*string, bool)`

GetAdditionalInfoOk returns a tuple with the AdditionalInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalInfo

`func (o *LinkAdditionOrderBriefing) SetAdditionalInfo(v string)`

SetAdditionalInfo sets AdditionalInfo field to given value.


### SetAdditionalInfoNil

`func (o *LinkAdditionOrderBriefing) SetAdditionalInfoNil(b bool)`

 SetAdditionalInfoNil sets the value for AdditionalInfo to be an explicit nil

### UnsetAdditionalInfo
`func (o *LinkAdditionOrderBriefing) UnsetAdditionalInfo()`

UnsetAdditionalInfo ensures that no value is present for AdditionalInfo, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


