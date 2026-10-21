# GetMe200ResponseManagedService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether you have a managed service: Growwer&#39;s team runs link building campaigns for you (tag Managed services). With one, request a new campaign with POST /managed-service/campaign-requests; without one, ask about the service with POST /managed-service/info-requests. | 

## Example

```python
from growwer.models.get_me200_response_managed_service import GetMe200ResponseManagedService

# TODO update the JSON string below
json = "{}"
# create an instance of GetMe200ResponseManagedService from a JSON string
get_me200_response_managed_service_instance = GetMe200ResponseManagedService.from_json(json)
# print the JSON string representation of the object
print(GetMe200ResponseManagedService.to_json())

# convert the object into a dict
get_me200_response_managed_service_dict = get_me200_response_managed_service_instance.to_dict()
# create an instance of GetMe200ResponseManagedService from a dict
get_me200_response_managed_service_from_dict = GetMe200ResponseManagedService.from_dict(get_me200_response_managed_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


