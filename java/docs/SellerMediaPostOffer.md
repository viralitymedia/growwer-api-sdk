

# SellerMediaPostOffer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pricingOptions** | [**List&lt;SellerMediaPostOfferPricingOptionsInner&gt;**](SellerMediaPostOfferPricingOptionsInner.md) | One entry per link type you offer. |  |
|**maximumLinks** | **Integer** | How many links a sponsored post may hold, 1 to 4. |  |
|**advertisingLabellingPolicy** | [**AdvertisingLabellingPolicyEnum**](#AdvertisingLabellingPolicyEnum) | Whether sponsored posts are labelled as advertising. |  |
|**promotedSocialNetworks** | [**List&lt;PromotedSocialNetworksEnum&gt;**](#List&lt;PromotedSocialNetworksEnum&gt;) | The social networks sponsored posts are promoted on. |  |
|**extraServices** | [**List&lt;UpdateSellerMediaRequestExtraServicesInner&gt;**](UpdateSellerMediaRequestExtraServicesInner.md) | Read here, but PATCH /seller/medias/{id} and POST /seller/medias take it at the top level of the body. |  |



## Enum: AdvertisingLabellingPolicyEnum

| Name | Value |
|---- | -----|
| ALWAYS | &quot;always&quot; |
| NEVER | &quot;never&quot; |



## Enum: List&lt;PromotedSocialNetworksEnum&gt;

| Name | Value |
|---- | -----|
| TWITTER | &quot;twitter&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |
| PINTEREST | &quot;pinterest&quot; |
| TUMBLR | &quot;tumblr&quot; |
| NEWSLETTER | &quot;newsletter&quot; |



