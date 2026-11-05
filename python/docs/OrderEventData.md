# OrderEventData

The `data` of an `order.*` event: the order as GET /orders/{id} answers it at the time of the event. Order by its `updatedAt` when events arrive out of order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**Order**](Order.md) |  | 

## Example

```python
from growwer.models.order_event_data import OrderEventData

# TODO update the JSON string below
json = "{}"
# create an instance of OrderEventData from a JSON string
order_event_data_instance = OrderEventData.from_json(json)
# print the JSON string representation of the object
print(OrderEventData.to_json())

# convert the object into a dict
order_event_data_dict = order_event_data_instance.to_dict()
# create an instance of OrderEventData from a dict
order_event_data_from_dict = OrderEventData.from_dict(order_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


