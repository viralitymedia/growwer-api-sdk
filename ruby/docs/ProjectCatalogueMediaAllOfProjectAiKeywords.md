# Growwer::ProjectCatalogueMediaAllOfProjectAiKeywords

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **keyword** | **String** |  |  |
| **source** | **String** | The AI engine that gave the keyword, as the &#x60;ranksAiKeyword&#x60; filter names it, or null for an engine it does not name. It is never where the media comes from. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::ProjectCatalogueMediaAllOfProjectAiKeywords.new(
  keyword: null,
  source: null
)
```

