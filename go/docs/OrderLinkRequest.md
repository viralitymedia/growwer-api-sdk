# OrderLinkRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TargetUrl** | Pointer to **string** | Where the link points; leave it out for a citation. | [optional] 
**Anchor** | Pointer to **string** | The anchor text; leave it out to let the media choose it. A citation needs one. | [optional] 
**Type** | **string** | A link type the media offers for this type of order (CatalogueOffer &#x60;linkTypes&#x60;). | 

## Methods

### NewOrderLinkRequest

`func NewOrderLinkRequest(type_ string, ) *OrderLinkRequest`

NewOrderLinkRequest instantiates a new OrderLinkRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderLinkRequestWithDefaults

`func NewOrderLinkRequestWithDefaults() *OrderLinkRequest`

NewOrderLinkRequestWithDefaults instantiates a new OrderLinkRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTargetUrl

`func (o *OrderLinkRequest) GetTargetUrl() string`

GetTargetUrl returns the TargetUrl field if non-nil, zero value otherwise.

### GetTargetUrlOk

`func (o *OrderLinkRequest) GetTargetUrlOk() (*string, bool)`

GetTargetUrlOk returns a tuple with the TargetUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetUrl

`func (o *OrderLinkRequest) SetTargetUrl(v string)`

SetTargetUrl sets TargetUrl field to given value.

### HasTargetUrl

`func (o *OrderLinkRequest) HasTargetUrl() bool`

HasTargetUrl returns a boolean if a field has been set.

### GetAnchor

`func (o *OrderLinkRequest) GetAnchor() string`

GetAnchor returns the Anchor field if non-nil, zero value otherwise.

### GetAnchorOk

`func (o *OrderLinkRequest) GetAnchorOk() (*string, bool)`

GetAnchorOk returns a tuple with the Anchor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAnchor

`func (o *OrderLinkRequest) SetAnchor(v string)`

SetAnchor sets Anchor field to given value.

### HasAnchor

`func (o *OrderLinkRequest) HasAnchor() bool`

HasAnchor returns a boolean if a field has been set.

### GetType

`func (o *OrderLinkRequest) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *OrderLinkRequest) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *OrderLinkRequest) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


