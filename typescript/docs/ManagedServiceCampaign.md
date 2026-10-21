
# ManagedServiceCampaign

A campaign your managed service runs for you. Every figure about proposals counts only those you can see (not the ones the team is still preparing).

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`state` | string
`deadline` | Date
`budget` | [Money](Money.md)
`project` | [ManagedServiceCampaignProject](ManagedServiceCampaignProject.md)
`strategy` | [ManagedServiceCampaignStrategy](ManagedServiceCampaignStrategy.md)
`proposalCounts` | [ManagedServiceCampaignProposalCounts](ManagedServiceCampaignProposalCounts.md)
`proposalsTotal` | [Money](Money.md)
`budgetExceededBy` | [MoneyOrNull](MoneyOrNull.md)
`createdAt` | Date
`updatedAt` | Date

## Example

```typescript
import type { ManagedServiceCampaign } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "state": null,
  "deadline": null,
  "budget": null,
  "project": null,
  "strategy": null,
  "proposalCounts": null,
  "proposalsTotal": null,
  "budgetExceededBy": null,
  "createdAt": null,
  "updatedAt": null,
} satisfies ManagedServiceCampaign

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ManagedServiceCampaign
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


