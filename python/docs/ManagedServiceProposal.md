# ManagedServiceProposal

A media the team proposes for a campaign, with the publication it would get.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**state** | **str** | &#x60;proposed&#x60; awaits your review. &#x60;accepted&#x60; awaits the order the team places for you. &#x60;purchase_started&#x60; and &#x60;purchase_finished&#x60; follow that order. | 
**media** | [**ManagedServiceProposalMedia**](ManagedServiceProposalMedia.md) |  | 
**service** | **str** |  | 
**proposed_price** | [**Money**](Money.md) | The price the proposal was made at, the one the summary PDF shows. | 
**current_price** | [**MoneyOrNull**](MoneyOrNull.md) | What the media charges for the service today; null when it no longer offers it. | 
**briefing** | [**ManagedServiceProposalBriefing**](ManagedServiceProposalBriefing.md) |  | 
**state_reason** | **str** | Why the proposal reached its state, in your language, such as your comment when you rejected it. | 
**order_id** | **UUID** | The order placed for the proposal (GET /orders/{id}). | 
**order_state** | **str** | The state of that order while its purchase is in progress. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** | When the proposal last changed state. | 

## Example

```python
from growwer.models.managed_service_proposal import ManagedServiceProposal

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedServiceProposal from a JSON string
managed_service_proposal_instance = ManagedServiceProposal.from_json(json)
# print the JSON string representation of the object
print(ManagedServiceProposal.to_json())

# convert the object into a dict
managed_service_proposal_dict = managed_service_proposal_instance.to_dict()
# create an instance of ManagedServiceProposal from a dict
managed_service_proposal_from_dict = ManagedServiceProposal.from_dict(managed_service_proposal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


