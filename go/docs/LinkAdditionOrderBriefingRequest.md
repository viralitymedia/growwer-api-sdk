# LinkAdditionOrderBriefingRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LinkingFrom** | **string** | The URL of an existing article on the media&#39;s domain that the link goes into. | 
**Link** | [**OrderLinkRequest**](OrderLinkRequest.md) |  | 
**AdditionalInfo** | Pointer to **string** |  | [optional] 

## Methods

### NewLinkAdditionOrderBriefingRequest

`func NewLinkAdditionOrderBriefingRequest(linkingFrom string, link OrderLinkRequest, ) *LinkAdditionOrderBriefingRequest`

NewLinkAdditionOrderBriefingRequest instantiates a new LinkAdditionOrderBriefingRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLinkAdditionOrderBriefingRequestWithDefaults

`func NewLinkAdditionOrderBriefingRequestWithDefaults() *LinkAdditionOrderBriefingRequest`

NewLinkAdditionOrderBriefingRequestWithDefaults instantiates a new LinkAdditionOrderBriefingRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLinkingFrom

`func (o *LinkAdditionOrderBriefingRequest) GetLinkingFrom() string`

GetLinkingFrom returns the LinkingFrom field if non-nil, zero value otherwise.

### GetLinkingFromOk

`func (o *LinkAdditionOrderBriefingRequest) GetLinkingFromOk() (*string, bool)`

GetLinkingFromOk returns a tuple with the LinkingFrom field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkingFrom

`func (o *LinkAdditionOrderBriefingRequest) SetLinkingFrom(v string)`

SetLinkingFrom sets LinkingFrom field to given value.


### GetLink

`func (o *LinkAdditionOrderBriefingRequest) GetLink() OrderLinkRequest`

GetLink returns the Link field if non-nil, zero value otherwise.

### GetLinkOk

`func (o *LinkAdditionOrderBriefingRequest) GetLinkOk() (*OrderLinkRequest, bool)`

GetLinkOk returns a tuple with the Link field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLink

`func (o *LinkAdditionOrderBriefingRequest) SetLink(v OrderLinkRequest)`

SetLink sets Link field to given value.


### GetAdditionalInfo

`func (o *LinkAdditionOrderBriefingRequest) GetAdditionalInfo() string`

GetAdditionalInfo returns the AdditionalInfo field if non-nil, zero value otherwise.

### GetAdditionalInfoOk

`func (o *LinkAdditionOrderBriefingRequest) GetAdditionalInfoOk() (*string, bool)`

GetAdditionalInfoOk returns a tuple with the AdditionalInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalInfo

`func (o *LinkAdditionOrderBriefingRequest) SetAdditionalInfo(v string)`

SetAdditionalInfo sets AdditionalInfo field to given value.

### HasAdditionalInfo

`func (o *LinkAdditionOrderBriefingRequest) HasAdditionalInfo() bool`

HasAdditionalInfo returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


