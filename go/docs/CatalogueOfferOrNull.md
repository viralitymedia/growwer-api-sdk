# CatalogueOfferOrNull

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Price** | [**Money**](Money.md) | What you pay for the offer with its dearest link type, flash offer discount included. | 
**LinkType** | **NullableString** | The link type &#x60;price&#x60; is for. | 
**Prices** | [**map[string]Money**](Money.md) | What you pay for each link type the offer gives, by link type. | 
**PreviousPrice** | [**NullableMoneyOrNull**](MoneyOrNull.md) | The highest price the offer has had, when &#x60;price&#x60; is more than 5% below it; otherwise null. | 

## Methods

### NewCatalogueOfferOrNull

`func NewCatalogueOfferOrNull(price Money, linkType NullableString, prices map[string]Money, previousPrice NullableMoneyOrNull, ) *CatalogueOfferOrNull`

NewCatalogueOfferOrNull instantiates a new CatalogueOfferOrNull object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCatalogueOfferOrNullWithDefaults

`func NewCatalogueOfferOrNullWithDefaults() *CatalogueOfferOrNull`

NewCatalogueOfferOrNullWithDefaults instantiates a new CatalogueOfferOrNull object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrice

`func (o *CatalogueOfferOrNull) GetPrice() Money`

GetPrice returns the Price field if non-nil, zero value otherwise.

### GetPriceOk

`func (o *CatalogueOfferOrNull) GetPriceOk() (*Money, bool)`

GetPriceOk returns a tuple with the Price field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrice

`func (o *CatalogueOfferOrNull) SetPrice(v Money)`

SetPrice sets Price field to given value.


### GetLinkType

`func (o *CatalogueOfferOrNull) GetLinkType() string`

GetLinkType returns the LinkType field if non-nil, zero value otherwise.

### GetLinkTypeOk

`func (o *CatalogueOfferOrNull) GetLinkTypeOk() (*string, bool)`

GetLinkTypeOk returns a tuple with the LinkType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkType

`func (o *CatalogueOfferOrNull) SetLinkType(v string)`

SetLinkType sets LinkType field to given value.


### SetLinkTypeNil

`func (o *CatalogueOfferOrNull) SetLinkTypeNil(b bool)`

 SetLinkTypeNil sets the value for LinkType to be an explicit nil

### UnsetLinkType
`func (o *CatalogueOfferOrNull) UnsetLinkType()`

UnsetLinkType ensures that no value is present for LinkType, not even an explicit nil
### GetPrices

`func (o *CatalogueOfferOrNull) GetPrices() map[string]Money`

GetPrices returns the Prices field if non-nil, zero value otherwise.

### GetPricesOk

`func (o *CatalogueOfferOrNull) GetPricesOk() (*map[string]Money, bool)`

GetPricesOk returns a tuple with the Prices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrices

`func (o *CatalogueOfferOrNull) SetPrices(v map[string]Money)`

SetPrices sets Prices field to given value.


### GetPreviousPrice

`func (o *CatalogueOfferOrNull) GetPreviousPrice() MoneyOrNull`

GetPreviousPrice returns the PreviousPrice field if non-nil, zero value otherwise.

### GetPreviousPriceOk

`func (o *CatalogueOfferOrNull) GetPreviousPriceOk() (*MoneyOrNull, bool)`

GetPreviousPriceOk returns a tuple with the PreviousPrice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreviousPrice

`func (o *CatalogueOfferOrNull) SetPreviousPrice(v MoneyOrNull)`

SetPreviousPrice sets PreviousPrice field to given value.


### SetPreviousPriceNil

`func (o *CatalogueOfferOrNull) SetPreviousPriceNil(b bool)`

 SetPreviousPriceNil sets the value for PreviousPrice to be an explicit nil

### UnsetPreviousPrice
`func (o *CatalogueOfferOrNull) UnsetPreviousPrice()`

UnsetPreviousPrice ensures that no value is present for PreviousPrice, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


