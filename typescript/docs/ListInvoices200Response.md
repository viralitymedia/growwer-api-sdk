
# ListInvoices200Response


## Properties

Name | Type
------------ | -------------
`items` | [Array&lt;Invoice&gt;](Invoice.md)
`total` | number

## Example

```typescript
import type { ListInvoices200Response } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "items": null,
  "total": null,
} satisfies ListInvoices200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListInvoices200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


