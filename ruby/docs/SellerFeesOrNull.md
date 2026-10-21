# Growwer::SellerFeesOrNull

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **fee_when_seller_writes_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post you write, or null when you do not offer it. |  |
| **fee_when_seller_does_not_write_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post the buyer or Growwer writes, or null when you do not offer it. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerFeesOrNull.new(
  fee_when_seller_writes_post: null,
  fee_when_seller_does_not_write_post: null
)
```

