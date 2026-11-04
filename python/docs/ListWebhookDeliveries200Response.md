# ListWebhookDeliveries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WebhookDelivery]**](WebhookDelivery.md) |  | 
**total** | **int** |  | 

## Example

```python
from growwer.models.list_webhook_deliveries200_response import ListWebhookDeliveries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhookDeliveries200Response from a JSON string
list_webhook_deliveries200_response_instance = ListWebhookDeliveries200Response.from_json(json)
# print the JSON string representation of the object
print(ListWebhookDeliveries200Response.to_json())

# convert the object into a dict
list_webhook_deliveries200_response_dict = list_webhook_deliveries200_response_instance.to_dict()
# create an instance of ListWebhookDeliveries200Response from a dict
list_webhook_deliveries200_response_from_dict = ListWebhookDeliveries200Response.from_dict(list_webhook_deliveries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


