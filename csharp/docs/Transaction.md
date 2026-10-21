# Growwer.Api.Model.Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Type** | **string** | What moved the money, for example &#x60;deposit&#x60; (a top-up), &#x60;debit_from_order&#x60; (an order), &#x60;gift&#x60; or &#x60;manual_charge&#x60;. | 
**State** | **string** | An order&#39;s debit stays &#x60;pending_confirmation&#x60; until the order settles, and is &#x60;cancelled&#x60; when the order is refunded. | 
**Direction** | **string** |  | 
**Amount** | [**Money**](Money.md) |  | 
**Description** | **string** | The text the wallet page prints as it is, or null where it prints a translated label instead (then see &#x60;descriptionCode&#x60;). | 
**DescriptionCode** | **string** | A stable code for the label the wallet page translates: a payment method for a top-up, or &#x60;affiliate_promo&#x60;. Null otherwise. | 
**OrderId** | **Guid?** | The order this transaction paid for or refunded, while it exists. | 
**InvoiceId** | **Guid?** | The invoice of this transaction, if any; GET /invoices/{id}/pdf downloads it. | 
**HasDocument** | **bool** | Whether GET /wallets/buyer/transactions/{id}/document downloads a document for it. | 
**CreatedAt** | **DateTime** |  | 
**UpdatedAt** | **DateTime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

