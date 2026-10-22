# Growwer::ManagedServicesApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**estimate_managed_service_proposals**](ManagedServicesApi.md#estimate_managed_service_proposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/estimate | Estimate accepting proposals |
| [**get_managed_service_campaign**](ManagedServicesApi.md#get_managed_service_campaign) | **GET** /api/v1/managed-service/campaigns/{id} | Get a managed service campaign |
| [**get_managed_service_proposals_summary**](ManagedServicesApi.md#get_managed_service_proposals_summary) | **GET** /api/v1/managed-service/campaigns/{id}/proposals-summary | Download the summary of a campaign&#39;s proposals |
| [**list_managed_service_campaigns**](ManagedServicesApi.md#list_managed_service_campaigns) | **GET** /api/v1/managed-service/campaigns | List your managed service campaigns |
| [**list_managed_service_proposals**](ManagedServicesApi.md#list_managed_service_proposals) | **GET** /api/v1/managed-service/campaigns/{id}/proposals | List the proposals of a campaign |
| [**request_managed_service_campaign**](ManagedServicesApi.md#request_managed_service_campaign) | **POST** /api/v1/managed-service/campaign-requests | Request a new campaign |
| [**request_managed_service_info**](ManagedServicesApi.md#request_managed_service_info) | **POST** /api/v1/managed-service/info-requests | Ask about the managed service |
| [**review_managed_service_proposals**](ManagedServicesApi.md#review_managed_service_proposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/review | Accept or reject proposals |


## estimate_managed_service_proposals

> <ManagedServiceProposalsEstimate> estimate_managed_service_proposals(id, opts)

Estimate accepting proposals

Totals the campaign's accepted proposals that still await their order and the `proposed` ones you name in `accept`, and compares the total with your wallet's available balance. Each proposal counts at its `currentPrice`, or at its `proposedPrice` when the media no longer offers the service. Nothing is accepted, charged or reserved, so a read-only key may call it and it takes no Idempotency-Key.  The estimate is advisory: accepting a proposal charges nothing. The team charges your wallet when it places the order for an accepted proposal, and the same balance pays for the orders you place yourself.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ManagedServicesApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
opts = {
  managed_service_proposals_estimate_request: Growwer::ManagedServiceProposalsEstimateRequest.new # ManagedServiceProposalsEstimateRequest | 
}

begin
  # Estimate accepting proposals
  result = api_instance.estimate_managed_service_proposals(id, opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->estimate_managed_service_proposals: #{e}"
end
```

#### Using the estimate_managed_service_proposals_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ManagedServiceProposalsEstimate>, Integer, Hash)> estimate_managed_service_proposals_with_http_info(id, opts)

```ruby
begin
  # Estimate accepting proposals
  data, status_code, headers = api_instance.estimate_managed_service_proposals_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ManagedServiceProposalsEstimate>
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->estimate_managed_service_proposals_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **managed_service_proposals_estimate_request** | [**ManagedServiceProposalsEstimateRequest**](ManagedServiceProposalsEstimateRequest.md) |  | [optional] |

### Return type

[**ManagedServiceProposalsEstimate**](ManagedServiceProposalsEstimate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_managed_service_campaign

> <ManagedServiceCampaign> get_managed_service_campaign(id)

Get a managed service campaign

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ManagedServicesApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Get a managed service campaign
  result = api_instance.get_managed_service_campaign(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->get_managed_service_campaign: #{e}"
end
```

#### Using the get_managed_service_campaign_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ManagedServiceCampaign>, Integer, Hash)> get_managed_service_campaign_with_http_info(id)

```ruby
begin
  # Get a managed service campaign
  data, status_code, headers = api_instance.get_managed_service_campaign_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ManagedServiceCampaign>
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->get_managed_service_campaign_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**ManagedServiceCampaign**](ManagedServiceCampaign.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_managed_service_proposals_summary

> File get_managed_service_proposals_summary(id, opts)

Download the summary of a campaign's proposals

The PDF the campaign page offers: the proposals awaiting your review, accepted or being published, newest first, in your language. With `extended=true` it also shows each proposal's price, the price it was proposed at (`proposedPrice`).

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ManagedServicesApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
opts = {
  extended: 'true' # String | Whether to show the prices.
}

begin
  # Download the summary of a campaign's proposals
  result = api_instance.get_managed_service_proposals_summary(id, opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->get_managed_service_proposals_summary: #{e}"
end
```

#### Using the get_managed_service_proposals_summary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(File, Integer, Hash)> get_managed_service_proposals_summary_with_http_info(id, opts)

```ruby
begin
  # Download the summary of a campaign's proposals
  data, status_code, headers = api_instance.get_managed_service_proposals_summary_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => File
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->get_managed_service_proposals_summary_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **extended** | **String** | Whether to show the prices. | [optional][default to &#39;false&#39;] |

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf, application/json


## list_managed_service_campaigns

> <ListManagedServiceCampaigns200Response> list_managed_service_campaigns(opts)

List your managed service campaigns

The campaigns your managed service runs for you, newest first. Without a managed service the list is empty: GET /me says whether you have one.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ManagedServicesApi.new
opts = {
  limit: 56, # Integer | Campaigns per page, 1 to 100.
  offset: 56 # Integer | Campaigns to skip.
}

begin
  # List your managed service campaigns
  result = api_instance.list_managed_service_campaigns(opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->list_managed_service_campaigns: #{e}"
end
```

#### Using the list_managed_service_campaigns_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListManagedServiceCampaigns200Response>, Integer, Hash)> list_managed_service_campaigns_with_http_info(opts)

```ruby
begin
  # List your managed service campaigns
  data, status_code, headers = api_instance.list_managed_service_campaigns_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListManagedServiceCampaigns200Response>
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->list_managed_service_campaigns_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **limit** | **Integer** | Campaigns per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Campaigns to skip. | [optional][default to 0] |

### Return type

[**ListManagedServiceCampaigns200Response**](ListManagedServiceCampaigns200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_managed_service_proposals

> <ListManagedServiceProposals200Response> list_managed_service_proposals(id, opts)

List the proposals of a campaign

The medias the team proposes for the campaign, newest first. Those `proposed` await your review (POST /managed-service/campaigns/{id}/proposals/review).

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ManagedServicesApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
opts = {
  state: 'proposed,accepted', # String | Only proposals in these states, comma-separated: `proposed`, `accepted`, `cancelled`, `purchase_started`, `purchase_finished`.
  limit: 56, # Integer | Proposals per page, 1 to 100.
  offset: 56 # Integer | Proposals to skip.
}

begin
  # List the proposals of a campaign
  result = api_instance.list_managed_service_proposals(id, opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->list_managed_service_proposals: #{e}"
end
```

#### Using the list_managed_service_proposals_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListManagedServiceProposals200Response>, Integer, Hash)> list_managed_service_proposals_with_http_info(id, opts)

```ruby
begin
  # List the proposals of a campaign
  data, status_code, headers = api_instance.list_managed_service_proposals_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListManagedServiceProposals200Response>
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->list_managed_service_proposals_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **state** | **String** | Only proposals in these states, comma-separated: &#x60;proposed&#x60;, &#x60;accepted&#x60;, &#x60;cancelled&#x60;, &#x60;purchase_started&#x60;, &#x60;purchase_finished&#x60;. | [optional] |
| **limit** | **Integer** | Proposals per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Proposals to skip. | [optional][default to 0] |

### Return type

[**ListManagedServiceProposals200Response**](ListManagedServiceProposals200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## request_managed_service_campaign

> <ManagedServiceRequestSent> request_managed_service_campaign(idempotency_key, managed_service_request)

Request a new campaign

Asks your account manager for a new campaign, as the managed service page does: the team emails you to agree on it. For accounts with a managed service (GET /me `managedService.active`); without one, POST /managed-service/info-requests asks about the service.  You may send 5 such requests per UTC day through the API. Past them it answers 429 `managed_service_request_limit_reached`, with `Retry-After` the time to the next UTC midnight. A request that is refused (4xx) does not count; one that fails on the server (5xx) does, as it may have been sent.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ManagedServicesApi.new
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
managed_service_request = Growwer::ManagedServiceRequest.new({project_url: 'project_url_example', goal: 'link_building', country: 'country_example', duration: 'one_time', estimated_budget: Growwer::Money.new({amount: 12500, currency: 'EUR'})}) # ManagedServiceRequest | 

begin
  # Request a new campaign
  result = api_instance.request_managed_service_campaign(idempotency_key, managed_service_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->request_managed_service_campaign: #{e}"
end
```

#### Using the request_managed_service_campaign_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ManagedServiceRequestSent>, Integer, Hash)> request_managed_service_campaign_with_http_info(idempotency_key, managed_service_request)

```ruby
begin
  # Request a new campaign
  data, status_code, headers = api_instance.request_managed_service_campaign_with_http_info(idempotency_key, managed_service_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ManagedServiceRequestSent>
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->request_managed_service_campaign_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **managed_service_request** | [**ManagedServiceRequest**](ManagedServiceRequest.md) |  |  |

### Return type

[**ManagedServiceRequestSent**](ManagedServiceRequestSent.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## request_managed_service_info

> <ManagedServiceRequestSent> request_managed_service_info(idempotency_key, managed_service_request)

Ask about the managed service

Asks the team about the managed service for your website, as the managed service landing page does: the team contacts you. For accounts without a managed service (GET /me `managedService.active`); with one, POST /managed-service/campaign-requests requests a new campaign.  You may send 5 such requests per UTC day through the API. Past them it answers 429 `managed_service_request_limit_reached`, with `Retry-After` the time to the next UTC midnight. A request that is refused (4xx) does not count; one that fails on the server (5xx) does, as it may have been sent.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ManagedServicesApi.new
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
managed_service_request = Growwer::ManagedServiceRequest.new({project_url: 'project_url_example', goal: 'link_building', country: 'country_example', duration: 'one_time', estimated_budget: Growwer::Money.new({amount: 12500, currency: 'EUR'})}) # ManagedServiceRequest | 

begin
  # Ask about the managed service
  result = api_instance.request_managed_service_info(idempotency_key, managed_service_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->request_managed_service_info: #{e}"
end
```

#### Using the request_managed_service_info_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ManagedServiceRequestSent>, Integer, Hash)> request_managed_service_info_with_http_info(idempotency_key, managed_service_request)

```ruby
begin
  # Ask about the managed service
  data, status_code, headers = api_instance.request_managed_service_info_with_http_info(idempotency_key, managed_service_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ManagedServiceRequestSent>
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->request_managed_service_info_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **managed_service_request** | [**ManagedServiceRequest**](ManagedServiceRequest.md) |  |  |

### Return type

[**ManagedServiceRequestSent**](ManagedServiceRequestSent.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## review_managed_service_proposals

> <ManagedServiceProposalReview> review_managed_service_proposals(id, idempotency_key, managed_service_proposal_review_request)

Accept or reject proposals

Decides on every proposal of the campaign that awaits your review (`state` `proposed`), as the campaign page does: name each one once, with `accept` or `reject`, and a comment for the team to reject one. Their order in the body does not matter. Accepting charges nothing: the team places the orders for the accepted proposals and your wallet pays for them then. POST /managed-service/campaigns/{id}/proposals/estimate says what they would cost.  When every proposal is accepted the campaign moves to `proposal_accepted`; when one is rejected the team is told and prepares others. A proposal someone else moved on the campaign page while the request ran is answered in the state it reached.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ManagedServicesApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
managed_service_proposal_review_request = Growwer::ManagedServiceProposalReviewRequest.new({reviews: [Growwer::ManagedServiceProposalReviewRequestReviewsInner.new({proposal_id: 'proposal_id_example', decision: 'accept'})]}) # ManagedServiceProposalReviewRequest | 

begin
  # Accept or reject proposals
  result = api_instance.review_managed_service_proposals(id, idempotency_key, managed_service_proposal_review_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->review_managed_service_proposals: #{e}"
end
```

#### Using the review_managed_service_proposals_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ManagedServiceProposalReview>, Integer, Hash)> review_managed_service_proposals_with_http_info(id, idempotency_key, managed_service_proposal_review_request)

```ruby
begin
  # Accept or reject proposals
  data, status_code, headers = api_instance.review_managed_service_proposals_with_http_info(id, idempotency_key, managed_service_proposal_review_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ManagedServiceProposalReview>
rescue Growwer::ApiError => e
  puts "Error when calling ManagedServicesApi->review_managed_service_proposals_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **managed_service_proposal_review_request** | [**ManagedServiceProposalReviewRequest**](ManagedServiceProposalReviewRequest.md) |  |  |

### Return type

[**ManagedServiceProposalReview**](ManagedServiceProposalReview.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

