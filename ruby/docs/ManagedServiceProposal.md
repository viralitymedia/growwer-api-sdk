# Growwer::ManagedServiceProposal

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **state** | **String** | &#x60;proposed&#x60; awaits your review. &#x60;accepted&#x60; awaits the order the team places for you. &#x60;purchase_started&#x60; and &#x60;purchase_finished&#x60; follow that order. |  |
| **media** | [**ManagedServiceProposalMedia**](ManagedServiceProposalMedia.md) |  |  |
| **service** | **String** |  |  |
| **proposed_price** | [**Money**](Money.md) | The price the proposal was made at, the one the summary PDF shows. |  |
| **current_price** | [**MoneyOrNull**](MoneyOrNull.md) | What the media charges for the service today; null when it no longer offers it. |  |
| **briefing** | [**ManagedServiceProposalBriefing**](ManagedServiceProposalBriefing.md) |  |  |
| **state_reason** | **String** | Why the proposal reached its state, in your language, such as your comment when you rejected it. |  |
| **order_id** | **String** | The order placed for the proposal (GET /orders/{id}). |  |
| **order_state** | **String** | The state of that order while its purchase is in progress. |  |
| **created_at** | **Time** |  |  |
| **updated_at** | **Time** | When the proposal last changed state. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::ManagedServiceProposal.new(
  id: null,
  state: null,
  media: null,
  service: null,
  proposed_price: null,
  current_price: null,
  briefing: null,
  state_reason: null,
  order_id: null,
  order_state: null,
  created_at: null,
  updated_at: null
)
```

