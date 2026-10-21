# GetMe200ResponseSeller

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**\Growwer\Api\Model\Balance**](Balance.md) |  |
**restricted** | **bool** | Whether your seller account is restricted: it accepts no orders and its balance is held. Contact support for the reason. |
**on_holiday** | **bool** | Whether you are on holiday: your medias take no orders. Set it with PUT /seller/holiday. |
**holiday_end_date** | **\DateTime** | The day your holiday ends, at 00:00 of that day in Growwer&#39;s server time, or null when you are not on holiday or end it yourself. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
