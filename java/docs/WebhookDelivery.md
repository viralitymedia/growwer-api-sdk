

# WebhookDelivery


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**eventId** | **UUID** | The event&#39;s id, sent as &#x60;webhook-id&#x60; on every attempt and redelivery. |  |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;pending&#x60; while it is sent or retried, &#x60;succeeded&#x60; once an attempt got a 2xx, &#x60;failed&#x60; once the retries ran out, the endpoint answered 410 or the subscription was disabled. |  |
|**attemptCount** | **Integer** | How many attempts it took, redeliveries included. |  |
|**nextAttemptAt** | **OffsetDateTime** | When the next retry is due, null when none is. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**attempts** | [**List&lt;WebhookDeliveryAttempt&gt;**](WebhookDeliveryAttempt.md) | The latest 10 attempts, newest first. |  |



## Enum: EventTypeEnum

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



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| FAILED | &quot;failed&quot; |



