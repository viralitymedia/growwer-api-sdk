# PutSellerHolidayRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OnHoliday** | **bool** |  | 
**EndDate** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewPutSellerHolidayRequest

`func NewPutSellerHolidayRequest(onHoliday bool, ) *PutSellerHolidayRequest`

NewPutSellerHolidayRequest instantiates a new PutSellerHolidayRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPutSellerHolidayRequestWithDefaults

`func NewPutSellerHolidayRequestWithDefaults() *PutSellerHolidayRequest`

NewPutSellerHolidayRequestWithDefaults instantiates a new PutSellerHolidayRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOnHoliday

`func (o *PutSellerHolidayRequest) GetOnHoliday() bool`

GetOnHoliday returns the OnHoliday field if non-nil, zero value otherwise.

### GetOnHolidayOk

`func (o *PutSellerHolidayRequest) GetOnHolidayOk() (*bool, bool)`

GetOnHolidayOk returns a tuple with the OnHoliday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnHoliday

`func (o *PutSellerHolidayRequest) SetOnHoliday(v bool)`

SetOnHoliday sets OnHoliday field to given value.


### GetEndDate

`func (o *PutSellerHolidayRequest) GetEndDate() string`

GetEndDate returns the EndDate field if non-nil, zero value otherwise.

### GetEndDateOk

`func (o *PutSellerHolidayRequest) GetEndDateOk() (*string, bool)`

GetEndDateOk returns a tuple with the EndDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndDate

`func (o *PutSellerHolidayRequest) SetEndDate(v string)`

SetEndDate sets EndDate field to given value.

### HasEndDate

`func (o *PutSellerHolidayRequest) HasEndDate() bool`

HasEndDate returns a boolean if a field has been set.

### SetEndDateNil

`func (o *PutSellerHolidayRequest) SetEndDateNil(b bool)`

 SetEndDateNil sets the value for EndDate to be an explicit nil

### UnsetEndDate
`func (o *PutSellerHolidayRequest) UnsetEndDate()`

UnsetEndDate ensures that no value is present for EndDate, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


