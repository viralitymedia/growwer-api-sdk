# Growwer.Api.Model.WebhookEventData
What the event is about: an OrderEventData for the `order.*` events, a BalanceLowEventData for `balance.low` and a WebhookTestEventData for `webhook.test`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Order** | [**Order**](Order.md) |  | 
**Wallet** | [**BalanceLowEventDataWallet**](BalanceLowEventDataWallet.md) |  | 
**Threshold** | [**Money**](Money.md) | The subscription&#39;s &#x60;lowBalanceThreshold&#x60; that the balance dropped below. | 
**WebhookId** | **Guid** | The subscription it was sent to. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

