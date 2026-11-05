
# CreateWebhookRequest


## Properties

Name | Type
------------ | -------------
`url` | string
`events` | [Set&lt;WebhookEventType&gt;](WebhookEventType.md)
`lowBalanceThreshold` | [Money](Money.md)
`description` | string

## Example

```typescript
import type { CreateWebhookRequest } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "url": null,
  "events": null,
  "lowBalanceThreshold": null,
  "description": null,
} satisfies CreateWebhookRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateWebhookRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


