# Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**reference** | **string** |  |
**type** | **string** |  |
**state** | **string** | The raw state name. GET /orders documents the values its &#x60;state&#x60; filter takes. |
**pending_action** | **string** | Who the order is waiting on, or null when it waits on no one. |
**price** | [**\Growwer\Api\Model\Money**](Money.md) | What you pay for the order. |
**project** | [**\Growwer\Api\Model\OrderProject**](OrderProject.md) |  |
**media** | [**\Growwer\Api\Model\OrderMedia**](OrderMedia.md) |  |
**created_at** | **\DateTime** |  |
**updated_at** | **\DateTime** | When the order last changed state. It changes on state changes only, so poll with GET /orders?updatedSince&#x3D; on it. |
**scheduled_publication_date** | **\DateTime** |  |
**delivery** | [**\Growwer\Api\Model\OrderDelivery**](OrderDelivery.md) |  |
**briefing** | [**\Growwer\Api\Model\OrderBriefing**](OrderBriefing.md) |  |
**draft** | [**\Growwer\Api\Model\OrderDraft**](OrderDraft.md) |  |
**state_history** | [**\Growwer\Api\Model\OrderStateHistoryInner[]**](OrderStateHistoryInner.md) | Every state change, oldest first. |
**channel** | [**\Growwer\Api\Model\OrderChannel**](OrderChannel.md) |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
