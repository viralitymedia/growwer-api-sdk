# Growwer::SellerMediaPostOffer

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **pricing_options** | [**Array&lt;SellerMediaPostOfferPricingOptionsInner&gt;**](SellerMediaPostOfferPricingOptionsInner.md) | One entry per link type you offer. |  |
| **extra_services** | [**Array&lt;UpdateSellerMediaRequestExtraServicesInner&gt;**](UpdateSellerMediaRequestExtraServicesInner.md) |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerMediaPostOffer.new(
  pricing_options: null,
  extra_services: null
)
```

