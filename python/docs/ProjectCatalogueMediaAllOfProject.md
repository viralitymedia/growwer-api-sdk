# ProjectCatalogueMediaAllOfProject

The media's state in the project, and the AI keywords the web lists for the media in this project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favourite** | **bool** |  | 
**discarded** | **bool** |  | 
**requested** | **bool** |  | 
**recommended** | **bool** | Growwer recommends the media for the project. | 
**bought** | **bool** | You have ordered on the media for the project. | 
**new** | **bool** | Growwer matched the media with the project recently. | 
**ai_keywords** | [**List[ProjectCatalogueMediaAllOfProjectAiKeywords]**](ProjectCatalogueMediaAllOfProjectAiKeywords.md) | The AI keywords the web lists for the media in this project, one entry per keyword of each stored source, empty when there are none. Keywords an AI answer gave without referencing any domain may be listed for every media of the project, so an entry does not mean that the engine cited the media. Entries keep their order within an engine, and a keyword listed by two engines appears once for each; the order of the engines is not promised. | 

## Example

```python
from growwer.models.project_catalogue_media_all_of_project import ProjectCatalogueMediaAllOfProject

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCatalogueMediaAllOfProject from a JSON string
project_catalogue_media_all_of_project_instance = ProjectCatalogueMediaAllOfProject.from_json(json)
# print the JSON string representation of the object
print(ProjectCatalogueMediaAllOfProject.to_json())

# convert the object into a dict
project_catalogue_media_all_of_project_dict = project_catalogue_media_all_of_project_instance.to_dict()
# create an instance of ProjectCatalogueMediaAllOfProject from a dict
project_catalogue_media_all_of_project_from_dict = ProjectCatalogueMediaAllOfProject.from_dict(project_catalogue_media_all_of_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


