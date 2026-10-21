# OrderStateHistoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**var_date** | **datetime** |  | 
**reason** | [**OrderStateHistoryInnerReason**](OrderStateHistoryInnerReason.md) |  | 

## Example

```python
from growwer.models.order_state_history_inner import OrderStateHistoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStateHistoryInner from a JSON string
order_state_history_inner_instance = OrderStateHistoryInner.from_json(json)
# print the JSON string representation of the object
print(OrderStateHistoryInner.to_json())

# convert the object into a dict
order_state_history_inner_dict = order_state_history_inner_instance.to_dict()
# create an instance of OrderStateHistoryInner from a dict
order_state_history_inner_from_dict = OrderStateHistoryInner.from_dict(order_state_history_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


