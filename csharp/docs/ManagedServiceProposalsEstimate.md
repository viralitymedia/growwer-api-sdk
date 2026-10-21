# Growwer.Api.Model.ManagedServiceProposalsEstimate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AcceptedTotal** | [**Money**](Money.md) | The proposals already accepted and still awaiting their order. | 
**SelectedTotal** | [**Money**](Money.md) | The proposals named in &#x60;accept&#x60;. | 
**Total** | [**Money**](Money.md) | &#x60;acceptedTotal&#x60; plus &#x60;selectedTotal&#x60;. | 
**AvailableBalance** | [**Money**](Money.md) | Your wallet&#39;s available balance. | 
**Missing** | [**Money**](Money.md) | How much the available balance falls short of &#x60;total&#x60;; zero when it covers it. | 
**SufficientBalance** | **bool** | Whether the available balance covers &#x60;total&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

