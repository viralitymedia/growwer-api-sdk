# WebhookDelivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**event_id** | **string** | The event&#39;s id, sent as &#x60;webhook-id&#x60; on every attempt and redelivery. |
**event_type** | **string** |  |
**status** | **string** | &#x60;pending&#x60; while it is sent or retried, &#x60;succeeded&#x60; once an attempt got a 2xx, &#x60;failed&#x60; once the retries ran out, the endpoint answered 410 or the subscription was disabled. |
**attempt_count** | **int** | How many attempts it took, redeliveries included. |
**next_attempt_at** | **\DateTime** | When the next retry is due, null when none is. |
**created_at** | **\DateTime** |  |
**attempts** | [**\Growwer\Api\Model\WebhookDeliveryAttempt[]**](WebhookDeliveryAttempt.md) | The latest 10 attempts, newest first. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
