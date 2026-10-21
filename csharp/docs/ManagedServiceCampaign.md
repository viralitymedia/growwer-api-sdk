# Growwer.Api.Model.ManagedServiceCampaign
A campaign your managed service runs for you. Every figure about proposals counts only those you can see (not the ones the team is still preparing).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Name** | **string** |  | 
**State** | **string** | &#x60;proposal_delivered&#x60;: proposals await your review. &#x60;proposal_changes_requested&#x60;: you rejected some and the team is preparing others. &#x60;proposal_accepted&#x60;: none awaits your review and the team is placing the orders. | 
**Deadline** | **DateTime** |  | 
**Budget** | [**Money**](Money.md) |  | 
**Project** | [**ManagedServiceCampaignProject**](ManagedServiceCampaignProject.md) |  | 
**Strategy** | [**ManagedServiceCampaignStrategy**](ManagedServiceCampaignStrategy.md) |  | 
**ProposalCounts** | [**ManagedServiceCampaignProposalCounts**](ManagedServiceCampaignProposalCounts.md) |  | 
**ProposalsTotal** | [**Money**](Money.md) | The current price of every proposal not cancelled, as the campaign page totals it. | 
**BudgetExceededBy** | [**MoneyOrNull**](MoneyOrNull.md) | How far &#x60;proposalsTotal&#x60; goes beyond the budget; null within it. | 
**CreatedAt** | **DateTime** |  | 
**UpdatedAt** | **DateTime** | When the campaign last changed state. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

