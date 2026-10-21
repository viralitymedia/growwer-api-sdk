# ManagedServiceCampaignProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**url** | **str** |  | 

## Example

```python
from growwer.models.managed_service_campaign_project import ManagedServiceCampaignProject

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceCampaignProject from a JSON string
managed_service_campaign_project_instance = ManagedServiceCampaignProject.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceCampaignProject.to_json())

# convert the object into a dict
managed_service_campaign_project_dict = managed_service_campaign_project_instance.to_dict()
# create an instance of ManagedServiceCampaignProject from a dict
managed_service_campaign_project_from_dict = ManagedServiceCampaignProject.from_dict(managed_service_campaign_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


