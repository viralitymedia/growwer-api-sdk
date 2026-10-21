# SellerMediaPostOfferPricingOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_when_seller_writes_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post you write, or null when you do not offer it. | 
**fee_when_seller_does_not_write_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post the buyer or Growwer writes, or null when you do not offer it. | 
**link_type** | **str** |  | 
**current_cost** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid now for the link type, flash offer discount included; read-only. Null when the link type has no current pricing. | 

## Example

```python
from growwer.models.seller_media_post_offer_pricing_options_inner import SellerMediaPostOfferPricingOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SellerMediaPostOfferPricingOptionsInner from a JSON string
seller_media_post_offer_pricing_options_inner_instance = SellerMediaPostOfferPricingOptionsInner.from_json(json)
# print the JSON string representation of the object
print(SellerMediaPostOfferPricingOptionsInner.to_json())

# convert the object into a dict
seller_media_post_offer_pricing_options_inner_dict = seller_media_post_offer_pricing_options_inner_instance.to_dict()
# create an instance of SellerMediaPostOfferPricingOptionsInner from a dict
seller_media_post_offer_pricing_options_inner_from_dict = SellerMediaPostOfferPricingOptionsInner.from_dict(seller_media_post_offer_pricing_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


