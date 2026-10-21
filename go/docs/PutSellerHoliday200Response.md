# PutSellerHoliday200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OnHoliday** | **bool** |  | 
**EndDate** | **NullableString** | The day the holiday ends, at 00:00 of that day in Growwer&#39;s server time, or null for none. | 

## Methods

### NewPutSellerHoliday200Response

`func NewPutSellerHoliday200Response(onHoliday bool, endDate NullableString, ) *PutSellerHoliday200Response`

NewPutSellerHoliday200Response instantiates a new PutSellerHoliday200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPutSellerHoliday200ResponseWithDefaults

`func NewPutSellerHoliday200ResponseWithDefaults() *PutSellerHoliday200Response`

NewPutSellerHoliday200ResponseWithDefaults instantiates a new PutSellerHoliday200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOnHoliday

`func (o *PutSellerHoliday200Response) GetOnHoliday() bool`

GetOnHoliday returns the OnHoliday field if non-nil, zero value otherwise.

### GetOnHolidayOk

`func (o *PutSellerHoliday200Response) GetOnHolidayOk() (*bool, bool)`

GetOnHolidayOk returns a tuple with the OnHoliday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnHoliday

`func (o *PutSellerHoliday200Response) SetOnHoliday(v bool)`

SetOnHoliday sets OnHoliday field to given value.


### GetEndDate

`func (o *PutSellerHoliday200Response) GetEndDate() string`

GetEndDate returns the EndDate field if non-nil, zero value otherwise.

### GetEndDateOk

`func (o *PutSellerHoliday200Response) GetEndDateOk() (*string, bool)`

GetEndDateOk returns a tuple with the EndDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndDate

`func (o *PutSellerHoliday200Response) SetEndDate(v string)`

SetEndDate sets EndDate field to given value.


### SetEndDateNil

`func (o *PutSellerHoliday200Response) SetEndDateNil(b bool)`

 SetEndDateNil sets the value for EndDate to be an explicit nil

### UnsetEndDate
`func (o *PutSellerHoliday200Response) UnsetEndDate()`

UnsetEndDate ensures that no value is present for EndDate, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


