# Growwer::CataloguePostOfferAllOfExtrasSensitiveTopic

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **allowed** | **Boolean** | Whether the media publishes on sensitive topics. |  |
| **extra_price** | [**MoneyOrNull**](MoneyOrNull.md) | What a post on a sensitive topic costs on top, or null when it costs nothing more. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::CataloguePostOfferAllOfExtrasSensitiveTopic.new(
  allowed: null,
  extra_price: null
)
```

