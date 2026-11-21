# Growwer::SellerMediaLinkAdditionOfferPricingOptionsInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **link_type** | **String** |  |  |
| **fee** | [**Money**](Money.md) | Your base fee for the link type. |  |
| **current_cost** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid now for the link type, the discount of a running offer (&#x60;flashOffer&#x60;) included; read-only. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerMediaLinkAdditionOfferPricingOptionsInner.new(
  link_type: null,
  fee: null,
  current_cost: null
)
```

