# SellerFees


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_when_seller_writes_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post you write, or null when you do not offer it. | 
**fee_when_seller_does_not_write_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post the buyer or Growwer writes, or null when you do not offer it. | 

## Example

```python
from growwer.models.seller_fees import SellerFees

# TODO update the JSON string below
json = "{}"
# create an instance of SellerFees from a JSON string
seller_fees_instance = SellerFees.from_json(json)
# print the JSON string representation of the object
print(SellerFees.to_json())

# convert the object into a dict
seller_fees_dict = seller_fees_instance.to_dict()
# create an instance of SellerFees from a dict
seller_fees_from_dict = SellerFees.from_dict(seller_fees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


