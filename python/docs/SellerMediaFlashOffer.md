# SellerMediaFlashOffer

The flash offer running, or null. Its discount is in `currentCost`, never in the fees.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_percent** | **int** |  | 
**ends_at** | **datetime** |  | 

## Example

```python
from growwer.models.seller_media_flash_offer import SellerMediaFlashOffer

# TODO update the JSON string below
json = "{}"
# create an instance of SellerMediaFlashOffer from a JSON string
seller_media_flash_offer_instance = SellerMediaFlashOffer.from_json(json)
# print the JSON string representation of the object
print(SellerMediaFlashOffer.to_json())

# convert the object into a dict
seller_media_flash_offer_dict = seller_media_flash_offer_instance.to_dict()
# create an instance of SellerMediaFlashOffer from a dict
seller_media_flash_offer_from_dict = SellerMediaFlashOffer.from_dict(seller_media_flash_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


