

# GetMe200ResponseSeller


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balance** | [**Balance**](Balance.md) |  |  |
|**restricted** | **Boolean** | Whether your seller account is restricted: it accepts no orders and its balance is held. Contact support for the reason. |  |
|**onHoliday** | **Boolean** | Whether you are on holiday: your medias take no orders. Set it with PUT /seller/holiday. |  |
|**holidayEndDate** | **LocalDate** | The day your holiday ends, at 00:00 of that day in Growwer&#39;s server time, or null when you are not on holiday or end it yourself. |  |



