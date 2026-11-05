# WebhookDeliveryAttempt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AttemptedAt** | **time.Time** |  | 
**StatusCode** | **NullableInt32** | The HTTP status your endpoint answered, null when it did not answer. Only 2xx succeeds; a redirect is not followed and fails. | 
**DurationMs** | **int32** | How long the attempt took, in milliseconds. It gives up after 15 seconds. | 
**ResponseBody** | **NullableString** | Up to the first 1024 bytes of the response body, null when it did not answer. | 
**Error** | **NullableString** | Why there is no status, null when it answered. &#x60;address_not_allowed&#x60;, its host resolved to, or connected to, an address that is not public. | 

## Methods

### NewWebhookDeliveryAttempt

`func NewWebhookDeliveryAttempt(attemptedAt time.Time, statusCode NullableInt32, durationMs int32, responseBody NullableString, error_ NullableString, ) *WebhookDeliveryAttempt`

NewWebhookDeliveryAttempt instantiates a new WebhookDeliveryAttempt object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebhookDeliveryAttemptWithDefaults

`func NewWebhookDeliveryAttemptWithDefaults() *WebhookDeliveryAttempt`

NewWebhookDeliveryAttemptWithDefaults instantiates a new WebhookDeliveryAttempt object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAttemptedAt

`func (o *WebhookDeliveryAttempt) GetAttemptedAt() time.Time`

GetAttemptedAt returns the AttemptedAt field if non-nil, zero value otherwise.

### GetAttemptedAtOk

`func (o *WebhookDeliveryAttempt) GetAttemptedAtOk() (*time.Time, bool)`

GetAttemptedAtOk returns a tuple with the AttemptedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttemptedAt

`func (o *WebhookDeliveryAttempt) SetAttemptedAt(v time.Time)`

SetAttemptedAt sets AttemptedAt field to given value.


### GetStatusCode

`func (o *WebhookDeliveryAttempt) GetStatusCode() int32`

GetStatusCode returns the StatusCode field if non-nil, zero value otherwise.

### GetStatusCodeOk

`func (o *WebhookDeliveryAttempt) GetStatusCodeOk() (*int32, bool)`

GetStatusCodeOk returns a tuple with the StatusCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusCode

`func (o *WebhookDeliveryAttempt) SetStatusCode(v int32)`

SetStatusCode sets StatusCode field to given value.


### SetStatusCodeNil

`func (o *WebhookDeliveryAttempt) SetStatusCodeNil(b bool)`

 SetStatusCodeNil sets the value for StatusCode to be an explicit nil

### UnsetStatusCode
`func (o *WebhookDeliveryAttempt) UnsetStatusCode()`

UnsetStatusCode ensures that no value is present for StatusCode, not even an explicit nil
### GetDurationMs

`func (o *WebhookDeliveryAttempt) GetDurationMs() int32`

GetDurationMs returns the DurationMs field if non-nil, zero value otherwise.

### GetDurationMsOk

`func (o *WebhookDeliveryAttempt) GetDurationMsOk() (*int32, bool)`

GetDurationMsOk returns a tuple with the DurationMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDurationMs

`func (o *WebhookDeliveryAttempt) SetDurationMs(v int32)`

SetDurationMs sets DurationMs field to given value.


### GetResponseBody

`func (o *WebhookDeliveryAttempt) GetResponseBody() string`

GetResponseBody returns the ResponseBody field if non-nil, zero value otherwise.

### GetResponseBodyOk

`func (o *WebhookDeliveryAttempt) GetResponseBodyOk() (*string, bool)`

GetResponseBodyOk returns a tuple with the ResponseBody field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseBody

`func (o *WebhookDeliveryAttempt) SetResponseBody(v string)`

SetResponseBody sets ResponseBody field to given value.


### SetResponseBodyNil

`func (o *WebhookDeliveryAttempt) SetResponseBodyNil(b bool)`

 SetResponseBodyNil sets the value for ResponseBody to be an explicit nil

### UnsetResponseBody
`func (o *WebhookDeliveryAttempt) UnsetResponseBody()`

UnsetResponseBody ensures that no value is present for ResponseBody, not even an explicit nil
### GetError

`func (o *WebhookDeliveryAttempt) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *WebhookDeliveryAttempt) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *WebhookDeliveryAttempt) SetError(v string)`

SetError sets Error field to given value.


### SetErrorNil

`func (o *WebhookDeliveryAttempt) SetErrorNil(b bool)`

 SetErrorNil sets the value for Error to be an explicit nil

### UnsetError
`func (o *WebhookDeliveryAttempt) UnsetError()`

UnsetError ensures that no value is present for Error, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


