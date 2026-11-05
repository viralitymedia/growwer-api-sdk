# WebhookDeliveryAttempt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempted_at** | **datetime** |  | 
**status_code** | **int** | The HTTP status your endpoint answered, null when it did not answer. Only 2xx succeeds; a redirect is not followed and fails. | 
**duration_ms** | **int** | How long the attempt took, in milliseconds. It gives up after 15 seconds. | 
**response_body** | **str** | Up to the first 1024 bytes of the response body, null when it did not answer. | 
**error** | **str** | Why there is no status, null when it answered. &#x60;address_not_allowed&#x60;, its host resolved to, or connected to, an address that is not public. | 

## Example

```python
from growwer.models.webhook_delivery_attempt import WebhookDeliveryAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryAttempt from a JSON string
webhook_delivery_attempt_instance = WebhookDeliveryAttempt.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryAttempt.to_json())

# convert the object into a dict
webhook_delivery_attempt_dict = webhook_delivery_attempt_instance.to_dict()
# create an instance of WebhookDeliveryAttempt from a dict
webhook_delivery_attempt_from_dict = WebhookDeliveryAttempt.from_dict(webhook_delivery_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


