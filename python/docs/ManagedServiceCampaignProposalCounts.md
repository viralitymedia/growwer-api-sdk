# ManagedServiceCampaignProposalCounts

How many of the campaign's proposals are in each state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proposed** | **int** |  | 
**accepted** | **int** |  | 
**cancelled** | **int** |  | 
**purchase_started** | **int** |  | 
**purchase_finished** | **int** |  | 

## Example

```python
from growwer.models.managed_service_campaign_proposal_counts import ManagedServiceCampaignProposalCounts

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceCampaignProposalCounts from a JSON string
managed_service_campaign_proposal_counts_instance = ManagedServiceCampaignProposalCounts.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceCampaignProposalCounts.to_json())

# convert the object into a dict
managed_service_campaign_proposal_counts_dict = managed_service_campaign_proposal_counts_instance.to_dict()
# create an instance of ManagedServiceCampaignProposalCounts from a dict
managed_service_campaign_proposal_counts_from_dict = ManagedServiceCampaignProposalCounts.from_dict(managed_service_campaign_proposal_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


