# Growwer::UpdateWebhookRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **url** | **String** | An HTTPS URL of at most 2048 characters, without a backslash or credentials. Its host is an IP address or a domain name of two labels or more, such as hooks.example.com, with one trailing dot allowed; a single-label host such as localhost is refused (&#x60;validation_failed&#x60; on &#x60;url&#x60;). The host is checked, and resolved at each delivery, in lower case and with a Unicode name in punycode, the form a delivery connects to. | [optional] |
| **events** | [**Array&lt;WebhookEventType&gt;**](WebhookEventType.md) | The events to send, at least one; replaces the list. | [optional] |
| **low_balance_threshold** | [**MoneyOrNull**](MoneyOrNull.md) | With &#x60;balance.low&#x60;: the available buyer balance below which the event fires, in EUR. Null removes it. | [optional] |
| **description** | **String** | A note of yours, at most 255 characters. Null removes it. | [optional] |
| **enabled** | **Boolean** | Whether the subscription gets events. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::UpdateWebhookRequest.new(
  url: null,
  events: null,
  low_balance_threshold: null,
  description: null,
  enabled: null
)
```

