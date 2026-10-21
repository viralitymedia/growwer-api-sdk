# Growwer::ManagedServiceProposalReviewRequestReviewsInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **proposal_id** | **String** |  |  |
| **decision** | **String** |  |  |
| **comment** | **String** | Required to reject, at most 2000 characters once trimmed; the team reads it. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::ManagedServiceProposalReviewRequestReviewsInner.new(
  proposal_id: null,
  decision: null,
  comment: null
)
```

