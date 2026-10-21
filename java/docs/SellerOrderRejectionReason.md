

# SellerOrderRejectionReason


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**NameEnum**](#NameEnum) | Why you reject the order, as the seller order page offers it. |  |
|**additionalInfo** | **String** | More about the reason, which the buyer is told, 10 to 2000 characters. Required with &#x60;other_reasons&#x60;. |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| MEDIA_IS_COMPETITION | &quot;media_is_competition&quot; |
| MEDIA_HAS_EXCLUSIVITY | &quot;media_has_exclusivity&quot; |
| FORBIDDEN_TOPIC | &quot;forbidden_topic&quot; |
| OTHER_REASONS | &quot;other_reasons&quot; |



