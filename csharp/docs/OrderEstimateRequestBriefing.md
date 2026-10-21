# Growwer.Api.Model.OrderEstimateRequestBriefing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Links** | [**List&lt;OrderLinkRequest&gt;**](OrderLinkRequest.md) | No more links than the offer allows. | 
**ExtraServices** | **List&lt;OrderEstimateRequestBriefing.ExtraServicesEnum&gt;** | Extra services the offer has, added to the ones the web selects for your project by default. A project with a sensitive topic always carries &#x60;extra_charge_for_sensitive_topic&#x60; when the media charges it. | [optional] 
**Title** | **string** |  | [optional] 
**AdditionalInfo** | **string** |  | [optional] 
**LinkingFrom** | **string** | The URL of an existing article on the media&#39;s domain that the link goes into. | 
**Link** | [**OrderLinkRequest**](OrderLinkRequest.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

