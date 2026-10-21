
# GetMe200ResponseSeller


## Properties

Name | Type
------------ | -------------
`balance` | [Balance](Balance.md)
`restricted` | boolean
`onHoliday` | boolean
`holidayEndDate` | Date

## Example

```typescript
import type { GetMe200ResponseSeller } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "balance": null,
  "restricted": null,
  "onHoliday": null,
  "holidayEndDate": null,
} satisfies GetMe200ResponseSeller

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetMe200ResponseSeller
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


