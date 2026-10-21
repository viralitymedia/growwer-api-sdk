# SellerOrderProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL the buyer promotes, as recorded when the order was placed. | 

## Example

```python
from growwer.models.seller_order_project import SellerOrderProject

# TODO update the JSON string below
json = "{}"
# create an instance of SellerOrderProject from a JSON string
seller_order_project_instance = SellerOrderProject.from_json(json)
# print the JSON string representation of the object
print(SellerOrderProject.to_json())

# convert the object into a dict
seller_order_project_dict = seller_order_project_instance.to_dict()
# create an instance of SellerOrderProject from a dict
seller_order_project_from_dict = SellerOrderProject.from_dict(seller_order_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


