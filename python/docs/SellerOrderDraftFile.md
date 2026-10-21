# SellerOrderDraftFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **UUID** | A file you uploaded with POST /files and have not used yet. It must be an odt, doc, docx or txt file of up to 8 MB. It is used up once the draft is delivered. | 

## Example

```python
from growwer.models.seller_order_draft_file import SellerOrderDraftFile

# TODO update the JSON string below
json = "{}"
# create an instance of SellerOrderDraftFile from a JSON string
seller_order_draft_file_instance = SellerOrderDraftFile.from_json(json)
# print the JSON string representation of the object
print(SellerOrderDraftFile.to_json())

# convert the object into a dict
seller_order_draft_file_dict = seller_order_draft_file_instance.to_dict()
# create an instance of SellerOrderDraftFile from a dict
seller_order_draft_file_from_dict = SellerOrderDraftFile.from_dict(seller_order_draft_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


