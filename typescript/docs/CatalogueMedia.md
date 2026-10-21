
# CatalogueMedia


## Properties

Name | Type
------------ | -------------
`id` | string
`domain` | string
`type` | string
`language` | string
`country` | string
`topics` | Array&lt;number&gt;
`metrics` | [CatalogueMediaMetrics](CatalogueMediaMetrics.md)
`positiveTrafficTrend` | boolean
`bestSeller` | boolean
`publicationRate` | number
`averageDaysToPublication` | number
`onHoliday` | boolean
`flashOffer` | [CatalogueMediaFlashOffer](CatalogueMediaFlashOffer.md)
`postOffer` | [CataloguePostOffer](CataloguePostOffer.md)
`linkAdditionOffer` | [CatalogueOfferOrNull](CatalogueOfferOrNull.md)

## Example

```typescript
import type { CatalogueMedia } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "domain": example.com,
  "type": null,
  "language": null,
  "country": null,
  "topics": null,
  "metrics": null,
  "positiveTrafficTrend": null,
  "bestSeller": null,
  "publicationRate": null,
  "averageDaysToPublication": null,
  "onHoliday": null,
  "flashOffer": null,
  "postOffer": null,
  "linkAdditionOffer": null,
} satisfies CatalogueMedia

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CatalogueMedia
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


