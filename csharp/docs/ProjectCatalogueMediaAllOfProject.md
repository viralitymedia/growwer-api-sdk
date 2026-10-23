# Growwer.Api.Model.ProjectCatalogueMediaAllOfProject
The media's state in the project, and the AI keywords the web lists for the media in this project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Favourite** | **bool** |  | 
**Discarded** | **bool** |  | 
**Requested** | **bool** |  | 
**Recommended** | **bool** | Growwer recommends the media for the project. | 
**Bought** | **bool** | You have ordered on the media for the project. | 
**New** | **bool** | Growwer matched the media with the project recently. | 
**AiKeywords** | [**List&lt;ProjectCatalogueMediaAllOfProjectAiKeywords&gt;**](ProjectCatalogueMediaAllOfProjectAiKeywords.md) | The AI keywords the web lists for the media in this project, one entry per keyword of each stored source, empty when there are none. Keywords an AI answer gave without referencing any domain may be listed for every media of the project, so an entry does not mean that the engine cited the media. Entries keep their order within an engine, and a keyword listed by two engines appears once for each; the order of the engines is not promised. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

