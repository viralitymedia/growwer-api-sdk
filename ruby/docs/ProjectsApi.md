# Growwer::ProjectsApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_project**](ProjectsApi.md#create_project) | **POST** /api/v1/projects | Create a project |
| [**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /api/v1/projects/{id} | Delete a project |
| [**get_project**](ProjectsApi.md#get_project) | **GET** /api/v1/projects/{id} | Get a project |
| [**list_projects**](ProjectsApi.md#list_projects) | **GET** /api/v1/projects | List your projects |
| [**update_project**](ProjectsApi.md#update_project) | **PATCH** /api/v1/projects/{id} | Edit a project |


## create_project

> <Project> create_project(idempotency_key, create_project_request)

Create a project

Creates a project for a website, as the web's project creation does. Growwer then analyses it in the background to recommend media: the project is answered with `state: analyzing` and turns `finished` when the analysis ends. Analysis can take hours, and it never finishes when no medium matches the project, so poll GET /projects/{id} with backoff and use `createdAt` to decide when to stop.  Every value is validated as on the web: `topics`, `language` and `country` take the identifiers GET /vocabulary publishes.  Creating a project also categorises its website through an external service, as the web does. When that service fails the answer is 500, although the project may already be saved, and a retry under the same Idempotency-Key answers 409 `idempotency_outcome_unknown`. After either, list your projects (GET /projects) before retrying with a new key, or you may create a duplicate.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ProjectsApi.new
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
create_project_request = Growwer::CreateProjectRequest.new({root_url: 'https://www.example.com', website_type: 'ecommerce', topics: [37], language: 'es', promoted_products: ['promoted_products_example']}) # CreateProjectRequest | 

begin
  # Create a project
  result = api_instance.create_project(idempotency_key, create_project_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ProjectsApi->create_project: #{e}"
end
```

#### Using the create_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Project>, Integer, Hash)> create_project_with_http_info(idempotency_key, create_project_request)

```ruby
begin
  # Create a project
  data, status_code, headers = api_instance.create_project_with_http_info(idempotency_key, create_project_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Project>
rescue Growwer::ApiError => e
  puts "Error when calling ProjectsApi->create_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |
| **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md) |  |  |

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_project

> delete_project(id, idempotency_key)

Delete a project

Deletes one of your projects. A project with an order in progress cannot be deleted until its orders finish.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ProjectsApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

begin
  # Delete a project
  api_instance.delete_project(id, idempotency_key)
rescue Growwer::ApiError => e
  puts "Error when calling ProjectsApi->delete_project: #{e}"
end
```

#### Using the delete_project_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_project_with_http_info(id, idempotency_key)

```ruby
begin
  # Delete a project
  data, status_code, headers = api_instance.delete_project_with_http_info(id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Growwer::ApiError => e
  puts "Error when calling ProjectsApi->delete_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |

### Return type

nil (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_project

> <Project> get_project(id)

Get a project

One of your projects. Poll it to follow `state` after creating the project.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ProjectsApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Get a project
  result = api_instance.get_project(id)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ProjectsApi->get_project: #{e}"
end
```

#### Using the get_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Project>, Integer, Hash)> get_project_with_http_info(id)

```ruby
begin
  # Get a project
  data, status_code, headers = api_instance.get_project_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Project>
rescue Growwer::ApiError => e
  puts "Error when calling ProjectsApi->get_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_projects

> <ListProjects200Response> list_projects(opts)

List your projects

Your projects, newest first.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ProjectsApi.new
opts = {
  limit: 56, # Integer | Projects per page, 1 to 100.
  offset: 56 # Integer | Projects to skip.
}

begin
  # List your projects
  result = api_instance.list_projects(opts)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ProjectsApi->list_projects: #{e}"
end
```

#### Using the list_projects_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListProjects200Response>, Integer, Hash)> list_projects_with_http_info(opts)

```ruby
begin
  # List your projects
  data, status_code, headers = api_instance.list_projects_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListProjects200Response>
rescue Growwer::ApiError => e
  puts "Error when calling ProjectsApi->list_projects_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **limit** | **Integer** | Projects per page, 1 to 100. | [optional][default to 20] |
| **offset** | **Integer** | Projects to skip. | [optional][default to 0] |

### Return type

[**ListProjects200Response**](ListProjects200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_project

> <Project> update_project(id, idempotency_key, update_project_request)

Edit a project

Changes only the fields you send. `rootUrl` cannot be changed; any field not listed here is refused. Changing `language`, `country`, `promotedProducts` or `topics` makes Growwer categorise the project and work out its target keywords again, in the background.

### Examples

```ruby
require 'time'
require 'growwer'
# setup authorization
Growwer.configure do |config|
  # Configure Bearer authorization: apiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Growwer::ProjectsApi.new
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
update_project_request = Growwer::UpdateProjectRequest.new # UpdateProjectRequest | 

begin
  # Edit a project
  result = api_instance.update_project(id, idempotency_key, update_project_request)
  p result
rescue Growwer::ApiError => e
  puts "Error when calling ProjectsApi->update_project: #{e}"
end
```

#### Using the update_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Project>, Integer, Hash)> update_project_with_http_info(id, idempotency_key, update_project_request)

```ruby
begin
  # Edit a project
  data, status_code, headers = api_instance.update_project_with_http_info(id, idempotency_key, update_project_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Project>
rescue Growwer::ApiError => e
  puts "Error when calling ProjectsApi->update_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **idempotency_key** | **String** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |
| **update_project_request** | [**UpdateProjectRequest**](UpdateProjectRequest.md) |  |  |

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

