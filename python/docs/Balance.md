# Balance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | [**Money**](Money.md) | What can be spent, or withdrawn, now. | 
**pending** | [**Money**](Money.md) | What is held until orders in progress settle. | 

## Example

```python
from growwer.models.balance import Balance

# TODO update the JSON string below
json = "{}"
# create an instance of Balance from a JSON string
balance_instance = Balance.from_json(json)
# print the JSON string representation of the object
print(Balance.to_json())

# convert the object into a dict
balance_dict = balance_instance.to_dict()
# create an instance of Balance from a dict
balance_from_dict = Balance.from_dict(balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


