# GetVocabulary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | [**List[CodeName]**](CodeName.md) | ISO 3166-1 alpha-2 codes. | 
**languages** | [**List[CodeName]**](CodeName.md) | ISO 639 codes, as the web&#39;s language selectors offer them. | 
**topics** | [**List[GetVocabulary200ResponseTopicsInner]**](GetVocabulary200ResponseTopicsInner.md) |  | 
**product_types** | **List[str]** | What an order buys: a sponsored post, or a link added to an existing page. | 
**link_types** | **List[str]** |  | 
**order_states** | **List[str]** |  | 

## Example

```python
from growwer.models.get_vocabulary200_response import GetVocabulary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetVocabulary200Response from a JSON string
get_vocabulary200_response_instance = GetVocabulary200Response.from_json(json)
# print the JSON string representation of the object
print(GetVocabulary200Response.to_json())

# convert the object into a dict
get_vocabulary200_response_dict = get_vocabulary200_response_instance.to_dict()
# create an instance of GetVocabulary200Response from a dict
get_vocabulary200_response_from_dict = GetVocabulary200Response.from_dict(get_vocabulary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


