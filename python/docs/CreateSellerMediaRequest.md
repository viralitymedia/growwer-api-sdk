# CreateSellerMediaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_url** | **str** |  | 
**typology** | **str** |  | 
**country** | **str** | A country code from GET /vocabulary. | 
**language** | **str** | A language code from GET /vocabulary. | 
**topics** | **List[int]** | Topic ids from GET /vocabulary. | 
**banned_topics** | **List[int]** | The topic ids from GET /vocabulary the media refuses. | [optional] 
**post_offer** | [**CreateSellerMediaRequestPostOffer**](CreateSellerMediaRequestPostOffer.md) |  | 
**link_addition_offer** | [**UpdateSellerMediaRequestLinkAdditionOffer**](UpdateSellerMediaRequestLinkAdditionOffer.md) |  | [optional] 
**extra_services** | [**List[UpdateSellerMediaRequestExtraServicesInner]**](UpdateSellerMediaRequestExtraServicesInner.md) |  | [optional] 
**accept_media_publishing_terms** | **bool** | Must be true: you accept the media publishing terms. | 
**declare_media_ownership** | **bool** | Must be true: you own or manage this media. | 

## Example

```python
from growwer.models.create_seller_media_request import CreateSellerMediaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSellerMediaRequest from a JSON string
create_seller_media_request_instance = CreateSellerMediaRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSellerMediaRequest.to_json())

# convert the object into a dict
create_seller_media_request_dict = create_seller_media_request_instance.to_dict()
# create an instance of CreateSellerMediaRequest from a dict
create_seller_media_request_from_dict = CreateSellerMediaRequest.from_dict(create_seller_media_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


