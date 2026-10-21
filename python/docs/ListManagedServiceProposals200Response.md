# ListManagedServiceProposals200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ManagedServiceProposal]**](ManagedServiceProposal.md) |  | 
**total** | **int** |  | 

## Example

```python
from growwer.models.list_managed_service_proposals200_response import ListManagedServiceProposals200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListManagedServiceProposals200Response from a JSON string
list_managed_service_proposals200_response_instance = ListManagedServiceProposals200Response.from_json(json)
# print the JSON string representation of the object
print(ListManagedServiceProposals200Response.to_json())

# convert the object into a dict
list_managed_service_proposals200_response_dict = list_managed_service_proposals200_response_instance.to_dict()
# create an instance of ListManagedServiceProposals200Response from a dict
list_managed_service_proposals200_response_from_dict = ListManagedServiceProposals200Response.from_dict(list_managed_service_proposals200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


