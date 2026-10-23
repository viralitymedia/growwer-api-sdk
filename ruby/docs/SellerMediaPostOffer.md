# Growwer::SellerMediaPostOffer

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **pricing_options** | [**Array&lt;SellerMediaPostOfferPricingOptionsInner&gt;**](SellerMediaPostOfferPricingOptionsInner.md) | One entry per link type you offer. |  |
| **maximum_links** | **Integer** | How many links a sponsored post may hold, 1 to 4. |  |
| **advertising_labelling_policy** | **String** | Whether sponsored posts are labelled as advertising. |  |
| **promoted_social_networks** | **Array&lt;String&gt;** | The social networks sponsored posts are promoted on. |  |
| **extra_services** | [**Array&lt;UpdateSellerMediaRequestExtraServicesInner&gt;**](UpdateSellerMediaRequestExtraServicesInner.md) | Read here, but PATCH /seller/medias/{id} and POST /seller/medias take it at the top level of the body. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerMediaPostOffer.new(
  pricing_options: null,
  maximum_links: null,
  advertising_labelling_policy: null,
  promoted_social_networks: null,
  extra_services: null
)
```

