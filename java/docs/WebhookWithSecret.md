

# WebhookWithSecret

A subscription with its signing secret, which only create and rotate-secret answer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**url** | **URI** |  |  |
|**events** | **List&lt;WebhookEventType&gt;** |  |  |
|**lowBalanceThreshold** | [**MoneyOrNull**](MoneyOrNull.md) | With &#x60;balance.low&#x60;, the available buyer balance below which it fires; null otherwise. |  |
|**description** | **String** |  |  |
|**enabled** | **Boolean** | Whether the subscription gets events. |  |
|**disabledReason** | [**DisabledReasonEnum**](#DisabledReasonEnum) | Why it is disabled, null while enabled. &#x60;by_user&#x60;, through PATCH /webhooks/{id}; &#x60;endpoint_gone&#x60;, its endpoint answered 410; &#x60;failing&#x60;, every delivery failed for 5 days, and the account owner was emailed. |  |
|**failingSince** | **OffsetDateTime** | Since when its deliveries have failed without one succeeding, null while they succeed. At 5 days it is disabled. The check runs at each failed attempt, so a subscription whose &#x60;failingSince&#x60; is already more than 5 days old, say one that had no event for a while, is disabled at its next failed attempt, without the retries that delivery would otherwise get. |  |
|**previousSecretExpiresAt** | **OffsetDateTime** | Until when the secret replaced by the last rotation still signs beside the new one, null when it no longer does. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**secret** | **String** | The signing secret, &#x60;whsec_&#x60; and the base64 of 32 random bytes. Shown only in this answer, and absent when the request is replayed under its &#x60;Idempotency-Key&#x60; (or the MCP tool under its &#x60;requestId&#x60;), since the secret is never stored. |  [optional] |



## Enum: DisabledReasonEnum

| Name | Value |
|---- | -----|
| BY_USER | &quot;by_user&quot; |
| ENDPOINT_GONE | &quot;endpoint_gone&quot; |
| FAILING | &quot;failing&quot; |



