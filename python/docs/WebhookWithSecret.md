# WebhookWithSecret

A subscription with its signing secret, which only create and rotate-secret answer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**url** | **str** |  | 
**events** | [**List[WebhookEventType]**](WebhookEventType.md) |  | 
**low_balance_threshold** | [**MoneyOrNull**](MoneyOrNull.md) | With &#x60;balance.low&#x60;, the available buyer balance below which it fires; null otherwise. | 
**description** | **str** |  | 
**enabled** | **bool** | Whether the subscription gets events. | 
**disabled_reason** | **str** | Why it is disabled, null while enabled. &#x60;by_user&#x60;, through PATCH /webhooks/{id}; &#x60;endpoint_gone&#x60;, its endpoint answered 410; &#x60;failing&#x60;, every delivery failed for 5 days, and the account owner was emailed. | 
**failing_since** | **datetime** | Since when its deliveries have failed without one succeeding, null while they succeed. At 5 days it is disabled. The check runs at each failed attempt, so a subscription whose &#x60;failingSince&#x60; is already more than 5 days old, say one that had no event for a while, is disabled at its next failed attempt, without the retries that delivery would otherwise get. | 
**previous_secret_expires_at** | **datetime** | Until when the secret replaced by the last rotation still signs beside the new one, null when it no longer does. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**secret** | **str** | The signing secret, &#x60;whsec_&#x60; and the base64 of 32 random bytes. Shown only in this answer, and absent when the request is replayed under its &#x60;Idempotency-Key&#x60; (or the MCP tool under its &#x60;requestId&#x60;), since the secret is never stored. | [optional] 

## Example

```python
from growwer.models.webhook_with_secret import WebhookWithSecret

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWithSecret from a JSON string
webhook_with_secret_instance = WebhookWithSecret.from_json(json)
# print the JSON string representation of the object
print(WebhookWithSecret.to_json())

# convert the object into a dict
webhook_with_secret_dict = webhook_with_secret_instance.to_dict()
# create an instance of WebhookWithSecret from a dict
webhook_with_secret_from_dict = WebhookWithSecret.from_dict(webhook_with_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


