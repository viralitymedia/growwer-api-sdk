
# SellerMediaFlashOffer

The flash offer running, or null. Its discount is in `currentCost`, never in the fees.

## Properties

Name | Type
------------ | -------------
`discountPercent` | number
`endsAt` | Date

## Example

```typescript
import type { SellerMediaFlashOffer } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "discountPercent": null,
  "endsAt": null,
} satisfies SellerMediaFlashOffer

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SellerMediaFlashOffer
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


