# SellerMedia

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**domain** | **string** |  |
**url** | **string** | The media&#39;s root URL. |
**typology** | **string** |  |
**state** | **string** |  |
**deactivation_strikes** | **int** | How many times the media was deactivated for not publishing. |
**country** | **string** | A country code, as in GET /vocabulary, or null for none. |
**language** | **string** | A language code, as in GET /vocabulary. |
**topics** | **int[]** | Topic ids, as in GET /vocabulary. |
**banned_topics** | **int[]** | The topic ids the media refuses, as in GET /vocabulary. |
**provider_comments** | **string** | Your notes for buyers, or null for none. |
**publication_rate** | **int** | The share of the media&#39;s orders that were published, in percent, or null without orders. |
**average_days_to_publication** | **int** | The average days from order to publication, or null without published orders. |
**num_published_orders** | **int** |  |
**on_holiday** | **bool** |  |
**flash_offer** | [**\Growwer\Api\Model\SellerMediaFlashOffer**](SellerMediaFlashOffer.md) |  |
**post_offer** | [**\Growwer\Api\Model\SellerMediaPostOffer**](SellerMediaPostOffer.md) |  |
**link_addition_offer** | [**\Growwer\Api\Model\SellerMediaLinkAdditionOffer**](SellerMediaLinkAdditionOffer.md) |  |
**competitive_fees** | [**\Growwer\Api\Model\SellerFeesOrNull**](SellerFeesOrNull.md) | The post fees Growwer suggests to sell more, as the seller media page does, or null when it suggests none. A side Growwer finds no competitive fee for is null: unlike the page, it never shows the fixed fee the page falls back to. POST /seller/medias/{id}/apply-competitive-fees sets them. |
**created_at** | **\DateTime** |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
