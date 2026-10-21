# Growwer::GetMe200ResponseManagedService

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **active** | **Boolean** | Whether you have a managed service: Growwer&#39;s team runs link building campaigns for you (tag Managed services). With one, request a new campaign with POST /managed-service/campaign-requests; without one, ask about the service with POST /managed-service/info-requests. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::GetMe200ResponseManagedService.new(
  active: null
)
```

