# Growwer::WebhookDelivery

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **event_id** | **String** | The event&#39;s id, sent as &#x60;webhook-id&#x60; on every attempt and redelivery. |  |
| **event_type** | **String** |  |  |
| **status** | **String** | &#x60;pending&#x60; while it is sent or retried, &#x60;succeeded&#x60; once an attempt got a 2xx, &#x60;failed&#x60; once the retries ran out, the endpoint answered 410 or the subscription was disabled. |  |
| **attempt_count** | **Integer** | How many attempts it took, redeliveries included. |  |
| **next_attempt_at** | **Time** | When the next retry is due, null when none is. |  |
| **created_at** | **Time** |  |  |
| **attempts** | [**Array&lt;WebhookDeliveryAttempt&gt;**](WebhookDeliveryAttempt.md) | The latest 10 attempts, newest first. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::WebhookDelivery.new(
  id: null,
  event_id: null,
  event_type: null,
  status: null,
  attempt_count: null,
  next_attempt_at: null,
  created_at: null,
  attempts: null
)
```

