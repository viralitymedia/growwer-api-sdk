# SellerTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**type** | **string** | What moved the money, for example &#x60;credit_from_order&#x60; (an order you delivered), &#x60;credit_from_writing&#x60;, &#x60;withdrawal&#x60;, &#x60;manual_deposit&#x60; or &#x60;manual_charge&#x60;. |
**state** | **string** | An order&#39;s earning stays &#x60;pending_confirmation&#x60; until the order settles. |
**direction** | **string** |  |
**amount** | [**\Growwer\Api\Model\Money**](Money.md) |  |
**description** | **string** | The text the wallet page prints, or null when the movement points to an order or a withdrawal instead, or has no text. |
**order_id** | **string** | Your order this earning came from, while it exists; GET /seller/orders/{id} reads it. |
**withdrawal_id** | **string** | Your withdrawal this debit paid; GET /withdrawals lists it. |
**has_document** | **bool** | Whether GET /wallets/seller/transactions/{id}/document downloads a document for it. |
**created_at** | **\DateTime** |  |
**updated_at** | **\DateTime** |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
