# Growwer::ManagedServiceProposalReviewRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **reviews** | [**Array&lt;ManagedServiceProposalReviewRequestReviewsInner&gt;**](ManagedServiceProposalReviewRequestReviewsInner.md) | One decision on each proposal of the campaign that is &#x60;proposed&#x60;, each named once. Their order does not matter. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::ManagedServiceProposalReviewRequest.new(
  reviews: null
)
```

