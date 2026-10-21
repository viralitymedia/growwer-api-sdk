# Growwer::OrderBriefing

## Class instance methods

### `openapi_one_of`

Returns the list of classes defined in oneOf.

#### Example

```ruby
require 'growwer'

Growwer::OrderBriefing.openapi_one_of
# =>
# [
#   :'LinkAdditionOrderBriefing',
#   :'PostOrderBriefing'
# ]
```

### build

Find the appropriate object from the `openapi_one_of` list and casts the data into it.

#### Example

```ruby
require 'growwer'

Growwer::OrderBriefing.build(data)
# => #<LinkAdditionOrderBriefing:0x00007fdd4aab02a0>

Growwer::OrderBriefing.build(data_that_doesnt_match)
# => nil
```

#### Parameters

| Name | Type | Description |
| ---- | ---- | ----------- |
| **data** | **Mixed** | data to be matched against the list of oneOf items |

#### Return type

- `LinkAdditionOrderBriefing`
- `PostOrderBriefing`
- `nil` (if no type matches)

