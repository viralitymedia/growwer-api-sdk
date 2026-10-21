# Growwer::OrderLinkRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **target_url** | **String** | Where the link points; leave it out for a citation. | [optional] |
| **anchor** | **String** | The anchor text; leave it out to let the media choose it. A citation needs one. | [optional] |
| **type** | **String** | A link type the media offers for this type of order (CatalogueOffer &#x60;linkTypes&#x60;). |  |

## Example

```ruby
require 'growwer'

instance = Growwer::OrderLinkRequest.new(
  target_url: null,
  anchor: null,
  type: null
)
```

