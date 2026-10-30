# OrderChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | Whether the order was placed through this API (&#x60;api&#x60;), through its MCP server (&#x60;mcp&#x60;) or on the web. | 

## Example

```python
from growwer.models.order_channel import OrderChannel

# TODO update the JSON string below
json = "{}"
# create an instance of OrderChannel from a JSON string
order_channel_instance = OrderChannel.from_json(json)
# print the JSON string representation of the object
print(OrderChannel.to_json())

# convert the object into a dict
order_channel_dict = order_channel_instance.to_dict()
# create an instance of OrderChannel from a dict
order_channel_from_dict = OrderChannel.from_dict(order_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


