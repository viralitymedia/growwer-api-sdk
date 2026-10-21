# Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Reference** | **string** |  | 
**Type** | **string** |  | 
**State** | **string** | The raw state name. GET /orders documents the values its &#x60;state&#x60; filter takes. | 
**PendingAction** | **NullableString** | Who the order is waiting on, or null when it waits on no one. | 
**Price** | [**Money**](Money.md) | What you pay for the order. | 
**Project** | [**OrderProject**](OrderProject.md) |  | 
**Media** | [**OrderMedia**](OrderMedia.md) |  | 
**CreatedAt** | **time.Time** |  | 
**UpdatedAt** | **time.Time** | When the order last changed state. It changes on state changes only, so poll with GET /orders?updatedSince&#x3D; on it. | 
**ScheduledPublicationDate** | **NullableTime** |  | 
**Delivery** | [**NullableOrderDelivery**](OrderDelivery.md) |  | 
**Briefing** | [**OrderBriefing**](OrderBriefing.md) |  | 
**Draft** | [**NullableOrderDraft**](OrderDraft.md) |  | 
**StateHistory** | [**[]OrderStateHistoryInner**](OrderStateHistoryInner.md) | Every state change, oldest first. | 
**Channel** | [**OrderChannel**](OrderChannel.md) |  | 

## Methods

### NewOrder

`func NewOrder(id string, reference string, type_ string, state string, pendingAction NullableString, price Money, project OrderProject, media OrderMedia, createdAt time.Time, updatedAt time.Time, scheduledPublicationDate NullableTime, delivery NullableOrderDelivery, briefing OrderBriefing, draft NullableOrderDraft, stateHistory []OrderStateHistoryInner, channel OrderChannel, ) *Order`

NewOrder instantiates a new Order object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderWithDefaults

`func NewOrderWithDefaults() *Order`

NewOrderWithDefaults instantiates a new Order object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Order) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Order) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Order) SetId(v string)`

SetId sets Id field to given value.


### GetReference

`func (o *Order) GetReference() string`

GetReference returns the Reference field if non-nil, zero value otherwise.

### GetReferenceOk

`func (o *Order) GetReferenceOk() (*string, bool)`

GetReferenceOk returns a tuple with the Reference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReference

`func (o *Order) SetReference(v string)`

SetReference sets Reference field to given value.


### GetType

`func (o *Order) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Order) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Order) SetType(v string)`

SetType sets Type field to given value.


### GetState

`func (o *Order) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *Order) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *Order) SetState(v string)`

SetState sets State field to given value.


### GetPendingAction

`func (o *Order) GetPendingAction() string`

GetPendingAction returns the PendingAction field if non-nil, zero value otherwise.

### GetPendingActionOk

`func (o *Order) GetPendingActionOk() (*string, bool)`

GetPendingActionOk returns a tuple with the PendingAction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPendingAction

`func (o *Order) SetPendingAction(v string)`

SetPendingAction sets PendingAction field to given value.


### SetPendingActionNil

`func (o *Order) SetPendingActionNil(b bool)`

 SetPendingActionNil sets the value for PendingAction to be an explicit nil

### UnsetPendingAction
`func (o *Order) UnsetPendingAction()`

UnsetPendingAction ensures that no value is present for PendingAction, not even an explicit nil
### GetPrice

`func (o *Order) GetPrice() Money`

GetPrice returns the Price field if non-nil, zero value otherwise.

### GetPriceOk

`func (o *Order) GetPriceOk() (*Money, bool)`

GetPriceOk returns a tuple with the Price field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrice

`func (o *Order) SetPrice(v Money)`

SetPrice sets Price field to given value.


### GetProject

`func (o *Order) GetProject() OrderProject`

GetProject returns the Project field if non-nil, zero value otherwise.

### GetProjectOk

`func (o *Order) GetProjectOk() (*OrderProject, bool)`

GetProjectOk returns a tuple with the Project field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProject

`func (o *Order) SetProject(v OrderProject)`

SetProject sets Project field to given value.


### GetMedia

`func (o *Order) GetMedia() OrderMedia`

GetMedia returns the Media field if non-nil, zero value otherwise.

### GetMediaOk

`func (o *Order) GetMediaOk() (*OrderMedia, bool)`

GetMediaOk returns a tuple with the Media field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMedia

`func (o *Order) SetMedia(v OrderMedia)`

SetMedia sets Media field to given value.


### GetCreatedAt

`func (o *Order) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Order) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Order) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *Order) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Order) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Order) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetScheduledPublicationDate

`func (o *Order) GetScheduledPublicationDate() time.Time`

GetScheduledPublicationDate returns the ScheduledPublicationDate field if non-nil, zero value otherwise.

### GetScheduledPublicationDateOk

`func (o *Order) GetScheduledPublicationDateOk() (*time.Time, bool)`

GetScheduledPublicationDateOk returns a tuple with the ScheduledPublicationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledPublicationDate

`func (o *Order) SetScheduledPublicationDate(v time.Time)`

SetScheduledPublicationDate sets ScheduledPublicationDate field to given value.


### SetScheduledPublicationDateNil

`func (o *Order) SetScheduledPublicationDateNil(b bool)`

 SetScheduledPublicationDateNil sets the value for ScheduledPublicationDate to be an explicit nil

### UnsetScheduledPublicationDate
`func (o *Order) UnsetScheduledPublicationDate()`

UnsetScheduledPublicationDate ensures that no value is present for ScheduledPublicationDate, not even an explicit nil
### GetDelivery

`func (o *Order) GetDelivery() OrderDelivery`

GetDelivery returns the Delivery field if non-nil, zero value otherwise.

### GetDeliveryOk

`func (o *Order) GetDeliveryOk() (*OrderDelivery, bool)`

GetDeliveryOk returns a tuple with the Delivery field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDelivery

`func (o *Order) SetDelivery(v OrderDelivery)`

SetDelivery sets Delivery field to given value.


### SetDeliveryNil

`func (o *Order) SetDeliveryNil(b bool)`

 SetDeliveryNil sets the value for Delivery to be an explicit nil

### UnsetDelivery
`func (o *Order) UnsetDelivery()`

UnsetDelivery ensures that no value is present for Delivery, not even an explicit nil
### GetBriefing

`func (o *Order) GetBriefing() OrderBriefing`

GetBriefing returns the Briefing field if non-nil, zero value otherwise.

### GetBriefingOk

`func (o *Order) GetBriefingOk() (*OrderBriefing, bool)`

GetBriefingOk returns a tuple with the Briefing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBriefing

`func (o *Order) SetBriefing(v OrderBriefing)`

SetBriefing sets Briefing field to given value.


### GetDraft

`func (o *Order) GetDraft() OrderDraft`

GetDraft returns the Draft field if non-nil, zero value otherwise.

### GetDraftOk

`func (o *Order) GetDraftOk() (*OrderDraft, bool)`

GetDraftOk returns a tuple with the Draft field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDraft

`func (o *Order) SetDraft(v OrderDraft)`

SetDraft sets Draft field to given value.


### SetDraftNil

`func (o *Order) SetDraftNil(b bool)`

 SetDraftNil sets the value for Draft to be an explicit nil

### UnsetDraft
`func (o *Order) UnsetDraft()`

UnsetDraft ensures that no value is present for Draft, not even an explicit nil
### GetStateHistory

`func (o *Order) GetStateHistory() []OrderStateHistoryInner`

GetStateHistory returns the StateHistory field if non-nil, zero value otherwise.

### GetStateHistoryOk

`func (o *Order) GetStateHistoryOk() (*[]OrderStateHistoryInner, bool)`

GetStateHistoryOk returns a tuple with the StateHistory field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStateHistory

`func (o *Order) SetStateHistory(v []OrderStateHistoryInner)`

SetStateHistory sets StateHistory field to given value.


### GetChannel

`func (o *Order) GetChannel() OrderChannel`

GetChannel returns the Channel field if non-nil, zero value otherwise.

### GetChannelOk

`func (o *Order) GetChannelOk() (*OrderChannel, bool)`

GetChannelOk returns a tuple with the Channel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChannel

`func (o *Order) SetChannel(v OrderChannel)`

SetChannel sets Channel field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


