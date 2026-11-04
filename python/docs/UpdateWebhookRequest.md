# UpdateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | An HTTPS URL of at most 2048 characters, without a backslash or credentials. Its host is an IP address or a domain name of two labels or more, such as hooks.example.com, with one trailing dot allowed; a single-label host such as localhost is refused (&#x60;validation_failed&#x60; on &#x60;url&#x60;). The host is checked, and resolved at each delivery, in lower case and with a Unicode name in punycode, the form a delivery connects to. | [optional] 
**events** | [**List[WebhookEventType]**](WebhookEventType.md) | The events to send, at least one; replaces the list. | [optional] 
**low_balance_threshold** | [**MoneyOrNull**](MoneyOrNull.md) | With &#x60;balance.low&#x60;: the available buyer balance below which the event fires, in EUR. Null removes it. | [optional] 
**description** | **str** | A note of yours, at most 255 characters. Null removes it. | [optional] 
**enabled** | **bool** | Whether the subscription gets events. | [optional] 

## Example

```python
from growwer.models.update_webhook_request import UpdateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookRequest from a JSON string
update_webhook_request_instance = UpdateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookRequest.to_json())

# convert the object into a dict
update_webhook_request_dict = update_webhook_request_instance.to_dict()
# create an instance of UpdateWebhookRequest from a dict
update_webhook_request_from_dict = UpdateWebhookRequest.from_dict(update_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


