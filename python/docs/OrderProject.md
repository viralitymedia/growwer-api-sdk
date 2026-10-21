# OrderProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Null once the project is deleted. | 
**url** | **str** | The project&#39;s URL when the order was placed. | 

## Example

```python
from growwer.models.order_project import OrderProject

# TODO update the JSON string below
json = "{}"
# create an instance of OrderProject from a JSON string
order_project_instance = OrderProject.from_json(json)
# print the JSON string representation of the object
print(OrderProject.to_json())

# convert the object into a dict
order_project_dict = order_project_instance.to_dict()
# create an instance of OrderProject from a dict
order_project_from_dict = OrderProject.from_dict(order_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


