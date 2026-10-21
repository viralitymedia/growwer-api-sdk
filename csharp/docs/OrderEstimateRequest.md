# Growwer.Api.Model.OrderEstimateRequest
An order to price. `scheduledPublicationDate`, `draftReviewable` and `proposedDraftFileId` apply to a post order only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | 
**ProjectId** | **Guid** | One of your projects. | 
**MediaId** | **Guid** | A media you can order for the project (GET /projects/{id}/medias). | 
**Briefing** | [**OrderEstimateRequestBriefing**](OrderEstimateRequestBriefing.md) |  | 
**ScheduledPublicationDate** | **DateOnly** | The day to publish on, at least a few days ahead as the web requires. | [optional] 
**DraftReviewable** | **bool** | Whether you review the draft before it is published. Defaults to false. | [optional] 
**ProposedDraftFileId** | **Guid** | A file uploaded with POST /files to propose your own draft. The estimate checks it without using it up. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

