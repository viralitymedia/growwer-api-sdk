# ProjectCatalogueMediaAllOfProjectAiKeywords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** |  | 
**source** | **str** | The AI engine that gave the keyword, as the &#x60;ranksAiKeyword&#x60; filter names it, or null for an engine it does not name. It is never where the media comes from. | 

## Example

```python
from growwer.models.project_catalogue_media_all_of_project_ai_keywords import ProjectCatalogueMediaAllOfProjectAiKeywords

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCatalogueMediaAllOfProjectAiKeywords from a JSON string
project_catalogue_media_all_of_project_ai_keywords_instance = ProjectCatalogueMediaAllOfProjectAiKeywords.from_json(json)
# print the JSON string representation of the object
print(ProjectCatalogueMediaAllOfProjectAiKeywords.to_json())

# convert the object into a dict
project_catalogue_media_all_of_project_ai_keywords_dict = project_catalogue_media_all_of_project_ai_keywords_instance.to_dict()
# create an instance of ProjectCatalogueMediaAllOfProjectAiKeywords from a dict
project_catalogue_media_all_of_project_ai_keywords_from_dict = ProjectCatalogueMediaAllOfProjectAiKeywords.from_dict(project_catalogue_media_all_of_project_ai_keywords_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


