

# ManagedServiceProposal

A media the team proposes for a campaign, with the publication it would get.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**state** | [**StateEnum**](#StateEnum) | &#x60;proposed&#x60; awaits your review. &#x60;accepted&#x60; awaits the order the team places for you. &#x60;purchase_started&#x60; and &#x60;purchase_finished&#x60; follow that order. |  |
|**media** | [**ManagedServiceProposalMedia**](ManagedServiceProposalMedia.md) |  |  |
|**service** | [**ServiceEnum**](#ServiceEnum) |  |  |
|**proposedPrice** | [**Money**](Money.md) | The price the proposal was made at, the one the summary PDF shows. |  |
|**currentPrice** | [**MoneyOrNull**](MoneyOrNull.md) | What the media charges for the service today; null when it no longer offers it. |  |
|**briefing** | [**ManagedServiceProposalBriefing**](ManagedServiceProposalBriefing.md) |  |  |
|**stateReason** | **String** | Why the proposal reached its state, in your language, such as your comment when you rejected it. |  |
|**orderId** | **UUID** | The order placed for the proposal (GET /orders/{id}). |  |
|**orderState** | **String** | The state of that order while its purchase is in progress. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** | When the proposal last changed state. |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PROPOSED | &quot;proposed&quot; |
| ACCEPTED | &quot;accepted&quot; |
| CANCELLED | &quot;cancelled&quot; |
| PURCHASE_STARTED | &quot;purchase_started&quot; |
| PURCHASE_FINISHED | &quot;purchase_finished&quot; |



## Enum: ServiceEnum

| Name | Value |
|---- | -----|
| POST | &quot;post&quot; |
| LINK_ADDITION | &quot;link_addition&quot; |



