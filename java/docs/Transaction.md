

# Transaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**type** | **String** | What moved the money, for example &#x60;deposit&#x60; (a top-up), &#x60;debit_from_order&#x60; (an order), &#x60;gift&#x60; or &#x60;manual_charge&#x60;. |  |
|**state** | [**StateEnum**](#StateEnum) | An order&#39;s debit stays &#x60;pending_confirmation&#x60; until the order settles, and is &#x60;cancelled&#x60; when the order is refunded. |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  |
|**amount** | [**Money**](Money.md) |  |  |
|**description** | **String** | The text the wallet page prints as it is, or null where it prints a translated label instead (then see &#x60;descriptionCode&#x60;). |  |
|**descriptionCode** | **String** | A stable code for the label the wallet page translates: a payment method for a top-up, or &#x60;affiliate_promo&#x60;. Null otherwise. |  |
|**orderId** | **UUID** | The order this transaction paid for or refunded, while it exists. |  |
|**invoiceId** | **UUID** | The invoice of this transaction, if any; GET /invoices/{id}/pdf downloads it. |  |
|**hasDocument** | **Boolean** | Whether GET /wallets/buyer/transactions/{id}/document downloads a document for it. |  |
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



