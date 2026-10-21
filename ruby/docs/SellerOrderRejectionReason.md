# Growwer::SellerOrderRejectionReason

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Why you reject the order, as the seller order page offers it. |  |
| **additional_info** | **String** | More about the reason, which the buyer is told, 10 to 2000 characters. Required with &#x60;other_reasons&#x60;. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerOrderRejectionReason.new(
  name: null,
  additional_info: null
)
```

