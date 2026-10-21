# OrderBriefing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**language** | **str** | The language code of the article. | 
**links** | [**List[OrderLink]**](OrderLink.md) |  | 
**extra_services** | **List[str]** |  | 
**additional_info** | **str** |  | 
**has_proposed_draft** | **bool** | Whether you attached your own draft; GET /orders/{id}/briefing downloads it. | 
**linking_from** | **str** | The existing article of the media the link goes into. | 
**link** | [**OrderLink**](OrderLink.md) |  | 

## Example

```python
from growwer.models.order_briefing import OrderBriefing

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBriefing from a JSON string
order_briefing_instance = OrderBriefing.from_json(json)
# print the JSON string representation of the object
print(OrderBriefing.to_json())

# convert the object into a dict
order_briefing_dict = order_briefing_instance.to_dict()
# create an instance of OrderBriefing from a dict
order_briefing_from_dict = OrderBriefing.from_dict(order_briefing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


