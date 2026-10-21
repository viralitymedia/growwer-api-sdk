# Growwer.Api.Model.Withdrawal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**State** | **string** |  | 
**Amount** | [**Money**](Money.md) | What you withdraw. | 
**Method** | **string** |  | 
**HasInvoice** | **bool** | Whether you uploaded an invoice; GET /withdrawals/{id}/invoice downloads it. | 
**CreatedAt** | **DateTime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

