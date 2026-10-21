

# Project


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**name** | **String** | Your name for the project, or null when it has none. |  |
|**rootUrl** | **URI** | The website the project promotes. It cannot be changed once the project exists. |  |
|**websiteType** | [**WebsiteTypeEnum**](#WebsiteTypeEnum) | What the website is: an online shop (&#x60;ecommerce&#x60;), a services business (&#x60;services&#x60;) or anything else (&#x60;other&#x60;). |  |
|**topics** | **List&lt;Integer&gt;** | The website&#39;s topic, as a topic id from GET /vocabulary. Exactly one. |  |
|**language** | **String** | The language of the campaign, as a language code from GET /vocabulary. |  |
|**country** | **String** | The country the campaign targets, as a country code from GET /vocabulary, or null for worldwide. |  |
|**promotedProducts** | **List&lt;String&gt;** | The products or services the campaign promotes, 5 to 10. |  |
|**userKeywords** | **List&lt;String&gt;** | Keywords you want the campaign to target, at most 100. |  |
|**state** | [**StateEnum**](#StateEnum) | &#x60;finished&#x60; once Growwer has recommended media for the project, &#x60;analyzing&#x60; until then. Analysis can take hours, and it never finishes when no medium matches the project. Poll with backoff, and use &#x60;createdAt&#x60; to decide how long to keep polling.  |  |
|**createdAt** | **OffsetDateTime** |  |  |



## Enum: WebsiteTypeEnum

| Name | Value |
|---- | -----|
| ECOMMERCE | &quot;ecommerce&quot; |
| SERVICES | &quot;services&quot; |
| OTHER | &quot;other&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ANALYZING | &quot;analyzing&quot; |
| FINISHED | &quot;finished&quot; |



