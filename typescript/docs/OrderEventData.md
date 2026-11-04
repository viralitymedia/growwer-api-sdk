
# OrderEventData

The `data` of an `order.*` event: the order as GET /orders/{id} answers it at the time of the event. Order by its `updatedAt` when events arrive out of order.

## Properties

Name | Type
------------ | -------------
`order` | [Order](Order.md)

## Example

```typescript
import type { OrderEventData } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "order": null,
} satisfies OrderEventData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OrderEventData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


