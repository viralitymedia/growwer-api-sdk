# Growwer.Api.Model.SellerMedia
One of your medias, as its seller sees it.

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
**CompetitiveFees** | [**SellerFeesOrNull**](SellerFeesOrNull.md) | The post fees Growwer suggests to sell more, as the seller media page does, or null when it suggests none. A side Growwer finds no competitive fee for is null: unlike the page, it never shows the fixed fee the page falls back to. POST /seller/medias/{id}/apply-competitive-fees sets them. | 
**CreatedAt** | **DateTime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

