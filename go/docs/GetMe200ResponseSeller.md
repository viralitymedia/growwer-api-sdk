# GetMe200ResponseSeller

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Balance** | [**Balance**](Balance.md) |  | 
**Restricted** | **bool** | Whether your seller account is restricted: it accepts no orders and its balance is held. Contact support for the reason. | 
**OnHoliday** | **bool** | Whether you are on holiday: your medias take no orders. Set it with PUT /seller/holiday. | 
**HolidayEndDate** | **NullableString** | The day your holiday ends, at 00:00 of that day in Growwer&#39;s server time, or null when you are not on holiday or end it yourself. | 

## Methods

### NewGetMe200ResponseSeller

`func NewGetMe200ResponseSeller(balance Balance, restricted bool, onHoliday bool, holidayEndDate NullableString, ) *GetMe200ResponseSeller`

NewGetMe200ResponseSeller instantiates a new GetMe200ResponseSeller object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetMe200ResponseSellerWithDefaults

`func NewGetMe200ResponseSellerWithDefaults() *GetMe200ResponseSeller`

NewGetMe200ResponseSellerWithDefaults instantiates a new GetMe200ResponseSeller object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBalance

`func (o *GetMe200ResponseSeller) GetBalance() Balance`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *GetMe200ResponseSeller) GetBalanceOk() (*Balance, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *GetMe200ResponseSeller) SetBalance(v Balance)`

SetBalance sets Balance field to given value.


### GetRestricted

`func (o *GetMe200ResponseSeller) GetRestricted() bool`

GetRestricted returns the Restricted field if non-nil, zero value otherwise.

### GetRestrictedOk

`func (o *GetMe200ResponseSeller) GetRestrictedOk() (*bool, bool)`

GetRestrictedOk returns a tuple with the Restricted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestricted

`func (o *GetMe200ResponseSeller) SetRestricted(v bool)`

SetRestricted sets Restricted field to given value.


### GetOnHoliday

`func (o *GetMe200ResponseSeller) GetOnHoliday() bool`

GetOnHoliday returns the OnHoliday field if non-nil, zero value otherwise.

### GetOnHolidayOk

`func (o *GetMe200ResponseSeller) GetOnHolidayOk() (*bool, bool)`

GetOnHolidayOk returns a tuple with the OnHoliday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnHoliday

`func (o *GetMe200ResponseSeller) SetOnHoliday(v bool)`

SetOnHoliday sets OnHoliday field to given value.


### GetHolidayEndDate

`func (o *GetMe200ResponseSeller) GetHolidayEndDate() string`

GetHolidayEndDate returns the HolidayEndDate field if non-nil, zero value otherwise.

### GetHolidayEndDateOk

`func (o *GetMe200ResponseSeller) GetHolidayEndDateOk() (*string, bool)`

GetHolidayEndDateOk returns a tuple with the HolidayEndDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHolidayEndDate

`func (o *GetMe200ResponseSeller) SetHolidayEndDate(v string)`

SetHolidayEndDate sets HolidayEndDate field to given value.


### SetHolidayEndDateNil

`func (o *GetMe200ResponseSeller) SetHolidayEndDateNil(b bool)`

 SetHolidayEndDateNil sets the value for HolidayEndDate to be an explicit nil

### UnsetHolidayEndDate
`func (o *GetMe200ResponseSeller) UnsetHolidayEndDate()`

UnsetHolidayEndDate ensures that no value is present for HolidayEndDate, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


