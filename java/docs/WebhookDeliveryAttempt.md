

# WebhookDeliveryAttempt


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attemptedAt** | **OffsetDateTime** |  |  |
|**statusCode** | **Integer** | The HTTP status your endpoint answered, null when it did not answer. Only 2xx succeeds; a redirect is not followed and fails. |  |
|**durationMs** | **Integer** | How long the attempt took, in milliseconds. It gives up after 15 seconds. |  |
|**responseBody** | **String** | Up to the first 1024 bytes of the response body, null when it did not answer. |  |
|**error** | [**ErrorEnum**](#ErrorEnum) | Why there is no status, null when it answered. &#x60;address_not_allowed&#x60;, its host resolved to, or connected to, an address that is not public. |  |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| ADDRESS_NOT_ALLOWED | &quot;address_not_allowed&quot; |
| TIMEOUT | &quot;timeout&quot; |
| CONNECTION_FAILED | &quot;connection_failed&quot; |



