# SellerOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Reference** | **string** |  | 
**Type** | **string** |  | 
**State** | **string** | The raw state name. GET /seller/orders documents the values its &#x60;state&#x60; filter takes. | 
**RequiresYourAction** | **bool** | Whether the order waits on you, as the seller order list marks it. | 
**AvailableActions** | **[]string** | The seller actions the order allows now. | 
**Earnings** | [**Money**](Money.md) | What you are paid for the order, credited to your seller wallet once it settles. | 
**Project** | [**SellerOrderProject**](SellerOrderProject.md) |  | 
**Media** | [**OrderMedia**](OrderMedia.md) |  | 
**CreatedAt** | **time.Time** |  | 
**UpdatedAt** | **time.Time** | When the order last changed state. It changes on state changes only, so poll with GET /seller/orders?updatedSince&#x3D; on it. | 
**ScheduledPublicationDate** | **NullableTime** |  | 
**Delivery** | [**NullableOrderDelivery**](OrderDelivery.md) |  | 
**Briefing** | [**SellerOrderBriefing**](SellerOrderBriefing.md) |  | 
**Draft** | [**NullableSellerOrderDraft**](SellerOrderDraft.md) |  | 
**StateHistory** | [**[]OrderStateHistoryInner**](OrderStateHistoryInner.md) | Every state change, oldest first. | 
**Channel** | [**SellerOrderChannel**](SellerOrderChannel.md) |  | 

## Methods

### NewSellerOrder

`func NewSellerOrder(id string, reference string, type_ string, state string, requiresYourAction bool, availableActions []string, earnings Money, project SellerOrderProject, media OrderMedia, createdAt time.Time, updatedAt time.Time, scheduledPublicationDate NullableTime, delivery NullableOrderDelivery, briefing SellerOrderBriefing, draft NullableSellerOrderDraft, stateHistory []OrderStateHistoryInner, channel SellerOrderChannel, ) *SellerOrder`

NewSellerOrder instantiates a new SellerOrder object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerOrderWithDefaults

`func NewSellerOrderWithDefaults() *SellerOrder`

NewSellerOrderWithDefaults instantiates a new SellerOrder object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SellerOrder) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SellerOrder) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SellerOrder) SetId(v string)`

SetId sets Id field to given value.


### GetReference

`func (o *SellerOrder) GetReference() string`

GetReference returns the Reference field if non-nil, zero value otherwise.

### GetReferenceOk

`func (o *SellerOrder) GetReferenceOk() (*string, bool)`

GetReferenceOk returns a tuple with the Reference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReference

`func (o *SellerOrder) SetReference(v string)`

SetReference sets Reference field to given value.


### GetType

`func (o *SellerOrder) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SellerOrder) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SellerOrder) SetType(v string)`

SetType sets Type field to given value.


### GetState

`func (o *SellerOrder) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *SellerOrder) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *SellerOrder) SetState(v string)`

SetState sets State field to given value.


### GetRequiresYourAction

`func (o *SellerOrder) GetRequiresYourAction() bool`

GetRequiresYourAction returns the RequiresYourAction field if non-nil, zero value otherwise.

### GetRequiresYourActionOk

`func (o *SellerOrder) GetRequiresYourActionOk() (*bool, bool)`

GetRequiresYourActionOk returns a tuple with the RequiresYourAction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequiresYourAction

`func (o *SellerOrder) SetRequiresYourAction(v bool)`

SetRequiresYourAction sets RequiresYourAction field to given value.


### GetAvailableActions

`func (o *SellerOrder) GetAvailableActions() []string`

GetAvailableActions returns the AvailableActions field if non-nil, zero value otherwise.

### GetAvailableActionsOk

`func (o *SellerOrder) GetAvailableActionsOk() (*[]string, bool)`

GetAvailableActionsOk returns a tuple with the AvailableActions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvailableActions

`func (o *SellerOrder) SetAvailableActions(v []string)`

SetAvailableActions sets AvailableActions field to given value.


### GetEarnings

`func (o *SellerOrder) GetEarnings() Money`

GetEarnings returns the Earnings field if non-nil, zero value otherwise.

### GetEarningsOk

`func (o *SellerOrder) GetEarningsOk() (*Money, bool)`

GetEarningsOk returns a tuple with the Earnings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEarnings

`func (o *SellerOrder) SetEarnings(v Money)`

SetEarnings sets Earnings field to given value.


### GetProject

`func (o *SellerOrder) GetProject() SellerOrderProject`

GetProject returns the Project field if non-nil, zero value otherwise.

### GetProjectOk

`func (o *SellerOrder) GetProjectOk() (*SellerOrderProject, bool)`

GetProjectOk returns a tuple with the Project field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProject

`func (o *SellerOrder) SetProject(v SellerOrderProject)`

SetProject sets Project field to given value.


### GetMedia

`func (o *SellerOrder) GetMedia() OrderMedia`

GetMedia returns the Media field if non-nil, zero value otherwise.

### GetMediaOk

`func (o *SellerOrder) GetMediaOk() (*OrderMedia, bool)`

GetMediaOk returns a tuple with the Media field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMedia

`func (o *SellerOrder) SetMedia(v OrderMedia)`

SetMedia sets Media field to given value.


### GetCreatedAt

`func (o *SellerOrder) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SellerOrder) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SellerOrder) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *SellerOrder) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *SellerOrder) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *SellerOrder) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetScheduledPublicationDate

`func (o *SellerOrder) GetScheduledPublicationDate() time.Time`

GetScheduledPublicationDate returns the ScheduledPublicationDate field if non-nil, zero value otherwise.

### GetScheduledPublicationDateOk

`func (o *SellerOrder) GetScheduledPublicationDateOk() (*time.Time, bool)`

GetScheduledPublicationDateOk returns a tuple with the ScheduledPublicationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledPublicationDate

`func (o *SellerOrder) SetScheduledPublicationDate(v time.Time)`

SetScheduledPublicationDate sets ScheduledPublicationDate field to given value.


### SetScheduledPublicationDateNil

`func (o *SellerOrder) SetScheduledPublicationDateNil(b bool)`

 SetScheduledPublicationDateNil sets the value for ScheduledPublicationDate to be an explicit nil

### UnsetScheduledPublicationDate
`func (o *SellerOrder) UnsetScheduledPublicationDate()`

UnsetScheduledPublicationDate ensures that no value is present for ScheduledPublicationDate, not even an explicit nil
### GetDelivery

`func (o *SellerOrder) GetDelivery() OrderDelivery`

GetDelivery returns the Delivery field if non-nil, zero value otherwise.

### GetDeliveryOk

`func (o *SellerOrder) GetDeliveryOk() (*OrderDelivery, bool)`

GetDeliveryOk returns a tuple with the Delivery field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDelivery

`func (o *SellerOrder) SetDelivery(v OrderDelivery)`

SetDelivery sets Delivery field to given value.


### SetDeliveryNil

`func (o *SellerOrder) SetDeliveryNil(b bool)`

 SetDeliveryNil sets the value for Delivery to be an explicit nil

### UnsetDelivery
`func (o *SellerOrder) UnsetDelivery()`

UnsetDelivery ensures that no value is present for Delivery, not even an explicit nil
### GetBriefing

`func (o *SellerOrder) GetBriefing() SellerOrderBriefing`

GetBriefing returns the Briefing field if non-nil, zero value otherwise.

### GetBriefingOk

`func (o *SellerOrder) GetBriefingOk() (*SellerOrderBriefing, bool)`

GetBriefingOk returns a tuple with the Briefing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBriefing

`func (o *SellerOrder) SetBriefing(v SellerOrderBriefing)`

SetBriefing sets Briefing field to given value.


### GetDraft

`func (o *SellerOrder) GetDraft() SellerOrderDraft`

GetDraft returns the Draft field if non-nil, zero value otherwise.

### GetDraftOk

`func (o *SellerOrder) GetDraftOk() (*SellerOrderDraft, bool)`

GetDraftOk returns a tuple with the Draft field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDraft

`func (o *SellerOrder) SetDraft(v SellerOrderDraft)`

SetDraft sets Draft field to given value.


### SetDraftNil

`func (o *SellerOrder) SetDraftNil(b bool)`

 SetDraftNil sets the value for Draft to be an explicit nil

### UnsetDraft
`func (o *SellerOrder) UnsetDraft()`

UnsetDraft ensures that no value is present for Draft, not even an explicit nil
### GetStateHistory

`func (o *SellerOrder) GetStateHistory() []OrderStateHistoryInner`

GetStateHistory returns the StateHistory field if non-nil, zero value otherwise.

### GetStateHistoryOk

`func (o *SellerOrder) GetStateHistoryOk() (*[]OrderStateHistoryInner, bool)`

GetStateHistoryOk returns a tuple with the StateHistory field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStateHistory

`func (o *SellerOrder) SetStateHistory(v []OrderStateHistoryInner)`

SetStateHistory sets StateHistory field to given value.


### GetChannel

`func (o *SellerOrder) GetChannel() SellerOrderChannel`

GetChannel returns the Channel field if non-nil, zero value otherwise.

### GetChannelOk

`func (o *SellerOrder) GetChannelOk() (*SellerOrderChannel, bool)`

GetChannelOk returns a tuple with the Channel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChannel

`func (o *SellerOrder) SetChannel(v SellerOrderChannel)`

SetChannel sets Channel field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


