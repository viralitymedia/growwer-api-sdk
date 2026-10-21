# CataloguePostOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**Money**](Money.md) | What you pay for the offer with its dearest link type, flash offer discount included. | 
**link_type** | **str** | The link type &#x60;price&#x60; is for. | 
**prices** | [**Dict[str, Money]**](Money.md) | What you pay for each link type the offer gives, by link type. | 
**previous_price** | [**MoneyOrNull**](MoneyOrNull.md) | The highest price the offer has had, when &#x60;price&#x60; is more than 5% below it; otherwise null. | 
**advertising_label** | **bool** | Whether the media always labels posts as advertising. | 
**promoted_social_networks** | **List[str]** | Where the media promotes the post. | 
**extras** | [**CataloguePostOfferAllOfExtras**](CataloguePostOfferAllOfExtras.md) |  | 

## Example

```python
from growwer.models.catalogue_post_offer import CataloguePostOffer

# TODO update the JSON string below
json = "{}"
# create an instance of CataloguePostOffer from a JSON string
catalogue_post_offer_instance = CataloguePostOffer.from_json(json)
# print the JSON string representation of the object
print(CataloguePostOffer.to_json())

# convert the object into a dict
catalogue_post_offer_dict = catalogue_post_offer_instance.to_dict()
# create an instance of CataloguePostOffer from a dict
catalogue_post_offer_from_dict = CataloguePostOffer.from_dict(catalogue_post_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


