# SellerOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**reference** | **string** |  |
**type** | **string** |  |
**state** | **string** | The raw state name. GET /seller/orders documents the values its &#x60;state&#x60; filter takes. |
**requires_your_action** | **bool** | Whether the order waits on you, as the seller order list marks it. |
**available_actions** | **string[]** | The seller actions the order allows now. |
**earnings** | [**\Growwer\Api\Model\Money**](Money.md) | What you are paid for the order, credited to your seller wallet once it settles. |
**project** | [**\Growwer\Api\Model\SellerOrderProject**](SellerOrderProject.md) |  |
**media** | [**\Growwer\Api\Model\OrderMedia**](OrderMedia.md) |  |
**created_at** | **\DateTime** |  |
**updated_at** | **\DateTime** | When the order last changed state. It changes on state changes only, so poll with GET /seller/orders?updatedSince&#x3D; on it. |
**scheduled_publication_date** | **\DateTime** |  |
**delivery** | [**\Growwer\Api\Model\OrderDelivery**](OrderDelivery.md) |  |
**briefing** | [**\Growwer\Api\Model\SellerOrderBriefing**](SellerOrderBriefing.md) |  |
**draft** | [**\Growwer\Api\Model\SellerOrderDraft**](SellerOrderDraft.md) |  |
**state_history** | [**\Growwer\Api\Model\OrderStateHistoryInner[]**](OrderStateHistoryInner.md) | Every state change, oldest first. |
**channel** | [**\Growwer\Api\Model\SellerOrderChannel**](SellerOrderChannel.md) |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
