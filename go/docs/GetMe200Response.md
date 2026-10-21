# GetMe200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Email** | **string** |  | 
**FirstName** | **string** |  | 
**Language** | **string** | The language Growwer writes to you in. | 
**CreatedAt** | **time.Time** |  | 
**Buyer** | [**GetMe200ResponseBuyer**](GetMe200ResponseBuyer.md) |  | 
**Seller** | [**GetMe200ResponseSeller**](GetMe200ResponseSeller.md) |  | 
**Catalogue** | [**GetMe200ResponseCatalogue**](GetMe200ResponseCatalogue.md) |  | 
**ManagedService** | [**GetMe200ResponseManagedService**](GetMe200ResponseManagedService.md) |  | 

## Methods

### NewGetMe200Response

`func NewGetMe200Response(id string, email string, firstName string, language string, createdAt time.Time, buyer GetMe200ResponseBuyer, seller GetMe200ResponseSeller, catalogue GetMe200ResponseCatalogue, managedService GetMe200ResponseManagedService, ) *GetMe200Response`

NewGetMe200Response instantiates a new GetMe200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetMe200ResponseWithDefaults

`func NewGetMe200ResponseWithDefaults() *GetMe200Response`

NewGetMe200ResponseWithDefaults instantiates a new GetMe200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *GetMe200Response) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *GetMe200Response) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *GetMe200Response) SetId(v string)`

SetId sets Id field to given value.


### GetEmail

`func (o *GetMe200Response) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *GetMe200Response) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *GetMe200Response) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetFirstName

`func (o *GetMe200Response) GetFirstName() string`

GetFirstName returns the FirstName field if non-nil, zero value otherwise.

### GetFirstNameOk

`func (o *GetMe200Response) GetFirstNameOk() (*string, bool)`

GetFirstNameOk returns a tuple with the FirstName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstName

`func (o *GetMe200Response) SetFirstName(v string)`

SetFirstName sets FirstName field to given value.


### GetLanguage

`func (o *GetMe200Response) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *GetMe200Response) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *GetMe200Response) SetLanguage(v string)`

SetLanguage sets Language field to given value.


### GetCreatedAt

`func (o *GetMe200Response) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *GetMe200Response) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *GetMe200Response) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetBuyer

`func (o *GetMe200Response) GetBuyer() GetMe200ResponseBuyer`

GetBuyer returns the Buyer field if non-nil, zero value otherwise.

### GetBuyerOk

`func (o *GetMe200Response) GetBuyerOk() (*GetMe200ResponseBuyer, bool)`

GetBuyerOk returns a tuple with the Buyer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuyer

`func (o *GetMe200Response) SetBuyer(v GetMe200ResponseBuyer)`

SetBuyer sets Buyer field to given value.


### GetSeller

`func (o *GetMe200Response) GetSeller() GetMe200ResponseSeller`

GetSeller returns the Seller field if non-nil, zero value otherwise.

### GetSellerOk

`func (o *GetMe200Response) GetSellerOk() (*GetMe200ResponseSeller, bool)`

GetSellerOk returns a tuple with the Seller field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeller

`func (o *GetMe200Response) SetSeller(v GetMe200ResponseSeller)`

SetSeller sets Seller field to given value.


### GetCatalogue

`func (o *GetMe200Response) GetCatalogue() GetMe200ResponseCatalogue`

GetCatalogue returns the Catalogue field if non-nil, zero value otherwise.

### GetCatalogueOk

`func (o *GetMe200Response) GetCatalogueOk() (*GetMe200ResponseCatalogue, bool)`

GetCatalogueOk returns a tuple with the Catalogue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCatalogue

`func (o *GetMe200Response) SetCatalogue(v GetMe200ResponseCatalogue)`

SetCatalogue sets Catalogue field to given value.


### GetManagedService

`func (o *GetMe200Response) GetManagedService() GetMe200ResponseManagedService`

GetManagedService returns the ManagedService field if non-nil, zero value otherwise.

### GetManagedServiceOk

`func (o *GetMe200Response) GetManagedServiceOk() (*GetMe200ResponseManagedService, bool)`

GetManagedServiceOk returns a tuple with the ManagedService field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManagedService

`func (o *GetMe200Response) SetManagedService(v GetMe200ResponseManagedService)`

SetManagedService sets ManagedService field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


