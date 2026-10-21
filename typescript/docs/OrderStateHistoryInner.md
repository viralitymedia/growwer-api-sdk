
# OrderStateHistoryInner


## Properties

Name | Type
------------ | -------------
`state` | string
`date` | Date
`reason` | [OrderStateHistoryInnerReason](OrderStateHistoryInnerReason.md)

## Example

```typescript
import type { OrderStateHistoryInner } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "state": null,
  "date": null,
  "reason": null,
} satisfies OrderStateHistoryInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OrderStateHistoryInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


