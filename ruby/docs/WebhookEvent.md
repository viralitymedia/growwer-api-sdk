# Growwer::WebhookEvent

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **type** | **String** |  |  |
| **created_at** | **Time** |  |  |
| **api_version** | **String** |  |  |
| **mode** | **String** | The mode of the subscription it is sent to. |  |
| **data** | [**WebhookEventData**](WebhookEventData.md) |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::WebhookEvent.new(
  id: null,
  type: null,
  created_at: null,
  api_version: null,
  mode: null,
  data: null
)
```

