# ManagedServiceProposalsEstimate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_total** | [**Money**](Money.md) | The proposals already accepted and still awaiting their order. | 
**selected_total** | [**Money**](Money.md) | The proposals named in &#x60;accept&#x60;. | 
**total** | [**Money**](Money.md) | &#x60;acceptedTotal&#x60; plus &#x60;selectedTotal&#x60;. | 
**available_balance** | [**Money**](Money.md) | Your wallet&#39;s available balance. | 
**missing** | [**Money**](Money.md) | How much the available balance falls short of &#x60;total&#x60;; zero when it covers it. | 
**sufficient_balance** | **bool** | Whether the available balance covers &#x60;total&#x60;. | 

## Example

```python
from growwer.models.managed_service_proposals_estimate import ManagedServiceProposalsEstimate

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceProposalsEstimate from a JSON string
managed_service_proposals_estimate_instance = ManagedServiceProposalsEstimate.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceProposalsEstimate.to_json())

# convert the object into a dict
managed_service_proposals_estimate_dict = managed_service_proposals_estimate_instance.to_dict()
# create an instance of ManagedServiceProposalsEstimate from a dict
managed_service_proposals_estimate_from_dict = ManagedServiceProposalsEstimate.from_dict(managed_service_proposals_estimate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


