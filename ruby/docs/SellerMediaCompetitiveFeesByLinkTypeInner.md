# Growwer::SellerMediaCompetitiveFeesByLinkTypeInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **link_type** | **String** |  |  |
| **fee_when_seller_writes_post** | [**MoneyOrNull**](MoneyOrNull.md) | The fee the apply sets for a post you write on this link type, or null when it keeps your fee on that side. |  |
| **fee_when_seller_does_not_write_post** | [**MoneyOrNull**](MoneyOrNull.md) | The fee the apply sets for a post the buyer or Growwer writes on this link type, or null when it keeps your fee on that side. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerMediaCompetitiveFeesByLinkTypeInner.new(
  link_type: null,
  fee_when_seller_writes_post: null,
  fee_when_seller_does_not_write_post: null
)
```

