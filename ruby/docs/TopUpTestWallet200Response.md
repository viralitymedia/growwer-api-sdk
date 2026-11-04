# Growwer::TopUpTestWallet200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **balance** | [**Balance**](Balance.md) |  |  |
| **top_up_url** | **String** | The wallet page where a live buyer tops up, as GET /wallets/buyer gives it. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::TopUpTestWallet200Response.new(
  balance: null,
  top_up_url: null
)
```

