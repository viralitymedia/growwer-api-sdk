# OrderEstimateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | 
**ProjectId** | **string** | One of your projects. | 
**MediaId** | **string** | A media you can order for the project (GET /projects/{id}/medias). | 
**Briefing** | [**OrderEstimateRequestBriefing**](OrderEstimateRequestBriefing.md) |  | 
**ScheduledPublicationDate** | Pointer to **string** | The day to publish on, at least a few days ahead as the web requires. | [optional] 
**DraftReviewable** | Pointer to **bool** | Whether you review the draft before it is published. Defaults to false. | [optional] 
**ProposedDraftFileId** | Pointer to **string** | A file uploaded with POST /files to propose your own draft. The estimate checks it without using it up. | [optional] 

## Methods

### NewOrderEstimateRequest

`func NewOrderEstimateRequest(type_ string, projectId string, mediaId string, briefing OrderEstimateRequestBriefing, ) *OrderEstimateRequest`

NewOrderEstimateRequest instantiates a new OrderEstimateRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderEstimateRequestWithDefaults

`func NewOrderEstimateRequestWithDefaults() *OrderEstimateRequest`

NewOrderEstimateRequestWithDefaults instantiates a new OrderEstimateRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *OrderEstimateRequest) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *OrderEstimateRequest) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *OrderEstimateRequest) SetType(v string)`

SetType sets Type field to given value.


### GetProjectId

`func (o *OrderEstimateRequest) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *OrderEstimateRequest) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *OrderEstimateRequest) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.


### GetMediaId

`func (o *OrderEstimateRequest) GetMediaId() string`

GetMediaId returns the MediaId field if non-nil, zero value otherwise.

### GetMediaIdOk

`func (o *OrderEstimateRequest) GetMediaIdOk() (*string, bool)`

GetMediaIdOk returns a tuple with the MediaId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMediaId

`func (o *OrderEstimateRequest) SetMediaId(v string)`

SetMediaId sets MediaId field to given value.


### GetBriefing

`func (o *OrderEstimateRequest) GetBriefing() OrderEstimateRequestBriefing`

GetBriefing returns the Briefing field if non-nil, zero value otherwise.

### GetBriefingOk

`func (o *OrderEstimateRequest) GetBriefingOk() (*OrderEstimateRequestBriefing, bool)`

GetBriefingOk returns a tuple with the Briefing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBriefing

`func (o *OrderEstimateRequest) SetBriefing(v OrderEstimateRequestBriefing)`

SetBriefing sets Briefing field to given value.


### GetScheduledPublicationDate

`func (o *OrderEstimateRequest) GetScheduledPublicationDate() string`

GetScheduledPublicationDate returns the ScheduledPublicationDate field if non-nil, zero value otherwise.

### GetScheduledPublicationDateOk

`func (o *OrderEstimateRequest) GetScheduledPublicationDateOk() (*string, bool)`

GetScheduledPublicationDateOk returns a tuple with the ScheduledPublicationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledPublicationDate

`func (o *OrderEstimateRequest) SetScheduledPublicationDate(v string)`

SetScheduledPublicationDate sets ScheduledPublicationDate field to given value.

### HasScheduledPublicationDate

`func (o *OrderEstimateRequest) HasScheduledPublicationDate() bool`

HasScheduledPublicationDate returns a boolean if a field has been set.

### GetDraftReviewable

`func (o *OrderEstimateRequest) GetDraftReviewable() bool`

GetDraftReviewable returns the DraftReviewable field if non-nil, zero value otherwise.

### GetDraftReviewableOk

`func (o *OrderEstimateRequest) GetDraftReviewableOk() (*bool, bool)`

GetDraftReviewableOk returns a tuple with the DraftReviewable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDraftReviewable

`func (o *OrderEstimateRequest) SetDraftReviewable(v bool)`

SetDraftReviewable sets DraftReviewable field to given value.

### HasDraftReviewable

`func (o *OrderEstimateRequest) HasDraftReviewable() bool`

HasDraftReviewable returns a boolean if a field has been set.

### GetProposedDraftFileId

`func (o *OrderEstimateRequest) GetProposedDraftFileId() string`

GetProposedDraftFileId returns the ProposedDraftFileId field if non-nil, zero value otherwise.

### GetProposedDraftFileIdOk

`func (o *OrderEstimateRequest) GetProposedDraftFileIdOk() (*string, bool)`

GetProposedDraftFileIdOk returns a tuple with the ProposedDraftFileId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProposedDraftFileId

`func (o *OrderEstimateRequest) SetProposedDraftFileId(v string)`

SetProposedDraftFileId sets ProposedDraftFileId field to given value.

### HasProposedDraftFileId

`func (o *OrderEstimateRequest) HasProposedDraftFileId() bool`

HasProposedDraftFileId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


