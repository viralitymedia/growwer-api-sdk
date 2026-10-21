

# ManagedServiceProposalReviewRequestReviewsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**proposalId** | **UUID** |  |  |
|**decision** | [**DecisionEnum**](#DecisionEnum) |  |  |
|**comment** | **String** | Required to reject, at most 2000 characters once trimmed; the team reads it. |  [optional] |



## Enum: DecisionEnum

| Name | Value |
|---- | -----|
| ACCEPT | &quot;accept&quot; |
| REJECT | &quot;reject&quot; |



