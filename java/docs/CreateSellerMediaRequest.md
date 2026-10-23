

# CreateSellerMediaRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rootUrl** | **URI** |  |  |
|**typology** | [**TypologyEnum**](#TypologyEnum) |  |  |
|**country** | **String** | A country code from GET /vocabulary. |  |
|**language** | **String** | A language code from GET /vocabulary. |  |
|**topics** | **Set&lt;Integer&gt;** | Topic ids from GET /vocabulary. |  |
|**bannedTopics** | **Set&lt;Integer&gt;** | The topic ids from GET /vocabulary the media refuses. |  [optional] |
|**postOffer** | [**CreateSellerMediaRequestPostOffer**](CreateSellerMediaRequestPostOffer.md) |  |  |
|**linkAdditionOffer** | [**UpdateSellerMediaRequestLinkAdditionOffer**](UpdateSellerMediaRequestLinkAdditionOffer.md) |  |  [optional] |
|**extraServices** | [**List&lt;UpdateSellerMediaRequestExtraServicesInner&gt;**](UpdateSellerMediaRequestExtraServicesInner.md) |  |  [optional] |
|**acceptMediaPublishingTerms** | **Boolean** | Must be true: you accept the media publishing terms. |  |
|**declareMediaOwnership** | **Boolean** | Must be true: you own or manage this media. |  |



## Enum: TypologyEnum

| Name | Value |
|---- | -----|
| BLOG | &quot;blog&quot; |
| PRESS | &quot;press&quot; |



