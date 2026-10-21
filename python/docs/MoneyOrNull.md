# MoneyOrNull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Integer cents. | 
**currency** | **str** | ISO 4217 currency code. | 

## Example

```python
from growwer.models.money_or_null import MoneyOrNull

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyOrNull from a JSON string
money_or_null_instance = MoneyOrNull.from_json(json)
# print the JSON string representation of the object
print(MoneyOrNull.to_json())

# convert the object into a dict
money_or_null_dict = money_or_null_instance.to_dict()
# create an instance of MoneyOrNull from a dict
money_or_null_from_dict = MoneyOrNull.from_dict(money_or_null_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


