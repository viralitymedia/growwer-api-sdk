

# CataloguePostOffer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**price** | [**Money**](Money.md) | What you pay for the offer with its dearest link type, flash offer discount included. |  |
|**linkType** | [**LinkTypeEnum**](#LinkTypeEnum) | The link type &#x60;price&#x60; is for. |  |
|**prices** | [**Map&lt;String, Money&gt;**](Money.md) | What you pay for each link type the offer gives, by link type. |  |
|**previousPrice** | [**MoneyOrNull**](MoneyOrNull.md) | The highest price the offer has had, when &#x60;price&#x60; is more than 5% below it; otherwise null. |  |
|**advertisingLabel** | **Boolean** | Whether the media always labels posts as advertising. |  |
|**promotedSocialNetworks** | [**List&lt;PromotedSocialNetworksEnum&gt;**](#List&lt;PromotedSocialNetworksEnum&gt;) | Where the media promotes the post. |  |
|**extras** | [**CataloguePostOfferAllOfExtras**](CataloguePostOfferAllOfExtras.md) |  |  |



## Enum: LinkTypeEnum

| Name | Value |
|---- | -----|
| DOFOLLOW | &quot;dofollow&quot; |
| NOFOLLOW | &quot;nofollow&quot; |
| CITATION | &quot;citation&quot; |



## Enum: List&lt;PromotedSocialNetworksEnum&gt;

| Name | Value |
|---- | -----|
| TWITTER | &quot;twitter&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |
| PINTEREST | &quot;pinterest&quot; |
| TUMBLR | &quot;tumblr&quot; |
| NEWSLETTER | &quot;newsletter&quot; |



