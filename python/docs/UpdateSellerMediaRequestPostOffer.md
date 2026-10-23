# UpdateSellerMediaRequestPostOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_options** | [**List[UpdateSellerMediaRequestPostOfferPricingOptionsInner]**](UpdateSellerMediaRequestPostOfferPricingOptionsInner.md) |  | [optional] 
**maximum_links** | **int** |  | [optional] 
**advertising_labelling_policy** | **str** |  | [optional] 
**promoted_social_networks** | **List[str]** |  | [optional] 

## Example

```python
from growwer.models.update_seller_media_request_post_offer import UpdateSellerMediaRequestPostOffer

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSellerMediaRequestPostOffer from a JSON string
update_seller_media_request_post_offer_instance = UpdateSellerMediaRequestPostOffer.from_json(json)
# print the JSON string representation of the object
print(UpdateSellerMediaRequestPostOffer.to_json())

# convert the object into a dict
update_seller_media_request_post_offer_dict = update_seller_media_request_post_offer_instance.to_dict()
# create an instance of UpdateSellerMediaRequestPostOffer from a dict
update_seller_media_request_post_offer_from_dict = UpdateSellerMediaRequestPostOffer.from_dict(update_seller_media_request_post_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


