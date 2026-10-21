# ListWithdrawals200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Withdrawal]**](Withdrawal.md) |  | 
**total** | **int** |  | 

## Example

```python
from growwer.models.list_withdrawals200_response import ListWithdrawals200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListWithdrawals200Response from a JSON string
list_withdrawals200_response_instance = ListWithdrawals200Response.from_json(json)
# print the JSON string representation of the object
print(ListWithdrawals200Response.to_json())

# convert the object into a dict
list_withdrawals200_response_dict = list_withdrawals200_response_instance.to_dict()
# create an instance of ListWithdrawals200Response from a dict
list_withdrawals200_response_from_dict = ListWithdrawals200Response.from_dict(list_withdrawals200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


