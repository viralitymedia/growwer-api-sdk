

# ManagedServiceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectUrl** | **String** | The website the campaign is for. |  |
|**goal** | [**GoalEnum**](#GoalEnum) |  |  |
|**country** | **String** | ISO 3166-1 alpha-2 code of the target country. |  |
|**duration** | [**DurationEnum**](#DurationEnum) |  |  |
|**estimatedBudget** | [**Money**](Money.md) | At least 500 EUR. Only EUR is accepted. |  |
|**additionalInfo** | **String** |  |  [optional] |



## Enum: GoalEnum

| Name | Value |
|---- | -----|
| LINK_BUILDING | &quot;link_building&quot; |
| BRANDING | &quot;branding&quot; |
| REPUTATION | &quot;reputation&quot; |
| AI_VISIBILITY | &quot;ai_visibility&quot; |



## Enum: DurationEnum

| Name | Value |
|---- | -----|
| ONE_TIME | &quot;one_time&quot; |
| MONTHLY | &quot;monthly&quot; |



