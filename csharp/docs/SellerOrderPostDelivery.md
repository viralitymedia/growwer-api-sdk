# Growwer.Api.Model.SellerOrderPostDelivery
The published post of a post order. A link addition order takes no body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | **string** | The URL of the published post. It is checked to be a URL without &#x60;&lt;&#x60; or &#x60;&gt;&#x60;, as the web does; whether the post carries the links is not checked here. | 
**PublicationDateConfirmed** | **bool** | Must be true. Confirms the post is live, or for an order with a scheduled publication date, that it will be published on that date. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

