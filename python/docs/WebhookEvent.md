# WebhookEvent

What Growwer POSTs to a subscription's URL. OpenAPI 3.0, which this document follows, has no `webhooks` section: `x-webhooks` lists each event in the shape of OpenAPI 3.1's, with this envelope and the event's `data`. The headers are Standard Webhooks': `webhook-id` (the event's `id`, the same on every retry and redelivery), `webhook-timestamp` (Unix seconds of the attempt) and `webhook-signature`, space-separated `v1,<base64>` entries, each an HMAC-SHA256 with a secret's bytes (the base64 after `whsec_`) over `webhook-id.webhook-timestamp.body`; for 24 hours after a rotation there are two. Answer 2xx within 15 seconds; anything else, a redirect included, is retried with jitter, up to 10 attempts within 72 hours of the first, honouring `Retry-After` on 429 and 503 within those 72 hours. Events are delivered at least once and in no guaranteed order: dedupe by `webhook-id` and order by `createdAt`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**type** | **str** |  | 
**created_at** | **datetime** |  | 
**api_version** | **str** |  | 
**mode** | **str** | The mode of the subscription it is sent to. | 
**data** | [**WebhookEventData**](WebhookEventData.md) |  | 

## Example

```python
from growwer.models.webhook_event import WebhookEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEvent from a JSON string
webhook_event_instance = WebhookEvent.from_json(json)
# print the JSON string representation of the object
print(WebhookEvent.to_json())

# convert the object into a dict
webhook_event_dict = webhook_event_instance.to_dict()
# create an instance of WebhookEvent from a dict
webhook_event_from_dict = WebhookEvent.from_dict(webhook_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


