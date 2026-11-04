# WebhookDeliveryAttempt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempted_at** | **\DateTime** |  |
**status_code** | **int** | The HTTP status your endpoint answered, null when it did not answer. Only 2xx succeeds; a redirect is not followed and fails. |
**duration_ms** | **int** | How long the attempt took, in milliseconds. It gives up after 15 seconds. |
**response_body** | **string** | Up to the first 1024 bytes of the response body, null when it did not answer. |
**error** | **string** | Why there is no status, null when it answered. &#x60;address_not_allowed&#x60;, its host resolved to, or connected to, an address that is not public. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
