# UpdateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Null or an empty string removes the name. | [optional] 
**website_type** | **str** |  | [optional] 
**topics** | **List[int]** | Exactly one topic id from GET /vocabulary. | [optional] 
**language** | **str** | A language code from GET /vocabulary. | [optional] 
**country** | **str** | A country code from GET /vocabulary, or null for worldwide. | [optional] 
**promoted_products** | **List[str]** | 5 to 10 products or services the campaign promotes. | [optional] 
**user_keywords** | **List[str]** | At most 100 keywords, none with a line break. | [optional] 

## Example

```python
from growwer.models.update_project_request import UpdateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectRequest from a JSON string
update_project_request_instance = UpdateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectRequest.to_json())

# convert the object into a dict
update_project_request_dict = update_project_request_instance.to_dict()
# create an instance of UpdateProjectRequest from a dict
update_project_request_from_dict = UpdateProjectRequest.from_dict(update_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


