# ManagedServiceCampaign

A campaign your managed service runs for you. Every figure about proposals counts only those you can see (not the ones the team is still preparing).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**state** | **str** | &#x60;proposal_delivered&#x60;: proposals await your review. &#x60;proposal_changes_requested&#x60;: you rejected some and the team is preparing others. &#x60;proposal_accepted&#x60;: none awaits your review and the team is placing the orders. | 
**deadline** | **datetime** |  | 
**budget** | [**Money**](Money.md) |  | 
**project** | [**ManagedServiceCampaignProject**](ManagedServiceCampaignProject.md) |  | 
**strategy** | [**ManagedServiceCampaignStrategy**](ManagedServiceCampaignStrategy.md) |  | 
**proposal_counts** | [**ManagedServiceCampaignProposalCounts**](ManagedServiceCampaignProposalCounts.md) |  | 
**proposals_total** | [**Money**](Money.md) | The current price of every proposal not cancelled, as the campaign page totals it. | 
**budget_exceeded_by** | [**MoneyOrNull**](MoneyOrNull.md) | How far &#x60;proposalsTotal&#x60; goes beyond the budget; null within it. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** | When the campaign last changed state. | 

## Example

```python
from growwer.models.managed_service_campaign import ManagedServiceCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceCampaign from a JSON string
managed_service_campaign_instance = ManagedServiceCampaign.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceCampaign.to_json())

# convert the object into a dict
managed_service_campaign_dict = managed_service_campaign_instance.to_dict()
# create an instance of ManagedServiceCampaign from a dict
managed_service_campaign_from_dict = ManagedServiceCampaign.from_dict(managed_service_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


