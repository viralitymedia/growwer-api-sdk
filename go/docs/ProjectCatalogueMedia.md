# ProjectCatalogueMedia

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
**Project** | [**ProjectCatalogueMediaAllOfProject**](ProjectCatalogueMediaAllOfProject.md) |  | 

## Methods

### NewProjectCatalogueMedia

`func NewProjectCatalogueMedia(id string, domain string, type_ string, language string, country NullableString, topics []int32, metrics CatalogueMediaMetrics, positiveTrafficTrend bool, bestSeller bool, publicationRate NullableInt32, averageDaysToPublication NullableInt32, onHoliday bool, flashOffer NullableCatalogueMediaFlashOffer, postOffer CataloguePostOffer, linkAdditionOffer NullableCatalogueOfferOrNull, project ProjectCatalogueMediaAllOfProject, ) *ProjectCatalogueMedia`

NewProjectCatalogueMedia instantiates a new ProjectCatalogueMedia object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectCatalogueMediaWithDefaults

`func NewProjectCatalogueMediaWithDefaults() *ProjectCatalogueMedia`

NewProjectCatalogueMediaWithDefaults instantiates a new ProjectCatalogueMedia object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ProjectCatalogueMedia) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ProjectCatalogueMedia) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ProjectCatalogueMedia) SetId(v string)`

SetId sets Id field to given value.


### GetDomain

`func (o *ProjectCatalogueMedia) GetDomain() string`

GetDomain returns the Domain field if non-nil, zero value otherwise.

### GetDomainOk

`func (o *ProjectCatalogueMedia) GetDomainOk() (*string, bool)`

GetDomainOk returns a tuple with the Domain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomain

`func (o *ProjectCatalogueMedia) SetDomain(v string)`

SetDomain sets Domain field to given value.


### GetType

`func (o *ProjectCatalogueMedia) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ProjectCatalogueMedia) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ProjectCatalogueMedia) SetType(v string)`

SetType sets Type field to given value.


### GetLanguage

`func (o *ProjectCatalogueMedia) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *ProjectCatalogueMedia) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *ProjectCatalogueMedia) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetCountry

`func (o *ProjectCatalogueMedia) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *ProjectCatalogueMedia) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *ProjectCatalogueMedia) SetCountry(v string)`

SetCountry sets Country field to given value.


### SetCountryNil

`func (o *ProjectCatalogueMedia) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *ProjectCatalogueMedia) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil
### GetTopics

`func (o *ProjectCatalogueMedia) GetTopics() []int32`

GetTopics returns the Topics field if non-nil, zero value otherwise.

### GetTopicsOk

`func (o *ProjectCatalogueMedia) GetTopicsOk() (*[]int32, bool)`

GetTopicsOk returns a tuple with the Topics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopics

`func (o *ProjectCatalogueMedia) SetTopics(v []int32)`

SetTopics sets Topics field to given value.


### GetMetrics

`func (o *ProjectCatalogueMedia) GetMetrics() CatalogueMediaMetrics`

GetMetrics returns the Metrics field if non-nil, zero value otherwise.

### GetMetricsOk

`func (o *ProjectCatalogueMedia) GetMetricsOk() (*CatalogueMediaMetrics, bool)`

GetMetricsOk returns a tuple with the Metrics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetrics

`func (o *ProjectCatalogueMedia) SetMetrics(v CatalogueMediaMetrics)`

SetMetrics sets Metrics field to given value.


### GetPositiveTrafficTrend

`func (o *ProjectCatalogueMedia) GetPositiveTrafficTrend() bool`

GetPositiveTrafficTrend returns the PositiveTrafficTrend field if non-nil, zero value otherwise.

### GetPositiveTrafficTrendOk

`func (o *ProjectCatalogueMedia) GetPositiveTrafficTrendOk() (*bool, bool)`

GetPositiveTrafficTrendOk returns a tuple with the PositiveTrafficTrend field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositiveTrafficTrend

`func (o *ProjectCatalogueMedia) SetPositiveTrafficTrend(v bool)`

SetPositiveTrafficTrend sets PositiveTrafficTrend field to given value.


### GetBestSeller

`func (o *ProjectCatalogueMedia) GetBestSeller() bool`

GetBestSeller returns the BestSeller field if non-nil, zero value otherwise.

### GetBestSellerOk

`func (o *ProjectCatalogueMedia) GetBestSellerOk() (*bool, bool)`

GetBestSellerOk returns a tuple with the BestSeller field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBestSeller

`func (o *ProjectCatalogueMedia) SetBestSeller(v bool)`

SetBestSeller sets BestSeller field to given value.


### GetPublicationRate

`func (o *ProjectCatalogueMedia) GetPublicationRate() int32`

GetPublicationRate returns the PublicationRate field if non-nil, zero value otherwise.

### GetPublicationRateOk

`func (o *ProjectCatalogueMedia) GetPublicationRateOk() (*int32, bool)`

GetPublicationRateOk returns a tuple with the PublicationRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicationRate

`func (o *ProjectCatalogueMedia) SetPublicationRate(v int32)`

SetPublicationRate sets PublicationRate field to given value.


### SetPublicationRateNil

`func (o *ProjectCatalogueMedia) SetPublicationRateNil(b bool)`

 SetPublicationRateNil sets the value for PublicationRate to be an explicit nil

### UnsetPublicationRate
`func (o *ProjectCatalogueMedia) UnsetPublicationRate()`

UnsetPublicationRate ensures that no value is present for PublicationRate, not even an explicit nil
### GetAverageDaysToPublication

`func (o *ProjectCatalogueMedia) GetAverageDaysToPublication() int32`

GetAverageDaysToPublication returns the AverageDaysToPublication field if non-nil, zero value otherwise.

### GetAverageDaysToPublicationOk

`func (o *ProjectCatalogueMedia) GetAverageDaysToPublicationOk() (*int32, bool)`

GetAverageDaysToPublicationOk returns a tuple with the AverageDaysToPublication field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAverageDaysToPublication

`func (o *ProjectCatalogueMedia) SetAverageDaysToPublication(v int32)`

SetAverageDaysToPublication sets AverageDaysToPublication field to given value.


### SetAverageDaysToPublicationNil

`func (o *ProjectCatalogueMedia) SetAverageDaysToPublicationNil(b bool)`

 SetAverageDaysToPublicationNil sets the value for AverageDaysToPublication to be an explicit nil

### UnsetAverageDaysToPublication
`func (o *ProjectCatalogueMedia) UnsetAverageDaysToPublication()`

UnsetAverageDaysToPublication ensures that no value is present for AverageDaysToPublication, not even an explicit nil
### GetOnHoliday

`func (o *ProjectCatalogueMedia) GetOnHoliday() bool`

GetOnHoliday returns the OnHoliday field if non-nil, zero value otherwise.

### GetOnHolidayOk

`func (o *ProjectCatalogueMedia) GetOnHolidayOk() (*bool, bool)`

GetOnHolidayOk returns a tuple with the OnHoliday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnHoliday

`func (o *ProjectCatalogueMedia) SetOnHoliday(v bool)`

SetOnHoliday sets OnHoliday field to given value.


### GetFlashOffer

`func (o *ProjectCatalogueMedia) GetFlashOffer() CatalogueMediaFlashOffer`

GetFlashOffer returns the FlashOffer field if non-nil, zero value otherwise.

### GetFlashOfferOk

`func (o *ProjectCatalogueMedia) GetFlashOfferOk() (*CatalogueMediaFlashOffer, bool)`

GetFlashOfferOk returns a tuple with the FlashOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlashOffer

`func (o *ProjectCatalogueMedia) SetFlashOffer(v CatalogueMediaFlashOffer)`

SetFlashOffer sets FlashOffer field to given value.


### SetFlashOfferNil

`func (o *ProjectCatalogueMedia) SetFlashOfferNil(b bool)`

 SetFlashOfferNil sets the value for FlashOffer to be an explicit nil

### UnsetFlashOffer
`func (o *ProjectCatalogueMedia) UnsetFlashOffer()`

UnsetFlashOffer ensures that no value is present for FlashOffer, not even an explicit nil
### GetPostOffer

`func (o *ProjectCatalogueMedia) GetPostOffer() CataloguePostOffer`

GetPostOffer returns the PostOffer field if non-nil, zero value otherwise.

### GetPostOfferOk

`func (o *ProjectCatalogueMedia) GetPostOfferOk() (*CataloguePostOffer, bool)`

GetPostOfferOk returns a tuple with the PostOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostOffer

`func (o *ProjectCatalogueMedia) SetPostOffer(v CataloguePostOffer)`

SetPostOffer sets PostOffer field to given value.


### GetLinkAdditionOffer

`func (o *ProjectCatalogueMedia) GetLinkAdditionOffer() CatalogueOfferOrNull`

GetLinkAdditionOffer returns the LinkAdditionOffer field if non-nil, zero value otherwise.

### GetLinkAdditionOfferOk

`func (o *ProjectCatalogueMedia) GetLinkAdditionOfferOk() (*CatalogueOfferOrNull, bool)`

GetLinkAdditionOfferOk returns a tuple with the LinkAdditionOffer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkAdditionOffer

`func (o *ProjectCatalogueMedia) SetLinkAdditionOffer(v CatalogueOfferOrNull)`

SetLinkAdditionOffer sets LinkAdditionOffer field to given value.


### SetLinkAdditionOfferNil

`func (o *ProjectCatalogueMedia) SetLinkAdditionOfferNil(b bool)`

 SetLinkAdditionOfferNil sets the value for LinkAdditionOffer to be an explicit nil

### UnsetLinkAdditionOffer
`func (o *ProjectCatalogueMedia) UnsetLinkAdditionOffer()`

UnsetLinkAdditionOffer ensures that no value is present for LinkAdditionOffer, not even an explicit nil
### GetProject

`func (o *ProjectCatalogueMedia) GetProject() ProjectCatalogueMediaAllOfProject`

GetProject returns the Project field if non-nil, zero value otherwise.

### GetProjectOk

`func (o *ProjectCatalogueMedia) GetProjectOk() (*ProjectCatalogueMediaAllOfProject, bool)`

GetProjectOk returns a tuple with the Project field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProject

`func (o *ProjectCatalogueMedia) SetProject(v ProjectCatalogueMediaAllOfProject)`

SetProject sets Project field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


