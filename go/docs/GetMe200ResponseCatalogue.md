# GetMe200ResponseCatalogue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Eligible** | **bool** | Whether you have the full daily cap of the catalogue operations (tag Catalogue: searching a project&#39;s medias, flash offers and media details). It is open to accounts with recent completed orders, as buyer or as seller; until then the catalogue answers within a smaller daily trial quota, which rises to the full cap after a completed order. A media you have ordered is always readable with GET /medias/{id} and counts against neither. | 
**DailyCap** | **int32** | How many distinct medias the catalogue operations show you per UTC day: the full cap when &#x60;eligible&#x60; is true, the trial quota otherwise. 0 means the catalogue answers 403 &#x60;catalogue_requires_recent_order&#x60; until you have a recent completed order. | 
**RemainingToday** | **NullableInt32** | How many units of &#x60;dailyCap&#x60; still fit today (UTC): each new distinct media costs one, and a catalogue response that holds no new media, an empty one or a saved filter count included, costs one unless the same request was answered today and the media lists, topics and language of its project have not changed since. Medias you have already seen today, and requests already answered today, are free. Null when the count cannot be read right now; the catalogue operations then answer 503 until it can. | 

## Methods

### NewGetMe200ResponseCatalogue

`func NewGetMe200ResponseCatalogue(eligible bool, dailyCap int32, remainingToday NullableInt32, ) *GetMe200ResponseCatalogue`

NewGetMe200ResponseCatalogue instantiates a new GetMe200ResponseCatalogue object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetMe200ResponseCatalogueWithDefaults

`func NewGetMe200ResponseCatalogueWithDefaults() *GetMe200ResponseCatalogue`

NewGetMe200ResponseCatalogueWithDefaults instantiates a new GetMe200ResponseCatalogue object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEligible

`func (o *GetMe200ResponseCatalogue) GetEligible() bool`

GetEligible returns the Eligible field if non-nil, zero value otherwise.

### GetEligibleOk

`func (o *GetMe200ResponseCatalogue) GetEligibleOk() (*bool, bool)`

GetEligibleOk returns a tuple with the Eligible field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEligible

`func (o *GetMe200ResponseCatalogue) SetEligible(v bool)`

SetEligible sets Eligible field to given value.


### GetDailyCap

`func (o *GetMe200ResponseCatalogue) GetDailyCap() int32`

GetDailyCap returns the DailyCap field if non-nil, zero value otherwise.

### GetDailyCapOk

`func (o *GetMe200ResponseCatalogue) GetDailyCapOk() (*int32, bool)`

GetDailyCapOk returns a tuple with the DailyCap field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDailyCap

`func (o *GetMe200ResponseCatalogue) SetDailyCap(v int32)`

SetDailyCap sets DailyCap field to given value.


### GetRemainingToday

`func (o *GetMe200ResponseCatalogue) GetRemainingToday() int32`

GetRemainingToday returns the RemainingToday field if non-nil, zero value otherwise.

### GetRemainingTodayOk

`func (o *GetMe200ResponseCatalogue) GetRemainingTodayOk() (*int32, bool)`

GetRemainingTodayOk returns a tuple with the RemainingToday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemainingToday

`func (o *GetMe200ResponseCatalogue) SetRemainingToday(v int32)`

SetRemainingToday sets RemainingToday field to given value.


### SetRemainingTodayNil

`func (o *GetMe200ResponseCatalogue) SetRemainingTodayNil(b bool)`

 SetRemainingTodayNil sets the value for RemainingToday to be an explicit nil

### UnsetRemainingToday
`func (o *GetMe200ResponseCatalogue) UnsetRemainingToday()`

UnsetRemainingToday ensures that no value is present for RemainingToday, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


