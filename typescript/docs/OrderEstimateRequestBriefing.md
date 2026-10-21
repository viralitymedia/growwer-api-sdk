
# OrderEstimateRequestBriefing


## Properties

Name | Type
------------ | -------------
`links` | [Array&lt;OrderLinkRequest&gt;](OrderLinkRequest.md)
`extraServices` | Array&lt;string&gt;
`title` | string
`additionalInfo` | string
`linkingFrom` | string
`link` | [OrderLinkRequest](OrderLinkRequest.md)

## Example

```typescript
import type { OrderEstimateRequestBriefing } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "links": null,
  "extraServices": null,
  "title": null,
  "additionalInfo": null,
  "linkingFrom": null,
  "link": null,
} satisfies OrderEstimateRequestBriefing

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OrderEstimateRequestBriefing
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


