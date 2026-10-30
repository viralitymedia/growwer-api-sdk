# SellerOrderChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | Whether the order was placed through this API (&#x60;api&#x60;), through its MCP server (&#x60;mcp&#x60;) or on the web. | 
**accepted** | **str** | Whether you accepted the order through this API (&#x60;api&#x60;), through its MCP server (&#x60;mcp&#x60;) or elsewhere (&#x60;web&#x60;), or null while it is not accepted. | 

## Example

```python
from growwer.models.seller_order_channel import SellerOrderChannel

# TODO update the JSON string below
json = "{}"
# create an instance of SellerOrderChannel from a JSON string
seller_order_channel_instance = SellerOrderChannel.from_json(json)
# print the JSON string representation of the object
print(SellerOrderChannel.to_json())

# convert the object into a dict
seller_order_channel_dict = seller_order_channel_instance.to_dict()
# create an instance of SellerOrderChannel from a dict
seller_order_channel_from_dict = SellerOrderChannel.from_dict(seller_order_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


