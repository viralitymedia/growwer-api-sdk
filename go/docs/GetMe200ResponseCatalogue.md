# GetMe200ResponseCatalogue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Eligible** | **bool** | Whether the catalogue operations (tag Catalogue: searching a project&#39;s medias, flash offers and media details) are open to you. They are open to accounts with recent completed orders, as buyer or as seller; until then they answer 403 &#x60;catalogue_requires_recent_order&#x60;. A media you have ordered is always readable with GET /medias/{id}. | 

## Methods

### NewGetMe200ResponseCatalogue

`func NewGetMe200ResponseCatalogue(eligible bool, ) *GetMe200ResponseCatalogue`

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



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


