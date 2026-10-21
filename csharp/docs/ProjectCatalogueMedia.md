# Growwer.Api.Model.ProjectCatalogueMedia

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Domain** | **string** |  | 
**Type** | **string** |  | 
**Language** | **string** | A language code, as in GET /vocabulary. | 
**Country** | **string** | A country code, as in GET /vocabulary, or null for none. | 
**Topics** | **List&lt;int&gt;** | Topic ids, as in GET /vocabulary. | 
**Metrics** | [**CatalogueMediaMetrics**](CatalogueMediaMetrics.md) |  | 
**PositiveTrafficTrend** | **bool** |  | 
**BestSeller** | **bool** |  | 
**PublicationRate** | **int?** | The share of the media&#39;s orders that were published, in percent, or null without orders. | 
**AverageDaysToPublication** | **int?** | The average days from order to publication, or null without published orders. | 
**OnHoliday** | **bool** | Whether the media is on holiday and will take longer to publish. | 
**FlashOffer** | [**CatalogueMediaFlashOffer**](CatalogueMediaFlashOffer.md) |  | 
**PostOffer** | [**CataloguePostOffer**](CataloguePostOffer.md) |  | 
**LinkAdditionOffer** | [**CatalogueOfferOrNull**](CatalogueOfferOrNull.md) | Adding a link to an existing article, or null when the media does not offer it. | 
**Project** | [**ProjectCatalogueMediaAllOfProject**](ProjectCatalogueMediaAllOfProject.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

