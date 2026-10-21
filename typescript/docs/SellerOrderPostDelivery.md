
# SellerOrderPostDelivery

The published post of a post order. A link addition order takes no body.

## Properties

Name | Type
------------ | -------------
`url` | string
`publicationDateConfirmed` | boolean

## Example

```typescript
import type { SellerOrderPostDelivery } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "url": null,
  "publicationDateConfirmed": null,
} satisfies SellerOrderPostDelivery

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SellerOrderPostDelivery
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


