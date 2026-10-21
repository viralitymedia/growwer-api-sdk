# LinkAdditionOrderBriefingRequest

The briefing of a link addition (`type` `link_addition`), checked against the media's link addition offer as the web checks it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linking_from** | **str** | The URL of an existing article on the media&#39;s domain that the link goes into. | 
**link** | [**OrderLinkRequest**](OrderLinkRequest.md) |  | 
**additional_info** | **str** |  | [optional] 

## Example

```python
from growwer.models.link_addition_order_briefing_request import LinkAdditionOrderBriefingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkAdditionOrderBriefingRequest from a JSON string
link_addition_order_briefing_request_instance = LinkAdditionOrderBriefingRequest.from_json(json)
# print the JSON string representation of the object
print(LinkAdditionOrderBriefingRequest.to_json())

# convert the object into a dict
link_addition_order_briefing_request_dict = link_addition_order_briefing_request_instance.to_dict()
# create an instance of LinkAdditionOrderBriefingRequest from a dict
link_addition_order_briefing_request_from_dict = LinkAdditionOrderBriefingRequest.from_dict(link_addition_order_briefing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


