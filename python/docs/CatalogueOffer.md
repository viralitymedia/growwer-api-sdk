# CatalogueOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**Money**](Money.md) | What you pay for the offer with its dearest link type, flash offer discount included. | 
**link_type** | **str** | The link type &#x60;price&#x60; is for. | 
**prices** | [**Dict[str, Money]**](Money.md) | What you pay for each link type the offer gives, by link type. | 
**previous_price** | [**MoneyOrNull**](MoneyOrNull.md) | The highest price the offer has had, when &#x60;price&#x60; is more than 5% below it; otherwise null. | 

## Example

```python
from growwer.models.catalogue_offer import CatalogueOffer

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogueOffer from a JSON string
catalogue_offer_instance = CatalogueOffer.from_json(json)
# print the JSON string representation of the object
print(CatalogueOffer.to_json())

# convert the object into a dict
catalogue_offer_dict = catalogue_offer_instance.to_dict()
# create an instance of CatalogueOffer from a dict
catalogue_offer_from_dict = CatalogueOffer.from_dict(catalogue_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


