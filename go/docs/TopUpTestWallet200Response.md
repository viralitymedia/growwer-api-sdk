# TopUpTestWallet200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Balance** | [**Balance**](Balance.md) |  | 
**TopUpUrl** | **string** | The wallet page where a live buyer tops up, as GET /wallets/buyer gives it. | 

## Methods

### NewTopUpTestWallet200Response

`func NewTopUpTestWallet200Response(balance Balance, topUpUrl string, ) *TopUpTestWallet200Response`

NewTopUpTestWallet200Response instantiates a new TopUpTestWallet200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTopUpTestWallet200ResponseWithDefaults

`func NewTopUpTestWallet200ResponseWithDefaults() *TopUpTestWallet200Response`

NewTopUpTestWallet200ResponseWithDefaults instantiates a new TopUpTestWallet200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBalance

`func (o *TopUpTestWallet200Response) GetBalance() Balance`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *TopUpTestWallet200Response) GetBalanceOk() (*Balance, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *TopUpTestWallet200Response) SetBalance(v Balance)`

SetBalance sets Balance field to given value.


### GetTopUpUrl

`func (o *TopUpTestWallet200Response) GetTopUpUrl() string`

GetTopUpUrl returns the TopUpUrl field if non-nil, zero value otherwise.

### GetTopUpUrlOk

`func (o *TopUpTestWallet200Response) GetTopUpUrlOk() (*string, bool)`

GetTopUpUrlOk returns a tuple with the TopUpUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopUpUrl

`func (o *TopUpTestWallet200Response) SetTopUpUrl(v string)`

SetTopUpUrl sets TopUpUrl field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


