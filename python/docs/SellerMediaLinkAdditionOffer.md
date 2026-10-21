# SellerMediaLinkAdditionOffer

Adding a link to an existing article, or null when you do not offer it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_options** | [**List[SellerMediaLinkAdditionOfferPricingOptionsInner]**](SellerMediaLinkAdditionOfferPricingOptionsInner.md) |  | 

## Example

```python
from growwer.models.seller_media_link_addition_offer import SellerMediaLinkAdditionOffer

# TODO update the JSON string below
json = "{}"
# create an instance of SellerMediaLinkAdditionOffer from a JSON string
seller_media_link_addition_offer_instance = SellerMediaLinkAdditionOffer.from_json(json)
# print the JSON string representation of the object
print(SellerMediaLinkAdditionOffer.to_json())

# convert the object into a dict
seller_media_link_addition_offer_dict = seller_media_link_addition_offer_instance.to_dict()
# create an instance of SellerMediaLinkAdditionOffer from a dict
seller_media_link_addition_offer_from_dict = SellerMediaLinkAdditionOffer.from_dict(seller_media_link_addition_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


