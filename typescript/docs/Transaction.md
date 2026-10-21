
# Transaction


## Properties

Name | Type
------------ | -------------
`id` | string
`type` | string
`state` | string
`direction` | string
`amount` | [Money](Money.md)
`description` | string
`descriptionCode` | string
`orderId` | string
`invoiceId` | string
`hasDocument` | boolean
`createdAt` | Date
`updatedAt` | Date

## Example

```typescript
import type { Transaction } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "type": null,
  "state": null,
  "direction": null,
  "amount": null,
  "description": null,
  "descriptionCode": null,
  "orderId": null,
  "invoiceId": null,
  "hasDocument": null,
  "createdAt": null,
  "updatedAt": null,
} satisfies Transaction

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Transaction
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


