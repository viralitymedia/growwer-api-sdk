# OrderLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_url** | **str** | Where the link points; leave it out for a citation. | [optional] 
**anchor** | **str** | The anchor text; leave it out to let the media choose it. A citation needs one. | [optional] 
**type** | **str** | A link type the media offers for this type of order (CatalogueOffer &#x60;linkTypes&#x60;). | 

## Example

```python
from growwer.models.order_link_request import OrderLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLinkRequest from a JSON string
order_link_request_instance = OrderLinkRequest.from_json(json)
# print the JSON string representation of the object
print(OrderLinkRequest.to_json())

# convert the object into a dict
order_link_request_dict = order_link_request_instance.to_dict()
# create an instance of OrderLinkRequest from a dict
order_link_request_from_dict = OrderLinkRequest.from_dict(order_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


