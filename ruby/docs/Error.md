# Growwer::Error

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **String** | A stable, machine-readable error code. |  |
| **message** | **String** | A human-readable explanation. It may change. |  |
| **request_id** | **String** | The X-Request-Id of the call. Quote it when reporting a problem. |  |
| **details** | **Hash&lt;String, Object&gt;** | Extra data on some errors, such as the invalid fields of a validation_failed error. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::Error.new(
  code: unauthorized,
  message: null,
  request_id: null,
  details: null
)
```

