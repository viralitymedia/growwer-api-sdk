# Growwer::Withdrawal

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **state** | **String** |  |  |
| **amount** | [**Money**](Money.md) | What you withdraw. |  |
| **method** | **String** |  |  |
| **has_invoice** | **Boolean** | Whether you uploaded an invoice; GET /withdrawals/{id}/invoice downloads it. |  |
| **created_at** | **Time** |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::Withdrawal.new(
  id: null,
  state: null,
  amount: null,
  method: null,
  has_invoice: null,
  created_at: null
)
```

