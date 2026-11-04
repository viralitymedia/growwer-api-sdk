# ListWebhookDeliveries200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]WebhookDelivery**](WebhookDelivery.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewListWebhookDeliveries200Response

`func NewListWebhookDeliveries200Response(items []WebhookDelivery, total int32, ) *ListWebhookDeliveries200Response`

NewListWebhookDeliveries200Response instantiates a new ListWebhookDeliveries200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListWebhookDeliveries200ResponseWithDefaults

`func NewListWebhookDeliveries200ResponseWithDefaults() *ListWebhookDeliveries200Response`

NewListWebhookDeliveries200ResponseWithDefaults instantiates a new ListWebhookDeliveries200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListWebhookDeliveries200Response) GetItems() []WebhookDelivery`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListWebhookDeliveries200Response) GetItemsOk() (*[]WebhookDelivery, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListWebhookDeliveries200Response) SetItems(v []WebhookDelivery)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ListWebhookDeliveries200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListWebhookDeliveries200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListWebhookDeliveries200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


