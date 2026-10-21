
# Withdrawal


## Properties

Name | Type
------------ | -------------
`id` | string
`state` | string
`amount` | [Money](Money.md)
`method` | string
`hasInvoice` | boolean
`createdAt` | Date

## Example

```typescript
import type { Withdrawal } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "state": null,
  "amount": null,
  "method": null,
  "hasInvoice": null,
  "createdAt": null,
} satisfies Withdrawal

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Withdrawal
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


