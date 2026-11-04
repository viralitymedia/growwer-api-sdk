# Webhook

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

## Methods

### NewWebhook

`func NewWebhook(id string, url string, events []WebhookEventType, lowBalanceThreshold NullableMoneyOrNull, description NullableString, enabled bool, disabledReason NullableString, failingSince NullableTime, previousSecretExpiresAt NullableTime, createdAt time.Time, updatedAt time.Time, ) *Webhook`

NewWebhook instantiates a new Webhook object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebhookWithDefaults

`func NewWebhookWithDefaults() *Webhook`

NewWebhookWithDefaults instantiates a new Webhook object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Webhook) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Webhook) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Webhook) SetId(v string)`

SetId sets Id field to given value.


### GetUrl

`func (o *Webhook) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *Webhook) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *Webhook) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetEvents

`func (o *Webhook) GetEvents() []WebhookEventType`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *Webhook) GetEventsOk() (*[]WebhookEventType, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *Webhook) SetEvents(v []WebhookEventType)`

SetEvents sets Events field to given value.


### GetLowBalanceThreshold

`func (o *Webhook) GetLowBalanceThreshold() MoneyOrNull`

GetLowBalanceThreshold returns the LowBalanceThreshold field if non-nil, zero value otherwise.

### GetLowBalanceThresholdOk

`func (o *Webhook) GetLowBalanceThresholdOk() (*MoneyOrNull, bool)`

GetLowBalanceThresholdOk returns a tuple with the LowBalanceThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLowBalanceThreshold

`func (o *Webhook) SetLowBalanceThreshold(v MoneyOrNull)`

SetLowBalanceThreshold sets LowBalanceThreshold field to given value.


### SetLowBalanceThresholdNil

`func (o *Webhook) SetLowBalanceThresholdNil(b bool)`

 SetLowBalanceThresholdNil sets the value for LowBalanceThreshold to be an explicit nil

### UnsetLowBalanceThreshold
`func (o *Webhook) UnsetLowBalanceThreshold()`

UnsetLowBalanceThreshold ensures that no value is present for LowBalanceThreshold, not even an explicit nil
### GetDescription

`func (o *Webhook) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Webhook) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Webhook) SetDescription(v string)`

SetDescription sets Description field to given value.


### SetDescriptionNil

`func (o *Webhook) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Webhook) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetEnabled

`func (o *Webhook) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *Webhook) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *Webhook) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.


### GetDisabledReason

`func (o *Webhook) GetDisabledReason() string`

GetDisabledReason returns the DisabledReason field if non-nil, zero value otherwise.

### GetDisabledReasonOk

`func (o *Webhook) GetDisabledReasonOk() (*string, bool)`

GetDisabledReasonOk returns a tuple with the DisabledReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisabledReason

`func (o *Webhook) SetDisabledReason(v string)`

SetDisabledReason sets DisabledReason field to given value.


### SetDisabledReasonNil

`func (o *Webhook) SetDisabledReasonNil(b bool)`

 SetDisabledReasonNil sets the value for DisabledReason to be an explicit nil

### UnsetDisabledReason
`func (o *Webhook) UnsetDisabledReason()`

UnsetDisabledReason ensures that no value is present for DisabledReason, not even an explicit nil
### GetFailingSince

`func (o *Webhook) GetFailingSince() time.Time`

GetFailingSince returns the FailingSince field if non-nil, zero value otherwise.

### GetFailingSinceOk

`func (o *Webhook) GetFailingSinceOk() (*time.Time, bool)`

GetFailingSinceOk returns a tuple with the FailingSince field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailingSince

`func (o *Webhook) SetFailingSince(v time.Time)`

SetFailingSince sets FailingSince field to given value.


### SetFailingSinceNil

`func (o *Webhook) SetFailingSinceNil(b bool)`

 SetFailingSinceNil sets the value for FailingSince to be an explicit nil

### UnsetFailingSince
`func (o *Webhook) UnsetFailingSince()`

UnsetFailingSince ensures that no value is present for FailingSince, not even an explicit nil
### GetPreviousSecretExpiresAt

`func (o *Webhook) GetPreviousSecretExpiresAt() time.Time`

GetPreviousSecretExpiresAt returns the PreviousSecretExpiresAt field if non-nil, zero value otherwise.

### GetPreviousSecretExpiresAtOk

`func (o *Webhook) GetPreviousSecretExpiresAtOk() (*time.Time, bool)`

GetPreviousSecretExpiresAtOk returns a tuple with the PreviousSecretExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreviousSecretExpiresAt

`func (o *Webhook) SetPreviousSecretExpiresAt(v time.Time)`

SetPreviousSecretExpiresAt sets PreviousSecretExpiresAt field to given value.


### SetPreviousSecretExpiresAtNil

`func (o *Webhook) SetPreviousSecretExpiresAtNil(b bool)`

 SetPreviousSecretExpiresAtNil sets the value for PreviousSecretExpiresAt to be an explicit nil

### UnsetPreviousSecretExpiresAt
`func (o *Webhook) UnsetPreviousSecretExpiresAt()`

UnsetPreviousSecretExpiresAt ensures that no value is present for PreviousSecretExpiresAt, not even an explicit nil
### GetCreatedAt

`func (o *Webhook) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Webhook) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Webhook) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *Webhook) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Webhook) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Webhook) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


