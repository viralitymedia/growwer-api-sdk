
# OrderCreateRequest

An order to place, with the price you expect to pay.

## Properties

Name | Type
------------ | -------------
`type` | string
`projectId` | string
`mediaId` | string
`briefing` | [OrderEstimateRequestBriefing](OrderEstimateRequestBriefing.md)
`scheduledPublicationDate` | Date
`draftReviewable` | boolean
`proposedDraftFileId` | string
`expectedPrice` | [Money](Money.md)

## Example

```typescript
import type { OrderCreateRequest } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "type": null,
  "projectId": null,
  "mediaId": null,
  "briefing": null,
  "scheduledPublicationDate": null,
  "draftReviewable": null,
  "proposedDraftFileId": null,
  "expectedPrice": null,
} satisfies OrderCreateRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OrderCreateRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


