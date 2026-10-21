
# OrderDraft

The draft of a post order that has one; null otherwise, and always for a link addition.

## Properties

Name | Type
------------ | -------------
`authoredByBuyer` | boolean
`reviewable` | boolean
`hasFile` | boolean

## Example

```typescript
import type { OrderDraft } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "authoredByBuyer": null,
  "reviewable": null,
  "hasFile": null,
} satisfies OrderDraft

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OrderDraft
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


