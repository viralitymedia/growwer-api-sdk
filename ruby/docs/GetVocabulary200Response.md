# Growwer::GetVocabulary200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **countries** | [**Array&lt;CodeName&gt;**](CodeName.md) | ISO 3166-1 alpha-2 codes. |  |
| **languages** | [**Array&lt;CodeName&gt;**](CodeName.md) | ISO 639 codes, as the web&#39;s language selectors offer them. |  |
| **topics** | [**Array&lt;GetVocabulary200ResponseTopicsInner&gt;**](GetVocabulary200ResponseTopicsInner.md) |  |  |
| **product_types** | **Array&lt;String&gt;** | What an order buys: a sponsored post, or a link added to an existing page. |  |
| **link_types** | **Array&lt;String&gt;** |  |  |
| **order_states** | **Array&lt;String&gt;** |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::GetVocabulary200Response.new(
  countries: null,
  languages: null,
  topics: null,
  product_types: null,
  link_types: null,
  order_states: null
)
```

