# Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** | Your name for the project, or null when it has none. | 
**root_url** | **str** | The website the project promotes. It cannot be changed once the project exists. | 
**website_type** | **str** | What the website is: an online shop (&#x60;ecommerce&#x60;), a services business (&#x60;services&#x60;) or anything else (&#x60;other&#x60;). | 
**topics** | **List[int]** | The website&#39;s topic, as a topic id from GET /vocabulary. Exactly one. | 
**language** | **str** | The language of the campaign, as a language code from GET /vocabulary. | 
**country** | **str** | The country the campaign targets, as a country code from GET /vocabulary, or null for worldwide. | 
**promoted_products** | **List[str]** | The products or services the campaign promotes, 5 to 10. | 
**user_keywords** | **List[str]** | Keywords you want the campaign to target, at most 100. | 
**state** | **str** | &#x60;finished&#x60; once Growwer has recommended media for the project, &#x60;analyzing&#x60; until then. Analysis can take hours, and it never finishes when no medium matches the project. Poll with backoff, and use &#x60;createdAt&#x60; to decide how long to keep polling.  | 
**created_at** | **datetime** |  | 

## Example

```python
from growwer.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


