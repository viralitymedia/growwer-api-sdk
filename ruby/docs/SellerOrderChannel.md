# Growwer::SellerOrderChannel

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **created** | **String** | Whether the order was placed through this API or on the web. |  |
| **accepted** | **String** | Whether you accepted the order through this API or elsewhere, or null while it is not accepted. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerOrderChannel.new(
  created: null,
  accepted: null
)
```

