# Growwer::Error

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **String** | A stable, machine-readable error code. |  |
| **message** | **String** | A human-readable explanation. It may change. |  |
| **request_id** | **String** | UUID v4 generated per request, or the &#x60;X-Request-Id&#x60; you sent. Quote it when reporting a problem. |  |
| **details** | **Hash&lt;String, Object&gt;** | Extra data on some errors, such as the invalid fields of a validation_failed error. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::Error.new(
  code: unauthorized,
  message: null,
  request_id: 9b2f6c1e-4d7a-4e3b-8a5f-2c1d0e9f7a64,
  details: null
)
```

