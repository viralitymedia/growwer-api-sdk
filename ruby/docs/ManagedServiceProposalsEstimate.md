# Growwer::ManagedServiceProposalsEstimate

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **accepted_total** | [**Money**](Money.md) | The proposals already accepted and still awaiting their order. |  |
| **selected_total** | [**Money**](Money.md) | The proposals named in &#x60;accept&#x60;. |  |
| **total** | [**Money**](Money.md) | &#x60;acceptedTotal&#x60; plus &#x60;selectedTotal&#x60;. |  |
| **available_balance** | [**Money**](Money.md) | Your wallet&#39;s available balance. |  |
| **missing** | [**Money**](Money.md) | How much the available balance falls short of &#x60;total&#x60;; zero when it covers it. |  |
| **sufficient_balance** | **Boolean** | Whether the available balance covers &#x60;total&#x60;. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::ManagedServiceProposalsEstimate.new(
  accepted_total: null,
  selected_total: null,
  total: null,
  available_balance: null,
  missing: null,
  sufficient_balance: null
)
```

