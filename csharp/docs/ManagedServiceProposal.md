# Growwer.Api.Model.ManagedServiceProposal
A media the team proposes for a campaign, with the publication it would get.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**State** | **string** | &#x60;proposed&#x60; awaits your review. &#x60;accepted&#x60; awaits the order the team places for you. &#x60;purchase_started&#x60; and &#x60;purchase_finished&#x60; follow that order. | 
**Media** | [**ManagedServiceProposalMedia**](ManagedServiceProposalMedia.md) |  | 
**Service** | **string** |  | 
**ProposedPrice** | [**Money**](Money.md) | The price the proposal was made at, the one the summary PDF shows. | 
**CurrentPrice** | [**MoneyOrNull**](MoneyOrNull.md) | What the media charges for the service today; null when it no longer offers it. | 
**Briefing** | [**ManagedServiceProposalBriefing**](ManagedServiceProposalBriefing.md) |  | 
**StateReason** | **string** | Why the proposal reached its state, in your language, such as your comment when you rejected it. | 
**OrderId** | **Guid?** | The order placed for the proposal (GET /orders/{id}). | 
**OrderState** | **string** | The state of that order while its purchase is in progress. | 
**CreatedAt** | **DateTime** |  | 
**UpdatedAt** | **DateTime** | When the proposal last changed state. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

