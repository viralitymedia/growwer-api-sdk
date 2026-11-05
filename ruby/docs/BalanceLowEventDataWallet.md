# Growwer::BalanceLowEventDataWallet

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **available_balance** | [**Money**](Money.md) |  |  |
| **currency** | **String** | The currency of the wallet. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::BalanceLowEventDataWallet.new(
  available_balance: null,
  currency: EUR
)
```

