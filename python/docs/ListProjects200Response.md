# ListProjects200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Project]**](Project.md) |  | 
**total** | **int** |  | 

## Example

```python
from growwer.models.list_projects200_response import ListProjects200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListProjects200Response from a JSON string
list_projects200_response_instance = ListProjects200Response.from_json(json)
# print the JSON string representation of the object
print(ListProjects200Response.to_json())

# convert the object into a dict
list_projects200_response_dict = list_projects200_response_instance.to_dict()
# create an instance of ListProjects200Response from a dict
list_projects200_response_from_dict = ListProjects200Response.from_dict(list_projects200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


