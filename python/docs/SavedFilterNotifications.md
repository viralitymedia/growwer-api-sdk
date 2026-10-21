# SavedFilterNotifications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**frequency** | **str** | How often Growwer emails new matching medias, or null when it does not. | 

## Example

```python
from growwer.models.saved_filter_notifications import SavedFilterNotifications

# TODO update the JSON string below
json = "{}"
# create an instance of SavedFilterNotifications from a JSON string
saved_filter_notifications_instance = SavedFilterNotifications.from_json(json)
# print the JSON string representation of the object
print(SavedFilterNotifications.to_json())

# convert the object into a dict
saved_filter_notifications_dict = saved_filter_notifications_instance.to_dict()
# create an instance of SavedFilterNotifications from a dict
saved_filter_notifications_from_dict = SavedFilterNotifications.from_dict(saved_filter_notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


