# CreateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**root_url** | **str** |  | 
**website_type** | **str** |  | 
**topics** | **List[int]** | Exactly one topic id from GET /vocabulary. | 
**language** | **str** | A language code from GET /vocabulary. | 
**country** | **str** | A country code from GET /vocabulary; omit it or send null for worldwide. | [optional] 
**promoted_products** | **List[str]** | 5 to 10 products or services the campaign promotes. | 
**user_keywords** | **List[str]** | At most 100 keywords, none with a line break. | [optional] 

## Example

```python
from growwer.models.create_project_request import CreateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectRequest from a JSON string
create_project_request_instance = CreateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectRequest.to_json())

# convert the object into a dict
create_project_request_dict = create_project_request_instance.to_dict()
# create an instance of CreateProjectRequest from a dict
create_project_request_from_dict = CreateProjectRequest.from_dict(create_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


