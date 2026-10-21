
# CreateSavedFilterRequest


## Properties

Name | Type
------------ | -------------
`name` | string
`filters` | { [key: string]: any; }
`notificationFrequency` | string

## Example

```typescript
import type { CreateSavedFilterRequest } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "filters": {"language":["es"],"minDomainRating":30,"favourite":true},
  "notificationFrequency": null,
} satisfies CreateSavedFilterRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateSavedFilterRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


