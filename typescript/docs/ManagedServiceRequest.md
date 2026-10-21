
# ManagedServiceRequest


## Properties

Name | Type
------------ | -------------
`projectUrl` | string
`goal` | string
`country` | string
`duration` | string
`estimatedBudget` | [Money](Money.md)
`additionalInfo` | string

## Example

```typescript
import type { ManagedServiceRequest } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "projectUrl": null,
  "goal": null,
  "country": null,
  "duration": null,
  "estimatedBudget": null,
  "additionalInfo": null,
} satisfies ManagedServiceRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ManagedServiceRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


