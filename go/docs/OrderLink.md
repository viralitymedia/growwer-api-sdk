# OrderLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TargetUrl** | **NullableString** | Where the link points, or null for a citation. | 
**Anchor** | **NullableString** | The anchor text, or null when the media chooses it. A citation always has one. | 
**Type** | **string** |  | 

## Methods

### NewOrderLink

`func NewOrderLink(targetUrl NullableString, anchor NullableString, type_ string, ) *OrderLink`

NewOrderLink instantiates a new OrderLink object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderLinkWithDefaults

`func NewOrderLinkWithDefaults() *OrderLink`

NewOrderLinkWithDefaults instantiates a new OrderLink object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTargetUrl

`func (o *OrderLink) GetTargetUrl() string`

GetTargetUrl returns the TargetUrl field if non-nil, zero value otherwise.

### GetTargetUrlOk

`func (o *OrderLink) GetTargetUrlOk() (*string, bool)`

GetTargetUrlOk returns a tuple with the TargetUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetUrl

`func (o *OrderLink) SetTargetUrl(v string)`

SetTargetUrl sets TargetUrl field to given value.


### SetTargetUrlNil

`func (o *OrderLink) SetTargetUrlNil(b bool)`

 SetTargetUrlNil sets the value for TargetUrl to be an explicit nil

### UnsetTargetUrl
`func (o *OrderLink) UnsetTargetUrl()`

UnsetTargetUrl ensures that no value is present for TargetUrl, not even an explicit nil
### GetAnchor

`func (o *OrderLink) GetAnchor() string`

GetAnchor returns the Anchor field if non-nil, zero value otherwise.

### GetAnchorOk

`func (o *OrderLink) GetAnchorOk() (*string, bool)`

GetAnchorOk returns a tuple with the Anchor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAnchor

`func (o *OrderLink) SetAnchor(v string)`

SetAnchor sets Anchor field to given value.


### SetAnchorNil

`func (o *OrderLink) SetAnchorNil(b bool)`

 SetAnchorNil sets the value for Anchor to be an explicit nil

### UnsetAnchor
`func (o *OrderLink) UnsetAnchor()`

UnsetAnchor ensures that no value is present for Anchor, not even an explicit nil
### GetType

`func (o *OrderLink) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *OrderLink) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *OrderLink) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


