# SellerMediaPostOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_options** | [**List[SellerMediaPostOfferPricingOptionsInner]**](SellerMediaPostOfferPricingOptionsInner.md) | One entry per link type you offer. | 
**maximum_links** | **int** | How many links a sponsored post may hold, 1 to 4. | 
**advertising_labelling_policy** | **str** | Whether sponsored posts are labelled as advertising. | 
**promoted_social_networks** | **List[str]** | The social networks sponsored posts are promoted on. | 
**extra_services** | [**List[UpdateSellerMediaRequestExtraServicesInner]**](UpdateSellerMediaRequestExtraServicesInner.md) | Read here, but PATCH /seller/medias/{id} and POST /seller/medias take it at the top level of the body. | 

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


