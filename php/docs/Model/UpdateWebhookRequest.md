# UpdateWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **string** | An HTTPS URL of at most 2048 characters, without a backslash or credentials. Its host is an IP address or a domain name of two labels or more, such as hooks.example.com, with one trailing dot allowed; a single-label host such as localhost is refused (&#x60;validation_failed&#x60; on &#x60;url&#x60;). The host is checked, and resolved at each delivery, in lower case and with a Unicode name in punycode, the form a delivery connects to. | [optional]
**events** | [**\Growwer\Api\Model\WebhookEventType[]**](WebhookEventType.md) | The events to send, at least one; replaces the list. | [optional]
**low_balance_threshold** | [**\Growwer\Api\Model\MoneyOrNull**](MoneyOrNull.md) | With &#x60;balance.low&#x60;: the available buyer balance below which the event fires, in EUR. Null removes it. | [optional]
**description** | **string** | A note of yours, at most 255 characters. Null removes it. | [optional]
**enabled** | **bool** | Whether the subscription gets events. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
