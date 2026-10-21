# GetVocabulary200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Countries** | [**[]CodeName**](CodeName.md) | ISO 3166-1 alpha-2 codes. | 
**Languages** | [**[]CodeName**](CodeName.md) | ISO 639 codes, as the web&#39;s language selectors offer them. | 
**Topics** | [**[]GetVocabulary200ResponseTopicsInner**](GetVocabulary200ResponseTopicsInner.md) |  | 
**ProductTypes** | **[]string** | What an order buys: a sponsored post, or a link added to an existing page. | 
**LinkTypes** | **[]string** |  | 
**OrderStates** | **[]string** |  | 

## Methods

### NewGetVocabulary200Response

`func NewGetVocabulary200Response(countries []CodeName, languages []CodeName, topics []GetVocabulary200ResponseTopicsInner, productTypes []string, linkTypes []string, orderStates []string, ) *GetVocabulary200Response`

NewGetVocabulary200Response instantiates a new GetVocabulary200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetVocabulary200ResponseWithDefaults

`func NewGetVocabulary200ResponseWithDefaults() *GetVocabulary200Response`

NewGetVocabulary200ResponseWithDefaults instantiates a new GetVocabulary200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCountries

`func (o *GetVocabulary200Response) GetCountries() []CodeName`

GetCountries returns the Countries field if non-nil, zero value otherwise.

### GetCountriesOk

`func (o *GetVocabulary200Response) GetCountriesOk() (*[]CodeName, bool)`

GetCountriesOk returns a tuple with the Countries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountries

`func (o *GetVocabulary200Response) SetCountries(v []CodeName)`

SetCountries sets Countries field to given value.


### GetLanguages

`func (o *GetVocabulary200Response) GetLanguages() []CodeName`

GetLanguages returns the Languages field if non-nil, zero value otherwise.

### GetLanguagesOk

`func (o *GetVocabulary200Response) GetLanguagesOk() (*[]CodeName, bool)`

GetLanguagesOk returns a tuple with the Languages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguages

`func (o *GetVocabulary200Response) SetLanguages(v []CodeName)`

SetLanguages sets Languages field to given value.


### GetTopics

`func (o *GetVocabulary200Response) GetTopics() []GetVocabulary200ResponseTopicsInner`

GetTopics returns the Topics field if non-nil, zero value otherwise.

### GetTopicsOk

`func (o *GetVocabulary200Response) GetTopicsOk() (*[]GetVocabulary200ResponseTopicsInner, bool)`

GetTopicsOk returns a tuple with the Topics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopics

`func (o *GetVocabulary200Response) SetTopics(v []GetVocabulary200ResponseTopicsInner)`

SetTopics sets Topics field to given value.


### GetProductTypes

`func (o *GetVocabulary200Response) GetProductTypes() []string`

GetProductTypes returns the ProductTypes field if non-nil, zero value otherwise.

### GetProductTypesOk

`func (o *GetVocabulary200Response) GetProductTypesOk() (*[]string, bool)`

GetProductTypesOk returns a tuple with the ProductTypes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProductTypes

`func (o *GetVocabulary200Response) SetProductTypes(v []string)`

SetProductTypes sets ProductTypes field to given value.


### GetLinkTypes

`func (o *GetVocabulary200Response) GetLinkTypes() []string`

GetLinkTypes returns the LinkTypes field if non-nil, zero value otherwise.

### GetLinkTypesOk

`func (o *GetVocabulary200Response) GetLinkTypesOk() (*[]string, bool)`

GetLinkTypesOk returns a tuple with the LinkTypes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkTypes

`func (o *GetVocabulary200Response) SetLinkTypes(v []string)`

SetLinkTypes sets LinkTypes field to given value.


### GetOrderStates

`func (o *GetVocabulary200Response) GetOrderStates() []string`

GetOrderStates returns the OrderStates field if non-nil, zero value otherwise.

### GetOrderStatesOk

`func (o *GetVocabulary200Response) GetOrderStatesOk() (*[]string, bool)`

GetOrderStatesOk returns a tuple with the OrderStates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderStates

`func (o *GetVocabulary200Response) SetOrderStates(v []string)`

SetOrderStates sets OrderStates field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


