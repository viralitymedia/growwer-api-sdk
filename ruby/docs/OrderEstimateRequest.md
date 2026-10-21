# Growwer::OrderEstimateRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **type** | **String** |  |  |
| **project_id** | **String** | One of your projects. |  |
| **media_id** | **String** | A media you can order for the project (GET /projects/{id}/medias). |  |
| **briefing** | [**OrderEstimateRequestBriefing**](OrderEstimateRequestBriefing.md) |  |  |
| **scheduled_publication_date** | **Date** | The day to publish on, at least a few days ahead as the web requires. | [optional] |
| **draft_reviewable** | **Boolean** | Whether you review the draft before it is published. Defaults to false. | [optional] |
| **proposed_draft_file_id** | **String** | A file uploaded with POST /files to propose your own draft. The estimate checks it without using it up. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::OrderEstimateRequest.new(
  type: null,
  project_id: null,
  media_id: null,
  briefing: null,
  scheduled_publication_date: null,
  draft_reviewable: null,
  proposed_draft_file_id: null
)
```

