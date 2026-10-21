
# ManagedServiceProposalBriefing


## Properties

Name | Type
------------ | -------------
`mainInfo` | string
`links` | [Array&lt;ManagedServiceProposalBriefingLinksInner&gt;](ManagedServiceProposalBriefingLinksInner.md)
`additionalInfo` | string
`requiresDraft` | boolean

## Example

```typescript
import type { ManagedServiceProposalBriefing } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "mainInfo": null,
  "links": null,
  "additionalInfo": null,
  "requiresDraft": null,
} satisfies ManagedServiceProposalBriefing

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ManagedServiceProposalBriefing
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


