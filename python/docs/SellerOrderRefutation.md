# SellerOrderRefutation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Why you refuse the buyer&#39;s request, which the buyer is told, 10 to 2000 characters once trimmed. | 

## Example

```python
from growwer.models.seller_order_refutation import SellerOrderRefutation

# TODO update the JSON string below
json = "{}"
# create an instance of SellerOrderRefutation from a JSON string
seller_order_refutation_instance = SellerOrderRefutation.from_json(json)
# print the JSON string representation of the object
print(SellerOrderRefutation.to_json())

# convert the object into a dict
seller_order_refutation_dict = seller_order_refutation_instance.to_dict()
# create an instance of SellerOrderRefutation from a dict
seller_order_refutation_from_dict = SellerOrderRefutation.from_dict(seller_order_refutation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


