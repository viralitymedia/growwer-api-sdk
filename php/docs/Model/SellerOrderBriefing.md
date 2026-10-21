# SellerOrderBriefing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **string** |  |
**language** | **string** | The language code of the article. |
**links** | [**\Growwer\Api\Model\OrderLink[]**](OrderLink.md) |  |
**extra_services** | **string[]** |  |
**additional_info** | **string** |  |
**written_by** | **string** | Who writes the article; &#x60;seller&#x60; means you do. |
**has_proposed_draft** | **bool** | Whether the buyer attached a draft; GET /seller/orders/{id}/briefing downloads it. |
**linking_from** | **string** | The existing article of the media the link goes into. |
**link** | [**\Growwer\Api\Model\OrderLink**](OrderLink.md) |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
