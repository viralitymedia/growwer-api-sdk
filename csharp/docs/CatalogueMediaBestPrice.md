# Growwer.Api.Model.CatalogueMediaBestPrice
The best-price badge the catalogue shows, or null for none: cheaper means the price is at least 1 EUR below the cheapest listing of the media found on the other platforms checked in the last 7 days; only_here means none of the platforms checked lists it. It names neither the platforms nor any price.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Badge** | **string** |  | 
**PlatformCount** | **int** | How many platforms the claim was checked against. | 
**CheckedOn** | **DateOnly** | The day of that check. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

