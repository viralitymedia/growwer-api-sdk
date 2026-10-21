# Growwer::CreateProjectRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** |  | [optional] |
| **root_url** | **String** |  |  |
| **website_type** | **String** |  |  |
| **topics** | **Array&lt;Integer&gt;** | Exactly one topic id from GET /vocabulary. |  |
| **language** | **String** | A language code from GET /vocabulary. |  |
| **country** | **String** | A country code from GET /vocabulary; omit it or send null for worldwide. | [optional] |
| **promoted_products** | **Array&lt;String&gt;** | 5 to 10 products or services the campaign promotes. |  |
| **user_keywords** | **Array&lt;String&gt;** | At most 100 keywords, none with a line break. | [optional] |

## Example

```ruby
require 'growwer'

instance = Growwer::CreateProjectRequest.new(
  name: null,
  root_url: https://www.example.com,
  website_type: null,
  topics: null,
  language: es,
  country: ES,
  promoted_products: null,
  user_keywords: null
)
```

