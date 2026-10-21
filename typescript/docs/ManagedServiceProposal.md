
# ManagedServiceProposal

A media the team proposes for a campaign, with the publication it would get.

## Properties

Name | Type
------------ | -------------
`id` | string
`state` | string
`media` | [ManagedServiceProposalMedia](ManagedServiceProposalMedia.md)
`service` | string
`proposedPrice` | [Money](Money.md)
`currentPrice` | [MoneyOrNull](MoneyOrNull.md)
`briefing` | [ManagedServiceProposalBriefing](ManagedServiceProposalBriefing.md)
`stateReason` | string
`orderId` | string
`orderState` | string
`createdAt` | Date
`updatedAt` | Date

## Example

```typescript
import type { ManagedServiceProposal } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "state": null,
  "media": null,
  "service": null,
  "proposedPrice": null,
  "currentPrice": null,
  "briefing": null,
  "stateReason": null,
  "orderId": null,
  "orderState": null,
  "createdAt": null,
  "updatedAt": null,
} satisfies ManagedServiceProposal

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ManagedServiceProposal
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


