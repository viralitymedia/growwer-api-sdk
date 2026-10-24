# SellerOrderPostDelivery

The published post of a post order. A link addition order takes no body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the published post. It is checked to be a URL without &#x60;&lt;&#x60; or &#x60;&gt;&#x60;, as the web does; whether the post carries the links is not checked here. | 
**publication_date_confirmed** | **bool** | Must be true. Confirms the post is live, or for an order with a scheduled publication date, that it will be published on that date. | 

## Example

```python
from growwer.models.seller_order_post_delivery import SellerOrderPostDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of SellerOrderPostDelivery from a JSON string
seller_order_post_delivery_instance = SellerOrderPostDelivery.from_json(json)
# print the JSON string representation of the object
print(SellerOrderPostDelivery.to_json())

# convert the object into a dict
seller_order_post_delivery_dict = seller_order_post_delivery_instance.to_dict()
# create an instance of SellerOrderPostDelivery from a dict
seller_order_post_delivery_from_dict = SellerOrderPostDelivery.from_dict(seller_order_post_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


