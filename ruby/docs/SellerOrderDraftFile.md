# Growwer::SellerOrderDraftFile

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **file_id** | **String** | A file you uploaded with POST /files and have not used yet. It must be an odt, doc, docx or txt file of up to 8 MB. It is used up once the draft is delivered. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerOrderDraftFile.new(
  file_id: null
)
```

