# SellerOrderRejection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**SellerOrderRejectionReason**](SellerOrderRejectionReason.md) |  | 

## Example

```python
from growwer.models.seller_order_rejection import SellerOrderRejection

# TODO update the JSON string below
json = "{}"
# create an instance of SellerOrderRejection from a JSON string
seller_order_rejection_instance = SellerOrderRejection.from_json(json)
# print the JSON string representation of the object
print(SellerOrderRejection.to_json())

# convert the object into a dict
seller_order_rejection_dict = seller_order_rejection_instance.to_dict()
# create an instance of SellerOrderRejection from a dict
seller_order_rejection_from_dict = SellerOrderRejection.from_dict(seller_order_rejection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


