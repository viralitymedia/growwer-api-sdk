
# CatalogueMediaFlashOffer

The flash offer running, or null. Its discount is already in the prices.

## Properties

Name | Type
------------ | -------------
`discountPercent` | number
`endsAt` | Date

## Example

```typescript
import type { CatalogueMediaFlashOffer } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "discountPercent": null,
  "endsAt": null,
} satisfies CatalogueMediaFlashOffer

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CatalogueMediaFlashOffer
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


