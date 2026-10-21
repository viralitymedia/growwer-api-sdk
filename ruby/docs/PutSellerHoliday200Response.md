# Growwer::PutSellerHoliday200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **on_holiday** | **Boolean** |  |  |
| **end_date** | **Date** | The day the holiday ends, at 00:00 of that day in Growwer&#39;s server time, or null for none. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::PutSellerHoliday200Response.new(
  on_holiday: null,
  end_date: null
)
```

