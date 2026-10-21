# Growwer.Api.Model.CreateProjectRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | [optional] 
**RootUrl** | **string** |  | 
**WebsiteType** | **string** |  | 
**Topics** | **List&lt;int&gt;** | Exactly one topic id from GET /vocabulary. | 
**Language** | **string** | A language code from GET /vocabulary. | 
**Country** | **string** | A country code from GET /vocabulary; omit it or send null for worldwide. | [optional] 
**PromotedProducts** | **List&lt;string&gt;** | 5 to 10 products or services the campaign promotes. | 
**UserKeywords** | **List&lt;string&gt;** | At most 100 keywords, none with a line break. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

