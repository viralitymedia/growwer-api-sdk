# Growwer::MoneyOrNull

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **amount** | **Integer** | Integer cents: 12500 is 125.00 EUR. |  |
| **currency** | **String** | ISO 4217 currency code. |  |
| **amount_decimal** | **String** | Exact decimal of &#x60;amount&#x60; in major units: \&quot;125.00\&quot;. An input may only echo it unchanged. | [optional][readonly] |

## Example

```ruby
require 'growwer'

instance = Growwer::MoneyOrNull.new(
  amount: 12500,
  currency: EUR,
  amount_decimal: 125.00
)
```

