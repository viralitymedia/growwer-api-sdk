
# PutSellerHolidayRequest


## Properties

Name | Type
------------ | -------------
`onHoliday` | boolean
`endDate` | Date

## Example

```typescript
import type { PutSellerHolidayRequest } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "onHoliday": null,
  "endDate": Tue Dec 01 00:00:00 UTC 2026,
} satisfies PutSellerHolidayRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PutSellerHolidayRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


