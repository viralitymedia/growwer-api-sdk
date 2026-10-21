# GetMe200ResponseManagedService

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Active** | **bool** | Whether you have a managed service: Growwer&#39;s team runs link building campaigns for you (tag Managed services). With one, request a new campaign with POST /managed-service/campaign-requests; without one, ask about the service with POST /managed-service/info-requests. | 

## Methods

### NewGetMe200ResponseManagedService

`func NewGetMe200ResponseManagedService(active bool, ) *GetMe200ResponseManagedService`

NewGetMe200ResponseManagedService instantiates a new GetMe200ResponseManagedService object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetMe200ResponseManagedServiceWithDefaults

`func NewGetMe200ResponseManagedServiceWithDefaults() *GetMe200ResponseManagedService`

NewGetMe200ResponseManagedServiceWithDefaults instantiates a new GetMe200ResponseManagedService object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActive

`func (o *GetMe200ResponseManagedService) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *GetMe200ResponseManagedService) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *GetMe200ResponseManagedService) SetActive(v bool)`

SetActive sets Active field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


