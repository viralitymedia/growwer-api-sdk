# ManagedServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_url** | **str** | The website the campaign is for. | 
**goal** | **str** |  | 
**country** | **str** | ISO 3166-1 alpha-2 code of the target country. | 
**duration** | **str** |  | 
**estimated_budget** | [**Money**](Money.md) | At least 500 EUR. Only EUR is accepted. | 
**additional_info** | **str** |  | [optional] 

## Example

```python
from growwer.models.managed_service_request import ManagedServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceRequest from a JSON string
managed_service_request_instance = ManagedServiceRequest.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceRequest.to_json())

# convert the object into a dict
managed_service_request_dict = managed_service_request_instance.to_dict()
# create an instance of ManagedServiceRequest from a dict
managed_service_request_from_dict = ManagedServiceRequest.from_dict(managed_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


