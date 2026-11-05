

# GetMe200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**email** | **String** |  |  |
|**firstName** | **String** |  |  |
|**language** | **String** | The language Growwer writes to you in. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**buyer** | [**GetMe200ResponseBuyer**](GetMe200ResponseBuyer.md) |  |  |
|**seller** | [**GetMe200ResponseSeller**](GetMe200ResponseSeller.md) |  |  |
|**catalogue** | [**GetMe200ResponseCatalogue**](GetMe200ResponseCatalogue.md) |  |  |
|**managedService** | [**GetMe200ResponseManagedService**](GetMe200ResponseManagedService.md) |  |  |
|**mode** | [**ModeEnum**](#ModeEnum) | The mode of the key you called with. &#x60;live&#x60; works on your real account; &#x60;test&#x60; works in test mode, where nothing you do reaches real sellers, money or orders. Every response to a test key also carries the header &#x60;Growwer-Mode: test&#x60;. |  |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| LIVE | &quot;live&quot; |
| TEST | &quot;test&quot; |



