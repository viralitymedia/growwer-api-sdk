# SellerMediaSaved

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
**CompetitiveFees** | [**NullableSellerFeesOrNull**](SellerFeesOrNull.md) | The post fees Growwer suggests to sell more, as the seller media pages do, or null when it suggests none: for each side, the highest fee POST /seller/medias/{id}/apply-competitive-fees would set on that side, else null. The apply lowers, per link type, a fee above the highest whole-euro fee that lists the media at least 1 EUR below its cheapest price on the marketplaces Growwer compares with to that fee, and lowers by 1 EUR one fee of a link type that then still does not list the media at least 1 EUR below that price. It never raises a fee. Where it lowers several link types, this is the highest per side across them, so a link type&#39;s own new fee can be lower: &#x60;competitiveFeesByLinkType&#x60; gives the fees the apply sets on each link type. | 
**CompetitiveFeesByLinkType** | [**[]SellerMediaCompetitiveFeesByLinkTypeInner**](SellerMediaCompetitiveFeesByLinkTypeInner.md) | The fees POST /seller/medias/{id}/apply-competitive-fees would set, per link type: one entry per link type it lowers, in the order dofollow, nofollow, citation, or null when it suggests none (exactly when &#x60;competitiveFees&#x60; is null). Per side, the highest of these is &#x60;competitiveFees&#x60;. | 
**CreatedAt** | **time.Time** |  | 
**Warnings** | [**[]SellerMediaSavedAllOfWarnings**](SellerMediaSavedAllOfWarnings.md) | What the save left to know, empty when nothing. &#x60;saved_above_competitors&#x60;: the fees were saved, but the media still lists above the marketplaces that list the same domain cheaper, and some fee would list it under them. &#x60;saved_not_recommended&#x60;: the same, for a save that raised a fee or added a side or link type: the media is not recommended in buyers&#39; projects while it lists above them, and stays in the catalogue. &#x60;details.competitiveFees&#x60; holds the highest fee of each side that lists it under them (&#x60;feeWhenSellerWritesPost&#x60;, &#x60;feeWhenSellerDoesNotWritePost&#x60;, null when none does or the media does not offer that side) and &#x60;details.competitors&#x60; the names of those marketplaces, never their prices. | 

## Methods

### NewSellerMediaSaved

`func NewSellerMediaSaved(id string, domain string, url string, typology string, state string, deactivationStrikes int32, country NullableString, language string, topics []int32, bannedTopics []int32, providerComments NullableString, publicationRate NullableInt32, averageDaysToPublication NullableInt32, numPublishedOrders int32, onHoliday bool, flashOffer NullableSellerMediaFlashOffer, postOffer SellerMediaPostOffer, linkAdditionOffer NullableSellerMediaLinkAdditionOffer, competitiveFees NullableSellerFeesOrNull, competitiveFeesByLinkType []SellerMediaCompetitiveFeesByLinkTypeInner, createdAt time.Time, warnings []SellerMediaSavedAllOfWarnings, ) *SellerMediaSaved`

NewSellerMediaSaved instantiates a new SellerMediaSaved object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerMediaSavedWithDefaults

`func NewSellerMediaSavedWithDefaults() *SellerMediaSaved`

NewSellerMediaSavedWithDefaults instantiates a new SellerMediaSaved object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SellerMediaSaved) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SellerMediaSaved) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SellerMediaSaved) SetId(v string)`

SetId sets Id field to given value.


### GetDomain

`func (o *SellerMediaSaved) GetDomain() string`

GetDomain returns the Domain field if non-nil, zero value otherwise.

### GetDomainOk

`func (o *SellerMediaSaved) GetDomainOk() (*string, bool)`

GetDomainOk returns a tuple with the Domain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomain

`func (o *SellerMediaSaved) SetDomain(v string)`

SetDomain sets Domain field to given value.


### GetUrl

`func (o *SellerMediaSaved) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *SellerMediaSaved) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *SellerMediaSaved) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetTypology

`func (o *SellerMediaSaved) GetTypology() string`

GetTypology returns the Typology field if non-nil, zero value otherwise.

### GetTypologyOk

`func (o *SellerMediaSaved) GetTypologyOk() (*string, bool)`

GetTypologyOk returns a tuple with the Typology field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTypology

`func (o *SellerMediaSaved) SetTypology(v string)`

SetTypology sets Typology field to given value.


### GetState

`func (o *SellerMediaSaved) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *SellerMediaSaved) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *SellerMediaSaved) SetState(v string)`

SetState sets State field to given value.


### GetDeactivationStrikes

`func (o *SellerMediaSaved) GetDeactivationStrikes() int32`

GetDeactivationStrikes returns the DeactivationStrikes field if non-nil, zero value otherwise.

### GetDeactivationStrikesOk

`func (o *SellerMediaSaved) GetDeactivationStrikesOk() (*int32, bool)`

GetDeactivationStrikesOk returns a tuple with the DeactivationStrikes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeactivationStrikes

`func (o *SellerMediaSaved) SetDeactivationStrikes(v int32)`

SetDeactivationStrikes sets DeactivationStrikes field to given value.


### GetCountry

`func (o *SellerMediaSaved) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *SellerMediaSaved) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *SellerMediaSaved) SetCountry(v string)`

SetCountry sets Country field to given value.


### SetCountryNil

`func (o *SellerMediaSaved) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *SellerMediaSaved) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil
### GetLanguage

`func (o *SellerMediaSaved) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *SellerMediaSaved) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *SellerMediaSaved) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetTopics

`func (o *SellerMediaSaved) GetTopics() []int32`

GetTopics returns the Topics field if non-nil, zero value otherwise.

### GetTopicsOk

`func (o *SellerMediaSaved) GetTopicsOk() (*[]int32, bool)`

GetTopicsOk returns a tuple with the Topics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopics

`func (o *SellerMediaSaved) SetTopics(v []int32)`

SetTopics sets Topics field to given value.


### GetBannedTopics

`func (o *SellerMediaSaved) GetBannedTopics() []int32`

GetBannedTopics returns the BannedTopics field if non-nil, zero value otherwise.

### GetBannedTopicsOk

`func (o *SellerMediaSaved) GetBannedTopicsOk() (*[]int32, bool)`

GetBannedTopicsOk returns a tuple with the BannedTopics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBannedTopics

`func (o *SellerMediaSaved) SetBannedTopics(v []int32)`

SetBannedTopics sets BannedTopics field to given value.


### GetProviderComments

`func (o *SellerMediaSaved) GetProviderComments() string`

GetProviderComments returns the ProviderComments field if non-nil, zero value otherwise.

### GetProviderCommentsOk

`func (o *SellerMediaSaved) GetProviderCommentsOk() (*string, bool)`

GetProviderCommentsOk returns a tuple with the ProviderComments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderComments

`func (o *SellerMediaSaved) SetProviderComments(v string)`

SetProviderComments sets ProviderComments field to given value.


### SetProviderCommentsNil

`func (o *SellerMediaSaved) SetProviderCommentsNil(b bool)`

 SetProviderCommentsNil sets the value for ProviderComments to be an explicit nil

### UnsetProviderComments
`func (o *SellerMediaSaved) UnsetProviderComments()`

UnsetProviderComments ensures that no value is present for ProviderComments, not even an explicit nil
### GetPublicationRate

`func (o *SellerMediaSaved) GetPublicationRate() int32`

GetPublicationRate returns the PublicationRate field if non-nil, zero value otherwise.

### GetPublicationRateOk

`func (o *SellerMediaSaved) GetPublicationRateOk() (*int32, bool)`

GetPublicationRateOk returns a tuple with the PublicationRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicationRate

`func (o *SellerMediaSaved) SetPublicationRate(v int32)`

SetPublicationRate sets PublicationRate field to given value.


### SetPublicationRateNil

`func (o *SellerMediaSaved) SetPublicationRateNil(b bool)`

 SetPublicationRateNil sets the value for PublicationRate to be an explicit nil

### UnsetPublicationRate
`func (o *SellerMediaSaved) UnsetPublicationRate()`

UnsetPublicationRate ensures that no value is present for PublicationRate, not even an explicit nil
### GetAverageDaysToPublication

`func (o *SellerMediaSaved) GetAverageDaysToPublication() int32`

GetAverageDaysToPublication returns the AverageDaysToPublication field if non-nil, zero value otherwise.

### GetAverageDaysToPublicationOk

`func (o *SellerMediaSaved) GetAverageDaysToPublicationOk() (*int32, bool)`

GetAverageDaysToPublicationOk returns a tuple with the AverageDaysToPublication field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAverageDaysToPublication

`func (o *SellerMediaSaved) SetAverageDaysToPublication(v int32)`

SetAverageDaysToPublication sets AverageDaysToPublication field to given value.


### SetAverageDaysToPublicationNil

`func (o *SellerMediaSaved) SetAverageDaysToPublicationNil(b bool)`

 SetAverageDaysToPublicationNil sets the value for AverageDaysToPublication to be an explicit nil

### UnsetAverageDaysToPublication
`func (o *SellerMediaSaved) UnsetAverageDaysToPublication()`

UnsetAverageDaysToPublication ensures that no value is present for AverageDaysToPublication, not even an explicit nil
### GetNumPublishedOrders

`func (o *SellerMediaSaved) GetNumPublishedOrders() int32`

GetNumPublishedOrders returns the NumPublishedOrders field if non-nil, zero value otherwise.

### GetNumPublishedOrdersOk

`func (o *SellerMediaSaved) GetNumPublishedOrdersOk() (*int32, bool)`

GetNumPublishedOrdersOk returns a tuple with the NumPublishedOrders field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumPublishedOrders

`func (o *SellerMediaSaved) SetNumPublishedOrders(v int32)`

SetNumPublishedOrders sets NumPublishedOrders field to given value.


### GetOnHoliday

`func (o *SellerMediaSaved) GetOnHoliday() bool`

GetOnHoliday returns the OnHoliday field if non-nil, zero value otherwise.

### GetOnHolidayOk

`func (o *SellerMediaSaved) GetOnHolidayOk() (*bool, bool)`

GetOnHolidayOk returns a tuple with the OnHoliday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnHoliday

`func (o *SellerMediaSaved) SetOnHoliday(v bool)`

SetOnHoliday sets OnHoliday field to given value.


### GetFlashOffer

`func (o *SellerMediaSaved) GetFlashOffer() SellerMediaFlashOffer`

GetFlashOffer returns the FlashOffer field if non-nil, zero value otherwise.

### GetFlashOfferOk

`func (o *SellerMediaSaved) GetFlashOfferOk() (*SellerMediaFlashOffer, bool)`

GetFlashOfferOk returns a tuple with the FlashOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlashOffer

`func (o *SellerMediaSaved) SetFlashOffer(v SellerMediaFlashOffer)`

SetFlashOffer sets FlashOffer field to given value.


### SetFlashOfferNil

`func (o *SellerMediaSaved) SetFlashOfferNil(b bool)`

 SetFlashOfferNil sets the value for FlashOffer to be an explicit nil

### UnsetFlashOffer
`func (o *SellerMediaSaved) UnsetFlashOffer()`

UnsetFlashOffer ensures that no value is present for FlashOffer, not even an explicit nil
### GetPostOffer

`func (o *SellerMediaSaved) GetPostOffer() SellerMediaPostOffer`

GetPostOffer returns the PostOffer field if non-nil, zero value otherwise.

### GetPostOfferOk

`func (o *SellerMediaSaved) GetPostOfferOk() (*SellerMediaPostOffer, bool)`

GetPostOfferOk returns a tuple with the PostOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostOffer

`func (o *SellerMediaSaved) SetPostOffer(v SellerMediaPostOffer)`

SetPostOffer sets PostOffer field to given value.


### GetLinkAdditionOffer

`func (o *SellerMediaSaved) GetLinkAdditionOffer() SellerMediaLinkAdditionOffer`

GetLinkAdditionOffer returns the LinkAdditionOffer field if non-nil, zero value otherwise.

### GetLinkAdditionOfferOk

`func (o *SellerMediaSaved) GetLinkAdditionOfferOk() (*SellerMediaLinkAdditionOffer, bool)`

GetLinkAdditionOfferOk returns a tuple with the LinkAdditionOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkAdditionOffer

`func (o *SellerMediaSaved) SetLinkAdditionOffer(v SellerMediaLinkAdditionOffer)`

SetLinkAdditionOffer sets LinkAdditionOffer field to given value.


### SetLinkAdditionOfferNil

`func (o *SellerMediaSaved) SetLinkAdditionOfferNil(b bool)`

 SetLinkAdditionOfferNil sets the value for LinkAdditionOffer to be an explicit nil

### UnsetLinkAdditionOffer
`func (o *SellerMediaSaved) UnsetLinkAdditionOffer()`

UnsetLinkAdditionOffer ensures that no value is present for LinkAdditionOffer, not even an explicit nil
### GetCompetitiveFees

`func (o *SellerMediaSaved) GetCompetitiveFees() SellerFeesOrNull`

GetCompetitiveFees returns the CompetitiveFees field if non-nil, zero value otherwise.

### GetCompetitiveFeesOk

`func (o *SellerMediaSaved) GetCompetitiveFeesOk() (*SellerFeesOrNull, bool)`

GetCompetitiveFeesOk returns a tuple with the CompetitiveFees field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitiveFees

`func (o *SellerMediaSaved) SetCompetitiveFees(v SellerFeesOrNull)`

SetCompetitiveFees sets CompetitiveFees field to given value.


### SetCompetitiveFeesNil

`func (o *SellerMediaSaved) SetCompetitiveFeesNil(b bool)`

 SetCompetitiveFeesNil sets the value for CompetitiveFees to be an explicit nil

### UnsetCompetitiveFees
`func (o *SellerMediaSaved) UnsetCompetitiveFees()`

UnsetCompetitiveFees ensures that no value is present for CompetitiveFees, not even an explicit nil
### GetCompetitiveFeesByLinkType

`func (o *SellerMediaSaved) GetCompetitiveFeesByLinkType() []SellerMediaCompetitiveFeesByLinkTypeInner`

GetCompetitiveFeesByLinkType returns the CompetitiveFeesByLinkType field if non-nil, zero value otherwise.

### GetCompetitiveFeesByLinkTypeOk

`func (o *SellerMediaSaved) GetCompetitiveFeesByLinkTypeOk() (*[]SellerMediaCompetitiveFeesByLinkTypeInner, bool)`

GetCompetitiveFeesByLinkTypeOk returns a tuple with the CompetitiveFeesByLinkType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitiveFeesByLinkType

`func (o *SellerMediaSaved) SetCompetitiveFeesByLinkType(v []SellerMediaCompetitiveFeesByLinkTypeInner)`

SetCompetitiveFeesByLinkType sets CompetitiveFeesByLinkType field to given value.


### SetCompetitiveFeesByLinkTypeNil

`func (o *SellerMediaSaved) SetCompetitiveFeesByLinkTypeNil(b bool)`

 SetCompetitiveFeesByLinkTypeNil sets the value for CompetitiveFeesByLinkType to be an explicit nil

### UnsetCompetitiveFeesByLinkType
`func (o *SellerMediaSaved) UnsetCompetitiveFeesByLinkType()`

UnsetCompetitiveFeesByLinkType ensures that no value is present for CompetitiveFeesByLinkType, not even an explicit nil
### GetCreatedAt

`func (o *SellerMediaSaved) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SellerMediaSaved) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SellerMediaSaved) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetWarnings

`func (o *SellerMediaSaved) GetWarnings() []SellerMediaSavedAllOfWarnings`

GetWarnings returns the Warnings field if non-nil, zero value otherwise.

### GetWarningsOk

`func (o *SellerMediaSaved) GetWarningsOk() (*[]SellerMediaSavedAllOfWarnings, bool)`

GetWarningsOk returns a tuple with the Warnings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWarnings

`func (o *SellerMediaSaved) SetWarnings(v []SellerMediaSavedAllOfWarnings)`

SetWarnings sets Warnings field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


