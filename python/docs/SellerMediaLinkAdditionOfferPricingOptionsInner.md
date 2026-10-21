# SellerMediaLinkAdditionOfferPricingOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_type** | **str** |  | 
**fee** | [**Money**](Money.md) | Your base fee for the link type. | 
**current_cost** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid now for the link type, flash offer discount included; read-only. | 

## Example

```python
from growwer.models.seller_media_link_addition_offer_pricing_options_inner import SellerMediaLinkAdditionOfferPricingOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SellerMediaLinkAdditionOfferPricingOptionsInner from a JSON string
seller_media_link_addition_offer_pricing_options_inner_instance = SellerMediaLinkAdditionOfferPricingOptionsInner.from_json(json)
# print the JSON string representation of the object
print(SellerMediaLinkAdditionOfferPricingOptionsInner.to_json())

# convert the object into a dict
seller_media_link_addition_offer_pricing_options_inner_dict = seller_media_link_addition_offer_pricing_options_inner_instance.to_dict()
# create an instance of SellerMediaLinkAdditionOfferPricingOptionsInner from a dict
seller_media_link_addition_offer_pricing_options_inner_from_dict = SellerMediaLinkAdditionOfferPricingOptionsInner.from_dict(seller_media_link_addition_offer_pricing_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


