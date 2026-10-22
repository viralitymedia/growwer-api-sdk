# GetMe200ResponseCatalogue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **bool** | Whether you have the full daily cap of the catalogue operations (tag Catalogue: searching a project&#39;s medias, flash offers and media details). It is open to accounts with recent completed orders, as buyer or as seller; until then the catalogue answers within a smaller daily trial quota, which rises to the full cap after a completed order. A media you have ordered is always readable with GET /medias/{id} and counts against neither. | 
**daily_cap** | **int** | How many distinct medias the catalogue operations show you per UTC day: the full cap when &#x60;eligible&#x60; is true, the trial quota otherwise. 0 means the catalogue answers 403 &#x60;catalogue_requires_recent_order&#x60; until you have a recent completed order. | 
**remaining_today** | **int** | How many new distinct medias still fit in &#x60;dailyCap&#x60; today (UTC). Medias you have already seen today are free. Null when the count cannot be read right now; the catalogue operations then answer 503 until it can. | 

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


