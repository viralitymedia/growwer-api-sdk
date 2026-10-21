# Growwer::OrderDraft

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **authored_by_buyer** | **Boolean** | Whether you write the draft. |  |
| **reviewable** | **Boolean** | Whether you review the draft before it is published. |  |
| **has_file** | **Boolean** | Whether the current draft has a file; GET /orders/{id}/draft downloads it. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::OrderDraft.new(
  authored_by_buyer: null,
  reviewable: null,
  has_file: null
)
```

