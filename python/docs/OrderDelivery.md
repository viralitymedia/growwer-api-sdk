# OrderDelivery

Where the order was published, once it is.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The published article, or for a link addition the article the link went into. | 
**published_at** | **datetime** | When the post was published; null for a link addition. | 

## Example

```python
from growwer.models.order_delivery import OrderDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDelivery from a JSON string
order_delivery_instance = OrderDelivery.from_json(json)
# print the JSON string representation of the object
print(OrderDelivery.to_json())

# convert the object into a dict
order_delivery_dict = order_delivery_instance.to_dict()
# create an instance of OrderDelivery from a dict
order_delivery_from_dict = OrderDelivery.from_dict(order_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


