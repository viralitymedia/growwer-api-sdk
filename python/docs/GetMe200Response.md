# GetMe200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**email** | **str** |  | 
**first_name** | **str** |  | 
**language** | **str** | The language Growwer writes to you in. | 
**created_at** | **datetime** |  | 
**buyer** | [**GetMe200ResponseBuyer**](GetMe200ResponseBuyer.md) |  | 
**seller** | [**GetMe200ResponseSeller**](GetMe200ResponseSeller.md) |  | 
**catalogue** | [**GetMe200ResponseCatalogue**](GetMe200ResponseCatalogue.md) |  | 
**managed_service** | [**GetMe200ResponseManagedService**](GetMe200ResponseManagedService.md) |  | 
**mode** | **str** | The mode of the key you called with. &#x60;live&#x60; works on your real account; &#x60;test&#x60; works in test mode, where nothing you do reaches real sellers, money or orders. Every response to a test key also carries the header &#x60;Growwer-Mode: test&#x60;. | 

## Example

```python
from growwer.models.get_me200_response import GetMe200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMe200Response from a JSON string
get_me200_response_instance = GetMe200Response.from_json(json)
# print the JSON string representation of the object
print(GetMe200Response.to_json())

# convert the object into a dict
get_me200_response_dict = get_me200_response_instance.to_dict()
# create an instance of GetMe200Response from a dict
get_me200_response_from_dict = GetMe200Response.from_dict(get_me200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


