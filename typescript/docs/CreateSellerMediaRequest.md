
# CreateSellerMediaRequest


## Properties

Name | Type
------------ | -------------
`rootUrl` | string
`typology` | string
`country` | string
`language` | string
`topics` | Set&lt;number&gt;
`bannedTopics` | Set&lt;number&gt;
`postOffer` | [CreateSellerMediaRequestPostOffer](CreateSellerMediaRequestPostOffer.md)
`linkAdditionOffer` | [UpdateSellerMediaRequestLinkAdditionOffer](UpdateSellerMediaRequestLinkAdditionOffer.md)
`extraServices` | [Array&lt;UpdateSellerMediaRequestExtraServicesInner&gt;](UpdateSellerMediaRequestExtraServicesInner.md)
`acceptMediaPublishingTerms` | boolean
`declareMediaOwnership` | boolean

## Example

```typescript
import type { CreateSellerMediaRequest } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "rootUrl": https://www.example.com,
  "typology": null,
  "country": ES,
  "language": es,
  "topics": null,
  "bannedTopics": null,
  "postOffer": null,
  "linkAdditionOffer": null,
  "extraServices": null,
  "acceptMediaPublishingTerms": null,
  "declareMediaOwnership": null,
} satisfies CreateSellerMediaRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateSellerMediaRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


