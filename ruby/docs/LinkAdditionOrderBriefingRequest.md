# Growwer::LinkAdditionOrderBriefingRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **linking_from** | **String** | The URL of an existing article on the media&#39;s domain that the link goes into, without &#x60;&lt;&#x60; or &#x60;&gt;&#x60;. |  |
| **link** | [**OrderLinkRequest**](OrderLinkRequest.md) |  |  |
| **additional_info** | **String** |  | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::LinkAdditionOrderBriefingRequest.new(
  linking_from: null,
  link: null,
  additional_info: null
)
```

