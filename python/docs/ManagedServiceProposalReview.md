# ManagedServiceProposalReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign** | [**ManagedServiceCampaign**](ManagedServiceCampaign.md) |  | 
**proposals** | [**List[ManagedServiceProposal]**](ManagedServiceProposal.md) | The proposals you reviewed, newest first. | 

## Example

```python
from growwer.models.managed_service_proposal_review import ManagedServiceProposalReview

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceProposalReview from a JSON string
managed_service_proposal_review_instance = ManagedServiceProposalReview.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceProposalReview.to_json())

# convert the object into a dict
managed_service_proposal_review_dict = managed_service_proposal_review_instance.to_dict()
# create an instance of ManagedServiceProposalReview from a dict
managed_service_proposal_review_from_dict = ManagedServiceProposalReview.from_dict(managed_service_proposal_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


