
# UpdateSellerMediaRequestPostOffer


## Properties

Name | Type
------------ | -------------
`pricingOptions` | [Array&lt;UpdateSellerMediaRequestPostOfferPricingOptionsInner&gt;](UpdateSellerMediaRequestPostOfferPricingOptionsInner.md)
`maximumLinks` | number
`advertisingLabellingPolicy` | string
`promotedSocialNetworks` | Set&lt;string&gt;

## Example

```typescript
import type { UpdateSellerMediaRequestPostOffer } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "pricingOptions": null,
  "maximumLinks": null,
  "advertisingLabellingPolicy": null,
  "promotedSocialNetworks": null,
} satisfies UpdateSellerMediaRequestPostOffer

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UpdateSellerMediaRequestPostOffer
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


