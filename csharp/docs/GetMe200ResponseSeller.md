# Growwer.Api.Model.GetMe200ResponseSeller

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Balance** | [**Balance**](Balance.md) |  | 
**Restricted** | **bool** | Whether your seller account is restricted: it accepts no orders and its balance is held. Contact support for the reason. | 
**OnHoliday** | **bool** | Whether you are on holiday: your medias take no orders. Set it with PUT /seller/holiday. | 
**HolidayEndDate** | **DateOnly?** | The day your holiday ends, at 00:00 of that day in Growwer&#39;s server time, or null when you are not on holiday or end it yourself. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

