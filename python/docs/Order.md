# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**reference** | **str** |  | 
**type** | **str** |  | 
**state** | **str** | The raw state name. GET /orders documents the values its &#x60;state&#x60; filter takes. | 
**pending_action** | **str** | Who the order is waiting on, or null when it waits on no one. | 
**price** | [**Money**](Money.md) | What you pay for the order. | 
**project** | [**OrderProject**](OrderProject.md) |  | 
**media** | [**OrderMedia**](OrderMedia.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** | When the order last changed state. It changes on state changes only, so poll with GET /orders?updatedSince&#x3D; on it. | 
**scheduled_publication_date** | **datetime** |  | 
**delivery** | [**OrderDelivery**](OrderDelivery.md) |  | 
**briefing** | [**OrderBriefing**](OrderBriefing.md) |  | 
**draft** | [**OrderDraft**](OrderDraft.md) |  | 
**state_history** | [**List[OrderStateHistoryInner]**](OrderStateHistoryInner.md) | Every state change, oldest first. | 
**channel** | [**OrderChannel**](OrderChannel.md) |  | 

## Example

```python
from growwer.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


