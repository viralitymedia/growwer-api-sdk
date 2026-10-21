# Project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | **NullableString** | Your name for the project, or null when it has none. | 
**RootUrl** | **string** | The website the project promotes. It cannot be changed once the project exists. | 
**WebsiteType** | **string** | What the website is: an online shop (&#x60;ecommerce&#x60;), a services business (&#x60;services&#x60;) or anything else (&#x60;other&#x60;). | 
**Topics** | **[]int32** | The website&#39;s topic, as a topic id from GET /vocabulary. Exactly one. | 
**Language** | **string** | The language of the campaign, as a language code from GET /vocabulary. | 
**Country** | **NullableString** | The country the campaign targets, as a country code from GET /vocabulary, or null for worldwide. | 
**PromotedProducts** | **[]string** | The products or services the campaign promotes, 5 to 10. | 
**UserKeywords** | **[]string** | Keywords you want the campaign to target, at most 100. | 
**State** | **string** | &#x60;finished&#x60; once Growwer has recommended media for the project, &#x60;analyzing&#x60; until then. Analysis can take hours, and it never finishes when no medium matches the project. Poll with backoff, and use &#x60;createdAt&#x60; to decide how long to keep polling.  | 
**CreatedAt** | **time.Time** |  | 

## Methods

### NewProject

`func NewProject(id string, name NullableString, rootUrl string, websiteType string, topics []int32, language string, country NullableString, promotedProducts []string, userKeywords []string, state string, createdAt time.Time, ) *Project`

NewProject instantiates a new Project object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectWithDefaults

`func NewProjectWithDefaults() *Project`

NewProjectWithDefaults instantiates a new Project object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Project) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Project) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Project) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *Project) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Project) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Project) SetName(v string)`

SetName sets Name field to given value.


### SetNameNil

`func (o *Project) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *Project) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetRootUrl

`func (o *Project) GetRootUrl() string`

GetRootUrl returns the RootUrl field if non-nil, zero value otherwise.

### GetRootUrlOk

`func (o *Project) GetRootUrlOk() (*string, bool)`

GetRootUrlOk returns a tuple with the RootUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRootUrl

`func (o *Project) SetRootUrl(v string)`

SetRootUrl sets RootUrl field to given value.


### GetWebsiteType

`func (o *Project) GetWebsiteType() string`

GetWebsiteType returns the WebsiteType field if non-nil, zero value otherwise.

### GetWebsiteTypeOk

`func (o *Project) GetWebsiteTypeOk() (*string, bool)`

GetWebsiteTypeOk returns a tuple with the WebsiteType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsiteType

`func (o *Project) SetWebsiteType(v string)`

SetWebsiteType sets WebsiteType field to given value.


### GetTopics

`func (o *Project) GetTopics() []int32`

GetTopics returns the Topics field if non-nil, zero value otherwise.

### GetTopicsOk

`func (o *Project) GetTopicsOk() (*[]int32, bool)`

GetTopicsOk returns a tuple with the Topics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopics

`func (o *Project) SetTopics(v []int32)`

SetTopics sets Topics field to given value.


### GetLanguage

`func (o *Project) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *Project) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *Project) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetCountry

`func (o *Project) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *Project) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *Project) SetCountry(v string)`

SetCountry sets Country field to given value.


### SetCountryNil

`func (o *Project) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *Project) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil
### GetPromotedProducts

`func (o *Project) GetPromotedProducts() []string`

GetPromotedProducts returns the PromotedProducts field if non-nil, zero value otherwise.

### GetPromotedProductsOk

`func (o *Project) GetPromotedProductsOk() (*[]string, bool)`

GetPromotedProductsOk returns a tuple with the PromotedProducts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPromotedProducts

`func (o *Project) SetPromotedProducts(v []string)`

SetPromotedProducts sets PromotedProducts field to given value.


### GetUserKeywords

`func (o *Project) GetUserKeywords() []string`

GetUserKeywords returns the UserKeywords field if non-nil, zero value otherwise.

### GetUserKeywordsOk

`func (o *Project) GetUserKeywordsOk() (*[]string, bool)`

GetUserKeywordsOk returns a tuple with the UserKeywords field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserKeywords

`func (o *Project) SetUserKeywords(v []string)`

SetUserKeywords sets UserKeywords field to given value.


### GetState

`func (o *Project) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *Project) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *Project) SetState(v string)`

SetState sets State field to given value.


### GetCreatedAt

`func (o *Project) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Project) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Project) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


