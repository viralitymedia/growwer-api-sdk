# OrderEstimate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**\Growwer\Api\Model\Money**](Money.md) | What the order costs you. Send it as &#x60;expectedPrice&#x60;. |
**available_balance** | [**\Growwer\Api\Model\Money**](Money.md) | Your wallet&#39;s available balance. |
**missing** | [**\Growwer\Api\Model\Money**](Money.md) | How much the available balance falls short of the price; zero when it covers it. |
**sufficient_balance** | **bool** | Whether the available balance covers the price. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
