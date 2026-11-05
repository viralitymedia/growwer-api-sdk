

# WebhookEventData

What the event is about: an OrderEventData for the `order.*` events, a BalanceLowEventData for `balance.low` and a WebhookTestEventData for `webhook.test`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**order** | [**Order**](Order.md) |  |  |
|**wallet** | [**BalanceLowEventDataWallet**](BalanceLowEventDataWallet.md) |  |  |
|**threshold** | [**Money**](Money.md) | The subscription&#39;s &#x60;lowBalanceThreshold&#x60; that the balance dropped below. |  |
|**webhookId** | **UUID** | The subscription it was sent to. |  |



