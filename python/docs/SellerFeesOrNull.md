# SellerFeesOrNull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_when_seller_writes_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post you write, or null when you do not offer it. | 
**fee_when_seller_does_not_write_post** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post the buyer or Growwer writes, or null when you do not offer it. | 

## Example

```python
from growwer.models.seller_fees_or_null import SellerFeesOrNull

# TODO update the JSON string below
json = "{}"
# create an instance of SellerFeesOrNull from a JSON string
seller_fees_or_null_instance = SellerFeesOrNull.from_json(json)
# print the JSON string representation of the object
print(SellerFeesOrNull.to_json())

# convert the object into a dict
seller_fees_or_null_dict = seller_fees_or_null_instance.to_dict()
# create an instance of SellerFeesOrNull from a dict
seller_fees_or_null_from_dict = SellerFeesOrNull.from_dict(seller_fees_or_null_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


