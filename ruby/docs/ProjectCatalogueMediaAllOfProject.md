# Growwer::ProjectCatalogueMediaAllOfProject

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **favourite** | **Boolean** |  |  |
| **discarded** | **Boolean** |  |  |
| **requested** | **Boolean** |  |  |
| **recommended** | **Boolean** | Growwer recommends the media for the project. |  |
| **bought** | **Boolean** | You have ordered on the media for the project. |  |
| **new** | **Boolean** | Growwer matched the media with the project recently. |  |
| **ai_keywords** | [**Array&lt;ProjectCatalogueMediaAllOfProjectAiKeywords&gt;**](ProjectCatalogueMediaAllOfProjectAiKeywords.md) | The AI keywords the web lists for the media in this project, one entry per keyword of each stored source, empty when there are none. Keywords an AI answer gave without referencing any domain may be listed for every media of the project, so an entry does not mean that the engine cited the media. Entries keep their order within an engine, and a keyword listed by two engines appears once for each; the order of the engines is not promised. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::ProjectCatalogueMediaAllOfProject.new(
  favourite: null,
  discarded: null,
  requested: null,
  recommended: null,
  bought: null,
  new: null,
  ai_keywords: null
)
```

