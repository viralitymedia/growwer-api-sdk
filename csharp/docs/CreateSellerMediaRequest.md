# Growwer.Api.Model.CreateSellerMediaRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RootUrl** | **string** |  | 
**Typology** | **string** |  | 
**Country** | **string** | A country code from GET /vocabulary. | 
**Language** | **string** | A language code from GET /vocabulary. | 
**Topics** | **List&lt;int&gt;** | Topic ids from GET /vocabulary. | 
**BannedTopics** | **List&lt;int&gt;** | The topic ids from GET /vocabulary the media refuses. | [optional] 
**PostOffer** | [**CreateSellerMediaRequestPostOffer**](CreateSellerMediaRequestPostOffer.md) |  | 
**LinkAdditionOffer** | [**UpdateSellerMediaRequestLinkAdditionOffer**](UpdateSellerMediaRequestLinkAdditionOffer.md) |  | [optional] 
**ExtraServices** | [**List&lt;UpdateSellerMediaRequestExtraServicesInner&gt;**](UpdateSellerMediaRequestExtraServicesInner.md) |  | [optional] 
**AcceptMediaPublishingTerms** | **bool** | Must be true: you accept the media publishing terms. | 
**DeclareMediaOwnership** | **bool** | Must be true: you own or manage this media. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

