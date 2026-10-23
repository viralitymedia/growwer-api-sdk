# SellerMediaPostOffer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_options** | [**\Growwer\Api\Model\SellerMediaPostOfferPricingOptionsInner[]**](SellerMediaPostOfferPricingOptionsInner.md) | One entry per link type you offer. |
**maximum_links** | **int** | How many links a sponsored post may hold, 1 to 4. |
**advertising_labelling_policy** | **string** | Whether sponsored posts are labelled as advertising. |
**promoted_social_networks** | **string[]** | The social networks sponsored posts are promoted on. |
**extra_services** | [**\Growwer\Api\Model\UpdateSellerMediaRequestExtraServicesInner[]**](UpdateSellerMediaRequestExtraServicesInner.md) | Read here, but PATCH /seller/medias/{id} and POST /seller/medias take it at the top level of the body. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
