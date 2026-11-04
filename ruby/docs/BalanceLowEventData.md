# Growwer::BalanceLowEventData

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **wallet** | [**BalanceLowEventDataWallet**](BalanceLowEventDataWallet.md) |  |  |
| **threshold** | [**Money**](Money.md) | The subscription&#39;s &#x60;lowBalanceThreshold&#x60; that the balance dropped below. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::BalanceLowEventData.new(
  wallet: null,
  threshold: null
)
```

