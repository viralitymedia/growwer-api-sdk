# ManagedServiceProposalReview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Campaign** | [**ManagedServiceCampaign**](ManagedServiceCampaign.md) |  | 
**Proposals** | [**[]ManagedServiceProposal**](ManagedServiceProposal.md) | The proposals you reviewed, newest first. | 

## Methods

### NewManagedServiceProposalReview

`func NewManagedServiceProposalReview(campaign ManagedServiceCampaign, proposals []ManagedServiceProposal, ) *ManagedServiceProposalReview`

NewManagedServiceProposalReview instantiates a new ManagedServiceProposalReview object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewManagedServiceProposalReviewWithDefaults

`func NewManagedServiceProposalReviewWithDefaults() *ManagedServiceProposalReview`

NewManagedServiceProposalReviewWithDefaults instantiates a new ManagedServiceProposalReview object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCampaign

`func (o *ManagedServiceProposalReview) GetCampaign() ManagedServiceCampaign`

GetCampaign returns the Campaign field if non-nil, zero value otherwise.

### GetCampaignOk

`func (o *ManagedServiceProposalReview) GetCampaignOk() (*ManagedServiceCampaign, bool)`

GetCampaignOk returns a tuple with the Campaign field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCampaign

`func (o *ManagedServiceProposalReview) SetCampaign(v ManagedServiceCampaign)`

SetCampaign sets Campaign field to given value.


### GetProposals

`func (o *ManagedServiceProposalReview) GetProposals() []ManagedServiceProposal`

GetProposals returns the Proposals field if non-nil, zero value otherwise.

### GetProposalsOk

`func (o *ManagedServiceProposalReview) GetProposalsOk() (*[]ManagedServiceProposal, bool)`

GetProposalsOk returns a tuple with the Proposals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProposals

`func (o *ManagedServiceProposalReview) SetProposals(v []ManagedServiceProposal)`

SetProposals sets Proposals field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


