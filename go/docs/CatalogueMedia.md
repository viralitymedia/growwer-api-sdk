# CatalogueMedia

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Domain** | **string** |  | 
**Type** | **string** |  | 
**Language** | **string** | A language code, as in GET /vocabulary. | 
**Country** | **NullableString** | A country code, as in GET /vocabulary, or null for none. | 
**Topics** | **[]int32** | Topic ids, as in GET /vocabulary. | 
**Metrics** | [**CatalogueMediaMetrics**](CatalogueMediaMetrics.md) |  | 
**PositiveTrafficTrend** | **bool** |  | 
**BestSeller** | **bool** |  | 
**PublicationRate** | **NullableInt32** | The share of the media&#39;s orders that were published, in percent, or null without orders. | 
**AverageDaysToPublication** | **NullableInt32** | The average days from order to publication, or null without published orders. | 
**OnHoliday** | **bool** | Whether the media is on holiday and will take longer to publish. | 
**FlashOffer** | [**NullableCatalogueMediaFlashOffer**](CatalogueMediaFlashOffer.md) |  | 
**PostOffer** | [**CataloguePostOffer**](CataloguePostOffer.md) |  | 
**LinkAdditionOffer** | [**NullableCatalogueOfferOrNull**](CatalogueOfferOrNull.md) | Adding a link to an existing article, or null when the media does not offer it. | 

## Methods

### NewCatalogueMedia

`func NewCatalogueMedia(id string, domain string, type_ string, language string, country NullableString, topics []int32, metrics CatalogueMediaMetrics, positiveTrafficTrend bool, bestSeller bool, publicationRate NullableInt32, averageDaysToPublication NullableInt32, onHoliday bool, flashOffer NullableCatalogueMediaFlashOffer, postOffer CataloguePostOffer, linkAdditionOffer NullableCatalogueOfferOrNull, ) *CatalogueMedia`

NewCatalogueMedia instantiates a new CatalogueMedia object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCatalogueMediaWithDefaults

`func NewCatalogueMediaWithDefaults() *CatalogueMedia`

NewCatalogueMediaWithDefaults instantiates a new CatalogueMedia object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *CatalogueMedia) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CatalogueMedia) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CatalogueMedia) SetId(v string)`

SetId sets Id field to given value.


### GetDomain

`func (o *CatalogueMedia) GetDomain() string`

GetDomain returns the Domain field if non-nil, zero value otherwise.

### GetDomainOk

`func (o *CatalogueMedia) GetDomainOk() (*string, bool)`

GetDomainOk returns a tuple with the Domain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomain

`func (o *CatalogueMedia) SetDomain(v string)`

SetDomain sets Domain field to given value.


### GetType

`func (o *CatalogueMedia) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *CatalogueMedia) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *CatalogueMedia) SetType(v string)`

SetType sets Type field to given value.


### GetLanguage

`func (o *CatalogueMedia) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *CatalogueMedia) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *CatalogueMedia) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetCountry

`func (o *CatalogueMedia) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *CatalogueMedia) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *CatalogueMedia) SetCountry(v string)`

SetCountry sets Country field to given value.


### SetCountryNil

`func (o *CatalogueMedia) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *CatalogueMedia) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil
### GetTopics

`func (o *CatalogueMedia) GetTopics() []int32`

GetTopics returns the Topics field if non-nil, zero value otherwise.

### GetTopicsOk

`func (o *CatalogueMedia) GetTopicsOk() (*[]int32, bool)`

GetTopicsOk returns a tuple with the Topics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopics

`func (o *CatalogueMedia) SetTopics(v []int32)`

SetTopics sets Topics field to given value.


### GetMetrics

`func (o *CatalogueMedia) GetMetrics() CatalogueMediaMetrics`

GetMetrics returns the Metrics field if non-nil, zero value otherwise.

### GetMetricsOk

`func (o *CatalogueMedia) GetMetricsOk() (*CatalogueMediaMetrics, bool)`

GetMetricsOk returns a tuple with the Metrics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetrics

`func (o *CatalogueMedia) SetMetrics(v CatalogueMediaMetrics)`

SetMetrics sets Metrics field to given value.


### GetPositiveTrafficTrend

`func (o *CatalogueMedia) GetPositiveTrafficTrend() bool`

GetPositiveTrafficTrend returns the PositiveTrafficTrend field if non-nil, zero value otherwise.

### GetPositiveTrafficTrendOk

`func (o *CatalogueMedia) GetPositiveTrafficTrendOk() (*bool, bool)`

GetPositiveTrafficTrendOk returns a tuple with the PositiveTrafficTrend field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositiveTrafficTrend

`func (o *CatalogueMedia) SetPositiveTrafficTrend(v bool)`

SetPositiveTrafficTrend sets PositiveTrafficTrend field to given value.


### GetBestSeller

`func (o *CatalogueMedia) GetBestSeller() bool`

GetBestSeller returns the BestSeller field if non-nil, zero value otherwise.

### GetBestSellerOk

`func (o *CatalogueMedia) GetBestSellerOk() (*bool, bool)`

GetBestSellerOk returns a tuple with the BestSeller field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBestSeller

`func (o *CatalogueMedia) SetBestSeller(v bool)`

SetBestSeller sets BestSeller field to given value.


### GetPublicationRate

`func (o *CatalogueMedia) GetPublicationRate() int32`

GetPublicationRate returns the PublicationRate field if non-nil, zero value otherwise.

### GetPublicationRateOk

`func (o *CatalogueMedia) GetPublicationRateOk() (*int32, bool)`

GetPublicationRateOk returns a tuple with the PublicationRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicationRate

`func (o *CatalogueMedia) SetPublicationRate(v int32)`

SetPublicationRate sets PublicationRate field to given value.


### SetPublicationRateNil

`func (o *CatalogueMedia) SetPublicationRateNil(b bool)`

 SetPublicationRateNil sets the value for PublicationRate to be an explicit nil

### UnsetPublicationRate
`func (o *CatalogueMedia) UnsetPublicationRate()`

UnsetPublicationRate ensures that no value is present for PublicationRate, not even an explicit nil
### GetAverageDaysToPublication

`func (o *CatalogueMedia) GetAverageDaysToPublication() int32`

GetAverageDaysToPublication returns the AverageDaysToPublication field if non-nil, zero value otherwise.

### GetAverageDaysToPublicationOk

`func (o *CatalogueMedia) GetAverageDaysToPublicationOk() (*int32, bool)`

GetAverageDaysToPublicationOk returns a tuple with the AverageDaysToPublication field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAverageDaysToPublication

`func (o *CatalogueMedia) SetAverageDaysToPublication(v int32)`

SetAverageDaysToPublication sets AverageDaysToPublication field to given value.


### SetAverageDaysToPublicationNil

`func (o *CatalogueMedia) SetAverageDaysToPublicationNil(b bool)`

 SetAverageDaysToPublicationNil sets the value for AverageDaysToPublication to be an explicit nil

### UnsetAverageDaysToPublication
`func (o *CatalogueMedia) UnsetAverageDaysToPublication()`

UnsetAverageDaysToPublication ensures that no value is present for AverageDaysToPublication, not even an explicit nil
### GetOnHoliday

`func (o *CatalogueMedia) GetOnHoliday() bool`

GetOnHoliday returns the OnHoliday field if non-nil, zero value otherwise.

### GetOnHolidayOk

`func (o *CatalogueMedia) GetOnHolidayOk() (*bool, bool)`

GetOnHolidayOk returns a tuple with the OnHoliday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnHoliday

`func (o *CatalogueMedia) SetOnHoliday(v bool)`

SetOnHoliday sets OnHoliday field to given value.


### GetFlashOffer

`func (o *CatalogueMedia) GetFlashOffer() CatalogueMediaFlashOffer`

GetFlashOffer returns the FlashOffer field if non-nil, zero value otherwise.

### GetFlashOfferOk

`func (o *CatalogueMedia) GetFlashOfferOk() (*CatalogueMediaFlashOffer, bool)`

GetFlashOfferOk returns a tuple with the FlashOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlashOffer

`func (o *CatalogueMedia) SetFlashOffer(v CatalogueMediaFlashOffer)`

SetFlashOffer sets FlashOffer field to given value.


### SetFlashOfferNil

`func (o *CatalogueMedia) SetFlashOfferNil(b bool)`

 SetFlashOfferNil sets the value for FlashOffer to be an explicit nil

### UnsetFlashOffer
`func (o *CatalogueMedia) UnsetFlashOffer()`

UnsetFlashOffer ensures that no value is present for FlashOffer, not even an explicit nil
### GetPostOffer

`func (o *CatalogueMedia) GetPostOffer() CataloguePostOffer`

GetPostOffer returns the PostOffer field if non-nil, zero value otherwise.

### GetPostOfferOk

`func (o *CatalogueMedia) GetPostOfferOk() (*CataloguePostOffer, bool)`

GetPostOfferOk returns a tuple with the PostOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostOffer

`func (o *CatalogueMedia) SetPostOffer(v CataloguePostOffer)`

SetPostOffer sets PostOffer field to given value.


### GetLinkAdditionOffer

`func (o *CatalogueMedia) GetLinkAdditionOffer() CatalogueOfferOrNull`

GetLinkAdditionOffer returns the LinkAdditionOffer field if non-nil, zero value otherwise.

### GetLinkAdditionOfferOk

`func (o *CatalogueMedia) GetLinkAdditionOfferOk() (*CatalogueOfferOrNull, bool)`

GetLinkAdditionOfferOk returns a tuple with the LinkAdditionOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkAdditionOffer

`func (o *CatalogueMedia) SetLinkAdditionOffer(v CatalogueOfferOrNull)`

SetLinkAdditionOffer sets LinkAdditionOffer field to given value.


### SetLinkAdditionOfferNil

`func (o *CatalogueMedia) SetLinkAdditionOfferNil(b bool)`

 SetLinkAdditionOfferNil sets the value for LinkAdditionOffer to be an explicit nil

### UnsetLinkAdditionOffer
`func (o *CatalogueMedia) UnsetLinkAdditionOffer()`

UnsetLinkAdditionOffer ensures that no value is present for LinkAdditionOffer, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


