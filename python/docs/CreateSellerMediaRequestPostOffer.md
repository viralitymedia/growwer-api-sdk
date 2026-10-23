# CreateSellerMediaRequestPostOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_options** | [**List[UpdateSellerMediaRequestPostOfferPricingOptionsInner]**](UpdateSellerMediaRequestPostOfferPricingOptionsInner.md) |  | 
**maximum_links** | **int** |  | 
**advertising_labelling_policy** | **str** |  | [optional] 
**promoted_social_networks** | **List[str]** |  | [optional] 

## Example

```python
from growwer.models.create_seller_media_request_post_offer import CreateSellerMediaRequestPostOffer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSellerMediaRequestPostOffer from a JSON string
create_seller_media_request_post_offer_instance = CreateSellerMediaRequestPostOffer.from_json(json)
# print the JSON string representation of the object
print(CreateSellerMediaRequestPostOffer.to_json())

# convert the object into a dict
create_seller_media_request_post_offer_dict = create_seller_media_request_post_offer_instance.to_dict()
# create an instance of CreateSellerMediaRequestPostOffer from a dict
create_seller_media_request_post_offer_from_dict = CreateSellerMediaRequestPostOffer.from_dict(create_seller_media_request_post_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


