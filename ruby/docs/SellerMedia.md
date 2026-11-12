# Growwer::SellerMedia

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **domain** | **String** |  |  |
| **url** | **String** | The media&#39;s root URL. |  |
| **typology** | **String** |  |  |
| **state** | **String** |  |  |
| **deactivation_strikes** | **Integer** | How many times the media was deactivated for not publishing. |  |
| **country** | **String** | A country code, as in GET /vocabulary, or null for none. |  |
| **language** | **String** | A language code, as in GET /vocabulary. |  |
| **topics** | **Array&lt;Integer&gt;** | Topic ids, as in GET /vocabulary. |  |
| **banned_topics** | **Array&lt;Integer&gt;** | The topic ids the media refuses, as in GET /vocabulary. |  |
| **provider_comments** | **String** | Your notes for buyers, or null for none. |  |
| **publication_rate** | **Integer** | The share of the media&#39;s orders that were published, in percent, or null without orders. |  |
| **average_days_to_publication** | **Integer** | The average days from order to publication, or null without published orders. |  |
| **num_published_orders** | **Integer** |  |  |
| **on_holiday** | **Boolean** |  |  |
| **flash_offer** | [**SellerMediaFlashOffer**](SellerMediaFlashOffer.md) |  |  |
| **post_offer** | [**SellerMediaPostOffer**](SellerMediaPostOffer.md) |  |  |
| **link_addition_offer** | [**SellerMediaLinkAdditionOffer**](SellerMediaLinkAdditionOffer.md) |  |  |
| **competitive_fees** | [**SellerFeesOrNull**](SellerFeesOrNull.md) | The post fees Growwer suggests to sell more, as the seller media pages do, or null when it suggests none: for each side, the highest fee POST /seller/medias/{id}/apply-competitive-fees would set on that side, else null. The apply lowers, per link type, a fee above the highest whole-euro fee that lists the media at least 1 EUR below its cheapest price on the marketplaces Growwer compares with to that fee, and lowers by 1 EUR one fee of a link type that then still does not list the media at least 1 EUR below that price. It never raises a fee. Where it lowers several link types, this is the highest per side across them, so a link type&#39;s own new fee can be lower: &#x60;competitiveFeesByLinkType&#x60; gives the fees the apply sets on each link type. |  |
| **competitive_fees_by_link_type** | [**Array&lt;SellerMediaCompetitiveFeesByLinkTypeInner&gt;**](SellerMediaCompetitiveFeesByLinkTypeInner.md) | The fees POST /seller/medias/{id}/apply-competitive-fees would set, per link type: one entry per link type it lowers, in the order dofollow, nofollow, citation, or null when it suggests none (exactly when &#x60;competitiveFees&#x60; is null). Per side, the highest of these is &#x60;competitiveFees&#x60;. |  |
| **created_at** | **Time** |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerMedia.new(
  id: null,
  domain: example.com,
  url: null,
  typology: null,
  state: null,
  deactivation_strikes: null,
  country: null,
  language: null,
  topics: null,
  banned_topics: null,
  provider_comments: null,
  publication_rate: null,
  average_days_to_publication: null,
  num_published_orders: null,
  on_holiday: null,
  flash_offer: null,
  post_offer: null,
  link_addition_offer: null,
  competitive_fees: null,
  competitive_fees_by_link_type: null,
  created_at: null
)
```

