# OrderCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **string** |  |
**project_id** | **string** | One of your projects. |
**media_id** | **string** | A media you can order for the project (GET /projects/{id}/medias). |
**briefing** | [**\Growwer\Api\Model\OrderEstimateRequestBriefing**](OrderEstimateRequestBriefing.md) |  |
**scheduled_publication_date** | **\DateTime** | The day to publish on, at least a few days ahead as the web requires. | [optional]
**draft_reviewable** | **bool** | Whether you review the draft before it is published. Defaults to false. | [optional]
**proposed_draft_file_id** | **string** | A file uploaded with POST /files to propose your own draft. The estimate checks it without using it up. | [optional]
**expected_price** | [**\Growwer\Api\Model\Money**](Money.md) | The &#x60;price&#x60; POST /orders/estimate answered. Only EUR is accepted. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
