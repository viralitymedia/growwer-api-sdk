# Growwer::Invoice

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **number** | **String** |  |  |
| **issued_at** | **Time** |  |  |
| **total** | [**Money**](Money.md) | The invoice total, taxes included. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::Invoice.new(
  id: null,
  number: null,
  issued_at: null,
  total: null
)
```

