# SellerOrderBriefing


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
**linking_from** | **str** | The existing article of the media the link goes into. | 
**link** | [**OrderLink**](OrderLink.md) |  | 

## Example

```python
from growwer.models.seller_order_briefing import SellerOrderBriefing

# TODO update the JSON string below
json = "{}"
# create an instance of SellerOrderBriefing from a JSON string
seller_order_briefing_instance = SellerOrderBriefing.from_json(json)
# print the JSON string representation of the object
print(SellerOrderBriefing.to_json())

# convert the object into a dict
seller_order_briefing_dict = seller_order_briefing_instance.to_dict()
# create an instance of SellerOrderBriefing from a dict
seller_order_briefing_from_dict = SellerOrderBriefing.from_dict(seller_order_briefing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


