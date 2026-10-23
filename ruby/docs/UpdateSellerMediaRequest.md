# Growwer::UpdateSellerMediaRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **typology** | **String** |  | [optional] |
| **post_offer** | [**UpdateSellerMediaRequestPostOffer**](UpdateSellerMediaRequestPostOffer.md) |  | [optional] |
| **link_addition_offer** | [**UpdateSellerMediaRequestLinkAdditionOffer**](UpdateSellerMediaRequestLinkAdditionOffer.md) |  | [optional] |
| **extra_services** | [**Array&lt;UpdateSellerMediaRequestExtraServicesInner&gt;**](UpdateSellerMediaRequestExtraServicesInner.md) |  | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::UpdateSellerMediaRequest.new(
  typology: null,
  post_offer: null,
  link_addition_offer: null,
  extra_services: null
)
```

