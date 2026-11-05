# WebhookDelivery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**event_id** | **UUID** | The event&#39;s id, sent as &#x60;webhook-id&#x60; on every attempt and redelivery. | 
**event_type** | **str** |  | 
**status** | **str** | &#x60;pending&#x60; while it is sent or retried, &#x60;succeeded&#x60; once an attempt got a 2xx, &#x60;failed&#x60; once the retries ran out, the endpoint answered 410 or the subscription was disabled. | 
**attempt_count** | **int** | How many attempts it took, redeliveries included. | 
**next_attempt_at** | **datetime** | When the next retry is due, null when none is. | 
**created_at** | **datetime** |  | 
**attempts** | [**List[WebhookDeliveryAttempt]**](WebhookDeliveryAttempt.md) | The latest 10 attempts, newest first. | 

## Example

```python
from growwer.models.webhook_delivery import WebhookDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDelivery from a JSON string
webhook_delivery_instance = WebhookDelivery.from_json(json)
# print the JSON string representation of the object
print(WebhookDelivery.to_json())

# convert the object into a dict
webhook_delivery_dict = webhook_delivery_instance.to_dict()
# create an instance of WebhookDelivery from a dict
webhook_delivery_from_dict = WebhookDelivery.from_dict(webhook_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


