

# SellerOrderChannel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | [**CreatedEnum**](#CreatedEnum) | Whether the order was placed through this API (&#x60;api&#x60;), through its MCP server (&#x60;mcp&#x60;) or on the web. |  |
|**accepted** | [**AcceptedEnum**](#AcceptedEnum) | Whether you accepted the order through this API (&#x60;api&#x60;), through its MCP server (&#x60;mcp&#x60;) or elsewhere (&#x60;web&#x60;), or null while it is not accepted. |  |



## Enum: CreatedEnum

| Name | Value |
|---- | -----|
| API | &quot;api&quot; |
| MCP | &quot;mcp&quot; |
| WEB | &quot;web&quot; |



## Enum: AcceptedEnum

| Name | Value |
|---- | -----|
| API | &quot;api&quot; |
| MCP | &quot;mcp&quot; |
| WEB | &quot;web&quot; |



