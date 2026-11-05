

# WebhookEvent

What Growwer POSTs to a subscription's URL. OpenAPI 3.0, which this document follows, has no `webhooks` section: `x-webhooks` lists each event in the shape of OpenAPI 3.1's, with this envelope and the event's `data`. The headers are Standard Webhooks': `webhook-id` (the event's `id`, the same on every retry and redelivery), `webhook-timestamp` (Unix seconds of the attempt) and `webhook-signature`, space-separated `v1,<base64>` entries, each an HMAC-SHA256 with a secret's bytes (the base64 after `whsec_`) over `webhook-id.webhook-timestamp.body`; for 24 hours after a rotation there are two. Answer 2xx within 15 seconds; anything else, a redirect included, is retried with jitter, up to 10 attempts within 72 hours of the first, honouring `Retry-After` on 429 and 503 within those 72 hours. Events are delivered at least once and in no guaranteed order: dedupe by `webhook-id` and order by `createdAt`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**apiVersion** | [**ApiVersionEnum**](#ApiVersionEnum) |  |  |
|**mode** | [**ModeEnum**](#ModeEnum) | The mode of the subscription it is sent to. |  |
|**data** | [**WebhookEventData**](WebhookEventData.md) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ORDER_CREATED | &quot;order.created&quot; |
| ORDER_ACCEPTED | &quot;order.accepted&quot; |
| ORDER_REJECTED | &quot;order.rejected&quot; |
| ORDER_PUBLISHED | &quot;order.published&quot; |
| ORDER_UPDATE_REQUESTED | &quot;order.update_requested&quot; |
| ORDER_COMPLETED | &quot;order.completed&quot; |
| ORDER_CANCELLED | &quot;order.cancelled&quot; |
| BALANCE_LOW | &quot;balance.low&quot; |
| WEBHOOK_TEST | &quot;webhook.test&quot; |



## Enum: ApiVersionEnum

| Name | Value |
|---- | -----|
| V1 | &quot;v1&quot; |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| LIVE | &quot;live&quot; |
| TEST | &quot;test&quot; |



