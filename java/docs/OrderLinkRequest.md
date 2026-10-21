

# OrderLinkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetUrl** | **String** | Where the link points; leave it out for a citation. |  [optional] |
|**anchor** | **String** | The anchor text; leave it out to let the media choose it. A citation needs one. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | A link type the media offers for this type of order (CatalogueOffer &#x60;linkTypes&#x60;). |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DOFOLLOW | &quot;dofollow&quot; |
| NOFOLLOW | &quot;nofollow&quot; |
| CITATION | &quot;citation&quot; |



