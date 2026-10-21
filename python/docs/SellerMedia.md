# SellerMedia

One of your medias, as its seller sees it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**domain** | **str** |  | 
**url** | **str** | The media&#39;s root URL. | 
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
**competitive_fees** | [**SellerFeesOrNull**](SellerFeesOrNull.md) | The post fees Growwer suggests to sell more, as the seller media page does, or null when it suggests none. A side Growwer finds no competitive fee for is null: unlike the page, it never shows the fixed fee the page falls back to. POST /seller/medias/{id}/apply-competitive-fees sets them. | 
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


