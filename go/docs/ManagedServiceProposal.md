# ManagedServiceProposal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**State** | **string** | &#x60;proposed&#x60; awaits your review. &#x60;accepted&#x60; awaits the order the team places for you. &#x60;purchase_started&#x60; and &#x60;purchase_finished&#x60; follow that order. | 
**Media** | [**ManagedServiceProposalMedia**](ManagedServiceProposalMedia.md) |  | 
**Service** | **string** |  | 
**ProposedPrice** | [**Money**](Money.md) | The price the proposal was made at, the one the summary PDF shows. | 
**CurrentPrice** | [**NullableMoneyOrNull**](MoneyOrNull.md) | What the media charges for the service today; null when it no longer offers it. | 
**Briefing** | [**ManagedServiceProposalBriefing**](ManagedServiceProposalBriefing.md) |  | 
**StateReason** | **NullableString** | Why the proposal reached its state, in your language, such as your comment when you rejected it. | 
**OrderId** | **NullableString** | The order placed for the proposal (GET /orders/{id}). | 
**OrderState** | **NullableString** | The state of that order while its purchase is in progress. | 
**CreatedAt** | **time.Time** |  | 
**UpdatedAt** | **time.Time** | When the proposal last changed state. | 

## Methods

### NewManagedServiceProposal

`func NewManagedServiceProposal(id string, state string, media ManagedServiceProposalMedia, service string, proposedPrice Money, currentPrice NullableMoneyOrNull, briefing ManagedServiceProposalBriefing, stateReason NullableString, orderId NullableString, orderState NullableString, createdAt time.Time, updatedAt time.Time, ) *ManagedServiceProposal`

NewManagedServiceProposal instantiates a new ManagedServiceProposal object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewManagedServiceProposalWithDefaults

`func NewManagedServiceProposalWithDefaults() *ManagedServiceProposal`

NewManagedServiceProposalWithDefaults instantiates a new ManagedServiceProposal object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ManagedServiceProposal) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ManagedServiceProposal) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ManagedServiceProposal) SetId(v string)`

SetId sets Id field to given value.


### GetState

`func (o *ManagedServiceProposal) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *ManagedServiceProposal) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *ManagedServiceProposal) SetState(v string)`

SetState sets State field to given value.


### GetMedia

`func (o *ManagedServiceProposal) GetMedia() ManagedServiceProposalMedia`

GetMedia returns the Media field if non-nil, zero value otherwise.

### GetMediaOk

`func (o *ManagedServiceProposal) GetMediaOk() (*ManagedServiceProposalMedia, bool)`

GetMediaOk returns a tuple with the Media field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMedia

`func (o *ManagedServiceProposal) SetMedia(v ManagedServiceProposalMedia)`

SetMedia sets Media field to given value.


### GetService

`func (o *ManagedServiceProposal) GetService() string`

GetService returns the Service field if non-nil, zero value otherwise.

### GetServiceOk

`func (o *ManagedServiceProposal) GetServiceOk() (*string, bool)`

GetServiceOk returns a tuple with the Service field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetService

`func (o *ManagedServiceProposal) SetService(v string)`

SetService sets Service field to given value.


### GetProposedPrice

`func (o *ManagedServiceProposal) GetProposedPrice() Money`

GetProposedPrice returns the ProposedPrice field if non-nil, zero value otherwise.

### GetProposedPriceOk

`func (o *ManagedServiceProposal) GetProposedPriceOk() (*Money, bool)`

GetProposedPriceOk returns a tuple with the ProposedPrice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProposedPrice

`func (o *ManagedServiceProposal) SetProposedPrice(v Money)`

SetProposedPrice sets ProposedPrice field to given value.


### GetCurrentPrice

`func (o *ManagedServiceProposal) GetCurrentPrice() MoneyOrNull`

GetCurrentPrice returns the CurrentPrice field if non-nil, zero value otherwise.

### GetCurrentPriceOk

`func (o *ManagedServiceProposal) GetCurrentPriceOk() (*MoneyOrNull, bool)`

GetCurrentPriceOk returns a tuple with the CurrentPrice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentPrice

`func (o *ManagedServiceProposal) SetCurrentPrice(v MoneyOrNull)`

SetCurrentPrice sets CurrentPrice field to given value.


### SetCurrentPriceNil

`func (o *ManagedServiceProposal) SetCurrentPriceNil(b bool)`

 SetCurrentPriceNil sets the value for CurrentPrice to be an explicit nil

### UnsetCurrentPrice
`func (o *ManagedServiceProposal) UnsetCurrentPrice()`

UnsetCurrentPrice ensures that no value is present for CurrentPrice, not even an explicit nil
### GetBriefing

`func (o *ManagedServiceProposal) GetBriefing() ManagedServiceProposalBriefing`

GetBriefing returns the Briefing field if non-nil, zero value otherwise.

### GetBriefingOk

`func (o *ManagedServiceProposal) GetBriefingOk() (*ManagedServiceProposalBriefing, bool)`

GetBriefingOk returns a tuple with the Briefing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBriefing

`func (o *ManagedServiceProposal) SetBriefing(v ManagedServiceProposalBriefing)`

SetBriefing sets Briefing field to given value.


### GetStateReason

`func (o *ManagedServiceProposal) GetStateReason() string`

GetStateReason returns the StateReason field if non-nil, zero value otherwise.

### GetStateReasonOk

`func (o *ManagedServiceProposal) GetStateReasonOk() (*string, bool)`

GetStateReasonOk returns a tuple with the StateReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStateReason

`func (o *ManagedServiceProposal) SetStateReason(v string)`

SetStateReason sets StateReason field to given value.


### SetStateReasonNil

`func (o *ManagedServiceProposal) SetStateReasonNil(b bool)`

 SetStateReasonNil sets the value for StateReason to be an explicit nil

### UnsetStateReason
`func (o *ManagedServiceProposal) UnsetStateReason()`

UnsetStateReason ensures that no value is present for StateReason, not even an explicit nil
### GetOrderId

`func (o *ManagedServiceProposal) GetOrderId() string`

GetOrderId returns the OrderId field if non-nil, zero value otherwise.

### GetOrderIdOk

`func (o *ManagedServiceProposal) GetOrderIdOk() (*string, bool)`

GetOrderIdOk returns a tuple with the OrderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderId

`func (o *ManagedServiceProposal) SetOrderId(v string)`

SetOrderId sets OrderId field to given value.


### SetOrderIdNil

`func (o *ManagedServiceProposal) SetOrderIdNil(b bool)`

 SetOrderIdNil sets the value for OrderId to be an explicit nil

### UnsetOrderId
`func (o *ManagedServiceProposal) UnsetOrderId()`

UnsetOrderId ensures that no value is present for OrderId, not even an explicit nil
### GetOrderState

`func (o *ManagedServiceProposal) GetOrderState() string`

GetOrderState returns the OrderState field if non-nil, zero value otherwise.

### GetOrderStateOk

`func (o *ManagedServiceProposal) GetOrderStateOk() (*string, bool)`

GetOrderStateOk returns a tuple with the OrderState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderState

`func (o *ManagedServiceProposal) SetOrderState(v string)`

SetOrderState sets OrderState field to given value.


### SetOrderStateNil

`func (o *ManagedServiceProposal) SetOrderStateNil(b bool)`

 SetOrderStateNil sets the value for OrderState to be an explicit nil

### UnsetOrderState
`func (o *ManagedServiceProposal) UnsetOrderState()`

UnsetOrderState ensures that no value is present for OrderState, not even an explicit nil
### GetCreatedAt

`func (o *ManagedServiceProposal) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ManagedServiceProposal) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ManagedServiceProposal) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *ManagedServiceProposal) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *ManagedServiceProposal) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *ManagedServiceProposal) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


