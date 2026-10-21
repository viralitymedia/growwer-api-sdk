# Growwer::Money

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **amount** | **Integer** | Integer cents. |  |
| **currency** | **String** | ISO 4217 currency code. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::Money.new(
  amount: 12500,
  currency: EUR
)
```

