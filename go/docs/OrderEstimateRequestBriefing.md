# OrderEstimateRequestBriefing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Links** | [**[]OrderLinkRequest**](OrderLinkRequest.md) | No more links than the offer allows. | 
**ExtraServices** | Pointer to **[]string** | Extra services the offer has, added to the ones the web selects for your project by default. A project with a sensitive topic always carries &#x60;extra_charge_for_sensitive_topic&#x60; when the media charges it. | [optional] 
**Title** | Pointer to **string** |  | [optional] 
**AdditionalInfo** | Pointer to **string** |  | [optional] 
**LinkingFrom** | **string** | The URL of an existing article on the media&#39;s domain that the link goes into, without &#x60;&lt;&#x60; or &#x60;&gt;&#x60;. | 
**Link** | [**OrderLinkRequest**](OrderLinkRequest.md) |  | 

## Methods

### NewOrderEstimateRequestBriefing

`func NewOrderEstimateRequestBriefing(links []OrderLinkRequest, linkingFrom string, link OrderLinkRequest, ) *OrderEstimateRequestBriefing`

NewOrderEstimateRequestBriefing instantiates a new OrderEstimateRequestBriefing object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderEstimateRequestBriefingWithDefaults

`func NewOrderEstimateRequestBriefingWithDefaults() *OrderEstimateRequestBriefing`

NewOrderEstimateRequestBriefingWithDefaults instantiates a new OrderEstimateRequestBriefing object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLinks

`func (o *OrderEstimateRequestBriefing) GetLinks() []OrderLinkRequest`

GetLinks returns the Links field if non-nil, zero value otherwise.

### GetLinksOk

`func (o *OrderEstimateRequestBriefing) GetLinksOk() (*[]OrderLinkRequest, bool)`

GetLinksOk returns a tuple with the Links field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinks

`func (o *OrderEstimateRequestBriefing) SetLinks(v []OrderLinkRequest)`

SetLinks sets Links field to given value.


### GetExtraServices

`func (o *OrderEstimateRequestBriefing) GetExtraServices() []string`

GetExtraServices returns the ExtraServices field if non-nil, zero value otherwise.

### GetExtraServicesOk

`func (o *OrderEstimateRequestBriefing) GetExtraServicesOk() (*[]string, bool)`

GetExtraServicesOk returns a tuple with the ExtraServices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtraServices

`func (o *OrderEstimateRequestBriefing) SetExtraServices(v []string)`

SetExtraServices sets ExtraServices field to given value.

### HasExtraServices

`func (o *OrderEstimateRequestBriefing) HasExtraServices() bool`

HasExtraServices returns a boolean if a field has been set.

### GetTitle

`func (o *OrderEstimateRequestBriefing) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *OrderEstimateRequestBriefing) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *OrderEstimateRequestBriefing) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *OrderEstimateRequestBriefing) HasTitle() bool`

HasTitle returns a boolean if a field has been set.

### GetAdditionalInfo

`func (o *OrderEstimateRequestBriefing) GetAdditionalInfo() string`

GetAdditionalInfo returns the AdditionalInfo field if non-nil, zero value otherwise.

### GetAdditionalInfoOk

`func (o *OrderEstimateRequestBriefing) GetAdditionalInfoOk() (*string, bool)`

GetAdditionalInfoOk returns a tuple with the AdditionalInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalInfo

`func (o *OrderEstimateRequestBriefing) SetAdditionalInfo(v string)`

SetAdditionalInfo sets AdditionalInfo field to given value.

### HasAdditionalInfo

`func (o *OrderEstimateRequestBriefing) HasAdditionalInfo() bool`

HasAdditionalInfo returns a boolean if a field has been set.

### GetLinkingFrom

`func (o *OrderEstimateRequestBriefing) GetLinkingFrom() string`

GetLinkingFrom returns the LinkingFrom field if non-nil, zero value otherwise.

### GetLinkingFromOk

`func (o *OrderEstimateRequestBriefing) GetLinkingFromOk() (*string, bool)`

GetLinkingFromOk returns a tuple with the LinkingFrom field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkingFrom

`func (o *OrderEstimateRequestBriefing) SetLinkingFrom(v string)`

SetLinkingFrom sets LinkingFrom field to given value.


### GetLink

`func (o *OrderEstimateRequestBriefing) GetLink() OrderLinkRequest`

GetLink returns the Link field if non-nil, zero value otherwise.

### GetLinkOk

`func (o *OrderEstimateRequestBriefing) GetLinkOk() (*OrderLinkRequest, bool)`

GetLinkOk returns a tuple with the Link field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLink

`func (o *OrderEstimateRequestBriefing) SetLink(v OrderLinkRequest)`

SetLink sets Link field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


