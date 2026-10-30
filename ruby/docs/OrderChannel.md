# Growwer::OrderChannel

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **created** | **String** | Whether the order was placed through this API (&#x60;api&#x60;), through its MCP server (&#x60;mcp&#x60;) or on the web. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::OrderChannel.new(
  created: null
)
```

