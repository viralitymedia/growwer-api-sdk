
# OrderDelivery

Where the order was published, once it is.

## Properties

Name | Type
------------ | -------------
`url` | string
`publishedAt` | Date

## Example

```typescript
import type { OrderDelivery } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "url": null,
  "publishedAt": null,
} satisfies OrderDelivery

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OrderDelivery
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


