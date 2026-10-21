
# PostOrderBriefing

The briefing of a post order (`type` `post`).

## Properties

Name | Type
------------ | -------------
`title` | string
`language` | string
`links` | [Array&lt;OrderLink&gt;](OrderLink.md)
`extraServices` | Array&lt;string&gt;
`additionalInfo` | string
`hasProposedDraft` | boolean

## Example

```typescript
import type { PostOrderBriefing } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "title": null,
  "language": null,
  "links": null,
  "extraServices": null,
  "additionalInfo": null,
  "hasProposedDraft": null,
} satisfies PostOrderBriefing

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PostOrderBriefing
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


