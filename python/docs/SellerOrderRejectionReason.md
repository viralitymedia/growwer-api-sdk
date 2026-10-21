# SellerOrderRejectionReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Why you reject the order, as the seller order page offers it. | 
**additional_info** | **str** | More about the reason, which the buyer is told, 10 to 2000 characters. Required with &#x60;other_reasons&#x60;. | [optional] 

## Example

```python
from growwer.models.seller_order_rejection_reason import SellerOrderRejectionReason

# TODO update the JSON string below
json = "{}"
# create an instance of SellerOrderRejectionReason from a JSON string
seller_order_rejection_reason_instance = SellerOrderRejectionReason.from_json(json)
# print the JSON string representation of the object
print(SellerOrderRejectionReason.to_json())

# convert the object into a dict
seller_order_rejection_reason_dict = seller_order_rejection_reason_instance.to_dict()
# create an instance of SellerOrderRejectionReason from a dict
seller_order_rejection_reason_from_dict = SellerOrderRejectionReason.from_dict(seller_order_rejection_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


