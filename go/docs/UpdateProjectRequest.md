# UpdateProjectRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **NullableString** | Null or an empty string removes the name. | [optional] 
**WebsiteType** | Pointer to **string** |  | [optional] 
**Topics** | Pointer to **[]int32** | Exactly one topic id from GET /vocabulary. | [optional] 
**Language** | Pointer to **string** | A language code from GET /vocabulary. | [optional] 
**Country** | Pointer to **NullableString** | A country code from GET /vocabulary, or null for worldwide. | [optional] 
**PromotedProducts** | Pointer to **[]string** | 5 to 10 products or services the campaign promotes. | [optional] 
**UserKeywords** | Pointer to **[]string** | At most 100 keywords, none with a line break. | [optional] 

## Methods

### NewUpdateProjectRequest

`func NewUpdateProjectRequest() *UpdateProjectRequest`

NewUpdateProjectRequest instantiates a new UpdateProjectRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateProjectRequestWithDefaults

`func NewUpdateProjectRequestWithDefaults() *UpdateProjectRequest`

NewUpdateProjectRequestWithDefaults instantiates a new UpdateProjectRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *UpdateProjectRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateProjectRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpdateProjectRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *UpdateProjectRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *UpdateProjectRequest) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *UpdateProjectRequest) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetWebsiteType

`func (o *UpdateProjectRequest) GetWebsiteType() string`

GetWebsiteType returns the WebsiteType field if non-nil, zero value otherwise.

### GetWebsiteTypeOk

`func (o *UpdateProjectRequest) GetWebsiteTypeOk() (*string, bool)`

GetWebsiteTypeOk returns a tuple with the WebsiteType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsiteType

`func (o *UpdateProjectRequest) SetWebsiteType(v string)`

SetWebsiteType sets WebsiteType field to given value.

### HasWebsiteType

`func (o *UpdateProjectRequest) HasWebsiteType() bool`

HasWebsiteType returns a boolean if a field has been set.

### GetTopics

`func (o *UpdateProjectRequest) GetTopics() []int32`

GetTopics returns the Topics field if non-nil, zero value otherwise.

### GetTopicsOk

`func (o *UpdateProjectRequest) GetTopicsOk() (*[]int32, bool)`

GetTopicsOk returns a tuple with the Topics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopics

`func (o *UpdateProjectRequest) SetTopics(v []int32)`

SetTopics sets Topics field to given value.

### HasTopics

`func (o *UpdateProjectRequest) HasTopics() bool`

HasTopics returns a boolean if a field has been set.

### GetLanguage

`func (o *UpdateProjectRequest) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *UpdateProjectRequest) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *UpdateProjectRequest) SetLanguage(v string)`

SetLanguage sets Language field to given value.

### HasLanguage

`func (o *UpdateProjectRequest) HasLanguage() bool`

HasLanguage returns a boolean if a field has been set.

### GetCountry

`func (o *UpdateProjectRequest) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *UpdateProjectRequest) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *UpdateProjectRequest) SetCountry(v string)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *UpdateProjectRequest) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### SetCountryNil

`func (o *UpdateProjectRequest) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *UpdateProjectRequest) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil
### GetPromotedProducts

`func (o *UpdateProjectRequest) GetPromotedProducts() []string`

GetPromotedProducts returns the PromotedProducts field if non-nil, zero value otherwise.

### GetPromotedProductsOk

`func (o *UpdateProjectRequest) GetPromotedProductsOk() (*[]string, bool)`

GetPromotedProductsOk returns a tuple with the PromotedProducts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPromotedProducts

`func (o *UpdateProjectRequest) SetPromotedProducts(v []string)`

SetPromotedProducts sets PromotedProducts field to given value.

### HasPromotedProducts

`func (o *UpdateProjectRequest) HasPromotedProducts() bool`

HasPromotedProducts returns a boolean if a field has been set.

### GetUserKeywords

`func (o *UpdateProjectRequest) GetUserKeywords() []string`

GetUserKeywords returns the UserKeywords field if non-nil, zero value otherwise.

### GetUserKeywordsOk

`func (o *UpdateProjectRequest) GetUserKeywordsOk() (*[]string, bool)`

GetUserKeywordsOk returns a tuple with the UserKeywords field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserKeywords

`func (o *UpdateProjectRequest) SetUserKeywords(v []string)`

SetUserKeywords sets UserKeywords field to given value.

### HasUserKeywords

`func (o *UpdateProjectRequest) HasUserKeywords() bool`

HasUserKeywords returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


