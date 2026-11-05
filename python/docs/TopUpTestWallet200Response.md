# TopUpTestWallet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**Balance**](Balance.md) |  | 
**top_up_url** | **str** | The wallet page where a live buyer tops up, as GET /wallets/buyer gives it. | 

## Example

```python
from growwer.models.top_up_test_wallet200_response import TopUpTestWallet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TopUpTestWallet200Response from a JSON string
top_up_test_wallet200_response_instance = TopUpTestWallet200Response.from_json(json)
# print the JSON string representation of the object
print(TopUpTestWallet200Response.to_json())

# convert the object into a dict
top_up_test_wallet200_response_dict = top_up_test_wallet200_response_instance.to_dict()
# create an instance of TopUpTestWallet200Response from a dict
top_up_test_wallet200_response_from_dict = TopUpTestWallet200Response.from_dict(top_up_test_wallet200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


