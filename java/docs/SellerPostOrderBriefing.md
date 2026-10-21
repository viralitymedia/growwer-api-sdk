

# SellerPostOrderBriefing

The briefing of a post order (`type` `post`), as you, the seller, receive it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  |
|**language** | **String** | The language code of the article. |  |
|**links** | [**List&lt;OrderLink&gt;**](OrderLink.md) |  |  |
|**extraServices** | [**List&lt;ExtraServicesEnum&gt;**](#List&lt;ExtraServicesEnum&gt;) |  |  |
|**additionalInfo** | **String** |  |  |
|**writtenBy** | [**WrittenByEnum**](#WrittenByEnum) | Who writes the article; &#x60;seller&#x60; means you do. |  |
|**hasProposedDraft** | **Boolean** | Whether the buyer attached a draft; GET /seller/orders/{id}/briefing downloads it. |  |



## Enum: List&lt;ExtraServicesEnum&gt;

| Name | Value |
|---- | -----|
| LIST_ON_HOMEPAGE | &quot;list_on_homepage&quot; |
| EXTRA_CHARGE_FOR_SENSITIVE_TOPIC | &quot;extra_charge_for_sensitive_topic&quot; |



## Enum: WrittenByEnum

| Name | Value |
|---- | -----|
| SELLER | &quot;seller&quot; |
| BUYER | &quot;buyer&quot; |
| GROWWER | &quot;growwer&quot; |



