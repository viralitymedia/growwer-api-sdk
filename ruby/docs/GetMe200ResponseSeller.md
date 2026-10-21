# Growwer::GetMe200ResponseSeller

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **balance** | [**Balance**](Balance.md) |  |  |
| **restricted** | **Boolean** | Whether your seller account is restricted: it accepts no orders and its balance is held. Contact support for the reason. |  |
| **on_holiday** | **Boolean** | Whether you are on holiday: your medias take no orders. Set it with PUT /seller/holiday. |  |
| **holiday_end_date** | **Date** | The day your holiday ends, at 00:00 of that day in Growwer&#39;s server time, or null when you are not on holiday or end it yourself. |  |

## Example

```ruby
require 'growwer'

instance = Growwer::GetMe200ResponseSeller.new(
  balance: null,
  restricted: null,
  on_holiday: null,
  holiday_end_date: null
)
```

