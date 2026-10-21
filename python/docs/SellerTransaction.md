# SellerTransaction

A movement of your seller wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**type** | **str** | What moved the money, for example &#x60;credit_from_order&#x60; (an order you delivered), &#x60;credit_from_writing&#x60;, &#x60;withdrawal&#x60;, &#x60;manual_deposit&#x60; or &#x60;manual_charge&#x60;. | 
**state** | **str** | An order&#39;s earning stays &#x60;pending_confirmation&#x60; until the order settles. | 
**direction** | **str** |  | 
**amount** | [**Money**](Money.md) |  | 
**description** | **str** | The text the wallet page prints, or null when the movement points to an order or a withdrawal instead, or has no text. | 
**order_id** | **UUID** | Your order this earning came from, while it exists; GET /seller/orders/{id} reads it. | 
**withdrawal_id** | **UUID** | Your withdrawal this debit paid; GET /withdrawals lists it. | 
**has_document** | **bool** | Whether GET /wallets/seller/transactions/{id}/document downloads a document for it. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from growwer.models.seller_transaction import SellerTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of SellerTransaction from a JSON string
seller_transaction_instance = SellerTransaction.from_json(json)
# print the JSON string representation of the object
print(SellerTransaction.to_json())

# convert the object into a dict
seller_transaction_dict = seller_transaction_instance.to_dict()
# create an instance of SellerTransaction from a dict
seller_transaction_from_dict = SellerTransaction.from_dict(seller_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


