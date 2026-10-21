# GetSellerWallet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**Balance**](Balance.md) |  | 
**restricted** | **bool** | Whether your seller account is restricted. | 

## Example

```python
from growwer.models.get_seller_wallet200_response import GetSellerWallet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSellerWallet200Response from a JSON string
get_seller_wallet200_response_instance = GetSellerWallet200Response.from_json(json)
# print the JSON string representation of the object
print(GetSellerWallet200Response.to_json())

# convert the object into a dict
get_seller_wallet200_response_dict = get_seller_wallet200_response_instance.to_dict()
# create an instance of GetSellerWallet200Response from a dict
get_seller_wallet200_response_from_dict = GetSellerWallet200Response.from_dict(get_seller_wallet200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


