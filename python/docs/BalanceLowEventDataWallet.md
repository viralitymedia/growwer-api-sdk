# BalanceLowEventDataWallet

Your buyer wallet once the debit was made.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_balance** | [**Money**](Money.md) |  | 
**currency** | **str** | The currency of the wallet. | 

## Example

```python
from growwer.models.balance_low_event_data_wallet import BalanceLowEventDataWallet

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceLowEventDataWallet from a JSON string
balance_low_event_data_wallet_instance = BalanceLowEventDataWallet.from_json(json)
# print the JSON string representation of the object
print(BalanceLowEventDataWallet.to_json())

# convert the object into a dict
balance_low_event_data_wallet_dict = balance_low_event_data_wallet_instance.to_dict()
# create an instance of BalanceLowEventDataWallet from a dict
balance_low_event_data_wallet_from_dict = BalanceLowEventDataWallet.from_dict(balance_low_event_data_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


