# OrderEstimateRequestBriefing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[OrderLinkRequest]**](OrderLinkRequest.md) | No more links than the offer allows. | 
**extra_services** | **List[str]** | Extra services the offer has, added to the ones the web selects for your project by default. A project with a sensitive topic always carries &#x60;extra_charge_for_sensitive_topic&#x60; when the media charges it. | [optional] 
**title** | **str** |  | [optional] 
**additional_info** | **str** |  | [optional] 
**linking_from** | **str** | The URL of an existing article on the media&#39;s domain that the link goes into. | 
**link** | [**OrderLinkRequest**](OrderLinkRequest.md) |  | 

## Example

```python
from growwer.models.order_estimate_request_briefing import OrderEstimateRequestBriefing

# TODO update the JSON string below
json = "{}"
# create an instance of OrderEstimateRequestBriefing from a JSON string
order_estimate_request_briefing_instance = OrderEstimateRequestBriefing.from_json(json)
# print the JSON string representation of the object
print(OrderEstimateRequestBriefing.to_json())

# convert the object into a dict
order_estimate_request_briefing_dict = order_estimate_request_briefing_instance.to_dict()
# create an instance of OrderEstimateRequestBriefing from a dict
order_estimate_request_briefing_from_dict = OrderEstimateRequestBriefing.from_dict(order_estimate_request_briefing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


