# Growwer::PostOrderBriefingRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **links** | [**Array&lt;OrderLinkRequest&gt;**](OrderLinkRequest.md) | No more links than the offer allows. |  |
| **extra_services** | **Array&lt;String&gt;** | Extra services the offer has, added to the ones the web selects for your project by default. A project with a sensitive topic always carries &#x60;extra_charge_for_sensitive_topic&#x60; when the media charges it. | [optional] |
| **title** | **String** |  | [optional] |
| **additional_info** | **String** |  | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::PostOrderBriefingRequest.new(
  links: null,
  extra_services: null,
  title: null,
  additional_info: null
)
```

