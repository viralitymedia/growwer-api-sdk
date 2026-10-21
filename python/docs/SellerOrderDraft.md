# SellerOrderDraft

The draft of a post order that has one; null otherwise, and always for a link addition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewable** | **bool** | Whether the buyer reviews the draft before it is published. | 
**has_file** | **bool** | Whether the current draft has a file; GET /seller/orders/{id}/draft downloads it. | 

## Example

```python
from growwer.models.seller_order_draft import SellerOrderDraft

# TODO update the JSON string below
json = "{}"
# create an instance of SellerOrderDraft from a JSON string
seller_order_draft_instance = SellerOrderDraft.from_json(json)
# print the JSON string representation of the object
print(SellerOrderDraft.to_json())

# convert the object into a dict
seller_order_draft_dict = seller_order_draft_instance.to_dict()
# create an instance of SellerOrderDraft from a dict
seller_order_draft_from_dict = SellerOrderDraft.from_dict(seller_order_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


