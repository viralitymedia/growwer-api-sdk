# ProjectsApi

All URIs are relative to *https://tool.growwer.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProject**](ProjectsApi.md#createProject) | **POST** /api/v1/projects | Create a project |
| [**deleteProject**](ProjectsApi.md#deleteProject) | **DELETE** /api/v1/projects/{id} | Delete a project |
| [**getProject**](ProjectsApi.md#getProject) | **GET** /api/v1/projects/{id} | Get a project |
| [**listProjects**](ProjectsApi.md#listProjects) | **GET** /api/v1/projects | List your projects |
| [**updateProject**](ProjectsApi.md#updateProject) | **PATCH** /api/v1/projects/{id} | Edit a project |


<a id="createProject"></a>
# **createProject**
> Project createProject(idempotencyKey, createProjectRequest)

Create a project

Creates a project for a website, as the web&#39;s project creation does. Growwer then analyses it in the background to recommend media: the project is answered with &#x60;state: analyzing&#x60; and turns &#x60;finished&#x60; when the analysis ends. Analysis can take hours, and it never finishes when no medium matches the project, so poll GET /projects/{id} with backoff and use &#x60;createdAt&#x60; to decide when to stop.  Every value is validated as on the web: &#x60;topics&#x60;, &#x60;language&#x60; and &#x60;country&#x60; take the identifiers GET /vocabulary publishes.  Creating a project also categorises its website through an external service, as the web does. When that service fails the answer is 500, although the project may already be saved, and a retry under the same Idempotency-Key answers 409 &#x60;idempotency_outcome_unknown&#x60;. After either, list your projects (GET /projects) before retrying with a new key, or you may create a duplicate.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    CreateProjectRequest createProjectRequest = new CreateProjectRequest(); // CreateProjectRequest | 
    try {
      Project result = apiInstance.createProject(idempotencyKey, createProjectRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#createProject");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **createProjectRequest** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | |

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

<a id="deleteProject"></a>
# **deleteProject**
> deleteProject(id, idempotencyKey)

Delete a project

Deletes one of your projects. A project with an order in progress cannot be deleted until its orders finish.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    try {
      apiInstance.deleteProject(id, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteProject");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID**|  | |
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |

### Return type

null (empty response body)

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

<a id="getProject"></a>
# **getProject**
> Project getProject(id)

Get a project

One of your projects. Poll it to follow &#x60;state&#x60; after creating the project.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      Project result = apiInstance.getProject(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getProject");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID**|  | |

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

<a id="listProjects"></a>
# **listProjects**
> ListProjects200Response listProjects(limit, offset)

List your projects

Your projects, newest first.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer limit = 20; // Integer | Projects per page, 1 to 100.
    Integer offset = 0; // Integer | Projects to skip.
    try {
      ListProjects200Response result = apiInstance.listProjects(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#listProjects");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Projects per page, 1 to 100. | [optional] [default to 20] |
| **offset** | **Integer**| Projects to skip. | [optional] [default to 0] |

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

<a id="updateProject"></a>
# **updateProject**
> Project updateProject(id, idempotencyKey, updateProjectRequest)

Edit a project

Changes only the fields you send. &#x60;rootUrl&#x60; cannot be changed; any field not listed here is refused. Changing &#x60;language&#x60;, &#x60;country&#x60;, &#x60;promotedProducts&#x60; or &#x60;topics&#x60; makes Growwer categorise the project and work out its target keywords again, in the background.

### Example
```java
// Import classes:
import com.growwer.api.ApiClient;
import com.growwer.api.ApiException;
import com.growwer.api.Configuration;
import com.growwer.api.auth.*;
import com.growwer.api.models.*;
import com.growwer.api.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tool.growwer.com");
    
    // Configure HTTP bearer authorization: apiKey
    HttpBearerAuth apiKey = (HttpBearerAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setBearerToken("BEARER TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters.
    UpdateProjectRequest updateProjectRequest = new UpdateProjectRequest(); // UpdateProjectRequest | 
    try {
      Project result = apiInstance.updateProject(id, idempotencyKey, updateProjectRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#updateProject");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID**|  | |
| **idempotencyKey** | **String**| A new key for each write, reused only to retry that same write. 1 to 255 printable ASCII characters. | |
| **updateProjectRequest** | [**UpdateProjectRequest**](UpdateProjectRequest.md)|  | |

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

