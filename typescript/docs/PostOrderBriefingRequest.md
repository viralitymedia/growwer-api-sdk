
# PostOrderBriefingRequest

The briefing of a post order (`type` `post`), checked against the media\'s post offer as the web checks it.

## Properties

Name | Type
------------ | -------------
`links` | [Array&lt;OrderLinkRequest&gt;](OrderLinkRequest.md)
`extraServices` | Array&lt;string&gt;
`title` | string
`additionalInfo` | string

## Example

```typescript
import type { PostOrderBriefingRequest } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "links": null,
  "extraServices": null,
  "title": null,
  "additionalInfo": null,
} satisfies PostOrderBriefingRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PostOrderBriefingRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


