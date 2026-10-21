# ListFlashOffers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProjectCatalogueMedia]**](ProjectCatalogueMedia.md) |  | 
**total** | **int** |  | 

## Example

```python
from growwer.models.list_flash_offers200_response import ListFlashOffers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListFlashOffers200Response from a JSON string
list_flash_offers200_response_instance = ListFlashOffers200Response.from_json(json)
# print the JSON string representation of the object
print(ListFlashOffers200Response.to_json())

# convert the object into a dict
list_flash_offers200_response_dict = list_flash_offers200_response_instance.to_dict()
# create an instance of ListFlashOffers200Response from a dict
list_flash_offers200_response_from_dict = ListFlashOffers200Response.from_dict(list_flash_offers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


