# UpdateSellerMediaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typology** | **str** |  | [optional] 
**post_offer** | [**UpdateSellerMediaRequestPostOffer**](UpdateSellerMediaRequestPostOffer.md) |  | [optional] 
**link_addition_offer** | [**UpdateSellerMediaRequestLinkAdditionOffer**](UpdateSellerMediaRequestLinkAdditionOffer.md) |  | [optional] 
**extra_services** | [**List[UpdateSellerMediaRequestExtraServicesInner]**](UpdateSellerMediaRequestExtraServicesInner.md) |  | [optional] 

## Example

```python
from growwer.models.update_seller_media_request import UpdateSellerMediaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSellerMediaRequest from a JSON string
update_seller_media_request_instance = UpdateSellerMediaRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSellerMediaRequest.to_json())

# convert the object into a dict
update_seller_media_request_dict = update_seller_media_request_instance.to_dict()
# create an instance of UpdateSellerMediaRequest from a dict
update_seller_media_request_from_dict = UpdateSellerMediaRequest.from_dict(update_seller_media_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


