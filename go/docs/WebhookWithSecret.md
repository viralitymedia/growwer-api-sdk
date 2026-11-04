# WebhookWithSecret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Url** | **string** |  | 
**Events** | [**[]WebhookEventType**](WebhookEventType.md) |  | 
**LowBalanceThreshold** | [**NullableMoneyOrNull**](MoneyOrNull.md) | With &#x60;balance.low&#x60;, the available buyer balance below which it fires; null otherwise. | 
**Description** | **NullableString** |  | 
**Enabled** | **bool** | Whether the subscription gets events. | 
**DisabledReason** | **NullableString** | Why it is disabled, null while enabled. &#x60;by_user&#x60;, through PATCH /webhooks/{id}; &#x60;endpoint_gone&#x60;, its endpoint answered 410; &#x60;failing&#x60;, every delivery failed for 5 days, and the account owner was emailed. | 
**FailingSince** | **NullableTime** | Since when its deliveries have failed without one succeeding, null while they succeed. At 5 days it is disabled. The check runs at each failed attempt, so a subscription whose &#x60;failingSince&#x60; is already more than 5 days old, say one that had no event for a while, is disabled at its next failed attempt, without the retries that delivery would otherwise get. | 
**PreviousSecretExpiresAt** | **NullableTime** | Until when the secret replaced by the last rotation still signs beside the new one, null when it no longer does. | 
**CreatedAt** | **time.Time** |  | 
**UpdatedAt** | **time.Time** |  | 
**Secret** | Pointer to **string** | The signing secret, &#x60;whsec_&#x60; and the base64 of 32 random bytes. Shown only in this answer, and absent when the request is replayed under its &#x60;Idempotency-Key&#x60; (or the MCP tool under its &#x60;requestId&#x60;), since the secret is never stored. | [optional] 

## Methods

### NewWebhookWithSecret

`func NewWebhookWithSecret(id string, url string, events []WebhookEventType, lowBalanceThreshold NullableMoneyOrNull, description NullableString, enabled bool, disabledReason NullableString, failingSince NullableTime, previousSecretExpiresAt NullableTime, createdAt time.Time, updatedAt time.Time, ) *WebhookWithSecret`

NewWebhookWithSecret instantiates a new WebhookWithSecret object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebhookWithSecretWithDefaults

`func NewWebhookWithSecretWithDefaults() *WebhookWithSecret`

NewWebhookWithSecretWithDefaults instantiates a new WebhookWithSecret object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *WebhookWithSecret) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *WebhookWithSecret) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *WebhookWithSecret) SetId(v string)`

SetId sets Id field to given value.


### GetUrl

`func (o *WebhookWithSecret) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *WebhookWithSecret) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *WebhookWithSecret) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetEvents

`func (o *WebhookWithSecret) GetEvents() []WebhookEventType`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *WebhookWithSecret) GetEventsOk() (*[]WebhookEventType, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *WebhookWithSecret) SetEvents(v []WebhookEventType)`

SetEvents sets Events field to given value.


### GetLowBalanceThreshold

`func (o *WebhookWithSecret) GetLowBalanceThreshold() MoneyOrNull`

GetLowBalanceThreshold returns the LowBalanceThreshold field if non-nil, zero value otherwise.

### GetLowBalanceThresholdOk

`func (o *WebhookWithSecret) GetLowBalanceThresholdOk() (*MoneyOrNull, bool)`

GetLowBalanceThresholdOk returns a tuple with the LowBalanceThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLowBalanceThreshold

`func (o *WebhookWithSecret) SetLowBalanceThreshold(v MoneyOrNull)`

SetLowBalanceThreshold sets LowBalanceThreshold field to given value.


### SetLowBalanceThresholdNil

`func (o *WebhookWithSecret) SetLowBalanceThresholdNil(b bool)`

 SetLowBalanceThresholdNil sets the value for LowBalanceThreshold to be an explicit nil

### UnsetLowBalanceThreshold
`func (o *WebhookWithSecret) UnsetLowBalanceThreshold()`

UnsetLowBalanceThreshold ensures that no value is present for LowBalanceThreshold, not even an explicit nil
### GetDescription

`func (o *WebhookWithSecret) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *WebhookWithSecret) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *WebhookWithSecret) SetDescription(v string)`

SetDescription sets Description field to given value.


### SetDescriptionNil

`func (o *WebhookWithSecret) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *WebhookWithSecret) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetEnabled

`func (o *WebhookWithSecret) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *WebhookWithSecret) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *WebhookWithSecret) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.


### GetDisabledReason

`func (o *WebhookWithSecret) GetDisabledReason() string`

GetDisabledReason returns the DisabledReason field if non-nil, zero value otherwise.

### GetDisabledReasonOk

`func (o *WebhookWithSecret) GetDisabledReasonOk() (*string, bool)`

GetDisabledReasonOk returns a tuple with the DisabledReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabledReason

`func (o *WebhookWithSecret) SetDisabledReason(v string)`

SetDisabledReason sets DisabledReason field to given value.


### SetDisabledReasonNil

`func (o *WebhookWithSecret) SetDisabledReasonNil(b bool)`

 SetDisabledReasonNil sets the value for DisabledReason to be an explicit nil

### UnsetDisabledReason
`func (o *WebhookWithSecret) UnsetDisabledReason()`

UnsetDisabledReason ensures that no value is present for DisabledReason, not even an explicit nil
### GetFailingSince

`func (o *WebhookWithSecret) GetFailingSince() time.Time`

GetFailingSince returns the FailingSince field if non-nil, zero value otherwise.

### GetFailingSinceOk

`func (o *WebhookWithSecret) GetFailingSinceOk() (*time.Time, bool)`

GetFailingSinceOk returns a tuple with the FailingSince field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailingSince

`func (o *WebhookWithSecret) SetFailingSince(v time.Time)`

SetFailingSince sets FailingSince field to given value.


### SetFailingSinceNil

`func (o *WebhookWithSecret) SetFailingSinceNil(b bool)`

 SetFailingSinceNil sets the value for FailingSince to be an explicit nil

### UnsetFailingSince
`func (o *WebhookWithSecret) UnsetFailingSince()`

UnsetFailingSince ensures that no value is present for FailingSince, not even an explicit nil
### GetPreviousSecretExpiresAt

`func (o *WebhookWithSecret) GetPreviousSecretExpiresAt() time.Time`

GetPreviousSecretExpiresAt returns the PreviousSecretExpiresAt field if non-nil, zero value otherwise.

### GetPreviousSecretExpiresAtOk

`func (o *WebhookWithSecret) GetPreviousSecretExpiresAtOk() (*time.Time, bool)`

GetPreviousSecretExpiresAtOk returns a tuple with the PreviousSecretExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreviousSecretExpiresAt

`func (o *WebhookWithSecret) SetPreviousSecretExpiresAt(v time.Time)`

SetPreviousSecretExpiresAt sets PreviousSecretExpiresAt field to given value.


### SetPreviousSecretExpiresAtNil

`func (o *WebhookWithSecret) SetPreviousSecretExpiresAtNil(b bool)`

 SetPreviousSecretExpiresAtNil sets the value for PreviousSecretExpiresAt to be an explicit nil

### UnsetPreviousSecretExpiresAt
`func (o *WebhookWithSecret) UnsetPreviousSecretExpiresAt()`

UnsetPreviousSecretExpiresAt ensures that no value is present for PreviousSecretExpiresAt, not even an explicit nil
### GetCreatedAt

`func (o *WebhookWithSecret) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *WebhookWithSecret) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *WebhookWithSecret) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *WebhookWithSecret) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *WebhookWithSecret) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *WebhookWithSecret) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetSecret

`func (o *WebhookWithSecret) GetSecret() string`

GetSecret returns the Secret field if non-nil, zero value otherwise.

### GetSecretOk

`func (o *WebhookWithSecret) GetSecretOk() (*string, bool)`

GetSecretOk returns a tuple with the Secret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecret

`func (o *WebhookWithSecret) SetSecret(v string)`

SetSecret sets Secret field to given value.

### HasSecret

`func (o *WebhookWithSecret) HasSecret() bool`

HasSecret returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


