# SellerMedia

One of your medias, as its seller sees it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**domain** | **str** |  | 
**url** | **str** | The media&#39;s root URL. | 
**typology** | **str** |  | 
**state** | **str** |  | 
**deactivation_strikes** | **int** | How many times the media was deactivated for not publishing. | 
**country** | **str** | A country code, as in GET /vocabulary, or null for none. | 
**language** | **str** | A language code, as in GET /vocabulary. | 
**topics** | **List[int]** | Topic ids, as in GET /vocabulary. | 
**banned_topics** | **List[int]** | The topic ids the media refuses, as in GET /vocabulary. | 
**provider_comments** | **str** | Your notes for buyers, or null for none. | 
**publication_rate** | **int** | The share of the media&#39;s orders that were published, in percent, or null without orders. | 
**average_days_to_publication** | **int** | The average days from order to publication, or null without published orders. | 
**num_published_orders** | **int** |  | 
**on_holiday** | **bool** |  | 
**flash_offer** | [**SellerMediaFlashOffer**](SellerMediaFlashOffer.md) |  | 
**post_offer** | [**SellerMediaPostOffer**](SellerMediaPostOffer.md) |  | 
**link_addition_offer** | [**SellerMediaLinkAdditionOffer**](SellerMediaLinkAdditionOffer.md) |  | 
**competitive_fees** | [**SellerFeesOrNull**](SellerFeesOrNull.md) | The post fees Growwer suggests to sell more, as the seller media pages do, or null when it suggests none: for each side, the highest fee POST /seller/medias/{id}/apply-competitive-fees would set on that side, else null. The apply lowers, per link type, a fee above the highest whole-euro fee that lists the media at least 1 EUR below its cheapest price on the marketplaces Growwer compares with to that fee, and lowers by 1 EUR one fee of a link type that then still does not list the media at least 1 EUR below that price. It never raises a fee. Where it lowers several link types, this is the highest per side across them, so a link type&#39;s own new fee can be lower: &#x60;competitiveFeesByLinkType&#x60; gives the fees the apply sets on each link type. | 
**competitive_fees_by_link_type** | [**List[SellerMediaCompetitiveFeesByLinkTypeInner]**](SellerMediaCompetitiveFeesByLinkTypeInner.md) | The fees POST /seller/medias/{id}/apply-competitive-fees would set, per link type: one entry per link type it lowers, in the order dofollow, nofollow, citation, or null when it suggests none (exactly when &#x60;competitiveFees&#x60; is null). Per side, the highest of these is &#x60;competitiveFees&#x60;. | 
**created_at** | **datetime** |  | 

## Example

```python
from growwer.models.seller_media import SellerMedia

# TODO update the JSON string below
json = "{}"
# create an instance of SellerMedia from a JSON string
seller_media_instance = SellerMedia.from_json(json)
# print the JSON string representation of the object
print(SellerMedia.to_json())

# convert the object into a dict
seller_media_dict = seller_media_instance.to_dict()
# create an instance of SellerMedia from a dict
seller_media_from_dict = SellerMedia.from_dict(seller_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


