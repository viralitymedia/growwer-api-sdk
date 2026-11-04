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
| **mode** | **String** | The mode of the key you called with. &#x60;live&#x60; works on your real account; &#x60;test&#x60; works in test mode, where nothing you do reaches real sellers, money or orders. Every response to a test key also carries the header &#x60;Growwer-Mode: test&#x60;. |  |

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
  managed_service: null,
  mode: null
)
```

