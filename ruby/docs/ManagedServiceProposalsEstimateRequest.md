# Growwer::ManagedServiceProposalsEstimateRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **accept** | **Array&lt;String&gt;** | The &#x60;proposed&#x60; proposals you would accept, each once. Leave it out to price only the accepted ones. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::ManagedServiceProposalsEstimateRequest.new(
  accept: null
)
```

