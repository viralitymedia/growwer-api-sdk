# Growwer::OrderDelivery

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **url** | **String** | The published article, or for a link addition the article the link went into. |  |
| **published_at** | **Time** | When the post was published; null for a link addition. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::OrderDelivery.new(
  url: null,
  published_at: null
)
```

