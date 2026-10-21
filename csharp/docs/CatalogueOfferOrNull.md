# Growwer.Api.Model.CatalogueOfferOrNull

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Price** | [**Money**](Money.md) | What you pay for the offer with its dearest link type, flash offer discount included. | 
**LinkType** | **string** | The link type &#x60;price&#x60; is for. | 
**Prices** | [**Dictionary&lt;string, Money&gt;**](Money.md) | What you pay for each link type the offer gives, by link type. | 
**PreviousPrice** | [**MoneyOrNull**](MoneyOrNull.md) | The highest price the offer has had, when &#x60;price&#x60; is more than 5% below it; otherwise null. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

