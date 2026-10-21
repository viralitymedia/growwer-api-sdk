# ManagedServiceCampaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | **string** |  | 
**State** | **string** | &#x60;proposal_delivered&#x60;: proposals await your review. &#x60;proposal_changes_requested&#x60;: you rejected some and the team is preparing others. &#x60;proposal_accepted&#x60;: none awaits your review and the team is placing the orders. | 
**Deadline** | **time.Time** |  | 
**Budget** | [**Money**](Money.md) |  | 
**Project** | [**NullableManagedServiceCampaignProject**](ManagedServiceCampaignProject.md) |  | 
**Strategy** | [**ManagedServiceCampaignStrategy**](ManagedServiceCampaignStrategy.md) |  | 
**ProposalCounts** | [**ManagedServiceCampaignProposalCounts**](ManagedServiceCampaignProposalCounts.md) |  | 
**ProposalsTotal** | [**Money**](Money.md) | The current price of every proposal not cancelled, as the campaign page totals it. | 
**BudgetExceededBy** | [**NullableMoneyOrNull**](MoneyOrNull.md) | How far &#x60;proposalsTotal&#x60; goes beyond the budget; null within it. | 
**CreatedAt** | **time.Time** |  | 
**UpdatedAt** | **time.Time** | When the campaign last changed state. | 

## Methods

### NewManagedServiceCampaign

`func NewManagedServiceCampaign(id string, name string, state string, deadline time.Time, budget Money, project NullableManagedServiceCampaignProject, strategy ManagedServiceCampaignStrategy, proposalCounts ManagedServiceCampaignProposalCounts, proposalsTotal Money, budgetExceededBy NullableMoneyOrNull, createdAt time.Time, updatedAt time.Time, ) *ManagedServiceCampaign`

NewManagedServiceCampaign instantiates a new ManagedServiceCampaign object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewManagedServiceCampaignWithDefaults

`func NewManagedServiceCampaignWithDefaults() *ManagedServiceCampaign`

NewManagedServiceCampaignWithDefaults instantiates a new ManagedServiceCampaign object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ManagedServiceCampaign) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ManagedServiceCampaign) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ManagedServiceCampaign) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *ManagedServiceCampaign) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ManagedServiceCampaign) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ManagedServiceCampaign) SetName(v string)`

SetName sets Name field to given value.


### GetState

`func (o *ManagedServiceCampaign) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *ManagedServiceCampaign) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *ManagedServiceCampaign) SetState(v string)`

SetState sets State field to given value.


### GetDeadline

`func (o *ManagedServiceCampaign) GetDeadline() time.Time`

GetDeadline returns the Deadline field if non-nil, zero value otherwise.

### GetDeadlineOk

`func (o *ManagedServiceCampaign) GetDeadlineOk() (*time.Time, bool)`

GetDeadlineOk returns a tuple with the Deadline field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeadline

`func (o *ManagedServiceCampaign) SetDeadline(v time.Time)`

SetDeadline sets Deadline field to given value.


### GetBudget

`func (o *ManagedServiceCampaign) GetBudget() Money`

GetBudget returns the Budget field if non-nil, zero value otherwise.

### GetBudgetOk

`func (o *ManagedServiceCampaign) GetBudgetOk() (*Money, bool)`

GetBudgetOk returns a tuple with the Budget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudget

`func (o *ManagedServiceCampaign) SetBudget(v Money)`

SetBudget sets Budget field to given value.


### GetProject

`func (o *ManagedServiceCampaign) GetProject() ManagedServiceCampaignProject`

GetProject returns the Project field if non-nil, zero value otherwise.

### GetProjectOk

`func (o *ManagedServiceCampaign) GetProjectOk() (*ManagedServiceCampaignProject, bool)`

GetProjectOk returns a tuple with the Project field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProject

`func (o *ManagedServiceCampaign) SetProject(v ManagedServiceCampaignProject)`

SetProject sets Project field to given value.


### SetProjectNil

`func (o *ManagedServiceCampaign) SetProjectNil(b bool)`

 SetProjectNil sets the value for Project to be an explicit nil

### UnsetProject
`func (o *ManagedServiceCampaign) UnsetProject()`

UnsetProject ensures that no value is present for Project, not even an explicit nil
### GetStrategy

`func (o *ManagedServiceCampaign) GetStrategy() ManagedServiceCampaignStrategy`

GetStrategy returns the Strategy field if non-nil, zero value otherwise.

### GetStrategyOk

`func (o *ManagedServiceCampaign) GetStrategyOk() (*ManagedServiceCampaignStrategy, bool)`

GetStrategyOk returns a tuple with the Strategy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStrategy

`func (o *ManagedServiceCampaign) SetStrategy(v ManagedServiceCampaignStrategy)`

SetStrategy sets Strategy field to given value.


### GetProposalCounts

`func (o *ManagedServiceCampaign) GetProposalCounts() ManagedServiceCampaignProposalCounts`

GetProposalCounts returns the ProposalCounts field if non-nil, zero value otherwise.

### GetProposalCountsOk

`func (o *ManagedServiceCampaign) GetProposalCountsOk() (*ManagedServiceCampaignProposalCounts, bool)`

GetProposalCountsOk returns a tuple with the ProposalCounts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProposalCounts

`func (o *ManagedServiceCampaign) SetProposalCounts(v ManagedServiceCampaignProposalCounts)`

SetProposalCounts sets ProposalCounts field to given value.


### GetProposalsTotal

`func (o *ManagedServiceCampaign) GetProposalsTotal() Money`

GetProposalsTotal returns the ProposalsTotal field if non-nil, zero value otherwise.

### GetProposalsTotalOk

`func (o *ManagedServiceCampaign) GetProposalsTotalOk() (*Money, bool)`

GetProposalsTotalOk returns a tuple with the ProposalsTotal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProposalsTotal

`func (o *ManagedServiceCampaign) SetProposalsTotal(v Money)`

SetProposalsTotal sets ProposalsTotal field to given value.


### GetBudgetExceededBy

`func (o *ManagedServiceCampaign) GetBudgetExceededBy() MoneyOrNull`

GetBudgetExceededBy returns the BudgetExceededBy field if non-nil, zero value otherwise.

### GetBudgetExceededByOk

`func (o *ManagedServiceCampaign) GetBudgetExceededByOk() (*MoneyOrNull, bool)`

GetBudgetExceededByOk returns a tuple with the BudgetExceededBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetExceededBy

`func (o *ManagedServiceCampaign) SetBudgetExceededBy(v MoneyOrNull)`

SetBudgetExceededBy sets BudgetExceededBy field to given value.


### SetBudgetExceededByNil

`func (o *ManagedServiceCampaign) SetBudgetExceededByNil(b bool)`

 SetBudgetExceededByNil sets the value for BudgetExceededBy to be an explicit nil

### UnsetBudgetExceededBy
`func (o *ManagedServiceCampaign) UnsetBudgetExceededBy()`

UnsetBudgetExceededBy ensures that no value is present for BudgetExceededBy, not even an explicit nil
### GetCreatedAt

`func (o *ManagedServiceCampaign) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ManagedServiceCampaign) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ManagedServiceCampaign) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *ManagedServiceCampaign) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *ManagedServiceCampaign) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *ManagedServiceCampaign) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


