# PutSellerHoliday200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_holiday** | **bool** |  | 
**end_date** | **date** | The day the holiday ends, at 00:00 of that day in Growwer&#39;s server time, or null for none. | 

## Example

```python
from growwer.models.put_seller_holiday200_response import PutSellerHoliday200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PutSellerHoliday200Response from a JSON string
put_seller_holiday200_response_instance = PutSellerHoliday200Response.from_json(json)
# print the JSON string representation of the object
print(PutSellerHoliday200Response.to_json())

# convert the object into a dict
put_seller_holiday200_response_dict = put_seller_holiday200_response_instance.to_dict()
# create an instance of PutSellerHoliday200Response from a dict
put_seller_holiday200_response_from_dict = PutSellerHoliday200Response.from_dict(put_seller_holiday200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


