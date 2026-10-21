# ManagedServiceProposal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**state** | **string** | &#x60;proposed&#x60; awaits your review. &#x60;accepted&#x60; awaits the order the team places for you. &#x60;purchase_started&#x60; and &#x60;purchase_finished&#x60; follow that order. |
**media** | [**\Growwer\Api\Model\ManagedServiceProposalMedia**](ManagedServiceProposalMedia.md) |  |
**service** | **string** |  |
**proposed_price** | [**\Growwer\Api\Model\Money**](Money.md) | The price the proposal was made at, the one the summary PDF shows. |
**current_price** | [**\Growwer\Api\Model\MoneyOrNull**](MoneyOrNull.md) | What the media charges for the service today; null when it no longer offers it. |
**briefing** | [**\Growwer\Api\Model\ManagedServiceProposalBriefing**](ManagedServiceProposalBriefing.md) |  |
**state_reason** | **string** | Why the proposal reached its state, in your language, such as your comment when you rejected it. |
**order_id** | **string** | The order placed for the proposal (GET /orders/{id}). |
**order_state** | **string** | The state of that order while its purchase is in progress. |
**created_at** | **\DateTime** |  |
**updated_at** | **\DateTime** | When the proposal last changed state. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
