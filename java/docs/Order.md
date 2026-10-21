

# Order


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**reference** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**state** | **String** | The raw state name. GET /orders documents the values its &#x60;state&#x60; filter takes. |  |
|**pendingAction** | [**PendingActionEnum**](#PendingActionEnum) | Who the order is waiting on, or null when it waits on no one. |  |
|**price** | [**Money**](Money.md) | What you pay for the order. |  |
|**project** | [**OrderProject**](OrderProject.md) |  |  |
|**media** | [**OrderMedia**](OrderMedia.md) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** | When the order last changed state. It changes on state changes only, so poll with GET /orders?updatedSince&#x3D; on it. |  |
|**scheduledPublicationDate** | **OffsetDateTime** |  |  |
|**delivery** | [**OrderDelivery**](OrderDelivery.md) |  |  |
|**briefing** | [**OrderBriefing**](OrderBriefing.md) |  |  |
|**draft** | [**OrderDraft**](OrderDraft.md) |  |  |
|**stateHistory** | [**List&lt;OrderStateHistoryInner&gt;**](OrderStateHistoryInner.md) | Every state change, oldest first. |  |
|**channel** | [**OrderChannel**](OrderChannel.md) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| POST | &quot;post&quot; |
| LINK_ADDITION | &quot;link_addition&quot; |



## Enum: PendingActionEnum

| Name | Value |
|---- | -----|
| BUYER | &quot;buyer&quot; |
| SELLER | &quot;seller&quot; |
| GROWWER | &quot;growwer&quot; |



