

# CreateWebhookRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **URI** | An HTTPS URL of at most 2048 characters, without a backslash or credentials. Its host is an IP address or a domain name of two labels or more, such as hooks.example.com, with one trailing dot allowed; a single-label host such as localhost is refused (&#x60;validation_failed&#x60; on &#x60;url&#x60;). The host is checked, and resolved at each delivery, in lower case and with a Unicode name in punycode, the form a delivery connects to. |  |
|**events** | **Set&lt;WebhookEventType&gt;** | The events to send, at least one. |  |
|**lowBalanceThreshold** | [**Money**](Money.md) | With &#x60;balance.low&#x60;: the available buyer balance below which the event fires, in EUR. |  [optional] |
|**description** | **String** | A note of yours, at most 255 characters. |  [optional] |



