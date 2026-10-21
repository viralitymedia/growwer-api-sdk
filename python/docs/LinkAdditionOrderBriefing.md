# LinkAdditionOrderBriefing

The briefing of a link addition (`type` `link_addition`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linking_from** | **str** | The existing article of the media the link goes into. | 
**link** | [**OrderLink**](OrderLink.md) |  | 
**additional_info** | **str** |  | 

## Example

```python
from growwer.models.link_addition_order_briefing import LinkAdditionOrderBriefing

# TODO update the JSON string below
json = "{}"
# create an instance of LinkAdditionOrderBriefing from a JSON string
link_addition_order_briefing_instance = LinkAdditionOrderBriefing.from_json(json)
# print the JSON string representation of the object
print(LinkAdditionOrderBriefing.to_json())

# convert the object into a dict
link_addition_order_briefing_dict = link_addition_order_briefing_instance.to_dict()
# create an instance of LinkAdditionOrderBriefing from a dict
link_addition_order_briefing_from_dict = LinkAdditionOrderBriefing.from_dict(link_addition_order_briefing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


