
# LinkAdditionOrderBriefingRequest

The briefing of a link addition (`type` `link_addition`), checked against the media\'s link addition offer as the web checks it.

## Properties

Name | Type
------------ | -------------
`linkingFrom` | string
`link` | [OrderLinkRequest](OrderLinkRequest.md)
`additionalInfo` | string

## Example

```typescript
import type { LinkAdditionOrderBriefingRequest } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "linkingFrom": null,
  "link": null,
  "additionalInfo": null,
} satisfies LinkAdditionOrderBriefingRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as LinkAdditionOrderBriefingRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


