# ManagedServiceCampaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**name** | **string** |  |
**state** | **string** | &#x60;proposal_delivered&#x60;: proposals await your review. &#x60;proposal_changes_requested&#x60;: you rejected some and the team is preparing others. &#x60;proposal_accepted&#x60;: none awaits your review and the team is placing the orders. |
**deadline** | **\DateTime** |  |
**budget** | [**\Growwer\Api\Model\Money**](Money.md) |  |
**project** | [**\Growwer\Api\Model\ManagedServiceCampaignProject**](ManagedServiceCampaignProject.md) |  |
**strategy** | [**\Growwer\Api\Model\ManagedServiceCampaignStrategy**](ManagedServiceCampaignStrategy.md) |  |
**proposal_counts** | [**\Growwer\Api\Model\ManagedServiceCampaignProposalCounts**](ManagedServiceCampaignProposalCounts.md) |  |
**proposals_total** | [**\Growwer\Api\Model\Money**](Money.md) | The current price of every proposal not cancelled, as the campaign page totals it. |
**budget_exceeded_by** | [**\Growwer\Api\Model\MoneyOrNull**](MoneyOrNull.md) | How far &#x60;proposalsTotal&#x60; goes beyond the budget; null within it. |
**created_at** | **\DateTime** |  |
**updated_at** | **\DateTime** | When the campaign last changed state. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
