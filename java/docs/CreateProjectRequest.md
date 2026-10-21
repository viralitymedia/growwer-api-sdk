

# CreateProjectRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**rootUrl** | **URI** |  |  |
|**websiteType** | [**WebsiteTypeEnum**](#WebsiteTypeEnum) |  |  |
|**topics** | **List&lt;Integer&gt;** | Exactly one topic id from GET /vocabulary. |  |
|**language** | **String** | A language code from GET /vocabulary. |  |
|**country** | **String** | A country code from GET /vocabulary; omit it or send null for worldwide. |  [optional] |
|**promotedProducts** | **List&lt;String&gt;** | 5 to 10 products or services the campaign promotes. |  |
|**userKeywords** | **List&lt;String&gt;** | At most 100 keywords, none with a line break. |  [optional] |



## Enum: WebsiteTypeEnum

| Name | Value |
|---- | -----|
| ECOMMERCE | &quot;ecommerce&quot; |
| SERVICES | &quot;services&quot; |
| OTHER | &quot;other&quot; |



