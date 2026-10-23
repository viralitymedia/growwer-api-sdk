# Growwer.Api.Model.SellerMediaPostOffer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PricingOptions** | [**List&lt;SellerMediaPostOfferPricingOptionsInner&gt;**](SellerMediaPostOfferPricingOptionsInner.md) | One entry per link type you offer. | 
**MaximumLinks** | **int** | How many links a sponsored post may hold, 1 to 4. | 
**AdvertisingLabellingPolicy** | **string** | Whether sponsored posts are labelled as advertising. | 
**PromotedSocialNetworks** | **List&lt;SellerMediaPostOffer.PromotedSocialNetworksEnum&gt;** | The social networks sponsored posts are promoted on. | 
**ExtraServices** | [**List&lt;UpdateSellerMediaRequestExtraServicesInner&gt;**](UpdateSellerMediaRequestExtraServicesInner.md) | Read here, but PATCH /seller/medias/{id} and POST /seller/medias take it at the top level of the body. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

