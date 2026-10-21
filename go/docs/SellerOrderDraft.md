# SellerOrderDraft

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Reviewable** | **bool** | Whether the buyer reviews the draft before it is published. | 
**HasFile** | **bool** | Whether the current draft has a file; GET /seller/orders/{id}/draft downloads it. | 

## Methods

### NewSellerOrderDraft

`func NewSellerOrderDraft(reviewable bool, hasFile bool, ) *SellerOrderDraft`

NewSellerOrderDraft instantiates a new SellerOrderDraft object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerOrderDraftWithDefaults

`func NewSellerOrderDraftWithDefaults() *SellerOrderDraft`

NewSellerOrderDraftWithDefaults instantiates a new SellerOrderDraft object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetReviewable

`func (o *SellerOrderDraft) GetReviewable() bool`

GetReviewable returns the Reviewable field if non-nil, zero value otherwise.

### GetReviewableOk

`func (o *SellerOrderDraft) GetReviewableOk() (*bool, bool)`

GetReviewableOk returns a tuple with the Reviewable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewable

`func (o *SellerOrderDraft) SetReviewable(v bool)`

SetReviewable sets Reviewable field to given value.


### GetHasFile

`func (o *SellerOrderDraft) GetHasFile() bool`

GetHasFile returns the HasFile field if non-nil, zero value otherwise.

### GetHasFileOk

`func (o *SellerOrderDraft) GetHasFileOk() (*bool, bool)`

GetHasFileOk returns a tuple with the HasFile field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasFile

`func (o *SellerOrderDraft) SetHasFile(v bool)`

SetHasFile sets HasFile field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


