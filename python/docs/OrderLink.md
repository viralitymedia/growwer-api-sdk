# OrderLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_url** | **str** | Where the link points, or null for a citation. | 
**anchor** | **str** | The anchor text, or null when the media chooses it. A citation always has one. | 
**type** | **str** |  | 

## Example

```python
from growwer.models.order_link import OrderLink

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLink from a JSON string
order_link_instance = OrderLink.from_json(json)
# print the JSON string representation of the object
print(OrderLink.to_json())

# convert the object into a dict
order_link_dict = order_link_instance.to_dict()
# create an instance of OrderLink from a dict
order_link_from_dict = OrderLink.from_dict(order_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


