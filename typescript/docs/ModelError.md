
# ModelError


## Properties

Name | Type
------------ | -------------
`code` | string
`message` | string
`requestId` | string
`details` | { [key: string]: any; }

## Example

```typescript
import type { ModelError } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "code": unauthorized,
  "message": null,
  "requestId": 9b2f6c1e-4d7a-4e3b-8a5f-2c1d0e9f7a64,
  "details": null,
} satisfies ModelError

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ModelError
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


