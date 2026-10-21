
# SellerOrder

An order placed on one of your medias, as its seller sees it.

## Properties

Name | Type
------------ | -------------
`id` | string
`reference` | string
`type` | string
`state` | string
`requiresYourAction` | boolean
`availableActions` | Array&lt;string&gt;
`earnings` | [Money](Money.md)
`project` | [SellerOrderProject](SellerOrderProject.md)
`media` | [OrderMedia](OrderMedia.md)
`createdAt` | Date
`updatedAt` | Date
`scheduledPublicationDate` | Date
`delivery` | [OrderDelivery](OrderDelivery.md)
`briefing` | [SellerOrderBriefing](SellerOrderBriefing.md)
`draft` | [SellerOrderDraft](SellerOrderDraft.md)
`stateHistory` | [Array&lt;OrderStateHistoryInner&gt;](OrderStateHistoryInner.md)
`channel` | [SellerOrderChannel](SellerOrderChannel.md)

## Example

```typescript
import type { SellerOrder } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "reference": null,
  "type": null,
  "state": null,
  "requiresYourAction": null,
  "availableActions": null,
  "earnings": null,
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
} satisfies SellerOrder

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SellerOrder
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


