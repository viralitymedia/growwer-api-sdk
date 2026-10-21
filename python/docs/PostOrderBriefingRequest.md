# PostOrderBriefingRequest

The briefing of a post order (`type` `post`), checked against the media's post offer as the web checks it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[OrderLinkRequest]**](OrderLinkRequest.md) | No more links than the offer allows. | 
**extra_services** | **List[str]** | Extra services the offer has, added to the ones the web selects for your project by default. A project with a sensitive topic always carries &#x60;extra_charge_for_sensitive_topic&#x60; when the media charges it. | [optional] 
**title** | **str** |  | [optional] 
**additional_info** | **str** |  | [optional] 

## Example

```python
from growwer.models.post_order_briefing_request import PostOrderBriefingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostOrderBriefingRequest from a JSON string
post_order_briefing_request_instance = PostOrderBriefingRequest.from_json(json)
# print the JSON string representation of the object
print(PostOrderBriefingRequest.to_json())

# convert the object into a dict
post_order_briefing_request_dict = post_order_briefing_request_instance.to_dict()
# create an instance of PostOrderBriefingRequest from a dict
post_order_briefing_request_from_dict = PostOrderBriefingRequest.from_dict(post_order_briefing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


