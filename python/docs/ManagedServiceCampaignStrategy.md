# ManagedServiceCampaignStrategy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal** | **str** |  | 
**countries** | **List[str]** | ISO 3166-1 alpha-2 codes. | 
**languages** | **List[str]** |  | 
**topics** | **List[int]** | Topic ids, as GET /vocabulary lists them. | 
**definition** | **str** |  | 

## Example

```python
from growwer.models.managed_service_campaign_strategy import ManagedServiceCampaignStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceCampaignStrategy from a JSON string
managed_service_campaign_strategy_instance = ManagedServiceCampaignStrategy.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceCampaignStrategy.to_json())

# convert the object into a dict
managed_service_campaign_strategy_dict = managed_service_campaign_strategy_instance.to_dict()
# create an instance of ManagedServiceCampaignStrategy from a dict
managed_service_campaign_strategy_from_dict = ManagedServiceCampaignStrategy.from_dict(managed_service_campaign_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


