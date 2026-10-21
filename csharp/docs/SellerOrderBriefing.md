# Growwer.Api.Model.SellerOrderBriefing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Title** | **string** |  | 
**Language** | **string** | The language code of the article. | 
**Links** | [**List&lt;OrderLink&gt;**](OrderLink.md) |  | 
**ExtraServices** | **List&lt;SellerOrderBriefing.ExtraServicesEnum&gt;** |  | 
**AdditionalInfo** | **string** |  | 
**WrittenBy** | **string** | Who writes the article; &#x60;seller&#x60; means you do. | 
**HasProposedDraft** | **bool** | Whether the buyer attached a draft; GET /seller/orders/{id}/briefing downloads it. | 
**LinkingFrom** | **string** | The existing article of the media the link goes into. | 
**Link** | [**OrderLink**](OrderLink.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

