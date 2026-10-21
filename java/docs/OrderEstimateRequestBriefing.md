

# OrderEstimateRequestBriefing


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;OrderLinkRequest&gt;**](OrderLinkRequest.md) | No more links than the offer allows. |  |
|**extraServices** | [**List&lt;ExtraServicesEnum&gt;**](#List&lt;ExtraServicesEnum&gt;) | Extra services the offer has, added to the ones the web selects for your project by default. A project with a sensitive topic always carries &#x60;extra_charge_for_sensitive_topic&#x60; when the media charges it. |  [optional] |
|**title** | **String** |  |  [optional] |
|**additionalInfo** | **String** |  |  [optional] |
|**linkingFrom** | **String** | The URL of an existing article on the media&#39;s domain that the link goes into. |  |
|**link** | [**OrderLinkRequest**](OrderLinkRequest.md) |  |  |



## Enum: List&lt;ExtraServicesEnum&gt;

| Name | Value |
|---- | -----|
| LIST_ON_HOMEPAGE | &quot;list_on_homepage&quot; |
| EXTRA_CHARGE_FOR_SENSITIVE_TOPIC | &quot;extra_charge_for_sensitive_topic&quot; |



