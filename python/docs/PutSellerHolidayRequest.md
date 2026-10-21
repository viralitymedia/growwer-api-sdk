# PutSellerHolidayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_holiday** | **bool** |  | 
**end_date** | **date** |  | [optional] 

## Example

```python
from growwer.models.put_seller_holiday_request import PutSellerHolidayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutSellerHolidayRequest from a JSON string
put_seller_holiday_request_instance = PutSellerHolidayRequest.from_json(json)
# print the JSON string representation of the object
print(PutSellerHolidayRequest.to_json())

# convert the object into a dict
put_seller_holiday_request_dict = put_seller_holiday_request_instance.to_dict()
# create an instance of PutSellerHolidayRequest from a dict
put_seller_holiday_request_from_dict = PutSellerHolidayRequest.from_dict(put_seller_holiday_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


