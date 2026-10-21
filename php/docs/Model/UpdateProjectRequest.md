# UpdateProjectRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **string** | Null or an empty string removes the name. | [optional]
**website_type** | **string** |  | [optional]
**topics** | **int[]** | Exactly one topic id from GET /vocabulary. | [optional]
**language** | **string** | A language code from GET /vocabulary. | [optional]
**country** | **string** | A country code from GET /vocabulary, or null for worldwide. | [optional]
**promoted_products** | **string[]** | 5 to 10 products or services the campaign promotes. | [optional]
**user_keywords** | **string[]** | At most 100 keywords, none with a line break. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
