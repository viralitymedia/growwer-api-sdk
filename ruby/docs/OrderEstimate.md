# Growwer::OrderEstimate

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **price** | [**Money**](Money.md) | What the order costs you. Send it as &#x60;expectedPrice&#x60;. |  |
| **available_balance** | [**Money**](Money.md) | Your wallet&#39;s available balance. |  |
| **missing** | [**Money**](Money.md) | How much the available balance falls short of the price; zero when it covers it. |  |
| **sufficient_balance** | **Boolean** | Whether the available balance covers the price. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::OrderEstimate.new(
  price: null,
  available_balance: null,
  missing: null,
  sufficient_balance: null
)
```

