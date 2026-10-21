
# ManagedServiceCampaignProposalCounts

How many of the campaign\'s proposals are in each state.

## Properties

Name | Type
------------ | -------------
`proposed` | number
`accepted` | number
`cancelled` | number
`purchaseStarted` | number
`purchaseFinished` | number

## Example

```typescript
import type { ManagedServiceCampaignProposalCounts } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "proposed": null,
  "accepted": null,
  "cancelled": null,
  "purchaseStarted": null,
  "purchaseFinished": null,
} satisfies ManagedServiceCampaignProposalCounts

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ManagedServiceCampaignProposalCounts
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


