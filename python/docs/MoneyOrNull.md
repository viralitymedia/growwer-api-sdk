# MoneyOrNull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Integer cents: 12500 is 125.00 EUR. | 
**currency** | **str** | ISO 4217 currency code. | 
**amount_decimal** | **str** | Exact decimal of &#x60;amount&#x60; in major units: \&quot;125.00\&quot;. An input may only echo it unchanged. | [optional] [readonly] 

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


