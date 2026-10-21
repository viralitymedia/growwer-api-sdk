# Growwer.Api.Model.OrderEstimate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Price** | [**Money**](Money.md) | What the order costs you. Send it as &#x60;expectedPrice&#x60;. | 
**AvailableBalance** | [**Money**](Money.md) | Your wallet&#39;s available balance. | 
**Missing** | [**Money**](Money.md) | How much the available balance falls short of the price; zero when it covers it. | 
**SufficientBalance** | **bool** | Whether the available balance covers the price. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

