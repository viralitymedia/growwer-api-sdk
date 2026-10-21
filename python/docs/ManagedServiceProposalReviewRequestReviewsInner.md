# ManagedServiceProposalReviewRequestReviewsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proposal_id** | **UUID** |  | 
**decision** | **str** |  | 
**comment** | **str** | Required to reject, at most 2000 characters once trimmed; the team reads it. | [optional] 

## Example

```python
from growwer.models.managed_service_proposal_review_request_reviews_inner import ManagedServiceProposalReviewRequestReviewsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceProposalReviewRequestReviewsInner from a JSON string
managed_service_proposal_review_request_reviews_inner_instance = ManagedServiceProposalReviewRequestReviewsInner.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceProposalReviewRequestReviewsInner.to_json())

# convert the object into a dict
managed_service_proposal_review_request_reviews_inner_dict = managed_service_proposal_review_request_reviews_inner_instance.to_dict()
# create an instance of ManagedServiceProposalReviewRequestReviewsInner from a dict
managed_service_proposal_review_request_reviews_inner_from_dict = ManagedServiceProposalReviewRequestReviewsInner.from_dict(managed_service_proposal_review_request_reviews_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


