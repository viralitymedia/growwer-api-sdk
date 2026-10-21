
# ProjectCatalogueMediaAllOfProject

The media\'s state in the project.

## Properties

Name | Type
------------ | -------------
`favourite` | boolean
`discarded` | boolean
`requested` | boolean
`recommended` | boolean
`bought` | boolean
`_new` | boolean

## Example

```typescript
import type { ProjectCatalogueMediaAllOfProject } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "favourite": null,
  "discarded": null,
  "requested": null,
  "recommended": null,
  "bought": null,
  "_new": null,
} satisfies ProjectCatalogueMediaAllOfProject

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProjectCatalogueMediaAllOfProject
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


