# ProjectCatalogueMedia

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**domain** | **string** |  |
**type** | **string** |  |
**language** | **string** | A language code, as in GET /vocabulary. |
**country** | **string** | A country code, as in GET /vocabulary, or null for none. |
**topics** | **int[]** | Topic ids, as in GET /vocabulary. |
**metrics** | [**\Growwer\Api\Model\CatalogueMediaMetrics**](CatalogueMediaMetrics.md) |  |
**positive_traffic_trend** | **bool** |  |
**best_seller** | **bool** |  |
**publication_rate** | **int** | The share of the media&#39;s orders that were published, in percent, or null without orders. |
**average_days_to_publication** | **int** | The average days from order to publication, or null without published orders. |
**on_holiday** | **bool** | Whether the media is on holiday and will take longer to publish. |
**flash_offer** | [**\Growwer\Api\Model\CatalogueMediaFlashOffer**](CatalogueMediaFlashOffer.md) |  |
**post_offer** | [**\Growwer\Api\Model\CataloguePostOffer**](CataloguePostOffer.md) |  |
**link_addition_offer** | [**\Growwer\Api\Model\CatalogueOfferOrNull**](CatalogueOfferOrNull.md) | Adding a link to an existing article, or null when the media does not offer it. |
**project** | [**\Growwer\Api\Model\ProjectCatalogueMediaAllOfProject**](ProjectCatalogueMediaAllOfProject.md) |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
