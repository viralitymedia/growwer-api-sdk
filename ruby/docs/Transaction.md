# Growwer::Transaction

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **type** | **String** | What moved the money, for example &#x60;deposit&#x60; (a top-up), &#x60;debit_from_order&#x60; (an order), &#x60;gift&#x60; or &#x60;manual_charge&#x60;. |  |
| **state** | **String** | An order&#39;s debit stays &#x60;pending_confirmation&#x60; until the order settles, and is &#x60;cancelled&#x60; when the order is refunded. |  |
| **direction** | **String** |  |  |
| **amount** | [**Money**](Money.md) |  |  |
| **description** | **String** | The text the wallet page prints as it is, or null where it prints a translated label instead (then see &#x60;descriptionCode&#x60;). |  |
| **description_code** | **String** | A stable code for the label the wallet page translates: a payment method for a top-up, or &#x60;affiliate_promo&#x60;. Null otherwise. |  |
| **order_id** | **String** | The order this transaction paid for or refunded, while it exists. |  |
| **invoice_id** | **String** | The invoice of this transaction, if any; GET /invoices/{id}/pdf downloads it. |  |
| **has_document** | **Boolean** | Whether GET /wallets/buyer/transactions/{id}/document downloads a document for it. |  |
| **created_at** | **Time** |  |  |
| **updated_at** | **Time** |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::Transaction.new(
  id: null,
  type: null,
  state: null,
  direction: null,
  amount: null,
  description: null,
  description_code: null,
  order_id: null,
  invoice_id: null,
  has_document: null,
  created_at: null,
  updated_at: null
)
```

