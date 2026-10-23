# SellerMedia

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Domain** | **string** |  | 
**Url** | **string** | The media&#39;s root URL. | 
**Typology** | **string** |  | 
**State** | **string** |  | 
**DeactivationStrikes** | **int32** | How many times the media was deactivated for not publishing. | 
**Country** | **NullableString** | A country code, as in GET /vocabulary, or null for none. | 
**Language** | **string** | A language code, as in GET /vocabulary. | 
**Topics** | **[]int32** | Topic ids, as in GET /vocabulary. | 
**BannedTopics** | **[]int32** | The topic ids the media refuses, as in GET /vocabulary. | 
**ProviderComments** | **NullableString** | Your notes for buyers, or null for none. | 
**PublicationRate** | **NullableInt32** | The share of the media&#39;s orders that were published, in percent, or null without orders. | 
**AverageDaysToPublication** | **NullableInt32** | The average days from order to publication, or null without published orders. | 
**NumPublishedOrders** | **int32** |  | 
**OnHoliday** | **bool** |  | 
**FlashOffer** | [**NullableSellerMediaFlashOffer**](SellerMediaFlashOffer.md) |  | 
**PostOffer** | [**SellerMediaPostOffer**](SellerMediaPostOffer.md) |  | 
**LinkAdditionOffer** | [**NullableSellerMediaLinkAdditionOffer**](SellerMediaLinkAdditionOffer.md) |  | 
**CompetitiveFees** | [**NullableSellerFeesOrNull**](SellerFeesOrNull.md) | The post fees Growwer suggests to sell more, as the seller media page does, or null when it suggests none. A side Growwer finds no competitive fee for is null: unlike the page, it never shows the fixed fee the page falls back to. POST /seller/medias/{id}/apply-competitive-fees sets them. | 
**CreatedAt** | **time.Time** |  | 

## Methods

### NewSellerMedia

`func NewSellerMedia(id string, domain string, url string, typology string, state string, deactivationStrikes int32, country NullableString, language string, topics []int32, bannedTopics []int32, providerComments NullableString, publicationRate NullableInt32, averageDaysToPublication NullableInt32, numPublishedOrders int32, onHoliday bool, flashOffer NullableSellerMediaFlashOffer, postOffer SellerMediaPostOffer, linkAdditionOffer NullableSellerMediaLinkAdditionOffer, competitiveFees NullableSellerFeesOrNull, createdAt time.Time, ) *SellerMedia`

NewSellerMedia instantiates a new SellerMedia object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerMediaWithDefaults

`func NewSellerMediaWithDefaults() *SellerMedia`

NewSellerMediaWithDefaults instantiates a new SellerMedia object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SellerMedia) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SellerMedia) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SellerMedia) SetId(v string)`

SetId sets Id field to given value.


### GetDomain

`func (o *SellerMedia) GetDomain() string`

GetDomain returns the Domain field if non-nil, zero value otherwise.

### GetDomainOk

`func (o *SellerMedia) GetDomainOk() (*string, bool)`

GetDomainOk returns a tuple with the Domain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomain

`func (o *SellerMedia) SetDomain(v string)`

SetDomain sets Domain field to given value.


### GetUrl

`func (o *SellerMedia) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *SellerMedia) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *SellerMedia) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetTypology

`func (o *SellerMedia) GetTypology() string`

GetTypology returns the Typology field if non-nil, zero value otherwise.

### GetTypologyOk

`func (o *SellerMedia) GetTypologyOk() (*string, bool)`

GetTypologyOk returns a tuple with the Typology field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTypology

`func (o *SellerMedia) SetTypology(v string)`

SetTypology sets Typology field to given value.


### GetState

`func (o *SellerMedia) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *SellerMedia) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *SellerMedia) SetState(v string)`

SetState sets State field to given value.


### GetDeactivationStrikes

`func (o *SellerMedia) GetDeactivationStrikes() int32`

GetDeactivationStrikes returns the DeactivationStrikes field if non-nil, zero value otherwise.

### GetDeactivationStrikesOk

`func (o *SellerMedia) GetDeactivationStrikesOk() (*int32, bool)`

GetDeactivationStrikesOk returns a tuple with the DeactivationStrikes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeactivationStrikes

`func (o *SellerMedia) SetDeactivationStrikes(v int32)`

SetDeactivationStrikes sets DeactivationStrikes field to given value.


### GetCountry

`func (o *SellerMedia) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *SellerMedia) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *SellerMedia) SetCountry(v string)`

SetCountry sets Country field to given value.


### SetCountryNil

`func (o *SellerMedia) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *SellerMedia) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil
### GetLanguage

`func (o *SellerMedia) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *SellerMedia) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *SellerMedia) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetTopics

`func (o *SellerMedia) GetTopics() []int32`

GetTopics returns the Topics field if non-nil, zero value otherwise.

### GetTopicsOk

`func (o *SellerMedia) GetTopicsOk() (*[]int32, bool)`

GetTopicsOk returns a tuple with the Topics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopics

`func (o *SellerMedia) SetTopics(v []int32)`

SetTopics sets Topics field to given value.


### GetBannedTopics

`func (o *SellerMedia) GetBannedTopics() []int32`

GetBannedTopics returns the BannedTopics field if non-nil, zero value otherwise.

### GetBannedTopicsOk

`func (o *SellerMedia) GetBannedTopicsOk() (*[]int32, bool)`

GetBannedTopicsOk returns a tuple with the BannedTopics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBannedTopics

`func (o *SellerMedia) SetBannedTopics(v []int32)`

SetBannedTopics sets BannedTopics field to given value.


### GetProviderComments

`func (o *SellerMedia) GetProviderComments() string`

GetProviderComments returns the ProviderComments field if non-nil, zero value otherwise.

### GetProviderCommentsOk

`func (o *SellerMedia) GetProviderCommentsOk() (*string, bool)`

GetProviderCommentsOk returns a tuple with the ProviderComments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderComments

`func (o *SellerMedia) SetProviderComments(v string)`

SetProviderComments sets ProviderComments field to given value.


### SetProviderCommentsNil

`func (o *SellerMedia) SetProviderCommentsNil(b bool)`

 SetProviderCommentsNil sets the value for ProviderComments to be an explicit nil

### UnsetProviderComments
`func (o *SellerMedia) UnsetProviderComments()`

UnsetProviderComments ensures that no value is present for ProviderComments, not even an explicit nil
### GetPublicationRate

`func (o *SellerMedia) GetPublicationRate() int32`

GetPublicationRate returns the PublicationRate field if non-nil, zero value otherwise.

### GetPublicationRateOk

`func (o *SellerMedia) GetPublicationRateOk() (*int32, bool)`

GetPublicationRateOk returns a tuple with the PublicationRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicationRate

`func (o *SellerMedia) SetPublicationRate(v int32)`

SetPublicationRate sets PublicationRate field to given value.


### SetPublicationRateNil

`func (o *SellerMedia) SetPublicationRateNil(b bool)`

 SetPublicationRateNil sets the value for PublicationRate to be an explicit nil

### UnsetPublicationRate
`func (o *SellerMedia) UnsetPublicationRate()`

UnsetPublicationRate ensures that no value is present for PublicationRate, not even an explicit nil
### GetAverageDaysToPublication

`func (o *SellerMedia) GetAverageDaysToPublication() int32`

GetAverageDaysToPublication returns the AverageDaysToPublication field if non-nil, zero value otherwise.

### GetAverageDaysToPublicationOk

`func (o *SellerMedia) GetAverageDaysToPublicationOk() (*int32, bool)`

GetAverageDaysToPublicationOk returns a tuple with the AverageDaysToPublication field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAverageDaysToPublication

`func (o *SellerMedia) SetAverageDaysToPublication(v int32)`

SetAverageDaysToPublication sets AverageDaysToPublication field to given value.


### SetAverageDaysToPublicationNil

`func (o *SellerMedia) SetAverageDaysToPublicationNil(b bool)`

 SetAverageDaysToPublicationNil sets the value for AverageDaysToPublication to be an explicit nil

### UnsetAverageDaysToPublication
`func (o *SellerMedia) UnsetAverageDaysToPublication()`

UnsetAverageDaysToPublication ensures that no value is present for AverageDaysToPublication, not even an explicit nil
### GetNumPublishedOrders

`func (o *SellerMedia) GetNumPublishedOrders() int32`

GetNumPublishedOrders returns the NumPublishedOrders field if non-nil, zero value otherwise.

### GetNumPublishedOrdersOk

`func (o *SellerMedia) GetNumPublishedOrdersOk() (*int32, bool)`

GetNumPublishedOrdersOk returns a tuple with the NumPublishedOrders field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumPublishedOrders

`func (o *SellerMedia) SetNumPublishedOrders(v int32)`

SetNumPublishedOrders sets NumPublishedOrders field to given value.


### GetOnHoliday

`func (o *SellerMedia) GetOnHoliday() bool`

GetOnHoliday returns the OnHoliday field if non-nil, zero value otherwise.

### GetOnHolidayOk

`func (o *SellerMedia) GetOnHolidayOk() (*bool, bool)`

GetOnHolidayOk returns a tuple with the OnHoliday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnHoliday

`func (o *SellerMedia) SetOnHoliday(v bool)`

SetOnHoliday sets OnHoliday field to given value.


### GetFlashOffer

`func (o *SellerMedia) GetFlashOffer() SellerMediaFlashOffer`

GetFlashOffer returns the FlashOffer field if non-nil, zero value otherwise.

### GetFlashOfferOk

`func (o *SellerMedia) GetFlashOfferOk() (*SellerMediaFlashOffer, bool)`

GetFlashOfferOk returns a tuple with the FlashOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlashOffer

`func (o *SellerMedia) SetFlashOffer(v SellerMediaFlashOffer)`

SetFlashOffer sets FlashOffer field to given value.


### SetFlashOfferNil

`func (o *SellerMedia) SetFlashOfferNil(b bool)`

 SetFlashOfferNil sets the value for FlashOffer to be an explicit nil

### UnsetFlashOffer
`func (o *SellerMedia) UnsetFlashOffer()`

UnsetFlashOffer ensures that no value is present for FlashOffer, not even an explicit nil
### GetPostOffer

`func (o *SellerMedia) GetPostOffer() SellerMediaPostOffer`

GetPostOffer returns the PostOffer field if non-nil, zero value otherwise.

### GetPostOfferOk

`func (o *SellerMedia) GetPostOfferOk() (*SellerMediaPostOffer, bool)`

GetPostOfferOk returns a tuple with the PostOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostOffer

`func (o *SellerMedia) SetPostOffer(v SellerMediaPostOffer)`

SetPostOffer sets PostOffer field to given value.


### GetLinkAdditionOffer

`func (o *SellerMedia) GetLinkAdditionOffer() SellerMediaLinkAdditionOffer`

GetLinkAdditionOffer returns the LinkAdditionOffer field if non-nil, zero value otherwise.

### GetLinkAdditionOfferOk

`func (o *SellerMedia) GetLinkAdditionOfferOk() (*SellerMediaLinkAdditionOffer, bool)`

GetLinkAdditionOfferOk returns a tuple with the LinkAdditionOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkAdditionOffer

`func (o *SellerMedia) SetLinkAdditionOffer(v SellerMediaLinkAdditionOffer)`

SetLinkAdditionOffer sets LinkAdditionOffer field to given value.


### SetLinkAdditionOfferNil

`func (o *SellerMedia) SetLinkAdditionOfferNil(b bool)`

 SetLinkAdditionOfferNil sets the value for LinkAdditionOffer to be an explicit nil

### UnsetLinkAdditionOffer
`func (o *SellerMedia) UnsetLinkAdditionOffer()`

UnsetLinkAdditionOffer ensures that no value is present for LinkAdditionOffer, not even an explicit nil
### GetCompetitiveFees

`func (o *SellerMedia) GetCompetitiveFees() SellerFeesOrNull`

GetCompetitiveFees returns the CompetitiveFees field if non-nil, zero value otherwise.

### GetCompetitiveFeesOk

`func (o *SellerMedia) GetCompetitiveFeesOk() (*SellerFeesOrNull, bool)`

GetCompetitiveFeesOk returns a tuple with the CompetitiveFees field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitiveFees

`func (o *SellerMedia) SetCompetitiveFees(v SellerFeesOrNull)`

SetCompetitiveFees sets CompetitiveFees field to given value.


### SetCompetitiveFeesNil

`func (o *SellerMedia) SetCompetitiveFeesNil(b bool)`

 SetCompetitiveFeesNil sets the value for CompetitiveFees to be an explicit nil

### UnsetCompetitiveFees
`func (o *SellerMedia) UnsetCompetitiveFees()`

UnsetCompetitiveFees ensures that no value is present for CompetitiveFees, not even an explicit nil
### GetCreatedAt

`func (o *SellerMedia) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SellerMedia) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SellerMedia) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


