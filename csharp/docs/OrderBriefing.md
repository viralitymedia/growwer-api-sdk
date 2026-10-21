# Growwer.Api.Model.OrderBriefing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Title** | **string** |  | 
**Language** | **string** | The language code of the article. | 
**Links** | [**List&lt;OrderLink&gt;**](OrderLink.md) |  | 
**ExtraServices** | **List&lt;OrderBriefing.ExtraServicesEnum&gt;** |  | 
**AdditionalInfo** | **string** |  | 
**HasProposedDraft** | **bool** | Whether you attached your own draft; GET /orders/{id}/briefing downloads it. | 
**LinkingFrom** | **string** | The existing article of the media the link goes into. | 
**Link** | [**OrderLink**](OrderLink.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

