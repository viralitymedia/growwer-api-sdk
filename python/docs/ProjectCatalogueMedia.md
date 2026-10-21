# ProjectCatalogueMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**domain** | **str** |  | 
**type** | **str** |  | 
**language** | **str** | A language code, as in GET /vocabulary. | 
**country** | **str** | A country code, as in GET /vocabulary, or null for none. | 
**topics** | **List[int]** | Topic ids, as in GET /vocabulary. | 
**metrics** | [**CatalogueMediaMetrics**](CatalogueMediaMetrics.md) |  | 
**positive_traffic_trend** | **bool** |  | 
**best_seller** | **bool** |  | 
**publication_rate** | **int** | The share of the media&#39;s orders that were published, in percent, or null without orders. | 
**average_days_to_publication** | **int** | The average days from order to publication, or null without published orders. | 
**on_holiday** | **bool** | Whether the media is on holiday and will take longer to publish. | 
**flash_offer** | [**CatalogueMediaFlashOffer**](CatalogueMediaFlashOffer.md) |  | 
**post_offer** | [**CataloguePostOffer**](CataloguePostOffer.md) |  | 
**link_addition_offer** | [**CatalogueOfferOrNull**](CatalogueOfferOrNull.md) | Adding a link to an existing article, or null when the media does not offer it. | 
**project** | [**ProjectCatalogueMediaAllOfProject**](ProjectCatalogueMediaAllOfProject.md) |  | 

## Example

```python
from growwer.models.project_catalogue_media import ProjectCatalogueMedia

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCatalogueMedia from a JSON string
project_catalogue_media_instance = ProjectCatalogueMedia.from_json(json)
# print the JSON string representation of the object
print(ProjectCatalogueMedia.to_json())

# convert the object into a dict
project_catalogue_media_dict = project_catalogue_media_instance.to_dict()
# create an instance of ProjectCatalogueMedia from a dict
project_catalogue_media_from_dict = ProjectCatalogueMedia.from_dict(project_catalogue_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


