# Growwer.Api.Model.SellerTransaction
A movement of your seller wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Type** | **string** | What moved the money, for example &#x60;credit_from_order&#x60; (an order you delivered), &#x60;credit_from_writing&#x60;, &#x60;withdrawal&#x60;, &#x60;manual_deposit&#x60; or &#x60;manual_charge&#x60;. | 
**State** | **string** | An order&#39;s earning stays &#x60;pending_confirmation&#x60; until the order settles. | 
**Direction** | **string** |  | 
**Amount** | [**Money**](Money.md) |  | 
**Description** | **string** | The text the wallet page prints, or null when the movement points to an order or a withdrawal instead, or has no text. | 
**OrderId** | **Guid?** | Your order this earning came from, while it exists; GET /seller/orders/{id} reads it. | 
**WithdrawalId** | **Guid?** | Your withdrawal this debit paid; GET /withdrawals lists it. | 
**HasDocument** | **bool** | Whether GET /wallets/seller/transactions/{id}/document downloads a document for it. | 
**CreatedAt** | **DateTime** |  | 
**UpdatedAt** | **DateTime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

