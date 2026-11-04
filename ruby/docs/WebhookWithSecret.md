# Growwer::WebhookWithSecret

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **url** | **String** |  |  |
| **events** | [**Array&lt;WebhookEventType&gt;**](WebhookEventType.md) |  |  |
| **low_balance_threshold** | [**MoneyOrNull**](MoneyOrNull.md) | With &#x60;balance.low&#x60;, the available buyer balance below which it fires; null otherwise. |  |
| **description** | **String** |  |  |
| **enabled** | **Boolean** | Whether the subscription gets events. |  |
| **disabled_reason** | **String** | Why it is disabled, null while enabled. &#x60;by_user&#x60;, through PATCH /webhooks/{id}; &#x60;endpoint_gone&#x60;, its endpoint answered 410; &#x60;failing&#x60;, every delivery failed for 5 days, and the account owner was emailed. |  |
| **failing_since** | **Time** | Since when its deliveries have failed without one succeeding, null while they succeed. At 5 days it is disabled. The check runs at each failed attempt, so a subscription whose &#x60;failingSince&#x60; is already more than 5 days old, say one that had no event for a while, is disabled at its next failed attempt, without the retries that delivery would otherwise get. |  |
| **previous_secret_expires_at** | **Time** | Until when the secret replaced by the last rotation still signs beside the new one, null when it no longer does. |  |
| **created_at** | **Time** |  |  |
| **updated_at** | **Time** |  |  |
| **secret** | **String** | The signing secret, &#x60;whsec_&#x60; and the base64 of 32 random bytes. Shown only in this answer, and absent when the request is replayed under its &#x60;Idempotency-Key&#x60; (or the MCP tool under its &#x60;requestId&#x60;), since the secret is never stored. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::WebhookWithSecret.new(
  id: null,
  url: null,
  events: null,
  low_balance_threshold: null,
  description: null,
  enabled: null,
  disabled_reason: null,
  failing_since: null,
  previous_secret_expires_at: null,
  created_at: null,
  updated_at: null,
  secret: whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw
)
```

