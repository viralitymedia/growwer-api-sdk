

# CatalogueOfferOrNull


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**price** | [**Money**](Money.md) | What you pay for the offer with its dearest link type, flash offer discount included. |  |
|**linkType** | [**LinkTypeEnum**](#LinkTypeEnum) | The link type &#x60;price&#x60; is for. |  |
|**prices** | [**Map&lt;String, Money&gt;**](Money.md) | What you pay for each link type the offer gives, by link type. |  |
|**previousPrice** | [**MoneyOrNull**](MoneyOrNull.md) | The highest price the offer has had, when &#x60;price&#x60; is more than 5% below it; otherwise null. |  |



## Enum: LinkTypeEnum

| Name | Value |
|---- | -----|
| DOFOLLOW | &quot;dofollow&quot; |
| NOFOLLOW | &quot;nofollow&quot; |
| CITATION | &quot;citation&quot; |



