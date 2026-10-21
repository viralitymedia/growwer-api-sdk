# ManagedServiceProposalsEstimateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept** | **List[UUID]** | The &#x60;proposed&#x60; proposals you would accept, each once. Leave it out to price only the accepted ones. | [optional] 

## Example

```python
from growwer.models.managed_service_proposals_estimate_request import ManagedServiceProposalsEstimateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceProposalsEstimateRequest from a JSON string
managed_service_proposals_estimate_request_instance = ManagedServiceProposalsEstimateRequest.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceProposalsEstimateRequest.to_json())

# convert the object into a dict
managed_service_proposals_estimate_request_dict = managed_service_proposals_estimate_request_instance.to_dict()
# create an instance of ManagedServiceProposalsEstimateRequest from a dict
managed_service_proposals_estimate_request_from_dict = ManagedServiceProposalsEstimateRequest.from_dict(managed_service_proposals_estimate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


