# CataloguePostOfferAllOfExtras


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**homepage_listing** | [**MoneyOrNull**](MoneyOrNull.md) | What listing the post on the homepage costs, or null when the media does not offer it. | 
**sensitive_topic** | [**CataloguePostOfferAllOfExtrasSensitiveTopic**](CataloguePostOfferAllOfExtrasSensitiveTopic.md) |  | 

## Example

```python
from growwer.models.catalogue_post_offer_all_of_extras import CataloguePostOfferAllOfExtras

# TODO update the JSON string below
json = "{}"
# create an instance of CataloguePostOfferAllOfExtras from a JSON string
catalogue_post_offer_all_of_extras_instance = CataloguePostOfferAllOfExtras.from_json(json)
# print the JSON string representation of the object
print(CataloguePostOfferAllOfExtras.to_json())

# convert the object into a dict
catalogue_post_offer_all_of_extras_dict = catalogue_post_offer_all_of_extras_instance.to_dict()
# create an instance of CataloguePostOfferAllOfExtras from a dict
catalogue_post_offer_all_of_extras_from_dict = CataloguePostOfferAllOfExtras.from_dict(catalogue_post_offer_all_of_extras_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


