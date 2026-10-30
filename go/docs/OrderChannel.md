# OrderChannel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Created** | **string** | Whether the order was placed through this API (&#x60;api&#x60;), through its MCP server (&#x60;mcp&#x60;) or on the web. | 

## Methods

### NewOrderChannel

`func NewOrderChannel(created string, ) *OrderChannel`

NewOrderChannel instantiates a new OrderChannel object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderChannelWithDefaults

`func NewOrderChannelWithDefaults() *OrderChannel`

NewOrderChannelWithDefaults instantiates a new OrderChannel object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreated

`func (o *OrderChannel) GetCreated() string`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *OrderChannel) GetCreatedOk() (*string, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *OrderChannel) SetCreated(v string)`

SetCreated sets Created field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


