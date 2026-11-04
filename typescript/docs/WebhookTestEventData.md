
# WebhookTestEventData

The `data` of a `webhook.test` event.

## Properties

Name | Type
------------ | -------------
`webhookId` | string

## Example

```typescript
import type { WebhookTestEventData } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "webhookId": null,
} satisfies WebhookTestEventData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WebhookTestEventData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


