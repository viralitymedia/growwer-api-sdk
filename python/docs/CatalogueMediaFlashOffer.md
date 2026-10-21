# CatalogueMediaFlashOffer

The flash offer running, or null. Its discount is already in the prices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_percent** | **int** |  | 
**ends_at** | **datetime** |  | 

## Example

```python
from growwer.models.catalogue_media_flash_offer import CatalogueMediaFlashOffer

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogueMediaFlashOffer from a JSON string
catalogue_media_flash_offer_instance = CatalogueMediaFlashOffer.from_json(json)
# print the JSON string representation of the object
print(CatalogueMediaFlashOffer.to_json())

# convert the object into a dict
catalogue_media_flash_offer_dict = catalogue_media_flash_offer_instance.to_dict()
# create an instance of CatalogueMediaFlashOffer from a dict
catalogue_media_flash_offer_from_dict = CatalogueMediaFlashOffer.from_dict(catalogue_media_flash_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


