# UploadFile201Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | **string** | The name the file was uploaded with. | 
**Size** | **int32** | Bytes. | 
**ExpiresAt** | **time.Time** |  | 

## Methods

### NewUploadFile201Response

`func NewUploadFile201Response(id string, name string, size int32, expiresAt time.Time, ) *UploadFile201Response`

NewUploadFile201Response instantiates a new UploadFile201Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadFile201ResponseWithDefaults

`func NewUploadFile201ResponseWithDefaults() *UploadFile201Response`

NewUploadFile201ResponseWithDefaults instantiates a new UploadFile201Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UploadFile201Response) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UploadFile201Response) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UploadFile201Response) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *UploadFile201Response) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UploadFile201Response) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UploadFile201Response) SetName(v string)`

SetName sets Name field to given value.


### GetSize

`func (o *UploadFile201Response) GetSize() int32`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *UploadFile201Response) GetSizeOk() (*int32, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *UploadFile201Response) SetSize(v int32)`

SetSize sets Size field to given value.


### GetExpiresAt

`func (o *UploadFile201Response) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *UploadFile201Response) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *UploadFile201Response) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


