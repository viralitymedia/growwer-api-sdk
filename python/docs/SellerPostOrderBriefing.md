# SellerPostOrderBriefing

The briefing of a post order (`type` `post`), as you, the seller, receive it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**language** | **str** | The language code of the article. | 
**links** | [**List[OrderLink]**](OrderLink.md) |  | 
**extra_services** | **List[str]** |  | 
**additional_info** | **str** |  | 
**written_by** | **str** | Who writes the article; &#x60;seller&#x60; means you do. | 
**has_proposed_draft** | **bool** | Whether the buyer attached a draft; GET /seller/orders/{id}/briefing downloads it. | 

## Example

```python
from growwer.models.seller_post_order_briefing import SellerPostOrderBriefing

# TODO update the JSON string below
json = "{}"
# create an instance of SellerPostOrderBriefing from a JSON string
seller_post_order_briefing_instance = SellerPostOrderBriefing.from_json(json)
# print the JSON string representation of the object
print(SellerPostOrderBriefing.to_json())

# convert the object into a dict
seller_post_order_briefing_dict = seller_post_order_briefing_instance.to_dict()
# create an instance of SellerPostOrderBriefing from a dict
seller_post_order_briefing_from_dict = SellerPostOrderBriefing.from_dict(seller_post_order_briefing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


