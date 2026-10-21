# ListSavedFilters200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SavedFilter]**](SavedFilter.md) |  | 
**total** | **int** |  | 

## Example

```python
from growwer.models.list_saved_filters200_response import ListSavedFilters200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSavedFilters200Response from a JSON string
list_saved_filters200_response_instance = ListSavedFilters200Response.from_json(json)
# print the JSON string representation of the object
print(ListSavedFilters200Response.to_json())

# convert the object into a dict
list_saved_filters200_response_dict = list_saved_filters200_response_instance.to_dict()
# create an instance of ListSavedFilters200Response from a dict
list_saved_filters200_response_from_dict = ListSavedFilters200Response.from_dict(list_saved_filters200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


