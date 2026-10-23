# CreateSellerMediaRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_url** | **string** |  |
**typology** | **string** |  |
**country** | **string** | A country code from GET /vocabulary. |
**language** | **string** | A language code from GET /vocabulary. |
**topics** | **int[]** | Topic ids from GET /vocabulary. |
**banned_topics** | **int[]** | The topic ids from GET /vocabulary the media refuses. | [optional]
**post_offer** | [**\Growwer\Api\Model\CreateSellerMediaRequestPostOffer**](CreateSellerMediaRequestPostOffer.md) |  |
**link_addition_offer** | [**\Growwer\Api\Model\UpdateSellerMediaRequestLinkAdditionOffer**](UpdateSellerMediaRequestLinkAdditionOffer.md) |  | [optional]
**extra_services** | [**\Growwer\Api\Model\UpdateSellerMediaRequestExtraServicesInner[]**](UpdateSellerMediaRequestExtraServicesInner.md) |  | [optional]
**accept_media_publishing_terms** | **bool** | Must be true: you accept the media publishing terms. |
**declare_media_ownership** | **bool** | Must be true: you own or manage this media. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
