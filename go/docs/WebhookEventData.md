# WebhookEventData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Order** | [**Order**](Order.md) |  | 
**Wallet** | [**BalanceLowEventDataWallet**](BalanceLowEventDataWallet.md) |  | 
**Threshold** | [**Money**](Money.md) | The subscription&#39;s &#x60;lowBalanceThreshold&#x60; that the balance dropped below. | 
**WebhookId** | **string** | The subscription it was sent to. | 

## Methods

### NewWebhookEventData

`func NewWebhookEventData(order Order, wallet BalanceLowEventDataWallet, threshold Money, webhookId string, ) *WebhookEventData`

NewWebhookEventData instantiates a new WebhookEventData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebhookEventDataWithDefaults

`func NewWebhookEventDataWithDefaults() *WebhookEventData`

NewWebhookEventDataWithDefaults instantiates a new WebhookEventData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOrder

`func (o *WebhookEventData) GetOrder() Order`

GetOrder returns the Order field if non-nil, zero value otherwise.

### GetOrderOk

`func (o *WebhookEventData) GetOrderOk() (*Order, bool)`

GetOrderOk returns a tuple with the Order field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrder

`func (o *WebhookEventData) SetOrder(v Order)`

SetOrder sets Order field to given value.


### GetWallet

`func (o *WebhookEventData) GetWallet() BalanceLowEventDataWallet`

GetWallet returns the Wallet field if non-nil, zero value otherwise.

### GetWalletOk

`func (o *WebhookEventData) GetWalletOk() (*BalanceLowEventDataWallet, bool)`

GetWalletOk returns a tuple with the Wallet field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWallet

`func (o *WebhookEventData) SetWallet(v BalanceLowEventDataWallet)`

SetWallet sets Wallet field to given value.


### GetThreshold

`func (o *WebhookEventData) GetThreshold() Money`

GetThreshold returns the Threshold field if non-nil, zero value otherwise.

### GetThresholdOk

`func (o *WebhookEventData) GetThresholdOk() (*Money, bool)`

GetThresholdOk returns a tuple with the Threshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreshold

`func (o *WebhookEventData) SetThreshold(v Money)`

SetThreshold sets Threshold field to given value.


### GetWebhookId

`func (o *WebhookEventData) GetWebhookId() string`

GetWebhookId returns the WebhookId field if non-nil, zero value otherwise.

### GetWebhookIdOk

`func (o *WebhookEventData) GetWebhookIdOk() (*string, bool)`

GetWebhookIdOk returns a tuple with the WebhookId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebhookId

`func (o *WebhookEventData) SetWebhookId(v string)`

SetWebhookId sets WebhookId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


