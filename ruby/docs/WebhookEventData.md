# Growwer::WebhookEventData

## Class instance methods

### `openapi_one_of`

Returns the list of classes defined in oneOf.

#### Example

```ruby
require 'growwer'

Growwer::WebhookEventData.openapi_one_of
# =>
# [
#   :'BalanceLowEventData',
#   :'OrderEventData',
#   :'WebhookTestEventData'
# ]
```

### build

Find the appropriate object from the `openapi_one_of` list and casts the data into it.

#### Example

```ruby
require 'growwer'

Growwer::WebhookEventData.build(data)
# => #<BalanceLowEventData:0x00007fdd4aab02a0>

Growwer::WebhookEventData.build(data_that_doesnt_match)
# => nil
```

#### Parameters

| Name | Type | Description |
| ---- | ---- | ----------- |
| **data** | **Mixed** | data to be matched against the list of oneOf items |

#### Return type

- `BalanceLowEventData`
- `OrderEventData`
- `WebhookTestEventData`
- `nil` (if no type matches)

