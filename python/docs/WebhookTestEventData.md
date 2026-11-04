# WebhookTestEventData

The `data` of a `webhook.test` event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **UUID** | The subscription it was sent to. | 

## Example

```python
from growwer.models.webhook_test_event_data import WebhookTestEventData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTestEventData from a JSON string
webhook_test_event_data_instance = WebhookTestEventData.from_json(json)
# print the JSON string representation of the object
print(WebhookTestEventData.to_json())

# convert the object into a dict
webhook_test_event_data_dict = webhook_test_event_data_instance.to_dict()
# create an instance of WebhookTestEventData from a dict
webhook_test_event_data_from_dict = WebhookTestEventData.from_dict(webhook_test_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


