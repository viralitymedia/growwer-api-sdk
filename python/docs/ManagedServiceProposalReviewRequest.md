# ManagedServiceProposalReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviews** | [**List[ManagedServiceProposalReviewRequestReviewsInner]**](ManagedServiceProposalReviewRequestReviewsInner.md) | One decision on each proposal of the campaign that is &#x60;proposed&#x60;, each named once. Their order does not matter. | 

## Example

```python
from growwer.models.managed_service_proposal_review_request import ManagedServiceProposalReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceProposalReviewRequest from a JSON string
managed_service_proposal_review_request_instance = ManagedServiceProposalReviewRequest.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceProposalReviewRequest.to_json())

# convert the object into a dict
managed_service_proposal_review_request_dict = managed_service_proposal_review_request_instance.to_dict()
# create an instance of ManagedServiceProposalReviewRequest from a dict
managed_service_proposal_review_request_from_dict = ManagedServiceProposalReviewRequest.from_dict(managed_service_proposal_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


