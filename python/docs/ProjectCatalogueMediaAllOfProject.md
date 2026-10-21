# ProjectCatalogueMediaAllOfProject

The media's state in the project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favourite** | **bool** |  | 
**discarded** | **bool** |  | 
**requested** | **bool** |  | 
**recommended** | **bool** | Growwer recommends the media for the project. | 
**bought** | **bool** | You have ordered on the media for the project. | 
**new** | **bool** | Growwer matched the media with the project recently. | 

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


