# Growwer.Api.Model.Project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Name** | **string** | Your name for the project, or null when it has none. | 
**RootUrl** | **string** | The website the project promotes. It cannot be changed once the project exists. | 
**WebsiteType** | **string** | What the website is: an online shop (&#x60;ecommerce&#x60;), a services business (&#x60;services&#x60;) or anything else (&#x60;other&#x60;). | 
**Topics** | **List&lt;int&gt;** | The website&#39;s topic, as a topic id from GET /vocabulary. Exactly one. | 
**Language** | **string** | The language of the campaign, as a language code from GET /vocabulary. | 
**Country** | **string** | The country the campaign targets, as a country code from GET /vocabulary, or null for worldwide. | 
**PromotedProducts** | **List&lt;string&gt;** | The products or services the campaign promotes, 5 to 10. | 
**UserKeywords** | **List&lt;string&gt;** | Keywords you want the campaign to target, at most 100. | 
**State** | **string** | &#x60;finished&#x60; once Growwer has recommended media for the project, &#x60;analyzing&#x60; until then. Analysis can take hours, and it never finishes when no medium matches the project. Poll with backoff, and use &#x60;createdAt&#x60; to decide how long to keep polling.  | 
**CreatedAt** | **DateTime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

