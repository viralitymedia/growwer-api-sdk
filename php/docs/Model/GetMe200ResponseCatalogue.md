# GetMe200ResponseCatalogue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **bool** | Whether you have the full daily cap of the catalogue operations (tag Catalogue: searching a project&#39;s medias, flash offers and media details). It is open to accounts with recent completed orders, as buyer or as seller; until then the catalogue answers within a smaller daily trial quota, which rises to the full cap after a completed order. A media you have ordered is always readable with GET /medias/{id} and counts against neither. |
**daily_cap** | **int** | How many distinct medias the catalogue operations show you per UTC day: the full cap when &#x60;eligible&#x60; is true, the trial quota otherwise. 0 means the catalogue answers 403 &#x60;catalogue_requires_recent_order&#x60; until you have a recent completed order. |
**remaining_today** | **int** | How many new distinct medias still fit in &#x60;dailyCap&#x60; today (UTC). Medias you have already seen today are free. Null when the count cannot be read right now; the catalogue operations then answer 503 until it can. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
