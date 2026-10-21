# PostOrderBriefingRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Links** | [**[]OrderLinkRequest**](OrderLinkRequest.md) | No more links than the offer allows. | 
**ExtraServices** | Pointer to **[]string** | Extra services the offer has, added to the ones the web selects for your project by default. A project with a sensitive topic always carries &#x60;extra_charge_for_sensitive_topic&#x60; when the media charges it. | [optional] 
**Title** | Pointer to **string** |  | [optional] 
**AdditionalInfo** | Pointer to **string** |  | [optional] 

## Methods

### NewPostOrderBriefingRequest

`func NewPostOrderBriefingRequest(links []OrderLinkRequest, ) *PostOrderBriefingRequest`

NewPostOrderBriefingRequest instantiates a new PostOrderBriefingRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPostOrderBriefingRequestWithDefaults

`func NewPostOrderBriefingRequestWithDefaults() *PostOrderBriefingRequest`

NewPostOrderBriefingRequestWithDefaults instantiates a new PostOrderBriefingRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLinks

`func (o *PostOrderBriefingRequest) GetLinks() []OrderLinkRequest`

GetLinks returns the Links field if non-nil, zero value otherwise.

### GetLinksOk

`func (o *PostOrderBriefingRequest) GetLinksOk() (*[]OrderLinkRequest, bool)`

GetLinksOk returns a tuple with the Links field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinks

`func (o *PostOrderBriefingRequest) SetLinks(v []OrderLinkRequest)`

SetLinks sets Links field to given value.


### GetExtraServices

`func (o *PostOrderBriefingRequest) GetExtraServices() []string`

GetExtraServices returns the ExtraServices field if non-nil, zero value otherwise.

### GetExtraServicesOk

`func (o *PostOrderBriefingRequest) GetExtraServicesOk() (*[]string, bool)`

GetExtraServicesOk returns a tuple with the ExtraServices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtraServices

`func (o *PostOrderBriefingRequest) SetExtraServices(v []string)`

SetExtraServices sets ExtraServices field to given value.

### HasExtraServices

`func (o *PostOrderBriefingRequest) HasExtraServices() bool`

HasExtraServices returns a boolean if a field has been set.

### GetTitle

`func (o *PostOrderBriefingRequest) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *PostOrderBriefingRequest) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *PostOrderBriefingRequest) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *PostOrderBriefingRequest) HasTitle() bool`

HasTitle returns a boolean if a field has been set.

### GetAdditionalInfo

`func (o *PostOrderBriefingRequest) GetAdditionalInfo() string`

GetAdditionalInfo returns the AdditionalInfo field if non-nil, zero value otherwise.

### GetAdditionalInfoOk

`func (o *PostOrderBriefingRequest) GetAdditionalInfoOk() (*string, bool)`

GetAdditionalInfoOk returns a tuple with the AdditionalInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalInfo

`func (o *PostOrderBriefingRequest) SetAdditionalInfo(v string)`

SetAdditionalInfo sets AdditionalInfo field to given value.

### HasAdditionalInfo

`func (o *PostOrderBriefingRequest) HasAdditionalInfo() bool`

HasAdditionalInfo returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


