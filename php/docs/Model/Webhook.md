# Webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**url** | **string** |  |
**events** | [**\Growwer\Api\Model\WebhookEventType[]**](WebhookEventType.md) |  |
**low_balance_threshold** | [**\Growwer\Api\Model\MoneyOrNull**](MoneyOrNull.md) | With &#x60;balance.low&#x60;, the available buyer balance below which it fires; null otherwise. |
**description** | **string** |  |
**enabled** | **bool** | Whether the subscription gets events. |
**disabled_reason** | **string** | Why it is disabled, null while enabled. &#x60;by_user&#x60;, through PATCH /webhooks/{id}; &#x60;endpoint_gone&#x60;, its endpoint answered 410; &#x60;failing&#x60;, every delivery failed for 5 days, and the account owner was emailed. |
**failing_since** | **\DateTime** | Since when its deliveries have failed without one succeeding, null while they succeed. At 5 days it is disabled. The check runs at each failed attempt, so a subscription whose &#x60;failingSince&#x60; is already more than 5 days old, say one that had no event for a while, is disabled at its next failed attempt, without the retries that delivery would otherwise get. |
**previous_secret_expires_at** | **\DateTime** | Until when the secret replaced by the last rotation still signs beside the new one, null when it no longer does. |
**created_at** | **\DateTime** |  |
**updated_at** | **\DateTime** |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
