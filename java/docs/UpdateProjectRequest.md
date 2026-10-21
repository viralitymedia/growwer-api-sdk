

# UpdateProjectRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Null or an empty string removes the name. |  [optional] |
|**websiteType** | [**WebsiteTypeEnum**](#WebsiteTypeEnum) |  |  [optional] |
|**topics** | **List&lt;Integer&gt;** | Exactly one topic id from GET /vocabulary. |  [optional] |
|**language** | **String** | A language code from GET /vocabulary. |  [optional] |
|**country** | **String** | A country code from GET /vocabulary, or null for worldwide. |  [optional] |
|**promotedProducts** | **List&lt;String&gt;** | 5 to 10 products or services the campaign promotes. |  [optional] |
|**userKeywords** | **List&lt;String&gt;** | At most 100 keywords, none with a line break. |  [optional] |



## Enum: WebsiteTypeEnum

| Name | Value |
|---- | -----|
| ECOMMERCE | &quot;ecommerce&quot; |
| SERVICES | &quot;services&quot; |
| OTHER | &quot;other&quot; |



