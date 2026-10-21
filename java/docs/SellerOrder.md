

# SellerOrder

An order placed on one of your medias, as its seller sees it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**reference** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**state** | **String** | The raw state name. GET /seller/orders documents the values its &#x60;state&#x60; filter takes. |  |
|**requiresYourAction** | **Boolean** | Whether the order waits on you, as the seller order list marks it. |  |
|**availableActions** | [**List&lt;AvailableActionsEnum&gt;**](#List&lt;AvailableActionsEnum&gt;) | The seller actions the order allows now. |  |
|**earnings** | [**Money**](Money.md) | What you are paid for the order, credited to your seller wallet once it settles. |  |
|**project** | [**SellerOrderProject**](SellerOrderProject.md) |  |  |
|**media** | [**OrderMedia**](OrderMedia.md) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** | When the order last changed state. It changes on state changes only, so poll with GET /seller/orders?updatedSince&#x3D; on it. |  |
|**scheduledPublicationDate** | **OffsetDateTime** |  |  |
|**delivery** | [**OrderDelivery**](OrderDelivery.md) |  |  |
|**briefing** | [**SellerOrderBriefing**](SellerOrderBriefing.md) |  |  |
|**draft** | [**SellerOrderDraft**](SellerOrderDraft.md) |  |  |
|**stateHistory** | [**List&lt;OrderStateHistoryInner&gt;**](OrderStateHistoryInner.md) | Every state change, oldest first. |  |
|**channel** | [**SellerOrderChannel**](SellerOrderChannel.md) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| POST | &quot;post&quot; |
| LINK_ADDITION | &quot;link_addition&quot; |



## Enum: List&lt;AvailableActionsEnum&gt;

| Name | Value |
|---- | -----|
| ACCEPT | &quot;accept&quot; |
| REJECT | &quot;reject&quot; |
| DELIVER | &quot;deliver&quot; |
| DELIVER_UPDATE | &quot;deliver-update&quot; |
| REFUTE_UPDATE | &quot;refute-update&quot; |
| DELIVER_DRAFT | &quot;deliver-draft&quot; |
| DELIVER_DRAFT_UPDATE | &quot;deliver-draft-update&quot; |
| REFUTE_DRAFT_UPDATE | &quot;refute-draft-update&quot; |



