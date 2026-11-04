# Growwer::TopUpTestWalletRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **amount** | [**Money**](Money.md) | What to credit, in EUR: from 1 to 1000000 cents. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::TopUpTestWalletRequest.new(
  amount: null
)
```

