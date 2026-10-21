# Growwer::SavedFilter

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **name** | **String** |  |  |
| **active_filter_count** | **Integer** | How many filters it applies. |  |
| **notifications** | [**SavedFilterNotifications**](SavedFilterNotifications.md) |  |  |
| **created_at** | **Time** |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SavedFilter.new(
  id: null,
  name: null,
  active_filter_count: null,
  notifications: null,
  created_at: null
)
```

