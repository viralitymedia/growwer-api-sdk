# CreateSavedFilterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 1 to 255 characters. | 
**filters** | **Dict[str, object]** | At least one filter parameter of GET /projects/{id}/medias, or &#x60;source&#x60;, by name. | 
**notification_frequency** | **str** | Email new matching medias this often. Omit it for no emails. | [optional] 

## Example

```python
from growwer.models.create_saved_filter_request import CreateSavedFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSavedFilterRequest from a JSON string
create_saved_filter_request_instance = CreateSavedFilterRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSavedFilterRequest.to_json())

# convert the object into a dict
create_saved_filter_request_dict = create_saved_filter_request_instance.to_dict()
# create an instance of CreateSavedFilterRequest from a dict
create_saved_filter_request_from_dict = CreateSavedFilterRequest.from_dict(create_saved_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


