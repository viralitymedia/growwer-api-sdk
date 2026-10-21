# SellerOrderDraftFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FileId** | **string** | A file you uploaded with POST /files and have not used yet. It must be an odt, doc, docx or txt file of up to 8 MB. It is used up once the draft is delivered. | 

## Methods

### NewSellerOrderDraftFile

`func NewSellerOrderDraftFile(fileId string, ) *SellerOrderDraftFile`

NewSellerOrderDraftFile instantiates a new SellerOrderDraftFile object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSellerOrderDraftFileWithDefaults

`func NewSellerOrderDraftFileWithDefaults() *SellerOrderDraftFile`

NewSellerOrderDraftFileWithDefaults instantiates a new SellerOrderDraftFile object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFileId

`func (o *SellerOrderDraftFile) GetFileId() string`

GetFileId returns the FileId field if non-nil, zero value otherwise.

### GetFileIdOk

`func (o *SellerOrderDraftFile) GetFileIdOk() (*string, bool)`

GetFileIdOk returns a tuple with the FileId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileId

`func (o *SellerOrderDraftFile) SetFileId(v string)`

SetFileId sets FileId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


