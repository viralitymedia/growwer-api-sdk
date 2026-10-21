# Growwer::SellerTransaction

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **type** | **String** | What moved the money, for example &#x60;credit_from_order&#x60; (an order you delivered), &#x60;credit_from_writing&#x60;, &#x60;withdrawal&#x60;, &#x60;manual_deposit&#x60; or &#x60;manual_charge&#x60;. |  |
| **state** | **String** | An order&#39;s earning stays &#x60;pending_confirmation&#x60; until the order settles. |  |
| **direction** | **String** |  |  |
| **amount** | [**Money**](Money.md) |  |  |
| **description** | **String** | The text the wallet page prints, or null when the movement points to an order or a withdrawal instead, or has no text. |  |
| **order_id** | **String** | Your order this earning came from, while it exists; GET /seller/orders/{id} reads it. |  |
| **withdrawal_id** | **String** | Your withdrawal this debit paid; GET /withdrawals lists it. |  |
| **has_document** | **Boolean** | Whether GET /wallets/seller/transactions/{id}/document downloads a document for it. |  |
| **created_at** | **Time** |  |  |
| **updated_at** | **Time** |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerTransaction.new(
  id: null,
  type: null,
  state: null,
  direction: null,
  amount: null,
  description: null,
  order_id: null,
  withdrawal_id: null,
  has_document: null,
  created_at: null,
  updated_at: null
)
```

