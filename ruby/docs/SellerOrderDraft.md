# Growwer::SellerOrderDraft

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **reviewable** | **Boolean** | Whether the buyer reviews the draft before it is published. |  |
| **has_file** | **Boolean** | Whether the current draft has a file; GET /seller/orders/{id}/draft downloads it. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerOrderDraft.new(
  reviewable: null,
  has_file: null
)
```

