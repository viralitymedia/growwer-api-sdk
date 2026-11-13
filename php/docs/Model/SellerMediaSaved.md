# SellerMediaSaved

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
**competitive_fees** | [**\Growwer\Api\Model\SellerFeesOrNull**](SellerFeesOrNull.md) | The post fees Growwer suggests to sell more, as the seller media pages do, or null when it suggests none: for each side, the highest fee POST /seller/medias/{id}/apply-competitive-fees would set on that side, else null. The apply lowers, per link type, a fee above the highest whole-euro fee that lists the media at least 1 EUR below its cheapest price on the marketplaces Growwer compares with to that fee, and lowers by 1 EUR one fee of a link type that then still does not list the media at least 1 EUR below that price. It never raises a fee. Where it lowers several link types, this is the highest per side across them, so a link type&#39;s own new fee can be lower: &#x60;competitiveFeesByLinkType&#x60; gives the fees the apply sets on each link type. |
**competitive_fees_by_link_type** | [**\Growwer\Api\Model\SellerMediaCompetitiveFeesByLinkTypeInner[]**](SellerMediaCompetitiveFeesByLinkTypeInner.md) | The fees POST /seller/medias/{id}/apply-competitive-fees would set, per link type: one entry per link type it lowers, in the order dofollow, nofollow, citation, or null when it suggests none (exactly when &#x60;competitiveFees&#x60; is null). Per side, the highest of these is &#x60;competitiveFees&#x60;. |
**created_at** | **\DateTime** |  |
**warnings** | [**\Growwer\Api\Model\SellerMediaSavedAllOfWarnings[]**](SellerMediaSavedAllOfWarnings.md) | What the save left to know, empty when nothing. &#x60;saved_above_competitors&#x60;: the fees were saved, but the media still lists above the marketplaces that list the same domain cheaper, and some fee would list it under them. &#x60;saved_not_recommended&#x60;: the same, for a save that raised a fee or added a side or link type: the media is not recommended in buyers&#39; projects while it lists above them, and stays in the catalogue. &#x60;details.competitiveFees&#x60; holds the highest fee of each side that lists it under them (&#x60;feeWhenSellerWritesPost&#x60;, &#x60;feeWhenSellerDoesNotWritePost&#x60;, null when none does or the media does not offer that side) and &#x60;details.competitors&#x60; the names of those marketplaces, never their prices. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
