# OrderProject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **NullableString** | Null once the project is deleted. | 
**Url** | **string** | The project&#39;s URL when the order was placed. | 

## Methods

### NewOrderProject

`func NewOrderProject(id NullableString, url string, ) *OrderProject`

NewOrderProject instantiates a new OrderProject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderProjectWithDefaults

`func NewOrderProjectWithDefaults() *OrderProject`

NewOrderProjectWithDefaults instantiates a new OrderProject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *OrderProject) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *OrderProject) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *OrderProject) SetId(v string)`

SetId sets Id field to given value.


### SetIdNil

`func (o *OrderProject) SetIdNil(b bool)`

 SetIdNil sets the value for Id to be an explicit nil

### UnsetId
`func (o *OrderProject) UnsetId()`

UnsetId ensures that no value is present for Id, not even an explicit nil
### GetUrl

`func (o *OrderProject) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *OrderProject) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *OrderProject) SetUrl(v string)`

SetUrl sets Url field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


