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

## Example

```ruby
require 'growwer'

instance = Growwer::ProjectCatalogueMediaAllOfProject.new(
  favourite: null,
  discarded: null,
  requested: null,
  recommended: null,
  bought: null,
  new: null
)
```

