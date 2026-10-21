# Growwer::SellerMedia

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **domain** | **String** |  |  |
| **url** | **String** | The media&#39;s root URL. |  |
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
| **competitive_fees** | [**SellerFeesOrNull**](SellerFeesOrNull.md) | The post fees Growwer suggests to sell more, as the seller media page does, or null when it suggests none. A side Growwer finds no competitive fee for is null: unlike the page, it never shows the fixed fee the page falls back to. POST /seller/medias/{id}/apply-competitive-fees sets them. |  |
| **created_at** | **Time** |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerMedia.new(
  id: null,
  domain: example.com,
  url: null,
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
  created_at: null
)
```

