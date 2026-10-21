# UpdateSellerMediaRequestExtraServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cost** | [**Money**](Money.md) | What you are paid for the extra service. | 

## Example

```python
from growwer.models.update_seller_media_request_extra_services_inner import UpdateSellerMediaRequestExtraServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSellerMediaRequestExtraServicesInner from a JSON string
update_seller_media_request_extra_services_inner_instance = UpdateSellerMediaRequestExtraServicesInner.from_json(json)
# print the JSON string representation of the object
print(UpdateSellerMediaRequestExtraServicesInner.to_json())

# convert the object into a dict
update_seller_media_request_extra_services_inner_dict = update_seller_media_request_extra_services_inner_instance.to_dict()
# create an instance of UpdateSellerMediaRequestExtraServicesInner from a dict
update_seller_media_request_extra_services_inner_from_dict = UpdateSellerMediaRequestExtraServicesInner.from_dict(update_seller_media_request_extra_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


