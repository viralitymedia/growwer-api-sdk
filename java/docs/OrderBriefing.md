

# OrderBriefing


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  |
|**language** | **String** | The language code of the article. |  |
|**links** | [**List&lt;OrderLink&gt;**](OrderLink.md) |  |  |
|**extraServices** | [**List&lt;ExtraServicesEnum&gt;**](#List&lt;ExtraServicesEnum&gt;) |  |  |
|**additionalInfo** | **String** |  |  |
|**hasProposedDraft** | **Boolean** | Whether you attached your own draft; GET /orders/{id}/briefing downloads it. |  |
|**linkingFrom** | **String** | The existing article of the media the link goes into. |  |
|**link** | [**OrderLink**](OrderLink.md) |  |  |



## Enum: List&lt;ExtraServicesEnum&gt;

| Name | Value |
|---- | -----|
| LIST_ON_HOMEPAGE | &quot;list_on_homepage&quot; |
| EXTRA_CHARGE_FOR_SENSITIVE_TOPIC | &quot;extra_charge_for_sensitive_topic&quot; |



