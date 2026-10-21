# GetSellerWallet200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Balance** | [**Balance**](Balance.md) |  | 
**Restricted** | **bool** | Whether your seller account is restricted. | 

## Methods

### NewGetSellerWallet200Response

`func NewGetSellerWallet200Response(balance Balance, restricted bool, ) *GetSellerWallet200Response`

NewGetSellerWallet200Response instantiates a new GetSellerWallet200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetSellerWallet200ResponseWithDefaults

`func NewGetSellerWallet200ResponseWithDefaults() *GetSellerWallet200Response`

NewGetSellerWallet200ResponseWithDefaults instantiates a new GetSellerWallet200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBalance

`func (o *GetSellerWallet200Response) GetBalance() Balance`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *GetSellerWallet200Response) GetBalanceOk() (*Balance, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *GetSellerWallet200Response) SetBalance(v Balance)`

SetBalance sets Balance field to given value.


### GetRestricted

`func (o *GetSellerWallet200Response) GetRestricted() bool`

GetRestricted returns the Restricted field if non-nil, zero value otherwise.

### GetRestrictedOk

`func (o *GetSellerWallet200Response) GetRestrictedOk() (*bool, bool)`

GetRestrictedOk returns a tuple with the Restricted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestricted

`func (o *GetSellerWallet200Response) SetRestricted(v bool)`

SetRestricted sets Restricted field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


