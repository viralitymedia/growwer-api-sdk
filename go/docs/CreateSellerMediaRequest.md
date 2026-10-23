# CreateSellerMediaRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RootUrl** | **string** |  | 
**Typology** | **string** |  | 
**Country** | **string** | A country code from GET /vocabulary. | 
**Language** | **string** | A language code from GET /vocabulary. | 
**Topics** | **[]int32** | Topic ids from GET /vocabulary. | 
**BannedTopics** | Pointer to **[]int32** | The topic ids from GET /vocabulary the media refuses. | [optional] 
**PostOffer** | [**CreateSellerMediaRequestPostOffer**](CreateSellerMediaRequestPostOffer.md) |  | 
**LinkAdditionOffer** | Pointer to [**NullableUpdateSellerMediaRequestLinkAdditionOffer**](UpdateSellerMediaRequestLinkAdditionOffer.md) |  | [optional] 
**ExtraServices** | Pointer to [**[]UpdateSellerMediaRequestExtraServicesInner**](UpdateSellerMediaRequestExtraServicesInner.md) |  | [optional] 
**AcceptMediaPublishingTerms** | **bool** | Must be true: you accept the media publishing terms. | 
**DeclareMediaOwnership** | **bool** | Must be true: you own or manage this media. | 

## Methods

### NewCreateSellerMediaRequest

`func NewCreateSellerMediaRequest(rootUrl string, typology string, country string, language string, topics []int32, postOffer CreateSellerMediaRequestPostOffer, acceptMediaPublishingTerms bool, declareMediaOwnership bool, ) *CreateSellerMediaRequest`

NewCreateSellerMediaRequest instantiates a new CreateSellerMediaRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateSellerMediaRequestWithDefaults

`func NewCreateSellerMediaRequestWithDefaults() *CreateSellerMediaRequest`

NewCreateSellerMediaRequestWithDefaults instantiates a new CreateSellerMediaRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRootUrl

`func (o *CreateSellerMediaRequest) GetRootUrl() string`

GetRootUrl returns the RootUrl field if non-nil, zero value otherwise.

### GetRootUrlOk

`func (o *CreateSellerMediaRequest) GetRootUrlOk() (*string, bool)`

GetRootUrlOk returns a tuple with the RootUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRootUrl

`func (o *CreateSellerMediaRequest) SetRootUrl(v string)`

SetRootUrl sets RootUrl field to given value.


### GetTypology

`func (o *CreateSellerMediaRequest) GetTypology() string`

GetTypology returns the Typology field if non-nil, zero value otherwise.

### GetTypologyOk

`func (o *CreateSellerMediaRequest) GetTypologyOk() (*string, bool)`

GetTypologyOk returns a tuple with the Typology field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTypology

`func (o *CreateSellerMediaRequest) SetTypology(v string)`

SetTypology sets Typology field to given value.


### GetCountry

`func (o *CreateSellerMediaRequest) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *CreateSellerMediaRequest) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *CreateSellerMediaRequest) SetCountry(v string)`

SetCountry sets Country field to given value.


### GetLanguage

`func (o *CreateSellerMediaRequest) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *CreateSellerMediaRequest) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *CreateSellerMediaRequest) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetTopics

`func (o *CreateSellerMediaRequest) GetTopics() []int32`

GetTopics returns the Topics field if non-nil, zero value otherwise.

### GetTopicsOk

`func (o *CreateSellerMediaRequest) GetTopicsOk() (*[]int32, bool)`

GetTopicsOk returns a tuple with the Topics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopics

`func (o *CreateSellerMediaRequest) SetTopics(v []int32)`

SetTopics sets Topics field to given value.


### GetBannedTopics

`func (o *CreateSellerMediaRequest) GetBannedTopics() []int32`

GetBannedTopics returns the BannedTopics field if non-nil, zero value otherwise.

### GetBannedTopicsOk

`func (o *CreateSellerMediaRequest) GetBannedTopicsOk() (*[]int32, bool)`

GetBannedTopicsOk returns a tuple with the BannedTopics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBannedTopics

`func (o *CreateSellerMediaRequest) SetBannedTopics(v []int32)`

SetBannedTopics sets BannedTopics field to given value.

### HasBannedTopics

`func (o *CreateSellerMediaRequest) HasBannedTopics() bool`

HasBannedTopics returns a boolean if a field has been set.

### GetPostOffer

`func (o *CreateSellerMediaRequest) GetPostOffer() CreateSellerMediaRequestPostOffer`

GetPostOffer returns the PostOffer field if non-nil, zero value otherwise.

### GetPostOfferOk

`func (o *CreateSellerMediaRequest) GetPostOfferOk() (*CreateSellerMediaRequestPostOffer, bool)`

GetPostOfferOk returns a tuple with the PostOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostOffer

`func (o *CreateSellerMediaRequest) SetPostOffer(v CreateSellerMediaRequestPostOffer)`

SetPostOffer sets PostOffer field to given value.


### GetLinkAdditionOffer

`func (o *CreateSellerMediaRequest) GetLinkAdditionOffer() UpdateSellerMediaRequestLinkAdditionOffer`

GetLinkAdditionOffer returns the LinkAdditionOffer field if non-nil, zero value otherwise.

### GetLinkAdditionOfferOk

`func (o *CreateSellerMediaRequest) GetLinkAdditionOfferOk() (*UpdateSellerMediaRequestLinkAdditionOffer, bool)`

GetLinkAdditionOfferOk returns a tuple with the LinkAdditionOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkAdditionOffer

`func (o *CreateSellerMediaRequest) SetLinkAdditionOffer(v UpdateSellerMediaRequestLinkAdditionOffer)`

SetLinkAdditionOffer sets LinkAdditionOffer field to given value.

### HasLinkAdditionOffer

`func (o *CreateSellerMediaRequest) HasLinkAdditionOffer() bool`

HasLinkAdditionOffer returns a boolean if a field has been set.

### SetLinkAdditionOfferNil

`func (o *CreateSellerMediaRequest) SetLinkAdditionOfferNil(b bool)`

 SetLinkAdditionOfferNil sets the value for LinkAdditionOffer to be an explicit nil

### UnsetLinkAdditionOffer
`func (o *CreateSellerMediaRequest) UnsetLinkAdditionOffer()`

UnsetLinkAdditionOffer ensures that no value is present for LinkAdditionOffer, not even an explicit nil
### GetExtraServices

`func (o *CreateSellerMediaRequest) GetExtraServices() []UpdateSellerMediaRequestExtraServicesInner`

GetExtraServices returns the ExtraServices field if non-nil, zero value otherwise.

### GetExtraServicesOk

`func (o *CreateSellerMediaRequest) GetExtraServicesOk() (*[]UpdateSellerMediaRequestExtraServicesInner, bool)`

GetExtraServicesOk returns a tuple with the ExtraServices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtraServices

`func (o *CreateSellerMediaRequest) SetExtraServices(v []UpdateSellerMediaRequestExtraServicesInner)`

SetExtraServices sets ExtraServices field to given value.

### HasExtraServices

`func (o *CreateSellerMediaRequest) HasExtraServices() bool`

HasExtraServices returns a boolean if a field has been set.

### GetAcceptMediaPublishingTerms

`func (o *CreateSellerMediaRequest) GetAcceptMediaPublishingTerms() bool`

GetAcceptMediaPublishingTerms returns the AcceptMediaPublishingTerms field if non-nil, zero value otherwise.

### GetAcceptMediaPublishingTermsOk

`func (o *CreateSellerMediaRequest) GetAcceptMediaPublishingTermsOk() (*bool, bool)`

GetAcceptMediaPublishingTermsOk returns a tuple with the AcceptMediaPublishingTerms field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAcceptMediaPublishingTerms

`func (o *CreateSellerMediaRequest) SetAcceptMediaPublishingTerms(v bool)`

SetAcceptMediaPublishingTerms sets AcceptMediaPublishingTerms field to given value.


### GetDeclareMediaOwnership

`func (o *CreateSellerMediaRequest) GetDeclareMediaOwnership() bool`

GetDeclareMediaOwnership returns the DeclareMediaOwnership field if non-nil, zero value otherwise.

### GetDeclareMediaOwnershipOk

`func (o *CreateSellerMediaRequest) GetDeclareMediaOwnershipOk() (*bool, bool)`

GetDeclareMediaOwnershipOk returns a tuple with the DeclareMediaOwnership field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeclareMediaOwnership

`func (o *CreateSellerMediaRequest) SetDeclareMediaOwnership(v bool)`

SetDeclareMediaOwnership sets DeclareMediaOwnership field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


