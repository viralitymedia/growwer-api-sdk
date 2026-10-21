

# ProjectCatalogueMedia


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**domain** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**language** | **String** | A language code, as in GET /vocabulary. |  |
|**country** | **String** | A country code, as in GET /vocabulary, or null for none. |  |
|**topics** | **List&lt;Integer&gt;** | Topic ids, as in GET /vocabulary. |  |
|**metrics** | [**CatalogueMediaMetrics**](CatalogueMediaMetrics.md) |  |  |
|**positiveTrafficTrend** | **Boolean** |  |  |
|**bestSeller** | **Boolean** |  |  |
|**publicationRate** | **Integer** | The share of the media&#39;s orders that were published, in percent, or null without orders. |  |
|**averageDaysToPublication** | **Integer** | The average days from order to publication, or null without published orders. |  |
|**onHoliday** | **Boolean** | Whether the media is on holiday and will take longer to publish. |  |
|**flashOffer** | [**CatalogueMediaFlashOffer**](CatalogueMediaFlashOffer.md) |  |  |
|**postOffer** | [**CataloguePostOffer**](CataloguePostOffer.md) |  |  |
|**linkAdditionOffer** | [**CatalogueOfferOrNull**](CatalogueOfferOrNull.md) | Adding a link to an existing article, or null when the media does not offer it. |  |
|**project** | [**ProjectCatalogueMediaAllOfProject**](ProjectCatalogueMediaAllOfProject.md) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BLOG | &quot;blog&quot; |
| PRESS | &quot;press&quot; |



