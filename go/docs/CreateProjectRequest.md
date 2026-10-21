# CreateProjectRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **NullableString** |  | [optional] 
**RootUrl** | **string** |  | 
**WebsiteType** | **string** |  | 
**Topics** | **[]int32** | Exactly one topic id from GET /vocabulary. | 
**Language** | **string** | A language code from GET /vocabulary. | 
**Country** | Pointer to **NullableString** | A country code from GET /vocabulary; omit it or send null for worldwide. | [optional] 
**PromotedProducts** | **[]string** | 5 to 10 products or services the campaign promotes. | 
**UserKeywords** | Pointer to **[]string** | At most 100 keywords, none with a line break. | [optional] 

## Methods

### NewCreateProjectRequest

`func NewCreateProjectRequest(rootUrl string, websiteType string, topics []int32, language string, promotedProducts []string, ) *CreateProjectRequest`

NewCreateProjectRequest instantiates a new CreateProjectRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateProjectRequestWithDefaults

`func NewCreateProjectRequestWithDefaults() *CreateProjectRequest`

NewCreateProjectRequestWithDefaults instantiates a new CreateProjectRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateProjectRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateProjectRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateProjectRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *CreateProjectRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *CreateProjectRequest) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *CreateProjectRequest) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetRootUrl

`func (o *CreateProjectRequest) GetRootUrl() string`

GetRootUrl returns the RootUrl field if non-nil, zero value otherwise.

### GetRootUrlOk

`func (o *CreateProjectRequest) GetRootUrlOk() (*string, bool)`

GetRootUrlOk returns a tuple with the RootUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRootUrl

`func (o *CreateProjectRequest) SetRootUrl(v string)`

SetRootUrl sets RootUrl field to given value.


### GetWebsiteType

`func (o *CreateProjectRequest) GetWebsiteType() string`

GetWebsiteType returns the WebsiteType field if non-nil, zero value otherwise.

### GetWebsiteTypeOk

`func (o *CreateProjectRequest) GetWebsiteTypeOk() (*string, bool)`

GetWebsiteTypeOk returns a tuple with the WebsiteType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsiteType

`func (o *CreateProjectRequest) SetWebsiteType(v string)`

SetWebsiteType sets WebsiteType field to given value.


### GetTopics

`func (o *CreateProjectRequest) GetTopics() []int32`

GetTopics returns the Topics field if non-nil, zero value otherwise.

### GetTopicsOk

`func (o *CreateProjectRequest) GetTopicsOk() (*[]int32, bool)`

GetTopicsOk returns a tuple with the Topics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopics

`func (o *CreateProjectRequest) SetTopics(v []int32)`

SetTopics sets Topics field to given value.


### GetLanguage

`func (o *CreateProjectRequest) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *CreateProjectRequest) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *CreateProjectRequest) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetCountry

`func (o *CreateProjectRequest) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *CreateProjectRequest) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *CreateProjectRequest) SetCountry(v string)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *CreateProjectRequest) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### SetCountryNil

`func (o *CreateProjectRequest) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *CreateProjectRequest) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil
### GetPromotedProducts

`func (o *CreateProjectRequest) GetPromotedProducts() []string`

GetPromotedProducts returns the PromotedProducts field if non-nil, zero value otherwise.

### GetPromotedProductsOk

`func (o *CreateProjectRequest) GetPromotedProductsOk() (*[]string, bool)`

GetPromotedProductsOk returns a tuple with the PromotedProducts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPromotedProducts

`func (o *CreateProjectRequest) SetPromotedProducts(v []string)`

SetPromotedProducts sets PromotedProducts field to given value.


### GetUserKeywords

`func (o *CreateProjectRequest) GetUserKeywords() []string`

GetUserKeywords returns the UserKeywords field if non-nil, zero value otherwise.

### GetUserKeywordsOk

`func (o *CreateProjectRequest) GetUserKeywordsOk() (*[]string, bool)`

GetUserKeywordsOk returns a tuple with the UserKeywords field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserKeywords

`func (o *CreateProjectRequest) SetUserKeywords(v []string)`

SetUserKeywords sets UserKeywords field to given value.

### HasUserKeywords

`func (o *CreateProjectRequest) HasUserKeywords() bool`

HasUserKeywords returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


