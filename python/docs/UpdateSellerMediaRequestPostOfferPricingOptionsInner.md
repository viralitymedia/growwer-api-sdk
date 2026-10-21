# UpdateSellerMediaRequestPostOfferPricingOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_type** | **str** |  | 
**fee_when_seller_writes_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post you write; null or left out when you do not offer it. | [optional] 
**fee_when_seller_does_not_write_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post the buyer or Growwer writes; null or left out when you do not offer it. | [optional] 

## Example

```python
from growwer.models.update_seller_media_request_post_offer_pricing_options_inner import UpdateSellerMediaRequestPostOfferPricingOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSellerMediaRequestPostOfferPricingOptionsInner from a JSON string
update_seller_media_request_post_offer_pricing_options_inner_instance = UpdateSellerMediaRequestPostOfferPricingOptionsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateSellerMediaRequestPostOfferPricingOptionsInner.to_json())

# convert the object into a dict
update_seller_media_request_post_offer_pricing_options_inner_dict = update_seller_media_request_post_offer_pricing_options_inner_instance.to_dict()
# create an instance of UpdateSellerMediaRequestPostOfferPricingOptionsInner from a dict
update_seller_media_request_post_offer_pricing_options_inner_from_dict = UpdateSellerMediaRequestPostOfferPricingOptionsInner.from_dict(update_seller_media_request_post_offer_pricing_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


