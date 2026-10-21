# ManagedServiceProposalMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**domain** | **str** |  | 
**language** | **str** |  | 
**country** | **str** |  | 

## Example

```python
from growwer.models.managed_service_proposal_media import ManagedServiceProposalMedia

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceProposalMedia from a JSON string
managed_service_proposal_media_instance = ManagedServiceProposalMedia.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceProposalMedia.to_json())

# convert the object into a dict
managed_service_proposal_media_dict = managed_service_proposal_media_instance.to_dict()
# create an instance of ManagedServiceProposalMedia from a dict
managed_service_proposal_media_from_dict = ManagedServiceProposalMedia.from_dict(managed_service_proposal_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


