# RequestMediasRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Domains** | **[]string** | Domains or URLs, 1 to 200 distinct domains. | 

## Methods

### NewRequestMediasRequest

`func NewRequestMediasRequest(domains []string, ) *RequestMediasRequest`

NewRequestMediasRequest instantiates a new RequestMediasRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRequestMediasRequestWithDefaults

`func NewRequestMediasRequestWithDefaults() *RequestMediasRequest`

NewRequestMediasRequestWithDefaults instantiates a new RequestMediasRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDomains

`func (o *RequestMediasRequest) GetDomains() []string`

GetDomains returns the Domains field if non-nil, zero value otherwise.

### GetDomainsOk

`func (o *RequestMediasRequest) GetDomainsOk() (*[]string, bool)`

GetDomainsOk returns a tuple with the Domains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomains

`func (o *RequestMediasRequest) SetDomains(v []string)`

SetDomains sets Domains field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


