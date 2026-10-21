# GetBuyerWallet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**Balance**](Balance.md) |  | 
**top_up_url** | **str** | The wallet page, in your language (English when the web is not available in it), where you top up your balance. | 

## Example

```python
from growwer.models.get_buyer_wallet200_response import GetBuyerWallet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBuyerWallet200Response from a JSON string
get_buyer_wallet200_response_instance = GetBuyerWallet200Response.from_json(json)
# print the JSON string representation of the object
print(GetBuyerWallet200Response.to_json())

# convert the object into a dict
get_buyer_wallet200_response_dict = get_buyer_wallet200_response_instance.to_dict()
# create an instance of GetBuyerWallet200Response from a dict
get_buyer_wallet200_response_from_dict = GetBuyerWallet200Response.from_dict(get_buyer_wallet200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


