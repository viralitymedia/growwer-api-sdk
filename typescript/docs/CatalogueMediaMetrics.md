
# CatalogueMediaMetrics

The latest measurements; each is null until it is first measured.

## Properties

Name | Type
------------ | -------------
`organicTraffic` | number
`domainRating` | number
`referringDomains` | number
`linkedDomains` | number
`linkedToReferringRatio` | number

## Example

```typescript
import type { CatalogueMediaMetrics } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "organicTraffic": null,
  "domainRating": null,
  "referringDomains": null,
  "linkedDomains": null,
  "linkedToReferringRatio": null,
} satisfies CatalogueMediaMetrics

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CatalogueMediaMetrics
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


