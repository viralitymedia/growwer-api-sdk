# Growwer::CataloguePostOfferAllOfExtras

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **homepage_listing** | [**MoneyOrNull**](MoneyOrNull.md) | What listing the post on the homepage costs, or null when the media does not offer it. |  |
| **sensitive_topic** | [**CataloguePostOfferAllOfExtrasSensitiveTopic**](CataloguePostOfferAllOfExtrasSensitiveTopic.md) |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::CataloguePostOfferAllOfExtras.new(
  homepage_listing: null,
  sensitive_topic: null
)
```

