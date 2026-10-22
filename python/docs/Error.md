# Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A stable, machine-readable error code. | 
**message** | **str** | A human-readable explanation. It may change. | 
**request_id** | **str** | UUID v4 generated per request, or the &#x60;X-Request-Id&#x60; you sent. Quote it when reporting a problem. | 
**details** | **Dict[str, object]** | Extra data on some errors, such as the invalid fields of a validation_failed error. | [optional] 

## Example

```python
from growwer.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


