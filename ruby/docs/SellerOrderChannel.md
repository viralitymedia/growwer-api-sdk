# Growwer::SellerOrderChannel

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **created** | **String** | Whether the order was placed through this API (&#x60;api&#x60;), through its MCP server (&#x60;mcp&#x60;) or on the web. |  |
| **accepted** | **String** | Whether you accepted the order through this API (&#x60;api&#x60;), through its MCP server (&#x60;mcp&#x60;) or elsewhere (&#x60;web&#x60;), or null while it is not accepted. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerOrderChannel.new(
  created: null,
  accepted: null
)
```

