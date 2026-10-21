# Growwer::GetMe200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **email** | **String** |  |  |
| **first_name** | **String** |  |  |
| **language** | **String** | The language Growwer writes to you in. |  |
| **created_at** | **Time** |  |  |
| **buyer** | [**GetMe200ResponseBuyer**](GetMe200ResponseBuyer.md) |  |  |
| **seller** | [**GetMe200ResponseSeller**](GetMe200ResponseSeller.md) |  |  |
| **catalogue** | [**GetMe200ResponseCatalogue**](GetMe200ResponseCatalogue.md) |  |  |
| **managed_service** | [**GetMe200ResponseManagedService**](GetMe200ResponseManagedService.md) |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::GetMe200Response.new(
  id: null,
  email: null,
  first_name: null,
  language: en,
  created_at: null,
  buyer: null,
  seller: null,
  catalogue: null,
  managed_service: null
)
```

