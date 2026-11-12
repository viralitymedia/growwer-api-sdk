# Money


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Integer cents: 12500 is 125.00 EUR. | 
**currency** | **str** | ISO 4217 currency code. | 
**amount_decimal** | **str** | Exact decimal of &#x60;amount&#x60; in major units: \&quot;125.00\&quot;. An input may only echo it unchanged. | [optional] [readonly] 

## Example

```python
from growwer.models.money import Money

# TODO update the JSON string below
json = "{}"
# create an instance of Money from a JSON string
money_instance = Money.from_json(json)
# print the JSON string representation of the object
print(Money.to_json())

# convert the object into a dict
money_dict = money_instance.to_dict()
# create an instance of Money from a dict
money_from_dict = Money.from_dict(money_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


