# OrderEstimateRequest

An order to price. `scheduledPublicationDate`, `draftReviewable` and `proposedDraftFileId` apply to a post order only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **UUID** | One of your projects. | 
**media_id** | **UUID** | A media you can order for the project (GET /projects/{id}/medias). | 
**briefing** | [**OrderEstimateRequestBriefing**](OrderEstimateRequestBriefing.md) |  | 
**scheduled_publication_date** | **date** | The day to publish on, at least a few days ahead as the web requires. | [optional] 
**draft_reviewable** | **bool** | Whether you review the draft before it is published. Defaults to false. | [optional] 
**proposed_draft_file_id** | **UUID** | A file uploaded with POST /files to propose your own draft. The estimate checks it without using it up. | [optional] 

## Example

```python
from growwer.models.order_estimate_request import OrderEstimateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderEstimateRequest from a JSON string
order_estimate_request_instance = OrderEstimateRequest.from_json(json)
# print the JSON string representation of the object
print(OrderEstimateRequest.to_json())

# convert the object into a dict
order_estimate_request_dict = order_estimate_request_instance.to_dict()
# create an instance of OrderEstimateRequest from a dict
order_estimate_request_from_dict = OrderEstimateRequest.from_dict(order_estimate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


