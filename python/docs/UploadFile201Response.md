# UploadFile201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** | The name the file was uploaded with. | 
**size** | **int** | Bytes. | 
**expires_at** | **datetime** |  | 

## Example

```python
from growwer.models.upload_file201_response import UploadFile201Response

# TODO update the JSON string below
json = "{}"
# create an instance of UploadFile201Response from a JSON string
upload_file201_response_instance = UploadFile201Response.from_json(json)
# print the JSON string representation of the object
print(UploadFile201Response.to_json())

# convert the object into a dict
upload_file201_response_dict = upload_file201_response_instance.to_dict()
# create an instance of UploadFile201Response from a dict
upload_file201_response_from_dict = UploadFile201Response.from_dict(upload_file201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


