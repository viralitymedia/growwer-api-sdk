# Growwer::WebhookDeliveryAttempt

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attempted_at** | **Time** |  |  |
| **status_code** | **Integer** | The HTTP status your endpoint answered, null when it did not answer. Only 2xx succeeds; a redirect is not followed and fails. |  |
| **duration_ms** | **Integer** | How long the attempt took, in milliseconds. It gives up after 15 seconds. |  |
| **response_body** | **String** | Up to the first 1024 bytes of the response body, null when it did not answer. |  |
| **error** | **String** | Why there is no status, null when it answered. &#x60;address_not_allowed&#x60;, its host resolved to, or connected to, an address that is not public. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::WebhookDeliveryAttempt.new(
  attempted_at: null,
  status_code: null,
  duration_ms: null,
  response_body: null,
  error: null
)
```

