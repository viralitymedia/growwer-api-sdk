# Growwer::ManagedServiceProposalReview

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **campaign** | [**ManagedServiceCampaign**](ManagedServiceCampaign.md) |  |  |
| **proposals** | [**Array&lt;ManagedServiceProposal&gt;**](ManagedServiceProposal.md) | The proposals you reviewed, newest first. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::ManagedServiceProposalReview.new(
  campaign: null,
  proposals: null
)
```

