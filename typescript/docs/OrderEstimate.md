
# OrderEstimate


## Properties

Name | Type
------------ | -------------
`price` | [Money](Money.md)
`availableBalance` | [Money](Money.md)
`missing` | [Money](Money.md)
`sufficientBalance` | boolean

## Example

```typescript
import type { OrderEstimate } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "price": null,
  "availableBalance": null,
  "missing": null,
  "sufficientBalance": null,
} satisfies OrderEstimate

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OrderEstimate
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


