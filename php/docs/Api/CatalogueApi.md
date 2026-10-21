# Growwer\Api\CatalogueApi

Catalogue

All URIs are relative to https://tool.growwer.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**discardMedia()**](CatalogueApi.md#discardMedia) | **PUT** /api/v1/projects/{id}/discards/{mediaId} | Discard a media for a project |
| [**favouriteMedia()**](CatalogueApi.md#favouriteMedia) | **PUT** /api/v1/projects/{id}/favourites/{mediaId} | Add a media to the favourites of a project |
| [**getCatalogueMedia()**](CatalogueApi.md#getCatalogueMedia) | **GET** /api/v1/medias/{id} | Get a media |
| [**listFlashOffers()**](CatalogueApi.md#listFlashOffers) | **GET** /api/v1/flash-offers | List flash offers |
| [**requestMedias()**](CatalogueApi.md#requestMedias) | **POST** /api/v1/projects/{id}/media-requests | Request specific medias for a project |
| [**searchProjectMedias()**](CatalogueApi.md#searchProjectMedias) | **GET** /api/v1/projects/{id}/medias | Search the catalogue for a project |
| [**undiscardMedia()**](CatalogueApi.md#undiscardMedia) | **DELETE** /api/v1/projects/{id}/discards/{mediaId} | Restore a discarded media for a project |
| [**unfavouriteMedia()**](CatalogueApi.md#unfavouriteMedia) | **DELETE** /api/v1/projects/{id}/favourites/{mediaId} | Remove a media from the favourites of a project |


## `discardMedia()`

```php
discardMedia($id, $media_id, $idempotency_key)
```

Discard a media for a project

Discards a media for one of your projects, as the web does. Discarding it again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\CatalogueApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The project.
$media_id = 'media_id_example'; // string | The media.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

try {
    $apiInstance->discardMedia($id, $media_id, $idempotency_key);
} catch (Exception $e) {
    echo 'Exception when calling CatalogueApi->discardMedia: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The project. | |
| **media_id** | **string**| The media. | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |

### Return type

void (empty response body)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `favouriteMedia()`

```php
favouriteMedia($id, $media_id, $idempotency_key)
```

Add a media to the favourites of a project

Marks a media as a favourite of one of your projects, as the heart on the web does. Adding a favourite again changes nothing. The media must be one the catalogue shows for the project: another media, including one of your own as a seller, is answered as not found.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\CatalogueApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The project.
$media_id = 'media_id_example'; // string | The media.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

try {
    $apiInstance->favouriteMedia($id, $media_id, $idempotency_key);
} catch (Exception $e) {
    echo 'Exception when calling CatalogueApi->favouriteMedia: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The project. | |
| **media_id** | **string**| The media. | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |

### Return type

void (empty response body)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCatalogueMedia()`

```php
getCatalogueMedia($id): \Growwer\Api\Model\CatalogueMedia
```

Get a media

One media of the catalogue: an active, public media. A media you have ordered is always readable, even if it has since left the catalogue, and is open to every account. Otherwise the catalogue is open to accounts with recent completed orders (see `catalogue.eligible` on GET /me), and the media counts towards the distinct medias the account may see per day (UTC). For the media's state in one of your projects, search the project with GET /projects/{id}/medias.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\CatalogueApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The media.

try {
    $result = $apiInstance->getCatalogueMedia($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CatalogueApi->getCatalogueMedia: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The media. | |

### Return type

[**\Growwer\Api\Model\CatalogueMedia**](../Model/CatalogueMedia.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listFlashOffers()`

```php
listFlashOffers($project_id, $source, $sort, $domain, $website_type, $language, $country, $topics, $not_banned_topics, $min_traffic, $max_traffic, $traffic_trend_upward, $min_domain_rating, $max_domain_rating, $min_linked_to_referring_ratio, $max_linked_to_referring_ratio, $min_post_price, $max_post_price, $post_link_type, $promoted_social_network, $without_advertising_label, $homepage_listing, $has_link_addition, $min_link_addition_price, $max_link_addition_price, $link_addition_link_type, $recommended, $favourite, $requested, $bought, $discarded, $new, $ranks_goal_keyword, $ranks_ai_keyword, $limit, $offset): \Growwer\Api\Model\ListFlashOffers200Response
```

List flash offers

The medias on a flash offer, a time-limited discount, in the catalogue of one of your projects. It is GET /projects/{id}/medias with `flashOffer=true`, and takes the same parameters except `flashOffer` and `savedFilterId`. The catalogue access and the daily distinct-media limit of that operation apply.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\CatalogueApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$project_id = 'project_id_example'; // string | The project to search flash offers for.
$source = 'source_example'; // string | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state.
$sort = 'sort_example'; // string | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first.
$domain = 'domain_example'; // string | Medias whose domain contains this text, 1 to 255 characters.
$website_type = 'website_type_example'; // string | A comma-separated list of website types: `blog`, `press`.
$language = 'language_example'; // string | A comma-separated list of language codes, as in GET /vocabulary.
$country = 'country_example'; // string | A comma-separated list of country codes, as in GET /vocabulary.
$topics = 'topics_example'; // string | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them.
$not_banned_topics = True; // bool | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise.
$min_traffic = 56; // int | Minimum monthly organic traffic.
$max_traffic = 56; // int | Maximum monthly organic traffic.
$traffic_trend_upward = True; // bool | Medias whose traffic is growing. Only `true` applies it; omit it otherwise.
$min_domain_rating = 56; // int | Minimum domain rating, 0 to 100.
$max_domain_rating = 56; // int | Maximum domain rating, 0 to 100.
$min_linked_to_referring_ratio = 3.4; // float | Minimum ratio of linked domains to referring domains, such as 0.5.
$max_linked_to_referring_ratio = 3.4; // float | Maximum ratio of linked domains to referring domains, such as 1.5.
$min_post_price = 56; // int | Minimum post price, in cents.
$max_post_price = 56; // int | Maximum post price, in cents.
$post_link_type = 'post_link_type_example'; // string | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`.
$promoted_social_network = 'promoted_social_network_example'; // string | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`.
$without_advertising_label = True; // bool | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise.
$homepage_listing = True; // bool | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise.
$has_link_addition = True; // bool | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise.
$min_link_addition_price = 56; // int | Minimum link addition price, in cents.
$max_link_addition_price = 56; // int | Maximum link addition price, in cents.
$link_addition_link_type = 'link_addition_link_type_example'; // string | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`.
$recommended = True; // bool | `true`: only the medias Growwer recommends for the project; `false`: only the others.
$favourite = True; // bool | `true`: only your favourites for the project; `false`: leave them out.
$requested = True; // bool | `true`: only the medias you requested for the project; `false`: leave them out.
$bought = True; // bool | `true`: only medias you bought for the project; `false`: leave them out.
$discarded = True; // bool | `true`: only the medias you discarded for the project; `false`: leave them out.
$new = True; // bool | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise.
$ranks_goal_keyword = 'ranks_goal_keyword_example'; // string | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project.
$ranks_ai_keyword = 'ranks_ai_keyword_example'; // string | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`.
$limit = 20; // int | Medias per page, 1 to 100.
$offset = 0; // int | Medias to skip, at most 99900.

try {
    $result = $apiInstance->listFlashOffers($project_id, $source, $sort, $domain, $website_type, $language, $country, $topics, $not_banned_topics, $min_traffic, $max_traffic, $traffic_trend_upward, $min_domain_rating, $max_domain_rating, $min_linked_to_referring_ratio, $max_linked_to_referring_ratio, $min_post_price, $max_post_price, $post_link_type, $promoted_social_network, $without_advertising_label, $homepage_listing, $has_link_addition, $min_link_addition_price, $max_link_addition_price, $link_addition_link_type, $recommended, $favourite, $requested, $bought, $discarded, $new, $ranks_goal_keyword, $ranks_ai_keyword, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CatalogueApi->listFlashOffers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**| The project to search flash offers for. | |
| **source** | **string**| Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [optional] |
| **sort** | **string**| The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [optional] |
| **domain** | **string**| Medias whose domain contains this text, 1 to 255 characters. | [optional] |
| **website_type** | **string**| A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [optional] |
| **language** | **string**| A comma-separated list of language codes, as in GET /vocabulary. | [optional] |
| **country** | **string**| A comma-separated list of country codes, as in GET /vocabulary. | [optional] |
| **topics** | **string**| A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [optional] |
| **not_banned_topics** | **bool**| Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_traffic** | **int**| Minimum monthly organic traffic. | [optional] |
| **max_traffic** | **int**| Maximum monthly organic traffic. | [optional] |
| **traffic_trend_upward** | **bool**| Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_domain_rating** | **int**| Minimum domain rating, 0 to 100. | [optional] |
| **max_domain_rating** | **int**| Maximum domain rating, 0 to 100. | [optional] |
| **min_linked_to_referring_ratio** | **float**| Minimum ratio of linked domains to referring domains, such as 0.5. | [optional] |
| **max_linked_to_referring_ratio** | **float**| Maximum ratio of linked domains to referring domains, such as 1.5. | [optional] |
| **min_post_price** | **int**| Minimum post price, in cents. | [optional] |
| **max_post_price** | **int**| Maximum post price, in cents. | [optional] |
| **post_link_type** | **string**| A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **promoted_social_network** | **string**| A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [optional] |
| **without_advertising_label** | **bool**| Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **homepage_listing** | **bool**| Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **has_link_addition** | **bool**| Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_link_addition_price** | **int**| Minimum link addition price, in cents. | [optional] |
| **max_link_addition_price** | **int**| Maximum link addition price, in cents. | [optional] |
| **link_addition_link_type** | **string**| A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **recommended** | **bool**| &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [optional] |
| **favourite** | **bool**| &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **requested** | **bool**| &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **bought** | **bool**| &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **discarded** | **bool**| &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **new** | **bool**| Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **ranks_goal_keyword** | **string**| A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [optional] |
| **ranks_ai_keyword** | **string**| A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [optional] |
| **limit** | **int**| Medias per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Medias to skip, at most 99900. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListFlashOffers200Response**](../Model/ListFlashOffers200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `requestMedias()`

```php
requestMedias($id, $idempotency_key, $request_medias_request): \Growwer\Api\Model\RequestMedias201Response
```

Request specific medias for a project

Asks Growwer to find the medias of these domains for one of your projects, as the \"request specific domains\" form on the web does. Each entry may be a domain or a URL; it is read as its full domain, lowercased. Repeated domains are requested once, and a domain already requested changes nothing. Up to 200 distinct domains per call. They then appear in the project's catalogue with `project.requested` true (`requested=true` on GET /projects/{id}/medias) once Growwer lists them.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\CatalogueApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The project.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
$request_medias_request = new \Growwer\Api\Model\RequestMediasRequest(); // \Growwer\Api\Model\RequestMediasRequest

try {
    $result = $apiInstance->requestMedias($id, $idempotency_key, $request_medias_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CatalogueApi->requestMedias: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The project. | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **request_medias_request** | [**\Growwer\Api\Model\RequestMediasRequest**](../Model/RequestMediasRequest.md)|  | |

### Return type

[**\Growwer\Api\Model\RequestMedias201Response**](../Model/RequestMedias201Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchProjectMedias()`

```php
searchProjectMedias($id, $source, $sort, $saved_filter_id, $domain, $website_type, $language, $country, $topics, $not_banned_topics, $min_traffic, $max_traffic, $traffic_trend_upward, $min_domain_rating, $max_domain_rating, $min_linked_to_referring_ratio, $max_linked_to_referring_ratio, $min_post_price, $max_post_price, $post_link_type, $promoted_social_network, $without_advertising_label, $homepage_listing, $has_link_addition, $min_link_addition_price, $max_link_addition_price, $link_addition_link_type, $recommended, $favourite, $requested, $flash_offer, $bought, $discarded, $new, $ranks_goal_keyword, $ranks_ai_keyword, $limit, $offset): \Growwer\Api\Model\ListFlashOffers200Response
```

Search the catalogue for a project

The medias the catalogue offers for one of your projects, as the web lists them, with each media's state in the project. Filter with the parameters below, which all combine, or apply one of your saved filters with `savedFilterId` alone. The catalogue is open to accounts with recent completed orders (see `catalogue.eligible` on GET /me), and each account can see a limited number of distinct medias per day (UTC) across the catalogue operations; medias seen again the same day are free.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\CatalogueApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The project.
$source = 'source_example'; // string | Which of the project's medias to search: `all` (the default), `recommended` (those Growwer recommends for the project), or those you marked `favourite`, `discarded` or `requested`, or `bought` for the project. Do not combine it with the parameter of the same state.
$sort = 'sort_example'; // string | The order. Without it, the web's default order: medias on the project's topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. `-growwerRank`: best match first; `postPrice`, `linkAdditionPrice`: cheapest first; `matchedAt`, `-matchedAt`: when Growwer matched the media with the project; `-traffic`, `-domainRating`, `-referringDomains`: highest first; `linkedToReferringRatio`: lowest first.
$saved_filter_id = 'saved_filter_id_example'; // string | Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, `source` or `sort`. A filter saved on the web that uses a filter the API does not support is refused with 422 `saved_filter_unsupported`.
$domain = 'domain_example'; // string | Medias whose domain contains this text, 1 to 255 characters.
$website_type = 'website_type_example'; // string | A comma-separated list of website types: `blog`, `press`.
$language = 'language_example'; // string | A comma-separated list of language codes, as in GET /vocabulary.
$country = 'country_example'; // string | A comma-separated list of country codes, as in GET /vocabulary.
$topics = 'topics_example'; // string | A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them.
$not_banned_topics = True; // bool | Leave out medias that refuse the topic of the project. Only `true` applies it; omit it otherwise.
$min_traffic = 56; // int | Minimum monthly organic traffic.
$max_traffic = 56; // int | Maximum monthly organic traffic.
$traffic_trend_upward = True; // bool | Medias whose traffic is growing. Only `true` applies it; omit it otherwise.
$min_domain_rating = 56; // int | Minimum domain rating, 0 to 100.
$max_domain_rating = 56; // int | Maximum domain rating, 0 to 100.
$min_linked_to_referring_ratio = 3.4; // float | Minimum ratio of linked domains to referring domains, such as 0.5.
$max_linked_to_referring_ratio = 3.4; // float | Maximum ratio of linked domains to referring domains, such as 1.5.
$min_post_price = 56; // int | Minimum post price, in cents.
$max_post_price = 56; // int | Maximum post price, in cents.
$post_link_type = 'post_link_type_example'; // string | A comma-separated list of link types the post offer gives: `dofollow`, `nofollow`, `citation`.
$promoted_social_network = 'promoted_social_network_example'; // string | A comma-separated list of social networks the media promotes posts on: `twitter`, `instagram`, `facebook`, `pinterest`, `tumblr`, `newsletter`.
$without_advertising_label = True; // bool | Medias that never label posts as advertising. Only `true` applies it; omit it otherwise.
$homepage_listing = True; // bool | Medias that offer listing the post on their homepage. Only `true` applies it; omit it otherwise.
$has_link_addition = True; // bool | Medias that offer adding a link to an existing article. Only `true` applies it; omit it otherwise.
$min_link_addition_price = 56; // int | Minimum link addition price, in cents.
$max_link_addition_price = 56; // int | Maximum link addition price, in cents.
$link_addition_link_type = 'link_addition_link_type_example'; // string | A comma-separated list of link types the link addition offer gives: `dofollow`, `nofollow`, `citation`.
$recommended = True; // bool | `true`: only the medias Growwer recommends for the project; `false`: only the others.
$favourite = True; // bool | `true`: only your favourites for the project; `false`: leave them out.
$requested = True; // bool | `true`: only the medias you requested for the project; `false`: leave them out.
$flash_offer = True; // bool | `true`: only medias with a flash offer running; `false`: leave them out.
$bought = True; // bool | `true`: only medias you bought for the project; `false`: leave them out.
$discarded = True; // bool | `true`: only the medias you discarded for the project; `false`: leave them out.
$new = True; // bool | Medias Growwer matched with the project recently. Only `true` applies it; omit it otherwise.
$ranks_goal_keyword = 'ranks_goal_keyword_example'; // string | A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. `user`: your keywords; `publicGenerated`: keywords Growwer found for the project.
$ranks_ai_keyword = 'ranks_ai_keyword_example'; // string | A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. `googleAiOverview`, `chatgpt`, `googleAiMode`.
$limit = 20; // int | Medias per page, 1 to 100.
$offset = 0; // int | Medias to skip, at most 99900.

try {
    $result = $apiInstance->searchProjectMedias($id, $source, $sort, $saved_filter_id, $domain, $website_type, $language, $country, $topics, $not_banned_topics, $min_traffic, $max_traffic, $traffic_trend_upward, $min_domain_rating, $max_domain_rating, $min_linked_to_referring_ratio, $max_linked_to_referring_ratio, $min_post_price, $max_post_price, $post_link_type, $promoted_social_network, $without_advertising_label, $homepage_listing, $has_link_addition, $min_link_addition_price, $max_link_addition_price, $link_addition_link_type, $recommended, $favourite, $requested, $flash_offer, $bought, $discarded, $new, $ranks_goal_keyword, $ranks_ai_keyword, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CatalogueApi->searchProjectMedias: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The project. | |
| **source** | **string**| Which of the project&#39;s medias to search: &#x60;all&#x60; (the default), &#x60;recommended&#x60; (those Growwer recommends for the project), or those you marked &#x60;favourite&#x60;, &#x60;discarded&#x60; or &#x60;requested&#x60;, or &#x60;bought&#x60; for the project. Do not combine it with the parameter of the same state. | [optional] |
| **sort** | **string**| The order. Without it, the web&#39;s default order: medias on the project&#39;s topic and language first, then best sellers and medias with more published orders. Ties are always broken by media id, so pages never overlap. &#x60;-growwerRank&#x60;: best match first; &#x60;postPrice&#x60;, &#x60;linkAdditionPrice&#x60;: cheapest first; &#x60;matchedAt&#x60;, &#x60;-matchedAt&#x60;: when Growwer matched the media with the project; &#x60;-traffic&#x60;, &#x60;-domainRating&#x60;, &#x60;-referringDomains&#x60;: highest first; &#x60;linkedToReferringRatio&#x60;: lowest first. | [optional] |
| **saved_filter_id** | **string**| Apply one of your saved filters of this project, including one saved on the web, instead of the other parameters. Do not combine it with any filter, &#x60;source&#x60; or &#x60;sort&#x60;. A filter saved on the web that uses a filter the API does not support is refused with 422 &#x60;saved_filter_unsupported&#x60;. | [optional] |
| **domain** | **string**| Medias whose domain contains this text, 1 to 255 characters. | [optional] |
| **website_type** | **string**| A comma-separated list of website types: &#x60;blog&#x60;, &#x60;press&#x60;. | [optional] |
| **language** | **string**| A comma-separated list of language codes, as in GET /vocabulary. | [optional] |
| **country** | **string**| A comma-separated list of country codes, as in GET /vocabulary. | [optional] |
| **topics** | **string**| A comma-separated list of topic ids, as in GET /vocabulary: medias on any of them. | [optional] |
| **not_banned_topics** | **bool**| Leave out medias that refuse the topic of the project. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_traffic** | **int**| Minimum monthly organic traffic. | [optional] |
| **max_traffic** | **int**| Maximum monthly organic traffic. | [optional] |
| **traffic_trend_upward** | **bool**| Medias whose traffic is growing. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_domain_rating** | **int**| Minimum domain rating, 0 to 100. | [optional] |
| **max_domain_rating** | **int**| Maximum domain rating, 0 to 100. | [optional] |
| **min_linked_to_referring_ratio** | **float**| Minimum ratio of linked domains to referring domains, such as 0.5. | [optional] |
| **max_linked_to_referring_ratio** | **float**| Maximum ratio of linked domains to referring domains, such as 1.5. | [optional] |
| **min_post_price** | **int**| Minimum post price, in cents. | [optional] |
| **max_post_price** | **int**| Maximum post price, in cents. | [optional] |
| **post_link_type** | **string**| A comma-separated list of link types the post offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **promoted_social_network** | **string**| A comma-separated list of social networks the media promotes posts on: &#x60;twitter&#x60;, &#x60;instagram&#x60;, &#x60;facebook&#x60;, &#x60;pinterest&#x60;, &#x60;tumblr&#x60;, &#x60;newsletter&#x60;. | [optional] |
| **without_advertising_label** | **bool**| Medias that never label posts as advertising. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **homepage_listing** | **bool**| Medias that offer listing the post on their homepage. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **has_link_addition** | **bool**| Medias that offer adding a link to an existing article. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **min_link_addition_price** | **int**| Minimum link addition price, in cents. | [optional] |
| **max_link_addition_price** | **int**| Maximum link addition price, in cents. | [optional] |
| **link_addition_link_type** | **string**| A comma-separated list of link types the link addition offer gives: &#x60;dofollow&#x60;, &#x60;nofollow&#x60;, &#x60;citation&#x60;. | [optional] |
| **recommended** | **bool**| &#x60;true&#x60;: only the medias Growwer recommends for the project; &#x60;false&#x60;: only the others. | [optional] |
| **favourite** | **bool**| &#x60;true&#x60;: only your favourites for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **requested** | **bool**| &#x60;true&#x60;: only the medias you requested for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **flash_offer** | **bool**| &#x60;true&#x60;: only medias with a flash offer running; &#x60;false&#x60;: leave them out. | [optional] |
| **bought** | **bool**| &#x60;true&#x60;: only medias you bought for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **discarded** | **bool**| &#x60;true&#x60;: only the medias you discarded for the project; &#x60;false&#x60;: leave them out. | [optional] |
| **new** | **bool**| Medias Growwer matched with the project recently. Only &#x60;true&#x60; applies it; omit it otherwise. | [optional] |
| **ranks_goal_keyword** | **string**| A comma-separated list of keyword origins: medias that rank for a keyword of the project from any of them. &#x60;user&#x60;: your keywords; &#x60;publicGenerated&#x60;: keywords Growwer found for the project. | [optional] |
| **ranks_ai_keyword** | **string**| A comma-separated list of AI answer engines: medias cited for a keyword of the project by any of them. &#x60;googleAiOverview&#x60;, &#x60;chatgpt&#x60;, &#x60;googleAiMode&#x60;. | [optional] |
| **limit** | **int**| Medias per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int**| Medias to skip, at most 99900. | [optional] [default to 0] |

### Return type

[**\Growwer\Api\Model\ListFlashOffers200Response**](../Model/ListFlashOffers200Response.md)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `undiscardMedia()`

```php
undiscardMedia($id, $media_id, $idempotency_key)
```

Restore a discarded media for a project

Restores a media you discarded for one of your projects. Restoring one that is not discarded changes nothing. It works for any media, even one the catalogue no longer shows.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\CatalogueApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The project.
$media_id = 'media_id_example'; // string | The media.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

try {
    $apiInstance->undiscardMedia($id, $media_id, $idempotency_key);
} catch (Exception $e) {
    echo 'Exception when calling CatalogueApi->undiscardMedia: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The project. | |
| **media_id** | **string**| The media. | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |

### Return type

void (empty response body)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `unfavouriteMedia()`

```php
unfavouriteMedia($id, $media_id, $idempotency_key)
```

Remove a media from the favourites of a project

Removes a media from the favourites of one of your projects. Removing one that is not a favourite changes nothing. It works for any media, even one the catalogue no longer shows.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\CatalogueApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The project.
$media_id = 'media_id_example'; // string | The media.
$idempotency_key = 'idempotency_key_example'; // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

try {
    $apiInstance->unfavouriteMedia($id, $media_id, $idempotency_key);
} catch (Exception $e) {
    echo 'Exception when calling CatalogueApi->unfavouriteMedia: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The project. | |
| **media_id** | **string**| The media. | |
| **idempotency_key** | **string**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |

### Return type

void (empty response body)

### Authorization

[apiKey](../../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
