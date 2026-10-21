# Growwer::ManagedServiceCampaignStrategy

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **goal** | **String** |  |  |
| **countries** | **Array&lt;String&gt;** | ISO 3166-1 alpha-2 codes. |  |
| **languages** | **Array&lt;String&gt;** |  |  |
| **topics** | **Array&lt;Integer&gt;** | Topic ids, as GET /vocabulary lists them. |  |
| **definition** | **String** |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::ManagedServiceCampaignStrategy.new(
  goal: null,
  countries: null,
  languages: null,
  topics: null,
  definition: null
)
```

