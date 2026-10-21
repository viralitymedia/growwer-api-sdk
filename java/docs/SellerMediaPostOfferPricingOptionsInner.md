

# SellerMediaPostOfferPricingOptionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**feeWhenSellerWritesPost** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post you write, or null when you do not offer it. |  |
|**feeWhenSellerDoesNotWritePost** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid for a post the buyer or Growwer writes, or null when you do not offer it. |  |
|**linkType** | [**LinkTypeEnum**](#LinkTypeEnum) |  |  |
|**currentCost** | [**MoneyOrNull**](MoneyOrNull.md) | What you are paid now for the link type, flash offer discount included; read-only. Null when the link type has no current pricing. |  |



## Enum: LinkTypeEnum

| Name | Value |
|---- | -----|
| DOFOLLOW | &quot;dofollow&quot; |
| NOFOLLOW | &quot;nofollow&quot; |
| CITATION | &quot;citation&quot; |



