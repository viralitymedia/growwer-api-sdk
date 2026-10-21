# CatalogueMediaMetrics

The latest measurements; each is null until it is first measured.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organic_traffic** | **float** | Monthly organic traffic. | 
**domain_rating** | **float** |  | 
**referring_domains** | **float** |  | 
**linked_domains** | **float** |  | 
**linked_to_referring_ratio** | **float** |  | 

## Example

```python
from growwer.models.catalogue_media_metrics import CatalogueMediaMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogueMediaMetrics from a JSON string
catalogue_media_metrics_instance = CatalogueMediaMetrics.from_json(json)
# print the JSON string representation of the object
print(CatalogueMediaMetrics.to_json())

# convert the object into a dict
catalogue_media_metrics_dict = catalogue_media_metrics_instance.to_dict()
# create an instance of CatalogueMediaMetrics from a dict
catalogue_media_metrics_from_dict = CatalogueMediaMetrics.from_dict(catalogue_media_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


