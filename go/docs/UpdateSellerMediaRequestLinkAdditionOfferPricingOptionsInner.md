# UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LinkType** | **string** |  | 
**Fee** | [**Money**](Money.md) | Your base fee for adding a link of this type. | 

## Methods

### NewUpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner

`func NewUpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner(linkType string, fee Money, ) *UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner`

NewUpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner instantiates a new UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInnerWithDefaults

`func NewUpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInnerWithDefaults() *UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner`

NewUpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInnerWithDefaults instantiates a new UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLinkType

`func (o *UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner) GetLinkType() string`

GetLinkType returns the LinkType field if non-nil, zero value otherwise.

### GetLinkTypeOk

`func (o *UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner) GetLinkTypeOk() (*string, bool)`

GetLinkTypeOk returns a tuple with the LinkType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkType

`func (o *UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner) SetLinkType(v string)`

SetLinkType sets LinkType field to given value.


### GetFee

`func (o *UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner) GetFee() Money`

GetFee returns the Fee field if non-nil, zero value otherwise.

### GetFeeOk

`func (o *UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner) GetFeeOk() (*Money, bool)`

GetFeeOk returns a tuple with the Fee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFee

`func (o *UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner) SetFee(v Money)`

SetFee sets Fee field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


