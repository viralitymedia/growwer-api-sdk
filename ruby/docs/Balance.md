# Growwer::Balance

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **available** | [**Money**](Money.md) | What can be spent, or withdrawn, now. |  |
| **pending** | [**Money**](Money.md) | What is held until orders in progress settle. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::Balance.new(
  available: null,
  pending: null
)
```

