
# Project


## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`rootUrl` | string
`websiteType` | string
`topics` | Array&lt;number&gt;
`language` | string
`country` | string
`promotedProducts` | Array&lt;string&gt;
`userKeywords` | Array&lt;string&gt;
`state` | string
`createdAt` | Date

## Example

```typescript
import type { Project } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "rootUrl": null,
  "websiteType": null,
  "topics": null,
  "language": es,
  "country": ES,
  "promotedProducts": null,
  "userKeywords": null,
  "state": null,
  "createdAt": null,
} satisfies Project

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Project
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


