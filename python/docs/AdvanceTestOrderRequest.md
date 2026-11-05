# AdvanceTestOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The state to move the test order to. | 

## Example

```python
from growwer.models.advance_test_order_request import AdvanceTestOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvanceTestOrderRequest from a JSON string
advance_test_order_request_instance = AdvanceTestOrderRequest.from_json(json)
# print the JSON string representation of the object
print(AdvanceTestOrderRequest.to_json())

# convert the object into a dict
advance_test_order_request_dict = advance_test_order_request_instance.to_dict()
# create an instance of AdvanceTestOrderRequest from a dict
advance_test_order_request_from_dict = AdvanceTestOrderRequest.from_dict(advance_test_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


