# Growwer::UpdateSellerMediaRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **post_offer** | [**UpdateSellerMediaRequestPostOffer**](UpdateSellerMediaRequestPostOffer.md) |  | [optional] |
| **link_addition_offer** | [**UpdateSellerMediaRequestLinkAdditionOffer**](UpdateSellerMediaRequestLinkAdditionOffer.md) |  | [optional] |
| **extra_services** | [**Array&lt;UpdateSellerMediaRequestExtraServicesInner&gt;**](UpdateSellerMediaRequestExtraServicesInner.md) |  | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::UpdateSellerMediaRequest.new(
  post_offer: null,
  link_addition_offer: null,
  extra_services: null
)
```

