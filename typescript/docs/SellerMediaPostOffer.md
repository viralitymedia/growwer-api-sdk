
# SellerMediaPostOffer


## Properties

Name | Type
------------ | -------------
`pricingOptions` | [Array&lt;SellerMediaPostOfferPricingOptionsInner&gt;](SellerMediaPostOfferPricingOptionsInner.md)
`maximumLinks` | number
`advertisingLabellingPolicy` | string
`promotedSocialNetworks` | Array&lt;string&gt;
`extraServices` | [Array&lt;UpdateSellerMediaRequestExtraServicesInner&gt;](UpdateSellerMediaRequestExtraServicesInner.md)

## Example

```typescript
import type { SellerMediaPostOffer } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "pricingOptions": null,
  "maximumLinks": null,
  "advertisingLabellingPolicy": null,
  "promotedSocialNetworks": null,
  "extraServices": null,
} satisfies SellerMediaPostOffer

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SellerMediaPostOffer
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


