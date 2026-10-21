# ListBuyerTransactions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Transaction]**](Transaction.md) |  | 
**total** | **int** |  | 

## Example

```python
from growwer.models.list_buyer_transactions200_response import ListBuyerTransactions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListBuyerTransactions200Response from a JSON string
list_buyer_transactions200_response_instance = ListBuyerTransactions200Response.from_json(json)
# print the JSON string representation of the object
print(ListBuyerTransactions200Response.to_json())

# convert the object into a dict
list_buyer_transactions200_response_dict = list_buyer_transactions200_response_instance.to_dict()
# create an instance of ListBuyerTransactions200Response from a dict
list_buyer_transactions200_response_from_dict = ListBuyerTransactions200Response.from_dict(list_buyer_transactions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


