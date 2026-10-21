

# SellerMedia

One of your medias, as its seller sees it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**domain** | **String** |  |  |
|**url** | **String** | The media&#39;s root URL. |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**deactivationStrikes** | **Integer** | How many times the media was deactivated for not publishing. |  |
|**country** | **String** | A country code, as in GET /vocabulary, or null for none. |  |
|**language** | **String** | A language code, as in GET /vocabulary. |  |
|**topics** | **List&lt;Integer&gt;** | Topic ids, as in GET /vocabulary. |  |
|**bannedTopics** | **List&lt;Integer&gt;** | The topic ids the media refuses, as in GET /vocabulary. |  |
|**providerComments** | **String** | Your notes for buyers, or null for none. |  |
|**publicationRate** | **Integer** | The share of the media&#39;s orders that were published, in percent, or null without orders. |  |
|**averageDaysToPublication** | **Integer** | The average days from order to publication, or null without published orders. |  |
|**numPublishedOrders** | **Integer** |  |  |
|**onHoliday** | **Boolean** |  |  |
|**flashOffer** | [**SellerMediaFlashOffer**](SellerMediaFlashOffer.md) |  |  |
|**postOffer** | [**SellerMediaPostOffer**](SellerMediaPostOffer.md) |  |  |
|**linkAdditionOffer** | [**SellerMediaLinkAdditionOffer**](SellerMediaLinkAdditionOffer.md) |  |  |
|**competitiveFees** | [**SellerFeesOrNull**](SellerFeesOrNull.md) | The post fees Growwer suggests to sell more, as the seller media page does, or null when it suggests none. A side Growwer finds no competitive fee for is null: unlike the page, it never shows the fixed fee the page falls back to. POST /seller/medias/{id}/apply-competitive-fees sets them. |  |
|**createdAt** | **OffsetDateTime** |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ANALYZING | &quot;analyzing&quot; |
| PENDING_REVIEW | &quot;pending_review&quot; |
| ACTIVE | &quot;active&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



