# Growwer.Api.Model.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | A stable, machine-readable error code. | 
**Message** | **string** | A human-readable explanation. It may change. | 
**RequestId** | **string** | UUID v4 generated per request, or the &#x60;X-Request-Id&#x60; you sent. Quote it when reporting a problem. | 
**Details** | **Dictionary&lt;string, Object&gt;** | Extra data on some errors, such as the invalid fields of a validation_failed error. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

