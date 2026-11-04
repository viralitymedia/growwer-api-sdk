# WebhookEventData

What the event is about: an OrderEventData for the `order.*` events, a BalanceLowEventData for `balance.low` and a WebhookTestEventData for `webhook.test`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**Order**](Order.md) |  | 
**wallet** | [**BalanceLowEventDataWallet**](BalanceLowEventDataWallet.md) |  | 
**threshold** | [**Money**](Money.md) | The subscription&#39;s &#x60;lowBalanceThreshold&#x60; that the balance dropped below. | 
**webhook_id** | **UUID** | The subscription it was sent to. | 

## Example

```python
from growwer.models.webhook_event_data import WebhookEventData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventData from a JSON string
webhook_event_data_instance = WebhookEventData.from_json(json)
# print the JSON string representation of the object
print(WebhookEventData.to_json())

# convert the object into a dict
webhook_event_data_dict = webhook_event_data_instance.to_dict()
# create an instance of WebhookEventData from a dict
webhook_event_data_from_dict = WebhookEventData.from_dict(webhook_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


