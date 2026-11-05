# Growwer.Api.Model.GetMe200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Email** | **string** |  | 
**FirstName** | **string** |  | 
**Language** | **string** | The language Growwer writes to you in. | 
**CreatedAt** | **DateTime** |  | 
**Buyer** | [**GetMe200ResponseBuyer**](GetMe200ResponseBuyer.md) |  | 
**Seller** | [**GetMe200ResponseSeller**](GetMe200ResponseSeller.md) |  | 
**Catalogue** | [**GetMe200ResponseCatalogue**](GetMe200ResponseCatalogue.md) |  | 
**ManagedService** | [**GetMe200ResponseManagedService**](GetMe200ResponseManagedService.md) |  | 
**Mode** | **string** | The mode of the key you called with. &#x60;live&#x60; works on your real account; &#x60;test&#x60; works in test mode, where nothing you do reaches real sellers, money or orders. Every response to a test key also carries the header &#x60;Growwer-Mode: test&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

