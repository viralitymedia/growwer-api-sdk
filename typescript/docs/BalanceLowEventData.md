
# BalanceLowEventData

The `data` of a `balance.low` event.

## Properties

Name | Type
------------ | -------------
`wallet` | [BalanceLowEventDataWallet](BalanceLowEventDataWallet.md)
`threshold` | [Money](Money.md)

## Example

```typescript
import type { BalanceLowEventData } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "wallet": null,
  "threshold": null,
} satisfies BalanceLowEventData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BalanceLowEventData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


