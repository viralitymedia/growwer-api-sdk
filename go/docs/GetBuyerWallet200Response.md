# GetBuyerWallet200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Balance** | [**Balance**](Balance.md) |  | 
**TopUpUrl** | **string** | The wallet page, in your language (English when the web is not available in it), where you top up your balance. | 

## Methods

### NewGetBuyerWallet200Response

`func NewGetBuyerWallet200Response(balance Balance, topUpUrl string, ) *GetBuyerWallet200Response`

NewGetBuyerWallet200Response instantiates a new GetBuyerWallet200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetBuyerWallet200ResponseWithDefaults

`func NewGetBuyerWallet200ResponseWithDefaults() *GetBuyerWallet200Response`

NewGetBuyerWallet200ResponseWithDefaults instantiates a new GetBuyerWallet200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBalance

`func (o *GetBuyerWallet200Response) GetBalance() Balance`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *GetBuyerWallet200Response) GetBalanceOk() (*Balance, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *GetBuyerWallet200Response) SetBalance(v Balance)`

SetBalance sets Balance field to given value.


### GetTopUpUrl

`func (o *GetBuyerWallet200Response) GetTopUpUrl() string`

GetTopUpUrl returns the TopUpUrl field if non-nil, zero value otherwise.

### GetTopUpUrlOk

`func (o *GetBuyerWallet200Response) GetTopUpUrlOk() (*string, bool)`

GetTopUpUrlOk returns a tuple with the TopUpUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopUpUrl

`func (o *GetBuyerWallet200Response) SetTopUpUrl(v string)`

SetTopUpUrl sets TopUpUrl field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


