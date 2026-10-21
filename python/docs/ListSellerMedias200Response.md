# ListSellerMedias200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SellerMedia]**](SellerMedia.md) |  | 
**total** | **int** |  | 

## Example

```python
from growwer.models.list_seller_medias200_response import ListSellerMedias200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSellerMedias200Response from a JSON string
list_seller_medias200_response_instance = ListSellerMedias200Response.from_json(json)
# print the JSON string representation of the object
print(ListSellerMedias200Response.to_json())

# convert the object into a dict
list_seller_medias200_response_dict = list_seller_medias200_response_instance.to_dict()
# create an instance of ListSellerMedias200Response from a dict
list_seller_medias200_response_from_dict = ListSellerMedias200Response.from_dict(list_seller_medias200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


