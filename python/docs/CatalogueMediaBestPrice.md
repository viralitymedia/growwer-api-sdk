# CatalogueMediaBestPrice

The best-price badge the catalogue shows, or null for none: cheaper means the price is at least 1 EUR below the cheapest listing of the media found on the other platforms checked in the last 7 days; only_here means none of the platforms checked lists it. It names neither the platforms nor any price.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **str** |  | 
**platform_count** | **int** | How many platforms the claim was checked against. | 
**checked_on** | **date** | The day of that check. | 

## Example

```python
from growwer.models.catalogue_media_best_price import CatalogueMediaBestPrice

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogueMediaBestPrice from a JSON string
catalogue_media_best_price_instance = CatalogueMediaBestPrice.from_json(json)
# print the JSON string representation of the object
print(CatalogueMediaBestPrice.to_json())

# convert the object into a dict
catalogue_media_best_price_dict = catalogue_media_best_price_instance.to_dict()
# create an instance of CatalogueMediaBestPrice from a dict
catalogue_media_best_price_from_dict = CatalogueMediaBestPrice.from_dict(catalogue_media_best_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


