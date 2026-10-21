# CatalogueOfferOrNull

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**\Growwer\Api\Model\Money**](Money.md) | What you pay for the offer with its dearest link type, flash offer discount included. |
**link_type** | **string** | The link type &#x60;price&#x60; is for. |
**prices** | [**array<string,\Growwer\Api\Model\Money>**](Money.md) | What you pay for each link type the offer gives, by link type. |
**previous_price** | [**\Growwer\Api\Model\MoneyOrNull**](MoneyOrNull.md) | The highest price the offer has had, when &#x60;price&#x60; is more than 5% below it; otherwise null. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
