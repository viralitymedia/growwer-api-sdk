# Growwer::CreateSellerMediaRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **root_url** | **String** |  |  |
| **typology** | **String** |  |  |
| **country** | **String** | A country code from GET /vocabulary. |  |
| **language** | **String** | A language code from GET /vocabulary. |  |
| **topics** | **Array&lt;Integer&gt;** | Topic ids from GET /vocabulary. |  |
| **banned_topics** | **Array&lt;Integer&gt;** | The topic ids from GET /vocabulary the media refuses. | [optional] |
| **post_offer** | [**CreateSellerMediaRequestPostOffer**](CreateSellerMediaRequestPostOffer.md) |  |  |
| **link_addition_offer** | [**UpdateSellerMediaRequestLinkAdditionOffer**](UpdateSellerMediaRequestLinkAdditionOffer.md) |  | [optional] |
| **extra_services** | [**Array&lt;UpdateSellerMediaRequestExtraServicesInner&gt;**](UpdateSellerMediaRequestExtraServicesInner.md) |  | [optional] |
| **accept_media_publishing_terms** | **Boolean** | Must be true: you accept the media publishing terms. |  |
| **declare_media_ownership** | **Boolean** | Must be true: you own or manage this media. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::CreateSellerMediaRequest.new(
  root_url: https://www.example.com,
  typology: null,
  country: ES,
  language: es,
  topics: null,
  banned_topics: null,
  post_offer: null,
  link_addition_offer: null,
  extra_services: null,
  accept_media_publishing_terms: null,
  declare_media_ownership: null
)
```

