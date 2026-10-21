# Growwer::UpdateProjectRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Null or an empty string removes the name. | [optional] |
| **website_type** | **String** |  | [optional] |
| **topics** | **Array&lt;Integer&gt;** | Exactly one topic id from GET /vocabulary. | [optional] |
| **language** | **String** | A language code from GET /vocabulary. | [optional] |
| **country** | **String** | A country code from GET /vocabulary, or null for worldwide. | [optional] |
| **promoted_products** | **Array&lt;String&gt;** | 5 to 10 products or services the campaign promotes. | [optional] |
| **user_keywords** | **Array&lt;String&gt;** | At most 100 keywords, none with a line break. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::UpdateProjectRequest.new(
  name: null,
  website_type: null,
  topics: null,
  language: null,
  country: null,
  promoted_products: null,
  user_keywords: null
)
```

