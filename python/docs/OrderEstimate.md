# OrderEstimate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**Money**](Money.md) | What the order costs you. Send it as &#x60;expectedPrice&#x60;. | 
**available_balance** | [**Money**](Money.md) | Your wallet&#39;s available balance. | 
**missing** | [**Money**](Money.md) | How much the available balance falls short of the price; zero when it covers it. | 
**sufficient_balance** | **bool** | Whether the available balance covers the price. | 

## Example

```python
from growwer.models.order_estimate import OrderEstimate

# TODO update the JSON string below
json = "{}"
# create an instance of OrderEstimate from a JSON string
order_estimate_instance = OrderEstimate.from_json(json)
# print the JSON string representation of the object
print(OrderEstimate.to_json())

# convert the object into a dict
order_estimate_dict = order_estimate_instance.to_dict()
# create an instance of OrderEstimate from a dict
order_estimate_from_dict = OrderEstimate.from_dict(order_estimate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


