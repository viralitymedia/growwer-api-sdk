# Growwer::ManagedServiceRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_url** | **String** | The website the campaign is for. |  |
| **goal** | **String** |  |  |
| **country** | **String** | ISO 3166-1 alpha-2 code of the target country. |  |
| **duration** | **String** |  |  |
| **estimated_budget** | [**Money**](Money.md) | At least 500 EUR. Only EUR is accepted. |  |
| **additional_info** | **String** |  | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::ManagedServiceRequest.new(
  project_url: null,
  goal: null,
  country: null,
  duration: null,
  estimated_budget: null,
  additional_info: null
)
```

