# Growwer.Api.Model.WebhookDelivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**EventId** | **Guid** | The event&#39;s id, sent as &#x60;webhook-id&#x60; on every attempt and redelivery. | 
**EventType** | **string** |  | 
**Status** | **string** | &#x60;pending&#x60; while it is sent or retried, &#x60;succeeded&#x60; once an attempt got a 2xx, &#x60;failed&#x60; once the retries ran out, the endpoint answered 410 or the subscription was disabled. | 
**AttemptCount** | **int** | How many attempts it took, redeliveries included. | 
**NextAttemptAt** | **DateTime?** | When the next retry is due, null when none is. | 
**CreatedAt** | **DateTime** |  | 
**Attempts** | [**List&lt;WebhookDeliveryAttempt&gt;**](WebhookDeliveryAttempt.md) | The latest 10 attempts, newest first. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

