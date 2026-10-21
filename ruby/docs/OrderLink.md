# Growwer::OrderLink

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **target_url** | **String** | Where the link points, or null for a citation. |  |
| **anchor** | **String** | The anchor text, or null when the media chooses it. A citation always has one. |  |
| **type** | **String** |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::OrderLink.new(
  target_url: null,
  anchor: null,
  type: null
)
```

