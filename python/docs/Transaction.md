# Transaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**type** | **str** | What moved the money, for example &#x60;deposit&#x60; (a top-up), &#x60;debit_from_order&#x60; (an order), &#x60;gift&#x60; or &#x60;manual_charge&#x60;. | 
**state** | **str** | An order&#39;s debit stays &#x60;pending_confirmation&#x60; until the order settles, and is &#x60;cancelled&#x60; when the order is refunded. | 
**direction** | **str** |  | 
**amount** | [**Money**](Money.md) |  | 
**description** | **str** | The text the wallet page prints as it is, or null where it prints a translated label instead (then see &#x60;descriptionCode&#x60;). | 
**description_code** | **str** | A stable code for the label the wallet page translates: a payment method for a top-up, or &#x60;affiliate_promo&#x60;. Null otherwise. | 
**order_id** | **UUID** | The order this transaction paid for or refunded, while it exists. | 
**invoice_id** | **UUID** | The invoice of this transaction, if any; GET /invoices/{id}/pdf downloads it. | 
**has_document** | **bool** | Whether GET /wallets/buyer/transactions/{id}/document downloads a document for it. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from growwer.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


