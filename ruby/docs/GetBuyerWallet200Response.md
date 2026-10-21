# Growwer::GetBuyerWallet200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **balance** | [**Balance**](Balance.md) |  |  |
| **top_up_url** | **String** | The wallet page, in your language (English when the web is not available in it), where you top up your balance. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::GetBuyerWallet200Response.new(
  balance: null,
  top_up_url: null
)
```

