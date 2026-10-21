# Growwer::ProjectCatalogueMedia

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **domain** | **String** |  |  |
| **type** | **String** |  |  |
| **language** | **String** | A language code, as in GET /vocabulary. |  |
| **country** | **String** | A country code, as in GET /vocabulary, or null for none. |  |
| **topics** | **Array&lt;Integer&gt;** | Topic ids, as in GET /vocabulary. |  |
| **metrics** | [**CatalogueMediaMetrics**](CatalogueMediaMetrics.md) |  |  |
| **positive_traffic_trend** | **Boolean** |  |  |
| **best_seller** | **Boolean** |  |  |
| **publication_rate** | **Integer** | The share of the media&#39;s orders that were published, in percent, or null without orders. |  |
| **average_days_to_publication** | **Integer** | The average days from order to publication, or null without published orders. |  |
| **on_holiday** | **Boolean** | Whether the media is on holiday and will take longer to publish. |  |
| **flash_offer** | [**CatalogueMediaFlashOffer**](CatalogueMediaFlashOffer.md) |  |  |
| **post_offer** | [**CataloguePostOffer**](CataloguePostOffer.md) |  |  |
| **link_addition_offer** | [**CatalogueOfferOrNull**](CatalogueOfferOrNull.md) | Adding a link to an existing article, or null when the media does not offer it. |  |
| **project** | [**ProjectCatalogueMediaAllOfProject**](ProjectCatalogueMediaAllOfProject.md) |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::ProjectCatalogueMedia.new(
  id: null,
  domain: example.com,
  type: null,
  language: null,
  country: null,
  topics: null,
  metrics: null,
  positive_traffic_trend: null,
  best_seller: null,
  publication_rate: null,
  average_days_to_publication: null,
  on_holiday: null,
  flash_offer: null,
  post_offer: null,
  link_addition_offer: null,
  project: null
)
```

