# ManagedServiceProposalReviewRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Reviews** | [**[]ManagedServiceProposalReviewRequestReviewsInner**](ManagedServiceProposalReviewRequestReviewsInner.md) | One decision on each proposal of the campaign that is &#x60;proposed&#x60;, each named once. Their order does not matter. | 

## Methods

### NewManagedServiceProposalReviewRequest

`func NewManagedServiceProposalReviewRequest(reviews []ManagedServiceProposalReviewRequestReviewsInner, ) *ManagedServiceProposalReviewRequest`

NewManagedServiceProposalReviewRequest instantiates a new ManagedServiceProposalReviewRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewManagedServiceProposalReviewRequestWithDefaults

`func NewManagedServiceProposalReviewRequestWithDefaults() *ManagedServiceProposalReviewRequest`

NewManagedServiceProposalReviewRequestWithDefaults instantiates a new ManagedServiceProposalReviewRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetReviews

`func (o *ManagedServiceProposalReviewRequest) GetReviews() []ManagedServiceProposalReviewRequestReviewsInner`

GetReviews returns the Reviews field if non-nil, zero value otherwise.

### GetReviewsOk

`func (o *ManagedServiceProposalReviewRequest) GetReviewsOk() (*[]ManagedServiceProposalReviewRequestReviewsInner, bool)`

GetReviewsOk returns a tuple with the Reviews field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviews

`func (o *ManagedServiceProposalReviewRequest) SetReviews(v []ManagedServiceProposalReviewRequestReviewsInner)`

SetReviews sets Reviews field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


