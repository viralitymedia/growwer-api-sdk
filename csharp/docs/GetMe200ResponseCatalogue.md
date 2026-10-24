# Growwer.Api.Model.GetMe200ResponseCatalogue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Eligible** | **bool** | Whether you have the full daily cap of the catalogue operations (tag Catalogue: searching a project&#39;s medias, flash offers and media details). It is open to accounts with recent completed orders, as buyer or as seller; until then the catalogue answers within a smaller daily trial quota, which rises to the full cap after a completed order. A media you have ordered is always readable with GET /medias/{id} and counts against neither. | 
**DailyCap** | **int** | How many distinct medias the catalogue operations show you per UTC day: the full cap when &#x60;eligible&#x60; is true, the trial quota otherwise. 0 means the catalogue answers 403 &#x60;catalogue_requires_recent_order&#x60; until you have a recent completed order. | 
**RemainingToday** | **int?** | How many units of &#x60;dailyCap&#x60; still fit today (UTC): each new distinct media costs one, and a catalogue response that holds no new media, an empty one or a saved filter count included, costs one unless the same request was answered today and the media lists, topics and language of its project have not changed since. Medias you have already seen today, and requests already answered today, are free. Null when the count cannot be read right now; the catalogue operations then answer 503 until it can. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

