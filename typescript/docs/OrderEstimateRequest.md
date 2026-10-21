
# OrderEstimateRequest

An order to price. `scheduledPublicationDate`, `draftReviewable` and `proposedDraftFileId` apply to a post order only.

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

## Example

```typescript
import type { OrderEstimateRequest } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "type": null,
  "projectId": null,
  "mediaId": null,
  "briefing": null,
  "scheduledPublicationDate": null,
  "draftReviewable": null,
  "proposedDraftFileId": null,
} satisfies OrderEstimateRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OrderEstimateRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


