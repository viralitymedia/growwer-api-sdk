# OrderDraft

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthoredByBuyer** | **bool** | Whether you write the draft. | 
**Reviewable** | **bool** | Whether you review the draft before it is published. | 
**HasFile** | **bool** | Whether the current draft has a file; GET /orders/{id}/draft downloads it. | 

## Methods

### NewOrderDraft

`func NewOrderDraft(authoredByBuyer bool, reviewable bool, hasFile bool, ) *OrderDraft`

NewOrderDraft instantiates a new OrderDraft object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderDraftWithDefaults

`func NewOrderDraftWithDefaults() *OrderDraft`

NewOrderDraftWithDefaults instantiates a new OrderDraft object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthoredByBuyer

`func (o *OrderDraft) GetAuthoredByBuyer() bool`

GetAuthoredByBuyer returns the AuthoredByBuyer field if non-nil, zero value otherwise.

### GetAuthoredByBuyerOk

`func (o *OrderDraft) GetAuthoredByBuyerOk() (*bool, bool)`

GetAuthoredByBuyerOk returns a tuple with the AuthoredByBuyer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthoredByBuyer

`func (o *OrderDraft) SetAuthoredByBuyer(v bool)`

SetAuthoredByBuyer sets AuthoredByBuyer field to given value.


### GetReviewable

`func (o *OrderDraft) GetReviewable() bool`

GetReviewable returns the Reviewable field if non-nil, zero value otherwise.

### GetReviewableOk

`func (o *OrderDraft) GetReviewableOk() (*bool, bool)`

GetReviewableOk returns a tuple with the Reviewable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewable

`func (o *OrderDraft) SetReviewable(v bool)`

SetReviewable sets Reviewable field to given value.


### GetHasFile

`func (o *OrderDraft) GetHasFile() bool`

GetHasFile returns the HasFile field if non-nil, zero value otherwise.

### GetHasFileOk

`func (o *OrderDraft) GetHasFileOk() (*bool, bool)`

GetHasFileOk returns a tuple with the HasFile field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasFile

`func (o *OrderDraft) SetHasFile(v bool)`

SetHasFile sets HasFile field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


