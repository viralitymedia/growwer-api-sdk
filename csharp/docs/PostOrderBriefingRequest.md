# Growwer.Api.Model.PostOrderBriefingRequest
The briefing of a post order (`type` `post`), checked against the media's post offer as the web checks it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Links** | [**List&lt;OrderLinkRequest&gt;**](OrderLinkRequest.md) | No more links than the offer allows. | 
**ExtraServices** | **List&lt;PostOrderBriefingRequest.ExtraServicesEnum&gt;** | Extra services the offer has, added to the ones the web selects for your project by default. A project with a sensitive topic always carries &#x60;extra_charge_for_sensitive_topic&#x60; when the media charges it. | [optional] 
**Title** | **string** |  | [optional] 
**AdditionalInfo** | **string** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

