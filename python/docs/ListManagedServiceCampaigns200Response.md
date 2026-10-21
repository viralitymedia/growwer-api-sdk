# ListManagedServiceCampaigns200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ManagedServiceCampaign]**](ManagedServiceCampaign.md) |  | 
**total** | **int** |  | 

## Example

```python
from growwer.models.list_managed_service_campaigns200_response import ListManagedServiceCampaigns200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListManagedServiceCampaigns200Response from a JSON string
list_managed_service_campaigns200_response_instance = ListManagedServiceCampaigns200Response.from_json(json)
# print the JSON string representation of the object
print(ListManagedServiceCampaigns200Response.to_json())

# convert the object into a dict
list_managed_service_campaigns200_response_dict = list_managed_service_campaigns200_response_instance.to_dict()
# create an instance of ListManagedServiceCampaigns200Response from a dict
list_managed_service_campaigns200_response_from_dict = ListManagedServiceCampaigns200Response.from_dict(list_managed_service_campaigns200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


