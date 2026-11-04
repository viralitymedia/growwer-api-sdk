# TopUpTestWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Money**](Money.md) | What to credit, in EUR: from 1 to 1000000 cents. | 

## Example

```python
from growwer.models.top_up_test_wallet_request import TopUpTestWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TopUpTestWalletRequest from a JSON string
top_up_test_wallet_request_instance = TopUpTestWalletRequest.from_json(json)
# print the JSON string representation of the object
print(TopUpTestWalletRequest.to_json())

# convert the object into a dict
top_up_test_wallet_request_dict = top_up_test_wallet_request_instance.to_dict()
# create an instance of TopUpTestWalletRequest from a dict
top_up_test_wallet_request_from_dict = TopUpTestWalletRequest.from_dict(top_up_test_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


