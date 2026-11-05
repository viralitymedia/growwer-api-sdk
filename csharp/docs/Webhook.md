# Growwer.Api.Model.Webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Url** | **string** |  | 
**Events** | [**List&lt;WebhookEventType&gt;**](WebhookEventType.md) |  | 
**LowBalanceThreshold** | [**MoneyOrNull**](MoneyOrNull.md) | With &#x60;balance.low&#x60;, the available buyer balance below which it fires; null otherwise. | 
**Description** | **string** |  | 
**Enabled** | **bool** | Whether the subscription gets events. | 
**DisabledReason** | **string** | Why it is disabled, null while enabled. &#x60;by_user&#x60;, through PATCH /webhooks/{id}; &#x60;endpoint_gone&#x60;, its endpoint answered 410; &#x60;failing&#x60;, every delivery failed for 5 days, and the account owner was emailed. | 
**FailingSince** | **DateTime?** | Since when its deliveries have failed without one succeeding, null while they succeed. At 5 days it is disabled. The check runs at each failed attempt, so a subscription whose &#x60;failingSince&#x60; is already more than 5 days old, say one that had no event for a while, is disabled at its next failed attempt, without the retries that delivery would otherwise get. | 
**PreviousSecretExpiresAt** | **DateTime?** | Until when the secret replaced by the last rotation still signs beside the new one, null when it no longer does. | 
**CreatedAt** | **DateTime** |  | 
**UpdatedAt** | **DateTime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

