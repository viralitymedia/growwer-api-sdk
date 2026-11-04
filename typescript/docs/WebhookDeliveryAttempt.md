
# WebhookDeliveryAttempt


## Properties

Name | Type
------------ | -------------
`attemptedAt` | Date
`statusCode` | number
`durationMs` | number
`responseBody` | string
`error` | string

## Example

```typescript
import type { WebhookDeliveryAttempt } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "attemptedAt": null,
  "statusCode": null,
  "durationMs": null,
  "responseBody": null,
  "error": null,
} satisfies WebhookDeliveryAttempt

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WebhookDeliveryAttempt
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


