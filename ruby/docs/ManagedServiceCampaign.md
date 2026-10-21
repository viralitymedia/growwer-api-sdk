# Growwer::ManagedServiceCampaign

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **name** | **String** |  |  |
| **state** | **String** | &#x60;proposal_delivered&#x60;: proposals await your review. &#x60;proposal_changes_requested&#x60;: you rejected some and the team is preparing others. &#x60;proposal_accepted&#x60;: none awaits your review and the team is placing the orders. |  |
| **deadline** | **Time** |  |  |
| **budget** | [**Money**](Money.md) |  |  |
| **project** | [**ManagedServiceCampaignProject**](ManagedServiceCampaignProject.md) |  |  |
| **strategy** | [**ManagedServiceCampaignStrategy**](ManagedServiceCampaignStrategy.md) |  |  |
| **proposal_counts** | [**ManagedServiceCampaignProposalCounts**](ManagedServiceCampaignProposalCounts.md) |  |  |
| **proposals_total** | [**Money**](Money.md) | The current price of every proposal not cancelled, as the campaign page totals it. |  |
| **budget_exceeded_by** | [**MoneyOrNull**](MoneyOrNull.md) | How far &#x60;proposalsTotal&#x60; goes beyond the budget; null within it. |  |
| **created_at** | **Time** |  |  |
| **updated_at** | **Time** | When the campaign last changed state. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::ManagedServiceCampaign.new(
  id: null,
  name: null,
  state: null,
  deadline: null,
  budget: null,
  project: null,
  strategy: null,
  proposal_counts: null,
  proposals_total: null,
  budget_exceeded_by: null,
  created_at: null,
  updated_at: null
)
```

