# RequestMediasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | Domains or URLs, 1 to 200 distinct domains. | 

## Example

```python
from growwer.models.request_medias_request import RequestMediasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMediasRequest from a JSON string
request_medias_request_instance = RequestMediasRequest.from_json(json)
# print the JSON string representation of the object
print(RequestMediasRequest.to_json())

# convert the object into a dict
request_medias_request_dict = request_medias_request_instance.to_dict()
# create an instance of RequestMediasRequest from a dict
request_medias_request_from_dict = RequestMediasRequest.from_dict(request_medias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


