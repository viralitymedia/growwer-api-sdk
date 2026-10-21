# Growwer.Api.Model.SellerOrder
An order placed on one of your medias, as its seller sees it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Reference** | **string** |  | 
**Type** | **string** |  | 
**State** | **string** | The raw state name. GET /seller/orders documents the values its &#x60;state&#x60; filter takes. | 
**RequiresYourAction** | **bool** | Whether the order waits on you, as the seller order list marks it. | 
**AvailableActions** | **List&lt;SellerOrder.AvailableActionsEnum&gt;** | The seller actions the order allows now. | 
**Earnings** | [**Money**](Money.md) | What you are paid for the order, credited to your seller wallet once it settles. | 
**Project** | [**SellerOrderProject**](SellerOrderProject.md) |  | 
**Media** | [**OrderMedia**](OrderMedia.md) |  | 
**CreatedAt** | **DateTime** |  | 
**UpdatedAt** | **DateTime** | When the order last changed state. It changes on state changes only, so poll with GET /seller/orders?updatedSince&#x3D; on it. | 
**ScheduledPublicationDate** | **DateTime?** |  | 
**Delivery** | [**OrderDelivery**](OrderDelivery.md) |  | 
**Briefing** | [**SellerOrderBriefing**](SellerOrderBriefing.md) |  | 
**Draft** | [**SellerOrderDraft**](SellerOrderDraft.md) |  | 
**StateHistory** | [**List&lt;OrderStateHistoryInner&gt;**](OrderStateHistoryInner.md) | Every state change, oldest first. | 
**Channel** | [**SellerOrderChannel**](SellerOrderChannel.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

