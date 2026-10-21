

# OrderCreateRequest

An order to place, with the price you expect to pay.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**projectId** | **UUID** | One of your projects. |  |
|**mediaId** | **UUID** | A media you can order for the project (GET /projects/{id}/medias). |  |
|**briefing** | [**OrderEstimateRequestBriefing**](OrderEstimateRequestBriefing.md) |  |  |
|**scheduledPublicationDate** | **LocalDate** | The day to publish on, at least a few days ahead as the web requires. |  [optional] |
|**draftReviewable** | **Boolean** | Whether you review the draft before it is published. Defaults to false. |  [optional] |
|**proposedDraftFileId** | **UUID** | A file uploaded with POST /files to propose your own draft. The estimate checks it without using it up. |  [optional] |
|**expectedPrice** | [**Money**](Money.md) | The &#x60;price&#x60; POST /orders/estimate answered. Only EUR is accepted. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| POST | &quot;post&quot; |
| LINK_ADDITION | &quot;link_addition&quot; |



