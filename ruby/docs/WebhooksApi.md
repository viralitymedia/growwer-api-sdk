# Growwer::WebhooksApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /api/v1/webhooks | Create a webhook subscription |
| [**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /api/v1/webhooks/{id} | Delete a webhook subscription |
| [**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /api/v1/webhooks/{id} | Get a webhook subscription |
| [**list_webhook_deliveries**](WebhooksApi.md#list_webhook_deliveries) | **GET** /api/v1/webhooks/{id}/deliveries | List the deliveries of a webhook subscription |
| [**list_webhooks**](WebhooksApi.md#list_webhooks) | **GET** /api/v1/webhooks | List your webhook subscriptions |
| [**redeliver_webhook**](WebhooksApi.md#redeliver_webhook) | **POST** /api/v1/webhooks/{id}/deliveries/{deliveryId}/redeliver | Redeliver a webhook event |
| [**rotate_webhook_secret**](WebhooksApi.md#rotate_webhook_secret) | **POST** /api/v1/webhooks/{id}/rotate-secret | Rotate a webhook secret |
| [**send_webhook_test**](WebhooksApi.md#send_webhook_test) | **POST** /api/v1/webhooks/{id}/test | Send a test event |
| [**update_webhook**](WebhooksApi.md#update_webhook) | **PATCH** /api/v1/webhooks/{id} | Edit a webhook subscription |


## create_webhook

> <WebhookWithSecret> create_webhook(idempotency_key, create_webhook_request)

Create a webhook subscription

Subscribes an HTTPS URL to the events you list. Growwer then POSTs each event to it, signed as Standard Webhooks signs (`webhook-id`, `webhook-timestamp`, `webhook-signature`) with the `secret` this answer carries. The secret is shown only here and on POST /webhooks/{id}/rotate-secret: store it now. A replay of this request under its `Idempotency-Key` answers the subscription without it.  The URL must be HTTPS and its host must resolve to public addresses only: a loopback, private, link-local, multicast or metadata address is refused with 422 `webhook_url_not_public`, a host that does not resolve with 422 `webhook_url_unresolvable`. `lowBalanceThreshold` is required with `balance.low` and refused without it. An account has at most 20 subscriptions per mode. Test keys get 403 `not_available_in_test_mode` for now.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::WebhooksApi.new
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
create_webhook_request = Growwer::CreateWebhookRequest.new({url: 'url_example', events: [Growwer::WebhookEventType::ORDER_CREATED]}) # CreateWebhookRequest | 

begin
  # Create a webhook subscription
  result = api_instance.create_webhook(idempotency_key, create_webhook_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->create_webhook: #{e}"
end
```

#### Using the create_webhook_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WebhookWithSecret>, Integer, Hash)> create_webhook_with_http_info(idempotency_key, create_webhook_request)

```ruby
begin
  # Create a webhook subscription
  data, status_code, headers = api_instance.create_webhook_with_http_info(idempotency_key, create_webhook_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WebhookWithSecret>
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->create_webhook_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md) |  |  |

### Return type

[**WebhookWithSecret**](WebhookWithSecret.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_webhook

> delete_webhook(id, idempotency_key)

Delete a webhook subscription

Deletes one of your webhook subscriptions and its delivery log. Deliveries still pending are not sent.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::WebhooksApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The subscription.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

begin
  # Delete a webhook subscription
  api_instance.delete_webhook(id, idempotency_key)
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->delete_webhook: #{e}"
end
```

#### Using the delete_webhook_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_webhook_with_http_info(id, idempotency_key)

```ruby
begin
  # Delete a webhook subscription
  data, status_code, headers = api_instance.delete_webhook_with_http_info(id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->delete_webhook_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The subscription. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

nil (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_webhook

> <Webhook> get_webhook(id)

Get a webhook subscription

One of your webhook subscriptions, without its secret. A subscription of the other mode is not found.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::WebhooksApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The subscription.

begin
  # Get a webhook subscription
  result = api_instance.get_webhook(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->get_webhook: #{e}"
end
```

#### Using the get_webhook_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Webhook>, Integer, Hash)> get_webhook_with_http_info(id)

```ruby
begin
  # Get a webhook subscription
  data, status_code, headers = api_instance.get_webhook_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Webhook>
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->get_webhook_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The subscription. |  |

### Return type

[**Webhook**](Webhook.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_webhook_deliveries

> <ListWebhookDeliveries200Response> list_webhook_deliveries(id, opts)

List the deliveries of a webhook subscription

The events sent to the subscription in the last 30 days, newest first, each with its status and its latest 10 attempts: when, the status code your endpoint answered, how long it took and the start of its response body. Older deliveries are deleted.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::WebhooksApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The subscription.
opts = {
  limit: 56, # Integer | Deliveries per page, 1 to 100.
  offset: 56 # Integer | Deliveries to skip.
}

begin
  # List the deliveries of a webhook subscription
  result = api_instance.list_webhook_deliveries(id, opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->list_webhook_deliveries: #{e}"
end
```

#### Using the list_webhook_deliveries_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListWebhookDeliveries200Response>, Integer, Hash)> list_webhook_deliveries_with_http_info(id, opts)

```ruby
begin
  # List the deliveries of a webhook subscription
  data, status_code, headers = api_instance.list_webhook_deliveries_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListWebhookDeliveries200Response>
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->list_webhook_deliveries_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The subscription. |  |
| **limit** | **Integer** | Deliveries per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Deliveries to skip. | [optional][default to 0] |

### Return type

[**ListWebhookDeliveries200Response**](ListWebhookDeliveries200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_webhooks

> <ListWebhooks200Response> list_webhooks(opts)

List your webhook subscriptions

Your webhook subscriptions in the mode of the key, newest first, disabled ones included. A live key lists the live ones and a test key the test ones.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::WebhooksApi.new
opts = {
  limit: 56, # Integer | Subscriptions per page, 1 to 100.
  offset: 56 # Integer | Subscriptions to skip.
}

begin
  # List your webhook subscriptions
  result = api_instance.list_webhooks(opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->list_webhooks: #{e}"
end
```

#### Using the list_webhooks_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListWebhooks200Response>, Integer, Hash)> list_webhooks_with_http_info(opts)

```ruby
begin
  # List your webhook subscriptions
  data, status_code, headers = api_instance.list_webhooks_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListWebhooks200Response>
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->list_webhooks_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **limit** | **Integer** | Subscriptions per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Subscriptions to skip. | [optional][default to 0] |

### Return type

[**ListWebhooks200Response**](ListWebhooks200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redeliver_webhook

> <WebhookDelivery> redeliver_webhook(id, delivery_id, idempotency_key)

Redeliver a webhook event

Queues a delivery that has succeeded or failed again, in a new round of retries, and answers it. It sends the same event with the same `webhook-id`, so a consumer that dedupes by it handles it once. Deliveries are kept 30 days. A delivery still pending, being sent or waiting for its next retry, answers 409 `webhook_delivery_pending` and takes none of the hour's sends; so does a redelivery while the subscription has 10 test events and redeliveries pending, its limit for a redelivery, given in `details.limit`. The pending deliveries of events never redelivered do not count. A subscription takes at most 10 test events and redeliveries an hour: past them it answers 429 `webhook_send_limit_reached` with `Retry-After`. A disabled subscription answers 409 `webhook_disabled`.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::WebhooksApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The subscription.
delivery_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The delivery.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

begin
  # Redeliver a webhook event
  result = api_instance.redeliver_webhook(id, delivery_id, idempotency_key)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->redeliver_webhook: #{e}"
end
```

#### Using the redeliver_webhook_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WebhookDelivery>, Integer, Hash)> redeliver_webhook_with_http_info(id, delivery_id, idempotency_key)

```ruby
begin
  # Redeliver a webhook event
  data, status_code, headers = api_instance.redeliver_webhook_with_http_info(id, delivery_id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WebhookDelivery>
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->redeliver_webhook_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The subscription. |  |
| **delivery_id** | **String** | The delivery. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

[**WebhookDelivery**](WebhookDelivery.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rotate_webhook_secret

> <WebhookWithSecret> rotate_webhook_secret(id, idempotency_key)

Rotate a webhook secret

Gives the subscription a new signing secret and answers it: it is shown only here, so store it now. For 24 hours, until `previousSecretExpiresAt`, every delivery carries two signatures in `webhook-signature`, one with each secret, so you can switch without missing an event; after that only the new secret signs. A replay of this request under its `Idempotency-Key` answers the subscription without the secret.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::WebhooksApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The subscription.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

begin
  # Rotate a webhook secret
  result = api_instance.rotate_webhook_secret(id, idempotency_key)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->rotate_webhook_secret: #{e}"
end
```

#### Using the rotate_webhook_secret_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WebhookWithSecret>, Integer, Hash)> rotate_webhook_secret_with_http_info(id, idempotency_key)

```ruby
begin
  # Rotate a webhook secret
  data, status_code, headers = api_instance.rotate_webhook_secret_with_http_info(id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WebhookWithSecret>
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->rotate_webhook_secret_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The subscription. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

[**WebhookWithSecret**](WebhookWithSecret.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## send_webhook_test

> <WebhookDelivery> send_webhook_test(id, idempotency_key)

Send a test event

Queues a `webhook.test` event for the subscription, whatever events it lists, and answers its delivery: follow it on GET /webhooks/{id}/deliveries. It is signed, retried and logged as any event. It normally supersedes the subscription's earlier test events still pending: their deliveries fail and are not retried, so a test right after fixing the endpoint does not wait behind them; one that cannot be failed then is failed by the next test. A subscription takes at most 10 test events and redeliveries an hour: past them it answers 429 `webhook_send_limit_reached` with `Retry-After`. A disabled subscription answers 409 `webhook_disabled`. A test event that cannot be recorded answers 503 `webhook_test_unavailable`: nothing was sent, the attempt counts toward the hourly limit, and a retry needs a new `Idempotency-Key`.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::WebhooksApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The subscription.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.

begin
  # Send a test event
  result = api_instance.send_webhook_test(id, idempotency_key)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->send_webhook_test: #{e}"
end
```

#### Using the send_webhook_test_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WebhookDelivery>, Integer, Hash)> send_webhook_test_with_http_info(id, idempotency_key)

```ruby
begin
  # Send a test event
  data, status_code, headers = api_instance.send_webhook_test_with_http_info(id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WebhookDelivery>
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->send_webhook_test_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The subscription. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |

### Return type

[**WebhookDelivery**](WebhookDelivery.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_webhook

> <Webhook> update_webhook(id, idempotency_key, update_webhook_request)

Edit a webhook subscription

Changes only the fields you send. A new `url` is checked as on create. Dropping `balance.low` from `events` drops the threshold with it. `enabled: false` disables the subscription, which then gets no events; `enabled: true` enables it again, including one Growwer disabled because its endpoint answered 410 or failed for 5 days, and forgets its failures.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::WebhooksApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The subscription.
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (`!` to `~`); any other value answers 400 `invalid_idempotency_key`.
update_webhook_request = Growwer::UpdateWebhookRequest.new # UpdateWebhookRequest | 

begin
  # Edit a webhook subscription
  result = api_instance.update_webhook(id, idempotency_key, update_webhook_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->update_webhook: #{e}"
end
```

#### Using the update_webhook_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Webhook>, Integer, Hash)> update_webhook_with_http_info(id, idempotency_key, update_webhook_request)

```ruby
begin
  # Edit a webhook subscription
  data, status_code, headers = api_instance.update_webhook_with_http_info(id, idempotency_key, update_webhook_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Webhook>
rescue Growwer::ApiError => e
  puts "Error when calling WebhooksApi->update_webhook_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The subscription. |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters without spaces (&#x60;!&#x60; to &#x60;~&#x60;); any other value answers 400 &#x60;invalid_idempotency_key&#x60;. |  |
| **update_webhook_request** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md) |  |  |

### Return type

[**Webhook**](Webhook.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

