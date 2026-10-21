# Growwer::Project

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **name** | **String** | Your name for the project, or null when it has none. |  |
| **root_url** | **String** | The website the project promotes. It cannot be changed once the project exists. |  |
| **website_type** | **String** | What the website is: an online shop (&#x60;ecommerce&#x60;), a services business (&#x60;services&#x60;) or anything else (&#x60;other&#x60;). |  |
| **topics** | **Array&lt;Integer&gt;** | The website&#39;s topic, as a topic id from GET /vocabulary. Exactly one. |  |
| **language** | **String** | The language of the campaign, as a language code from GET /vocabulary. |  |
| **country** | **String** | The country the campaign targets, as a country code from GET /vocabulary, or null for worldwide. |  |
| **promoted_products** | **Array&lt;String&gt;** | The products or services the campaign promotes, 5 to 10. |  |
| **user_keywords** | **Array&lt;String&gt;** | Keywords you want the campaign to target, at most 100. |  |
| **state** | **String** | &#x60;finished&#x60; once Growwer has recommended media for the project, &#x60;analyzing&#x60; until then. Analysis can take hours, and it never finishes when no medium matches the project. Poll with backoff, and use &#x60;createdAt&#x60; to decide how long to keep polling.  |  |
| **created_at** | **Time** |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::Project.new(
  id: null,
  name: null,
  root_url: null,
  website_type: null,
  topics: null,
  language: es,
  country: ES,
  promoted_products: null,
  user_keywords: null,
  state: null,
  created_at: null
)
```

