# Growwer.Api.Model.Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Reference** | **string** |  | 
**Type** | **string** |  | 
**State** | **string** | The raw state name. GET /orders documents the values its &#x60;state&#x60; filter takes. | 
**PendingAction** | **string** | Who the order is waiting on, or null when it waits on no one. | 
**Price** | [**Money**](Money.md) | What you pay for the order. | 
**Project** | [**OrderProject**](OrderProject.md) |  | 
**Media** | [**OrderMedia**](OrderMedia.md) |  | 
**CreatedAt** | **DateTime** |  | 
**UpdatedAt** | **DateTime** | When the order last changed state. It changes on state changes only, so poll with GET /orders?updatedSince&#x3D; on it. | 
**ScheduledPublicationDate** | **DateTime?** |  | 
**Delivery** | [**OrderDelivery**](OrderDelivery.md) |  | 
**Briefing** | [**OrderBriefing**](OrderBriefing.md) |  | 
**Draft** | [**OrderDraft**](OrderDraft.md) |  | 
**StateHistory** | [**List&lt;OrderStateHistoryInner&gt;**](OrderStateHistoryInner.md) | Every state change, oldest first. | 
**Channel** | [**OrderChannel**](OrderChannel.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

