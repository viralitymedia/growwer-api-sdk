
# Order


## Properties

Name | Type
------------ | -------------
`id` | string
`reference` | string
`type` | string
`state` | string
`pendingAction` | string
`price` | [Money](Money.md)
`project` | [OrderProject](OrderProject.md)
`media` | [OrderMedia](OrderMedia.md)
`createdAt` | Date
`updatedAt` | Date
`scheduledPublicationDate` | Date
`delivery` | [OrderDelivery](OrderDelivery.md)
`briefing` | [OrderBriefing](OrderBriefing.md)
`draft` | [OrderDraft](OrderDraft.md)
`stateHistory` | [Array&lt;OrderStateHistoryInner&gt;](OrderStateHistoryInner.md)
`channel` | [OrderChannel](OrderChannel.md)

## Example

```typescript
import type { Order } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "reference": null,
  "type": null,
  "state": null,
  "pendingAction": null,
  "price": null,
  "project": null,
  "media": null,
  "createdAt": null,
  "updatedAt": null,
  "scheduledPublicationDate": null,
  "delivery": null,
  "briefing": null,
  "draft": null,
  "stateHistory": null,
  "channel": null,
} satisfies Order

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Order
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


