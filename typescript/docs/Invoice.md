
# Invoice


## Properties

Name | Type
------------ | -------------
`id` | string
`number` | string
`issuedAt` | Date
`total` | [Money](Money.md)

## Example

```typescript
import type { Invoice } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "number": null,
  "issuedAt": null,
  "total": null,
} satisfies Invoice

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Invoice
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


