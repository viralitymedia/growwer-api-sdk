# Growwer.Api.Api.ProjectsApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CreateProject**](ProjectsApi.md#createproject) | **POST** /api/v1/projects | Create a project |
| [**DeleteProject**](ProjectsApi.md#deleteproject) | **DELETE** /api/v1/projects/{id} | Delete a project |
| [**GetProject**](ProjectsApi.md#getproject) | **GET** /api/v1/projects/{id} | Get a project |
| [**ListProjects**](ProjectsApi.md#listprojects) | **GET** /api/v1/projects | List your projects |
| [**UpdateProject**](ProjectsApi.md#updateproject) | **PATCH** /api/v1/projects/{id} | Edit a project |

<a id="createproject"></a>
# **CreateProject**
> Project CreateProject (string idempotencyKey, CreateProjectRequest createProjectRequest)

Create a project

Creates a project for a website, as the web's project creation does. Growwer then analyses it in the background to recommend media: the project is answered with `state: analyzing` and turns `finished` when the analysis ends. Analysis can take hours, and it never finishes when no medium matches the project, so poll GET /projects/{id} with backoff and use `createdAt` to decide when to stop.  Every value is validated as on the web: `topics`, `language` and `country` take the identifiers GET /vocabulary publishes.  Creating a project also categorises its website through an external service, as the web does. When that service fails the answer is 500, although the project may already be saved, and a retry under the same Idempotency-Key answers 409 `idempotency_outcome_unknown`. After either, list your projects (GET /projects) before retrying with a new key, or you may create a duplicate.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class CreateProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
            var createProjectRequest = new CreateProjectRequest(); // CreateProjectRequest | 

            try
            {
                // Create a project
                Project result = apiInstance.CreateProject(idempotencyKey, createProjectRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.CreateProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the CreateProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Create a project
    ApiResponse<Project> response = apiInstance.CreateProjectWithHttpInfo(idempotencyKey, createProjectRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.CreateProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |
| **createProjectRequest** | [**CreateProjectRequest**](CreateProjectRequest.md) |  |  |

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The project, created and being analysed. &#x60;Location&#x60; is its URL. |  * Location - The URL of the new project. <br>  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key is read-only (code &#x60;insufficient_capability&#x60;), or you have reached the number of projects an account may have without a wallet deposit in the last year (code &#x60;project_limit_reached&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="deleteproject"></a>
# **DeleteProject**
> void DeleteProject (Guid id, string idempotencyKey)

Delete a project

Deletes one of your projects. A project with an order in progress cannot be deleted until its orders finish.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class DeleteProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.

            try
            {
                // Delete a project
                apiInstance.DeleteProject(id, idempotencyKey);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.DeleteProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DeleteProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Delete a project
    apiInstance.DeleteProjectWithHttpInfo(id, idempotencyKey);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.DeleteProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The project was deleted. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The project has an order in progress (code &#x60;invalid_state&#x60;), or the &#x60;Idempotency-Key&#x60; conflicts (codes &#x60;idempotency_key_reused&#x60;, &#x60;idempotency_request_in_progress&#x60;, &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getproject"></a>
# **GetProject**
> Project GetProject (Guid id)

Get a project

One of your projects. Poll it to follow `state` after creating the project.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class GetProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 

            try
            {
                // Get a project
                Project result = apiInstance.GetProject(id);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.GetProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get a project
    ApiResponse<Project> response = apiInstance.GetProjectWithHttpInfo(id);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.GetProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listprojects"></a>
# **ListProjects**
> ListProjects200Response ListProjects (int? limit = null, int? offset = null)

List your projects

Your projects, newest first.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class ListProjectsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var limit = 20;  // int? | Projects per page, 1 to 100. (optional)  (default to 20)
            var offset = 0;  // int? | Projects to skip. (optional)  (default to 0)

            try
            {
                // List your projects
                ListProjects200Response result = apiInstance.ListProjects(limit, offset);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.ListProjects: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListProjectsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List your projects
    ApiResponse<ListProjects200Response> response = apiInstance.ListProjectsWithHttpInfo(limit, offset);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.ListProjectsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **limit** | **int?** | Projects per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **int?** | Projects to skip. | [optional] [default to 0] |

### Return type

[**ListProjects200Response**](ListProjects200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of your projects and how many you have in all. |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="updateproject"></a>
# **UpdateProject**
> Project UpdateProject (Guid id, string idempotencyKey, UpdateProjectRequest updateProjectRequest)

Edit a project

Changes only the fields you send. `rootUrl` cannot be changed; any field not listed here is refused. Changing `language`, `country`, `promotedProducts` or `topics` makes Growwer categorise the project and work out its target keywords again, in the background.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Growwer.Api.Api;
using Growwer.Api.Client;
using Growwer.Api.Model;

namespace Example
{
    public class UpdateProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://tool.growwer.com";
            // Configure Bearer token for authorization: apiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var id = "id_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
            var updateProjectRequest = new UpdateProjectRequest(); // UpdateProjectRequest | 

            try
            {
                // Edit a project
                Project result = apiInstance.UpdateProject(id, idempotencyKey, updateProjectRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.UpdateProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Edit a project
    ApiResponse<Project> response = apiInstance.UpdateProjectWithHttpInfo(id, idempotencyKey, updateProjectRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.UpdateProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **idempotencyKey** | **string** | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. |  |
| **updateProjectRequest** | [**UpdateProjectRequest**](UpdateProjectRequest.md) |  |  |

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project as edited. |  -  |
| **400** | The write has no &#x60;Idempotency-Key&#x60; header (code &#x60;idempotency_key_required&#x60;), the header is not 1 to 255 printable ASCII characters (code &#x60;invalid_idempotency_key&#x60;), or the body is not a JSON object (code &#x60;invalid_json&#x60;). |  -  |
| **401** | The API key is missing, malformed, unknown, revoked or expired, or its account cannot sign in (code &#x60;unauthorized&#x60;). |  -  |
| **403** | The key lacks the capability the operation needs (code &#x60;insufficient_capability&#x60;), or the account may not perform it (code &#x60;forbidden&#x60;). |  -  |
| **404** | The resource does not exist, or it is not yours (code &#x60;not_found&#x60;). |  -  |
| **409** | The &#x60;Idempotency-Key&#x60; was used for a different request (code &#x60;idempotency_key_reused&#x60;), its first request is still running (code &#x60;idempotency_request_in_progress&#x60;), or its first request failed and may have taken effect (code &#x60;idempotency_outcome_unknown&#x60;). |  -  |
| **422** | The request is not valid (code &#x60;validation_failed&#x60;). &#x60;details.fields&#x60; holds the messages for each invalid field, by field name. |  -  |
| **429** | Over the rate limit (code &#x60;rate_limit_exceeded&#x60;), or too many failed authentications from this address (code &#x60;too_many_failed_authentications&#x60;). On the catalogue operations, also when the response would take the account beyond the distinct medias it may see per UTC day (code &#x60;catalogue_daily_cap_reached&#x60;): &#x60;details.remaining&#x60; says how many new medias still fit today, &#x60;Retry-After&#x60; is the time to the next UTC midnight, and medias already seen today stay readable. On the managed service requests, also when you sent as many requests of that kind as you may per UTC day (code &#x60;managed_service_request_limit_reached&#x60;): &#x60;Retry-After&#x60; is the time to the next UTC midnight. |  * Retry-After -  <br>  |
| **500** | An unexpected error (code &#x60;internal_error&#x60;). |  -  |
| **503** | The rate limiter cannot be reached, so the call is refused (code &#x60;rate_limit_unavailable&#x60;), or a stored file cannot be read right now (code &#x60;storage_unavailable&#x60;). Retry later. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

