# SellerOrder

An order placed on one of your medias, as its seller sees it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**reference** | **str** |  | 
**type** | **str** |  | 
**state** | **str** | The raw state name. GET /seller/orders documents the values its &#x60;state&#x60; filter takes. | 
**requires_your_action** | **bool** | Whether the order waits on you, as the seller order list marks it. | 
**available_actions** | **List[str]** | The seller actions the order allows now. | 
**earnings** | [**Money**](Money.md) | What you are paid for the order, credited to your seller wallet once it settles. | 
**project** | [**SellerOrderProject**](SellerOrderProject.md) |  | 
**media** | [**OrderMedia**](OrderMedia.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** | When the order last changed state. It changes on state changes only, so poll with GET /seller/orders?updatedSince&#x3D; on it. | 
**scheduled_publication_date** | **datetime** |  | 
**delivery** | [**OrderDelivery**](OrderDelivery.md) |  | 
**briefing** | [**SellerOrderBriefing**](SellerOrderBriefing.md) |  | 
**draft** | [**SellerOrderDraft**](SellerOrderDraft.md) |  | 
**state_history** | [**List[OrderStateHistoryInner]**](OrderStateHistoryInner.md) | Every state change, oldest first. | 
**channel** | [**SellerOrderChannel**](SellerOrderChannel.md) |  | 

## Example

```python
from growwer.models.seller_order import SellerOrder

# TODO update the JSON string below
json = "{}"
# create an instance of SellerOrder from a JSON string
seller_order_instance = SellerOrder.from_json(json)
# print the JSON string representation of the object
print(SellerOrder.to_json())

# convert the object into a dict
seller_order_dict = seller_order_instance.to_dict()
# create an instance of SellerOrder from a dict
seller_order_from_dict = SellerOrder.from_dict(seller_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


