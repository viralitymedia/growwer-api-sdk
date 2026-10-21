# Growwer::SellerPostOrderBriefing

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **title** | **String** |  |  |
| **language** | **String** | The language code of the article. |  |
| **links** | [**Array&lt;OrderLink&gt;**](OrderLink.md) |  |  |
| **extra_services** | **Array&lt;String&gt;** |  |  |
| **additional_info** | **String** |  |  |
| **written_by** | **String** | Who writes the article; &#x60;seller&#x60; means you do. |  |
| **has_proposed_draft** | **Boolean** | Whether the buyer attached a draft; GET /seller/orders/{id}/briefing downloads it. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerPostOrderBriefing.new(
  title: null,
  language: null,
  links: null,
  extra_services: null,
  additional_info: null,
  written_by: null,
  has_proposed_draft: null
)
```

