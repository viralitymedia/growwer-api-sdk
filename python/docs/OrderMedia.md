# OrderMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Null once the media is deleted. | 
**url** | **str** | The media&#39;s URL when the order was placed. | 

## Example

```python
from growwer.models.order_media import OrderMedia

# TODO update the JSON string below
json = "{}"
# create an instance of OrderMedia from a JSON string
order_media_instance = OrderMedia.from_json(json)
# print the JSON string representation of the object
print(OrderMedia.to_json())

# convert the object into a dict
order_media_dict = order_media_instance.to_dict()
# create an instance of OrderMedia from a dict
order_media_from_dict = OrderMedia.from_dict(order_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


