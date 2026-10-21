# OrderActionReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | What the seller is told, 10 to 2000 characters once trimmed. | 

## Example

```python
from growwer.models.order_action_reason import OrderActionReason

# TODO update the JSON string below
json = "{}"
# create an instance of OrderActionReason from a JSON string
order_action_reason_instance = OrderActionReason.from_json(json)
# print the JSON string representation of the object
print(OrderActionReason.to_json())

# convert the object into a dict
order_action_reason_dict = order_action_reason_instance.to_dict()
# create an instance of OrderActionReason from a dict
order_action_reason_from_dict = OrderActionReason.from_dict(order_action_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


