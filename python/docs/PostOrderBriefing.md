# PostOrderBriefing

The briefing of a post order (`type` `post`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**language** | **str** | The language code of the article. | 
**links** | [**List[OrderLink]**](OrderLink.md) |  | 
**extra_services** | **List[str]** |  | 
**additional_info** | **str** |  | 
**has_proposed_draft** | **bool** | Whether you attached your own draft; GET /orders/{id}/briefing downloads it. | 

## Example

```python
from growwer.models.post_order_briefing import PostOrderBriefing

# TODO update the JSON string below
json = "{}"
# create an instance of PostOrderBriefing from a JSON string
post_order_briefing_instance = PostOrderBriefing.from_json(json)
# print the JSON string representation of the object
print(PostOrderBriefing.to_json())

# convert the object into a dict
post_order_briefing_dict = post_order_briefing_instance.to_dict()
# create an instance of PostOrderBriefing from a dict
post_order_briefing_from_dict = PostOrderBriefing.from_dict(post_order_briefing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


