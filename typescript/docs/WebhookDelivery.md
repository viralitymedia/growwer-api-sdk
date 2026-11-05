
# WebhookDelivery


## Properties

Name | Type
------------ | -------------
`id` | string
`eventId` | string
`eventType` | string
`status` | string
`attemptCount` | number
`nextAttemptAt` | Date
`createdAt` | Date
`attempts` | [Array&lt;WebhookDeliveryAttempt&gt;](WebhookDeliveryAttempt.md)

## Example

```typescript
import type { WebhookDelivery } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "eventId": null,
  "eventType": null,
  "status": null,
  "attemptCount": null,
  "nextAttemptAt": null,
  "createdAt": null,
  "attempts": null,
} satisfies WebhookDelivery

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WebhookDelivery
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


