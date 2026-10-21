
# SellerFeesOrNull


## Properties

Name | Type
------------ | -------------
`feeWhenSellerWritesPost` | [MoneyOrNull](MoneyOrNull.md)
`feeWhenSellerDoesNotWritePost` | [MoneyOrNull](MoneyOrNull.md)

## Example

```typescript
import type { SellerFeesOrNull } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "feeWhenSellerWritesPost": null,
  "feeWhenSellerDoesNotWritePost": null,
} satisfies SellerFeesOrNull

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SellerFeesOrNull
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


