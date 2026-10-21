
# SellerMediaLinkAdditionOffer

Adding a link to an existing article, or null when you do not offer it.

## Properties

Name | Type
------------ | -------------
`pricingOptions` | [Array&lt;SellerMediaLinkAdditionOfferPricingOptionsInner&gt;](SellerMediaLinkAdditionOfferPricingOptionsInner.md)

## Example

```typescript
import type { SellerMediaLinkAdditionOffer } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "pricingOptions": null,
} satisfies SellerMediaLinkAdditionOffer

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SellerMediaLinkAdditionOffer
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


