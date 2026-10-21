# CreateProjectRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **string** |  | [optional]
**root_url** | **string** |  |
**website_type** | **string** |  |
**topics** | **int[]** | Exactly one topic id from GET /vocabulary. |
**language** | **string** | A language code from GET /vocabulary. |
**country** | **string** | A country code from GET /vocabulary; omit it or send null for worldwide. | [optional]
**promoted_products** | **string[]** | 5 to 10 products or services the campaign promotes. |
**user_keywords** | **string[]** | At most 100 keywords, none with a line break. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
