# SellerMediaCompetitiveFeesByLinkTypeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_type** | **str** |  | 
**fee_when_seller_writes_post** | [**MoneyOrNull**](MoneyOrNull.md) | The fee the apply sets for a post you write on this link type, or null when it keeps your fee on that side. | 
**fee_when_seller_does_not_write_post** | [**MoneyOrNull**](MoneyOrNull.md) | The fee the apply sets for a post the buyer or Growwer writes on this link type, or null when it keeps your fee on that side. | 

## Example

```python
from growwer.models.seller_media_competitive_fees_by_link_type_inner import SellerMediaCompetitiveFeesByLinkTypeInner

# TODO update the JSON string below
json = "{}"
# create an instance of SellerMediaCompetitiveFeesByLinkTypeInner from a JSON string
seller_media_competitive_fees_by_link_type_inner_instance = SellerMediaCompetitiveFeesByLinkTypeInner.from_json(json)
# print the JSON string representation of the object
print(SellerMediaCompetitiveFeesByLinkTypeInner.to_json())

# convert the object into a dict
seller_media_competitive_fees_by_link_type_inner_dict = seller_media_competitive_fees_by_link_type_inner_instance.to_dict()
# create an instance of SellerMediaCompetitiveFeesByLinkTypeInner from a dict
seller_media_competitive_fees_by_link_type_inner_from_dict = SellerMediaCompetitiveFeesByLinkTypeInner.from_dict(seller_media_competitive_fees_by_link_type_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


