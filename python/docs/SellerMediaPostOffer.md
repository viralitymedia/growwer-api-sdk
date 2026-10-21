# SellerMediaPostOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_options** | [**List[SellerMediaPostOfferPricingOptionsInner]**](SellerMediaPostOfferPricingOptionsInner.md) | One entry per link type you offer. | 
**extra_services** | [**List[UpdateSellerMediaRequestExtraServicesInner]**](UpdateSellerMediaRequestExtraServicesInner.md) |  | 

## Example

```python
from growwer.models.seller_media_post_offer import SellerMediaPostOffer

# TODO update the JSON string below
json = "{}"
# create an instance of SellerMediaPostOffer from a JSON string
seller_media_post_offer_instance = SellerMediaPostOffer.from_json(json)
# print the JSON string representation of the object
print(SellerMediaPostOffer.to_json())

# convert the object into a dict
seller_media_post_offer_dict = seller_media_post_offer_instance.to_dict()
# create an instance of SellerMediaPostOffer from a dict
seller_media_post_offer_from_dict = SellerMediaPostOffer.from_dict(seller_media_post_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


