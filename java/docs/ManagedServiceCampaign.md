

# ManagedServiceCampaign

A campaign your managed service runs for you. Every figure about proposals counts only those you can see (not the ones the team is still preparing).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**name** | **String** |  |  |
|**state** | [**StateEnum**](#StateEnum) | &#x60;proposal_delivered&#x60;: proposals await your review. &#x60;proposal_changes_requested&#x60;: you rejected some and the team is preparing others. &#x60;proposal_accepted&#x60;: none awaits your review and the team is placing the orders. |  |
|**deadline** | **OffsetDateTime** |  |  |
|**budget** | [**Money**](Money.md) |  |  |
|**project** | [**ManagedServiceCampaignProject**](ManagedServiceCampaignProject.md) |  |  |
|**strategy** | [**ManagedServiceCampaignStrategy**](ManagedServiceCampaignStrategy.md) |  |  |
|**proposalCounts** | [**ManagedServiceCampaignProposalCounts**](ManagedServiceCampaignProposalCounts.md) |  |  |
|**proposalsTotal** | [**Money**](Money.md) | The current price of every proposal not cancelled, as the campaign page totals it. |  |
|**budgetExceededBy** | [**MoneyOrNull**](MoneyOrNull.md) | How far &#x60;proposalsTotal&#x60; goes beyond the budget; null within it. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** | When the campaign last changed state. |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING_PROPOSAL_DELIVERY | &quot;pending_proposal_delivery&quot; |
| PROPOSAL_DELIVERED | &quot;proposal_delivered&quot; |
| PROPOSAL_CHANGES_REQUESTED | &quot;proposal_changes_requested&quot; |
| PROPOSAL_ACCEPTED | &quot;proposal_accepted&quot; |
| FINISHED | &quot;finished&quot; |



