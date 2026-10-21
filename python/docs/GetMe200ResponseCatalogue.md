# GetMe200ResponseCatalogue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **bool** | Whether the catalogue operations (tag Catalogue: searching a project&#39;s medias, flash offers and media details) are open to you. They are open to accounts with recent completed orders, as buyer or as seller; until then they answer 403 &#x60;catalogue_requires_recent_order&#x60;. A media you have ordered is always readable with GET /medias/{id}. | 

## Example

```python
from growwer.models.get_me200_response_catalogue import GetMe200ResponseCatalogue

# TODO update the JSON string below
json = "{}"
# create an instance of GetMe200ResponseCatalogue from a JSON string
get_me200_response_catalogue_instance = GetMe200ResponseCatalogue.from_json(json)
# print the JSON string representation of the object
print(GetMe200ResponseCatalogue.to_json())

# convert the object into a dict
get_me200_response_catalogue_dict = get_me200_response_catalogue_instance.to_dict()
# create an instance of GetMe200ResponseCatalogue from a dict
get_me200_response_catalogue_from_dict = GetMe200ResponseCatalogue.from_dict(get_me200_response_catalogue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


