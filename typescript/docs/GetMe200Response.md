
# GetMe200Response


## Properties

Name | Type
------------ | -------------
`id` | string
`email` | string
`firstName` | string
`language` | string
`createdAt` | Date
`buyer` | [GetMe200ResponseBuyer](GetMe200ResponseBuyer.md)
`seller` | [GetMe200ResponseSeller](GetMe200ResponseSeller.md)
`catalogue` | [GetMe200ResponseCatalogue](GetMe200ResponseCatalogue.md)
`managedService` | [GetMe200ResponseManagedService](GetMe200ResponseManagedService.md)

## Example

```typescript
import type { GetMe200Response } from '@growwer/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "email": null,
  "firstName": null,
  "language": en,
  "createdAt": null,
  "buyer": null,
  "seller": null,
  "catalogue": null,
  "managedService": null,
} satisfies GetMe200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetMe200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


