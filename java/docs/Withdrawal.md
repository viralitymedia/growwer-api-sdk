

# Withdrawal


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**amount** | [**Money**](Money.md) | What you withdraw. |  |
|**method** | [**MethodEnum**](#MethodEnum) |  |  |
|**hasInvoice** | **Boolean** | Whether you uploaded an invoice; GET /withdrawals/{id}/invoice downloads it. |  |
|**createdAt** | **OffsetDateTime** |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STARTED | &quot;started&quot; |
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| BANK_TRANSFER | &quot;bank_transfer&quot; |
| PAYPAL | &quot;paypal&quot; |



