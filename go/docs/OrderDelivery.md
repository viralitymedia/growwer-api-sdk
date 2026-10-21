# OrderDelivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | **string** | The published article, or for a link addition the article the link went into. | 
**PublishedAt** | **NullableTime** | When the post was published; null for a link addition. | 

## Methods

### NewOrderDelivery

`func NewOrderDelivery(url string, publishedAt NullableTime, ) *OrderDelivery`

NewOrderDelivery instantiates a new OrderDelivery object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderDeliveryWithDefaults

`func NewOrderDeliveryWithDefaults() *OrderDelivery`

NewOrderDeliveryWithDefaults instantiates a new OrderDelivery object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUrl

`func (o *OrderDelivery) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *OrderDelivery) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *OrderDelivery) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetPublishedAt

`func (o *OrderDelivery) GetPublishedAt() time.Time`

GetPublishedAt returns the PublishedAt field if non-nil, zero value otherwise.

### GetPublishedAtOk

`func (o *OrderDelivery) GetPublishedAtOk() (*time.Time, bool)`

GetPublishedAtOk returns a tuple with the PublishedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublishedAt

`func (o *OrderDelivery) SetPublishedAt(v time.Time)`

SetPublishedAt sets PublishedAt field to given value.


### SetPublishedAtNil

`func (o *OrderDelivery) SetPublishedAtNil(b bool)`

 SetPublishedAtNil sets the value for PublishedAt to be an explicit nil

### UnsetPublishedAt
`func (o *OrderDelivery) UnsetPublishedAt()`

UnsetPublishedAt ensures that no value is present for PublishedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


