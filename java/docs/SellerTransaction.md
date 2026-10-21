

# SellerTransaction

A movement of your seller wallet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**type** | **String** | What moved the money, for example &#x60;credit_from_order&#x60; (an order you delivered), &#x60;credit_from_writing&#x60;, &#x60;withdrawal&#x60;, &#x60;manual_deposit&#x60; or &#x60;manual_charge&#x60;. |  |
|**state** | [**StateEnum**](#StateEnum) | An order&#39;s earning stays &#x60;pending_confirmation&#x60; until the order settles. |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  |
|**amount** | [**Money**](Money.md) |  |  |
|**description** | **String** | The text the wallet page prints, or null when the movement points to an order or a withdrawal instead, or has no text. |  |
|**orderId** | **UUID** | Your order this earning came from, while it exists; GET /seller/orders/{id} reads it. |  |
|**withdrawalId** | **UUID** | Your withdrawal this debit paid; GET /withdrawals lists it. |  |
|**hasDocument** | **Boolean** | Whether GET /wallets/seller/transactions/{id}/document downloads a document for it. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING_CONFIRMATION | &quot;pending_confirmation&quot; |
| CONFIRMED | &quot;confirmed&quot; |
| CANCELLED | &quot;cancelled&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



