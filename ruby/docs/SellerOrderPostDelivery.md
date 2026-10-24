# Growwer::SellerOrderPostDelivery

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **url** | **String** | The URL of the published post. It is checked to be a URL without &#x60;&lt;&#x60; or &#x60;&gt;&#x60;, as the web does; whether the post carries the links is not checked here. |  |
| **publication_date_confirmed** | **Boolean** | Must be true. Confirms the post is live, or for an order with a scheduled publication date, that it will be published on that date. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerOrderPostDelivery.new(
  url: null,
  publication_date_confirmed: null
)
```

