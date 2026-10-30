# SellerOrderChannel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Created** | **string** | Whether the order was placed through this API (&#x60;api&#x60;), through its MCP server (&#x60;mcp&#x60;) or on the web. | 
**Accepted** | **NullableString** | Whether you accepted the order through this API (&#x60;api&#x60;), through its MCP server (&#x60;mcp&#x60;) or elsewhere (&#x60;web&#x60;), or null while it is not accepted. | 

## Methods

### NewSellerOrderChannel

`func NewSellerOrderChannel(created string, accepted NullableString, ) *SellerOrderChannel`

NewSellerOrderChannel instantiates a new SellerOrderChannel object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerOrderChannelWithDefaults

`func NewSellerOrderChannelWithDefaults() *SellerOrderChannel`

NewSellerOrderChannelWithDefaults instantiates a new SellerOrderChannel object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreated

`func (o *SellerOrderChannel) GetCreated() string`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *SellerOrderChannel) GetCreatedOk() (*string, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *SellerOrderChannel) SetCreated(v string)`

SetCreated sets Created field to given value.


### GetAccepted

`func (o *SellerOrderChannel) GetAccepted() string`

GetAccepted returns the Accepted field if non-nil, zero value otherwise.

### GetAcceptedOk

`func (o *SellerOrderChannel) GetAcceptedOk() (*string, bool)`

GetAcceptedOk returns a tuple with the Accepted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccepted

`func (o *SellerOrderChannel) SetAccepted(v string)`

SetAccepted sets Accepted field to given value.


### SetAcceptedNil

`func (o *SellerOrderChannel) SetAcceptedNil(b bool)`

 SetAcceptedNil sets the value for Accepted to be an explicit nil

### UnsetAccepted
`func (o *SellerOrderChannel) UnsetAccepted()`

UnsetAccepted ensures that no value is present for Accepted, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


