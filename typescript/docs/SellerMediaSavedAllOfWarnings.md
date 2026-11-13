
# SellerMediaSavedAllOfWarnings


## Properties

Name | Type
------------ | -------------
`code` | string
`message` | string
`details` | [SellerMediaSavedAllOfDetails](SellerMediaSavedAllOfDetails.md)

## Example

```typescript
import type { SellerMediaSavedAllOfWarnings } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "code": null,
  "message": Saved. The media still lists above the marketplaces that list the same domain cheaper. Setting the fees at most at the competitive fees in details lists it under them.,
  "details": null,
} satisfies SellerMediaSavedAllOfWarnings

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SellerMediaSavedAllOfWarnings
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


