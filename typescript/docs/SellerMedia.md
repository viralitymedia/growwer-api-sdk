
# SellerMedia

One of your medias, as its seller sees it.

## Properties

Name | Type
------------ | -------------
`id` | string
`domain` | string
`url` | string
`typology` | string
`state` | string
`deactivationStrikes` | number
`country` | string
`language` | string
`topics` | Array&lt;number&gt;
`bannedTopics` | Array&lt;number&gt;
`providerComments` | string
`publicationRate` | number
`averageDaysToPublication` | number
`numPublishedOrders` | number
`onHoliday` | boolean
`flashOffer` | [SellerMediaFlashOffer](SellerMediaFlashOffer.md)
`postOffer` | [SellerMediaPostOffer](SellerMediaPostOffer.md)
`linkAdditionOffer` | [SellerMediaLinkAdditionOffer](SellerMediaLinkAdditionOffer.md)
`competitiveFees` | [SellerFeesOrNull](SellerFeesOrNull.md)
`createdAt` | Date

## Example

```typescript
import type { SellerMedia } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "domain": example.com,
  "url": null,
  "typology": null,
  "state": null,
  "deactivationStrikes": null,
  "country": null,
  "language": null,
  "topics": null,
  "bannedTopics": null,
  "providerComments": null,
  "publicationRate": null,
  "averageDaysToPublication": null,
  "numPublishedOrders": null,
  "onHoliday": null,
  "flashOffer": null,
  "postOffer": null,
  "linkAdditionOffer": null,
  "competitiveFees": null,
  "createdAt": null,
} satisfies SellerMedia

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SellerMedia
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


