# Growwer::UpdateSellerMediaRequestPostOfferPricingOptionsInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **link_type** | **String** |  |  |
| **fee_when_seller_writes_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post you write; null or left out when you do not offer it. | [optional] |
| **fee_when_seller_does_not_write_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post the buyer or Growwer writes; null or left out when you do not offer it. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::UpdateSellerMediaRequestPostOfferPricingOptionsInner.new(
  link_type: null,
  fee_when_seller_writes_post: null,
  fee_when_seller_does_not_write_post: null
)
```

