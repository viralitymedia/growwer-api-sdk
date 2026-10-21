# ManagedServiceProposalBriefing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main_info** | **str** |  | 
**links** | [**List[ManagedServiceProposalBriefingLinksInner]**](ManagedServiceProposalBriefingLinksInner.md) |  | 
**additional_info** | **str** |  | 
**requires_draft** | **bool** |  | 

## Example

```python
from growwer.models.managed_service_proposal_briefing import ManagedServiceProposalBriefing

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceProposalBriefing from a JSON string
managed_service_proposal_briefing_instance = ManagedServiceProposalBriefing.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceProposalBriefing.to_json())

# convert the object into a dict
managed_service_proposal_briefing_dict = managed_service_proposal_briefing_instance.to_dict()
# create an instance of ManagedServiceProposalBriefing from a dict
managed_service_proposal_briefing_from_dict = ManagedServiceProposalBriefing.from_dict(managed_service_proposal_briefing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


