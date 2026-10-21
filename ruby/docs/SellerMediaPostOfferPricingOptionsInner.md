# Growwer::SellerMediaPostOfferPricingOptionsInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **fee_when_seller_writes_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post you write, or null when you do not offer it. |  |
| **fee_when_seller_does_not_write_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post the buyer or Growwer writes, or null when you do not offer it. |  |
| **link_type** | **String** |  |  |
| **current_cost** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid now for the link type, flash offer discount included; read-only. Null when the link type has no current pricing. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerMediaPostOfferPricingOptionsInner.new(
  fee_when_seller_writes_post: null,
  fee_when_seller_does_not_write_post: null,
  link_type: null,
  current_cost: null
)
```

