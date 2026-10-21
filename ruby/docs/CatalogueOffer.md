# Growwer::CatalogueOffer

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **price** | [**Money**](Money.md) | What you pay for the offer with its dearest link type, flash offer discount included. |  |
| **link_type** | **String** | The link type &#x60;price&#x60; is for. |  |
| **prices** | [**Hash&lt;String, Money&gt;**](Money.md) | What you pay for each link type the offer gives, by link type. |  |
| **previous_price** | [**MoneyOrNull**](MoneyOrNull.md) | The highest price the offer has had, when &#x60;price&#x60; is more than 5% below it; otherwise null. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::CatalogueOffer.new(
  price: null,
  link_type: null,
  prices: null,
  previous_price: null
)
```

