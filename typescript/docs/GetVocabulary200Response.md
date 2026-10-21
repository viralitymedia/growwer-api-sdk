
# GetVocabulary200Response


## Properties

Name | Type
------------ | -------------
`countries` | [Array&lt;CodeName&gt;](CodeName.md)
`languages` | [Array&lt;CodeName&gt;](CodeName.md)
`topics` | [Array&lt;GetVocabulary200ResponseTopicsInner&gt;](GetVocabulary200ResponseTopicsInner.md)
`productTypes` | Array&lt;string&gt;
`linkTypes` | Array&lt;string&gt;
`orderStates` | Array&lt;string&gt;

## Example

```typescript
import type { GetVocabulary200Response } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "countries": null,
  "languages": null,
  "topics": null,
  "productTypes": null,
  "linkTypes": null,
  "orderStates": null,
} satisfies GetVocabulary200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetVocabulary200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


