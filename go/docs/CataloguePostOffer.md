# CataloguePostOffer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Price** | [**Money**](Money.md) | What you pay for the offer with its dearest link type, flash offer discount included. | 
**LinkType** | **NullableString** | The link type &#x60;price&#x60; is for. | 
**Prices** | [**map[string]Money**](Money.md) | What you pay for each link type the offer gives, by link type. | 
**PreviousPrice** | [**NullableMoneyOrNull**](MoneyOrNull.md) | The highest price the offer has had, when &#x60;price&#x60; is more than 5% below it; otherwise null. | 
**AdvertisingLabel** | **bool** | Whether the media always labels posts as advertising. | 
**PromotedSocialNetworks** | **[]string** | Where the media promotes the post. | 
**Extras** | [**CataloguePostOfferAllOfExtras**](CataloguePostOfferAllOfExtras.md) |  | 

## Methods

### NewCataloguePostOffer

`func NewCataloguePostOffer(price Money, linkType NullableString, prices map[string]Money, previousPrice NullableMoneyOrNull, advertisingLabel bool, promotedSocialNetworks []string, extras CataloguePostOfferAllOfExtras, ) *CataloguePostOffer`

NewCataloguePostOffer instantiates a new CataloguePostOffer object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCataloguePostOfferWithDefaults

`func NewCataloguePostOfferWithDefaults() *CataloguePostOffer`

NewCataloguePostOfferWithDefaults instantiates a new CataloguePostOffer object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrice

`func (o *CataloguePostOffer) GetPrice() Money`

GetPrice returns the Price field if non-nil, zero value otherwise.

### GetPriceOk

`func (o *CataloguePostOffer) GetPriceOk() (*Money, bool)`

GetPriceOk returns a tuple with the Price field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrice

`func (o *CataloguePostOffer) SetPrice(v Money)`

SetPrice sets Price field to given value.


### GetLinkType

`func (o *CataloguePostOffer) GetLinkType() string`

GetLinkType returns the LinkType field if non-nil, zero value otherwise.

### GetLinkTypeOk

`func (o *CataloguePostOffer) GetLinkTypeOk() (*string, bool)`

GetLinkTypeOk returns a tuple with the LinkType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkType

`func (o *CataloguePostOffer) SetLinkType(v string)`

SetLinkType sets LinkType field to given value.


### SetLinkTypeNil

`func (o *CataloguePostOffer) SetLinkTypeNil(b bool)`

 SetLinkTypeNil sets the value for LinkType to be an explicit nil

### UnsetLinkType
`func (o *CataloguePostOffer) UnsetLinkType()`

UnsetLinkType ensures that no value is present for LinkType, not even an explicit nil
### GetPrices

`func (o *CataloguePostOffer) GetPrices() map[string]Money`

GetPrices returns the Prices field if non-nil, zero value otherwise.

### GetPricesOk

`func (o *CataloguePostOffer) GetPricesOk() (*map[string]Money, bool)`

GetPricesOk returns a tuple with the Prices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrices

`func (o *CataloguePostOffer) SetPrices(v map[string]Money)`

SetPrices sets Prices field to given value.


### GetPreviousPrice

`func (o *CataloguePostOffer) GetPreviousPrice() MoneyOrNull`

GetPreviousPrice returns the PreviousPrice field if non-nil, zero value otherwise.

### GetPreviousPriceOk

`func (o *CataloguePostOffer) GetPreviousPriceOk() (*MoneyOrNull, bool)`

GetPreviousPriceOk returns a tuple with the PreviousPrice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreviousPrice

`func (o *CataloguePostOffer) SetPreviousPrice(v MoneyOrNull)`

SetPreviousPrice sets PreviousPrice field to given value.


### SetPreviousPriceNil

`func (o *CataloguePostOffer) SetPreviousPriceNil(b bool)`

 SetPreviousPriceNil sets the value for PreviousPrice to be an explicit nil

### UnsetPreviousPrice
`func (o *CataloguePostOffer) UnsetPreviousPrice()`

UnsetPreviousPrice ensures that no value is present for PreviousPrice, not even an explicit nil
### GetAdvertisingLabel

`func (o *CataloguePostOffer) GetAdvertisingLabel() bool`

GetAdvertisingLabel returns the AdvertisingLabel field if non-nil, zero value otherwise.

### GetAdvertisingLabelOk

`func (o *CataloguePostOffer) GetAdvertisingLabelOk() (*bool, bool)`

GetAdvertisingLabelOk returns a tuple with the AdvertisingLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdvertisingLabel

`func (o *CataloguePostOffer) SetAdvertisingLabel(v bool)`

SetAdvertisingLabel sets AdvertisingLabel field to given value.


### GetPromotedSocialNetworks

`func (o *CataloguePostOffer) GetPromotedSocialNetworks() []string`

GetPromotedSocialNetworks returns the PromotedSocialNetworks field if non-nil, zero value otherwise.

### GetPromotedSocialNetworksOk

`func (o *CataloguePostOffer) GetPromotedSocialNetworksOk() (*[]string, bool)`

GetPromotedSocialNetworksOk returns a tuple with the PromotedSocialNetworks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPromotedSocialNetworks

`func (o *CataloguePostOffer) SetPromotedSocialNetworks(v []string)`

SetPromotedSocialNetworks sets PromotedSocialNetworks field to given value.


### GetExtras

`func (o *CataloguePostOffer) GetExtras() CataloguePostOfferAllOfExtras`

GetExtras returns the Extras field if non-nil, zero value otherwise.

### GetExtrasOk

`func (o *CataloguePostOffer) GetExtrasOk() (*CataloguePostOfferAllOfExtras, bool)`

GetExtrasOk returns a tuple with the Extras field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtras

`func (o *CataloguePostOffer) SetExtras(v CataloguePostOfferAllOfExtras)`

SetExtras sets Extras field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


