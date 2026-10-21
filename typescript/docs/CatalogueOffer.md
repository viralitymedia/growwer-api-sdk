
# CatalogueOffer


## Properties

Name | Type
------------ | -------------
`price` | [Money](Money.md)
`linkType` | string
`prices` | [{ [key: string]: Money; }](Money.md)
`previousPrice` | [MoneyOrNull](MoneyOrNull.md)

## Example

```typescript
import type { CatalogueOffer } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "price": null,
  "linkType": null,
  "prices": null,
  "previousPrice": null,
} satisfies CatalogueOffer

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CatalogueOffer
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


