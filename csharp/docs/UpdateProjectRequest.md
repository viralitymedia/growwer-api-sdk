# Growwer.Api.Model.UpdateProjectRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Null or an empty string removes the name. | [optional] 
**WebsiteType** | **string** |  | [optional] 
**Topics** | **List&lt;int&gt;** | Exactly one topic id from GET /vocabulary. | [optional] 
**Language** | **string** | A language code from GET /vocabulary. | [optional] 
**Country** | **string** | A country code from GET /vocabulary, or null for worldwide. | [optional] 
**PromotedProducts** | **List&lt;string&gt;** | 5 to 10 products or services the campaign promotes. | [optional] 
**UserKeywords** | **List&lt;string&gt;** | At most 100 keywords, none with a line break. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

