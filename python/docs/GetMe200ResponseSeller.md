# GetMe200ResponseSeller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**Balance**](Balance.md) |  | 
**restricted** | **bool** | Whether your seller account is restricted: it accepts no orders and its balance is held. Contact support for the reason. | 
**on_holiday** | **bool** | Whether you are on holiday: your medias take no orders. Set it with PUT /seller/holiday. | 
**holiday_end_date** | **date** | The day your holiday ends, at 00:00 of that day in Growwer&#39;s server time, or null when you are not on holiday or end it yourself. | 

## Example

```python
from growwer.models.get_me200_response_seller import GetMe200ResponseSeller

# TODO update the JSON string below
json = "{}"
# create an instance of GetMe200ResponseSeller from a JSON string
get_me200_response_seller_instance = GetMe200ResponseSeller.from_json(json)
# print the JSON string representation of the object
print(GetMe200ResponseSeller.to_json())

# convert the object into a dict
get_me200_response_seller_dict = get_me200_response_seller_instance.to_dict()
# create an instance of GetMe200ResponseSeller from a dict
get_me200_response_seller_from_dict = GetMe200ResponseSeller.from_dict(get_me200_response_seller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


