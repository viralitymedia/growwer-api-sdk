# ManagedServiceProposalReviewRequestReviewsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProposalId** | **string** |  | 
**Decision** | **string** |  | 
**Comment** | Pointer to **NullableString** | Required to reject, at most 2000 characters once trimmed; the team reads it. | [optional] 

## Methods

### NewManagedServiceProposalReviewRequestReviewsInner

`func NewManagedServiceProposalReviewRequestReviewsInner(proposalId string, decision string, ) *ManagedServiceProposalReviewRequestReviewsInner`

NewManagedServiceProposalReviewRequestReviewsInner instantiates a new ManagedServiceProposalReviewRequestReviewsInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewManagedServiceProposalReviewRequestReviewsInnerWithDefaults

`func NewManagedServiceProposalReviewRequestReviewsInnerWithDefaults() *ManagedServiceProposalReviewRequestReviewsInner`

NewManagedServiceProposalReviewRequestReviewsInnerWithDefaults instantiates a new ManagedServiceProposalReviewRequestReviewsInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProposalId

`func (o *ManagedServiceProposalReviewRequestReviewsInner) GetProposalId() string`

GetProposalId returns the ProposalId field if non-nil, zero value otherwise.

### GetProposalIdOk

`func (o *ManagedServiceProposalReviewRequestReviewsInner) GetProposalIdOk() (*string, bool)`

GetProposalIdOk returns a tuple with the ProposalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProposalId

`func (o *ManagedServiceProposalReviewRequestReviewsInner) SetProposalId(v string)`

SetProposalId sets ProposalId field to given value.


### GetDecision

`func (o *ManagedServiceProposalReviewRequestReviewsInner) GetDecision() string`

GetDecision returns the Decision field if non-nil, zero value otherwise.

### GetDecisionOk

`func (o *ManagedServiceProposalReviewRequestReviewsInner) GetDecisionOk() (*string, bool)`

GetDecisionOk returns a tuple with the Decision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDecision

`func (o *ManagedServiceProposalReviewRequestReviewsInner) SetDecision(v string)`

SetDecision sets Decision field to given value.


### GetComment

`func (o *ManagedServiceProposalReviewRequestReviewsInner) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *ManagedServiceProposalReviewRequestReviewsInner) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *ManagedServiceProposalReviewRequestReviewsInner) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *ManagedServiceProposalReviewRequestReviewsInner) HasComment() bool`

HasComment returns a boolean if a field has been set.

### SetCommentNil

`func (o *ManagedServiceProposalReviewRequestReviewsInner) SetCommentNil(b bool)`

 SetCommentNil sets the value for Comment to be an explicit nil

### UnsetComment
`func (o *ManagedServiceProposalReviewRequestReviewsInner) UnsetComment()`

UnsetComment ensures that no value is present for Comment, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


