

# CreateSavedFilterRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | 1 to 255 characters. |  |
|**filters** | **Map&lt;String, Object&gt;** | At least one filter parameter of GET /projects/{id}/medias, or &#x60;source&#x60;, by name. |  |
|**notificationFrequency** | [**NotificationFrequencyEnum**](#NotificationFrequencyEnum) | Email new matching medias this often. Omit it for no emails. |  [optional] |



## Enum: NotificationFrequencyEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| WEEKLY | &quot;weekly&quot; |
| MONTHLY | &quot;monthly&quot; |



