# Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**type** | **string** | What moved the money, for example &#x60;deposit&#x60; (a top-up), &#x60;debit_from_order&#x60; (an order), &#x60;gift&#x60; or &#x60;manual_charge&#x60;. |
**state** | **string** | An order&#39;s debit stays &#x60;pending_confirmation&#x60; until the order settles, and is &#x60;cancelled&#x60; when the order is refunded. |
**direction** | **string** |  |
**amount** | [**\Growwer\Api\Model\Money**](Money.md) |  |
**description** | **string** | The text the wallet page prints as it is, or null where it prints a translated label instead (then see &#x60;descriptionCode&#x60;). |
**description_code** | **string** | A stable code for the label the wallet page translates: a payment method for a top-up, or &#x60;affiliate_promo&#x60;. Null otherwise. |
**order_id** | **string** | The order this transaction paid for or refunded, while it exists. |
**invoice_id** | **string** | The invoice of this transaction, if any; GET /invoices/{id}/pdf downloads it. |
**has_document** | **bool** | Whether GET /wallets/buyer/transactions/{id}/document downloads a document for it. |
**created_at** | **\DateTime** |  |
**updated_at** | **\DateTime** |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
