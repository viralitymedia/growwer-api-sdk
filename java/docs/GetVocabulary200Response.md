

# GetVocabulary200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countries** | [**List&lt;CodeName&gt;**](CodeName.md) | ISO 3166-1 alpha-2 codes. |  |
|**languages** | [**List&lt;CodeName&gt;**](CodeName.md) | ISO 639 codes, as the web&#39;s language selectors offer them. |  |
|**topics** | [**List&lt;GetVocabulary200ResponseTopicsInner&gt;**](GetVocabulary200ResponseTopicsInner.md) |  |  |
|**productTypes** | [**List&lt;ProductTypesEnum&gt;**](#List&lt;ProductTypesEnum&gt;) | What an order buys: a sponsored post, or a link added to an existing page. |  |
|**linkTypes** | [**List&lt;LinkTypesEnum&gt;**](#List&lt;LinkTypesEnum&gt;) |  |  |
|**orderStates** | **List&lt;String&gt;** |  |  |



## Enum: List&lt;ProductTypesEnum&gt;

| Name | Value |
|---- | -----|
| POST_ORDER | &quot;post_order&quot; |
| LINK_ADDITION_ORDER | &quot;link_addition_order&quot; |



## Enum: List&lt;LinkTypesEnum&gt;

| Name | Value |
|---- | -----|
| DOFOLLOW | &quot;dofollow&quot; |
| NOFOLLOW | &quot;nofollow&quot; |
| CITATION | &quot;citation&quot; |



