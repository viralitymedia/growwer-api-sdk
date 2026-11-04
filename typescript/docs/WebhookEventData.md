
# WebhookEventData

What the event is about: an OrderEventData for the `order.*` events, a BalanceLowEventData for `balance.low` and a WebhookTestEventData for `webhook.test`.

## Properties

Name | Type
------------ | -------------
`order` | [Order](Order.md)
`wallet` | [BalanceLowEventDataWallet](BalanceLowEventDataWallet.md)
`threshold` | [Money](Money.md)
`webhookId` | string

## Example

```typescript
import type { WebhookEventData } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "order": null,
  "wallet": null,
  "threshold": null,
  "webhookId": null,
} satisfies WebhookEventData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WebhookEventData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


