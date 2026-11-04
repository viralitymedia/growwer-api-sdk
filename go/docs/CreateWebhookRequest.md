# CreateWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | **string** | An HTTPS URL of at most 2048 characters, without a backslash or credentials. Its host is an IP address or a domain name of two labels or more, such as hooks.example.com, with one trailing dot allowed; a single-label host such as localhost is refused (&#x60;validation_failed&#x60; on &#x60;url&#x60;). The host is checked, and resolved at each delivery, in lower case and with a Unicode name in punycode, the form a delivery connects to. | 
**Events** | [**[]WebhookEventType**](WebhookEventType.md) | The events to send, at least one. | 
**LowBalanceThreshold** | Pointer to [**Money**](Money.md) | With &#x60;balance.low&#x60;: the available buyer balance below which the event fires, in EUR. | [optional] 
**Description** | Pointer to **NullableString** | A note of yours, at most 255 characters. | [optional] 

## Methods

### NewCreateWebhookRequest

`func NewCreateWebhookRequest(url string, events []WebhookEventType, ) *CreateWebhookRequest`

NewCreateWebhookRequest instantiates a new CreateWebhookRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateWebhookRequestWithDefaults

`func NewCreateWebhookRequestWithDefaults() *CreateWebhookRequest`

NewCreateWebhookRequestWithDefaults instantiates a new CreateWebhookRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUrl

`func (o *CreateWebhookRequest) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *CreateWebhookRequest) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *CreateWebhookRequest) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetEvents

`func (o *CreateWebhookRequest) GetEvents() []WebhookEventType`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *CreateWebhookRequest) GetEventsOk() (*[]WebhookEventType, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *CreateWebhookRequest) SetEvents(v []WebhookEventType)`

SetEvents sets Events field to given value.


### GetLowBalanceThreshold

`func (o *CreateWebhookRequest) GetLowBalanceThreshold() Money`

GetLowBalanceThreshold returns the LowBalanceThreshold field if non-nil, zero value otherwise.

### GetLowBalanceThresholdOk

`func (o *CreateWebhookRequest) GetLowBalanceThresholdOk() (*Money, bool)`

GetLowBalanceThresholdOk returns a tuple with the LowBalanceThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLowBalanceThreshold

`func (o *CreateWebhookRequest) SetLowBalanceThreshold(v Money)`

SetLowBalanceThreshold sets LowBalanceThreshold field to given value.

### HasLowBalanceThreshold

`func (o *CreateWebhookRequest) HasLowBalanceThreshold() bool`

HasLowBalanceThreshold returns a boolean if a field has been set.

### GetDescription

`func (o *CreateWebhookRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateWebhookRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateWebhookRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateWebhookRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *CreateWebhookRequest) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *CreateWebhookRequest) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


