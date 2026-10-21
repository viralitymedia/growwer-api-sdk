# Growwer::OrderEstimateRequestBriefing

## Class instance methods

### `openapi_one_of`

Returns the list of classes defined in oneOf.

#### Example

```ruby
require 'growwer'

Growwer::OrderEstimateRequestBriefing.openapi_one_of
# =>
# [
#   :'LinkAdditionOrderBriefingRequest',
#   :'PostOrderBriefingRequest'
# ]
```

### build

Find the appropriate object from the `openapi_one_of` list and casts the data into it.

#### Example

```ruby
require 'growwer'

Growwer::OrderEstimateRequestBriefing.build(data)
# => #<LinkAdditionOrderBriefingRequest:0x00007fdd4aab02a0>

Growwer::OrderEstimateRequestBriefing.build(data_that_doesnt_match)
# => nil
```

#### Parameters

| Name | Type | Description |
| ---- | ---- | ----------- |
| **data** | **Mixed** | data to be matched against the list of oneOf items |

#### Return type

- `LinkAdditionOrderBriefingRequest`
- `PostOrderBriefingRequest`
- `nil` (if no type matches)

