# Withdrawal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**state** | **str** |  | 
**amount** | [**Money**](Money.md) | What you withdraw. | 
**method** | **str** |  | 
**has_invoice** | **bool** | Whether you uploaded an invoice; GET /withdrawals/{id}/invoice downloads it. | 
**created_at** | **datetime** |  | 

## Example

```python
from growwer.models.withdrawal import Withdrawal

# TODO update the JSON string below
json = "{}"
# create an instance of Withdrawal from a JSON string
withdrawal_instance = Withdrawal.from_json(json)
# print the JSON string representation of the object
print(Withdrawal.to_json())

# convert the object into a dict
withdrawal_dict = withdrawal_instance.to_dict()
# create an instance of Withdrawal from a dict
withdrawal_from_dict = Withdrawal.from_dict(withdrawal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


