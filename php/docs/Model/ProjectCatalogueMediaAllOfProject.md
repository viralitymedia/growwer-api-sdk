# ProjectCatalogueMediaAllOfProject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favourite** | **bool** |  |
**discarded** | **bool** |  |
**requested** | **bool** |  |
**recommended** | **bool** | Growwer recommends the media for the project. |
**bought** | **bool** | You have ordered on the media for the project. |
**new** | **bool** | Growwer matched the media with the project recently. |
**ai_keywords** | [**\Growwer\Api\Model\ProjectCatalogueMediaAllOfProjectAiKeywords[]**](ProjectCatalogueMediaAllOfProjectAiKeywords.md) | The AI keywords the web lists for the media in this project, one entry per keyword of each stored source, empty when there are none. Keywords an AI answer gave without referencing any domain may be listed for every media of the project, so an entry does not mean that the engine cited the media. Entries keep their order within an engine, and a keyword listed by two engines appears once for each; the order of the engines is not promised. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
