
# CatalogueMediaBestPrice

The best-price badge the catalogue shows, or null for none: cheaper means the price is at least 1 EUR below the cheapest listing of the media found on the other platforms checked in the last 7 days; only_here means none of the platforms checked lists it. It names neither the platforms nor any price.

## Properties

Name | Type
------------ | -------------
`badge` | string
`platformCount` | number
`checkedOn` | Date

## Example

```typescript
import type { CatalogueMediaBestPrice } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "badge": null,
  "platformCount": null,
  "checkedOn": null,
} satisfies CatalogueMediaBestPrice

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CatalogueMediaBestPrice
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


