# Growwer::CreateSavedFilterRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | 1 to 255 characters. |  |
| **filters** | **Hash&lt;String, Object&gt;** | At least one filter parameter of GET /projects/{id}/medias, or &#x60;source&#x60;, by name. |  |
| **notification_frequency** | **String** | Email new matching medias this often. Omit it for no emails. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::CreateSavedFilterRequest.new(
  name: null,
  filters: {&quot;language&quot;:[&quot;es&quot;],&quot;minDomainRating&quot;:30,&quot;favourite&quot;:true},
  notification_frequency: null
)
```

