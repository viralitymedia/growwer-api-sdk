# BalanceLowEventData

The `data` of a `balance.low` event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet** | [**BalanceLowEventDataWallet**](BalanceLowEventDataWallet.md) |  | 
**threshold** | [**Money**](Money.md) | The subscription&#39;s &#x60;lowBalanceThreshold&#x60; that the balance dropped below. | 

## Example

```python
from growwer.models.balance_low_event_data import BalanceLowEventData

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceLowEventData from a JSON string
balance_low_event_data_instance = BalanceLowEventData.from_json(json)
# print the JSON string representation of the object
print(BalanceLowEventData.to_json())

# convert the object into a dict
balance_low_event_data_dict = balance_low_event_data_instance.to_dict()
# create an instance of BalanceLowEventData from a dict
balance_low_event_data_from_dict = BalanceLowEventData.from_dict(balance_low_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


