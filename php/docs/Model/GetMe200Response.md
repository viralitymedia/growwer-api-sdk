# GetMe200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**email** | **string** |  |
**first_name** | **string** |  |
**language** | **string** | The language Growwer writes to you in. |
**created_at** | **\DateTime** |  |
**buyer** | [**\Growwer\Api\Model\GetMe200ResponseBuyer**](GetMe200ResponseBuyer.md) |  |
**seller** | [**\Growwer\Api\Model\GetMe200ResponseSeller**](GetMe200ResponseSeller.md) |  |
**catalogue** | [**\Growwer\Api\Model\GetMe200ResponseCatalogue**](GetMe200ResponseCatalogue.md) |  |
**managed_service** | [**\Growwer\Api\Model\GetMe200ResponseManagedService**](GetMe200ResponseManagedService.md) |  |
**mode** | **string** | The mode of the key you called with. &#x60;live&#x60; works on your real account; &#x60;test&#x60; works in test mode, where nothing you do reaches real sellers, money or orders. Every response to a test key also carries the header &#x60;Growwer-Mode: test&#x60;. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
