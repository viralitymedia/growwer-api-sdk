# UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_type** | **str** |  | 
**fee** | [**Money**](Money.md) | Your base fee for adding a link of this type. | 

## Example

```python
from growwer.models.update_seller_media_request_link_addition_offer_pricing_options_inner import UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner from a JSON string
update_seller_media_request_link_addition_offer_pricing_options_inner_instance = UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner.to_json())

# convert the object into a dict
update_seller_media_request_link_addition_offer_pricing_options_inner_dict = update_seller_media_request_link_addition_offer_pricing_options_inner_instance.to_dict()
# create an instance of UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner from a dict
update_seller_media_request_link_addition_offer_pricing_options_inner_from_dict = UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner.from_dict(update_seller_media_request_link_addition_offer_pricing_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


