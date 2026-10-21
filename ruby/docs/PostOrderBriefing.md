# Growwer::PostOrderBriefing

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **title** | **String** |  |  |
| **language** | **String** | The language code of the article. |  |
| **links** | [**Array&lt;OrderLink&gt;**](OrderLink.md) |  |  |
| **extra_services** | **Array&lt;String&gt;** |  |  |
| **additional_info** | **String** |  |  |
| **has_proposed_draft** | **Boolean** | Whether you attached your own draft; GET /orders/{id}/briefing downloads it. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::PostOrderBriefing.new(
  title: null,
  language: null,
  links: null,
  extra_services: null,
  additional_info: null,
  has_proposed_draft: null
)
```

