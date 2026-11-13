# Growwer.Api.Model.SellerMediaSaved
A media you sell on as a write answers it (PATCH /seller/medias/{id} and POST /seller/medias/{id}/apply-competitive-fees), with the warnings about the save. GET and the list answer SellerMedia, without them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Domain** | **string** |  | 
**Url** | **string** | The media&#39;s root URL. | 
**Typology** | **string** |  | 
**State** | **string** |  | 
**DeactivationStrikes** | **int** | How many times the media was deactivated for not publishing. | 
**Country** | **string** | A country code, as in GET /vocabulary, or null for none. | 
**Language** | **string** | A language code, as in GET /vocabulary. | 
**Topics** | **List&lt;int&gt;** | Topic ids, as in GET /vocabulary. | 
**BannedTopics** | **List&lt;int&gt;** | The topic ids the media refuses, as in GET /vocabulary. | 
**ProviderComments** | **string** | Your notes for buyers, or null for none. | 
**PublicationRate** | **int?** | The share of the media&#39;s orders that were published, in percent, or null without orders. | 
**AverageDaysToPublication** | **int?** | The average days from order to publication, or null without published orders. | 
**NumPublishedOrders** | **int** |  | 
**OnHoliday** | **bool** |  | 
**FlashOffer** | [**SellerMediaFlashOffer**](SellerMediaFlashOffer.md) |  | 
**PostOffer** | [**SellerMediaPostOffer**](SellerMediaPostOffer.md) |  | 
**LinkAdditionOffer** | [**SellerMediaLinkAdditionOffer**](SellerMediaLinkAdditionOffer.md) |  | 
**CompetitiveFees** | [**SellerFeesOrNull**](SellerFeesOrNull.md) | The post fees Growwer suggests to sell more, as the seller media pages do, or null when it suggests none: for each side, the highest fee POST /seller/medias/{id}/apply-competitive-fees would set on that side, else null. The apply lowers, per link type, a fee above the highest whole-euro fee that lists the media at least 1 EUR below its cheapest price on the marketplaces Growwer compares with to that fee, and lowers by 1 EUR one fee of a link type that then still does not list the media at least 1 EUR below that price. It never raises a fee. Where it lowers several link types, this is the highest per side across them, so a link type&#39;s own new fee can be lower: &#x60;competitiveFeesByLinkType&#x60; gives the fees the apply sets on each link type. | 
**CompetitiveFeesByLinkType** | [**List&lt;SellerMediaCompetitiveFeesByLinkTypeInner&gt;**](SellerMediaCompetitiveFeesByLinkTypeInner.md) | The fees POST /seller/medias/{id}/apply-competitive-fees would set, per link type: one entry per link type it lowers, in the order dofollow, nofollow, citation, or null when it suggests none (exactly when &#x60;competitiveFees&#x60; is null). Per side, the highest of these is &#x60;competitiveFees&#x60;. | 
**CreatedAt** | **DateTime** |  | 
**Warnings** | [**List&lt;SellerMediaSavedAllOfWarnings&gt;**](SellerMediaSavedAllOfWarnings.md) | What the save left to know, empty when nothing. &#x60;saved_above_competitors&#x60;: the fees were saved, but the media still lists above the marketplaces that list the same domain cheaper, and some fee would list it under them. &#x60;details.competitiveFees&#x60; holds the highest fee of each side that lists it under them (&#x60;feeWhenSellerWritesPost&#x60;, &#x60;feeWhenSellerDoesNotWritePost&#x60;, null when none does or the media does not offer that side) and &#x60;details.competitors&#x60; the names of those marketplaces, never their prices. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

