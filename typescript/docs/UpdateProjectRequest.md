
# UpdateProjectRequest


## Properties

Name | Type
------------ | -------------
`name` | string
`websiteType` | string
`topics` | Array&lt;number&gt;
`language` | string
`country` | string
`promotedProducts` | Array&lt;string&gt;
`userKeywords` | Array&lt;string&gt;

## Example

```typescript
import type { UpdateProjectRequest } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "websiteType": null,
  "topics": null,
  "language": null,
  "country": null,
  "promotedProducts": null,
  "userKeywords": null,
} satisfies UpdateProjectRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UpdateProjectRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


