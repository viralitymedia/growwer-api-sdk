# OrderDraft

The draft of a post order that has one; null otherwise, and always for a link addition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authored_by_buyer** | **bool** | Whether you write the draft. | 
**reviewable** | **bool** | Whether you review the draft before it is published. | 
**has_file** | **bool** | Whether the current draft has a file; GET /orders/{id}/draft downloads it. | 

## Example

```python
from growwer.models.order_draft import OrderDraft

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDraft from a JSON string
order_draft_instance = OrderDraft.from_json(json)
# print the JSON string representation of the object
print(OrderDraft.to_json())

# convert the object into a dict
order_draft_dict = order_draft_instance.to_dict()
# create an instance of OrderDraft from a dict
order_draft_from_dict = OrderDraft.from_dict(order_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


