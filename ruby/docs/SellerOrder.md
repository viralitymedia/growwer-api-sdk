# Growwer::SellerOrder

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **reference** | **String** |  |  |
| **type** | **String** |  |  |
| **state** | **String** | The raw state name. GET /seller/orders documents the values its &#x60;state&#x60; filter takes. |  |
| **requires_your_action** | **Boolean** | Whether the order waits on you, as the seller order list marks it. |  |
| **available_actions** | **Array&lt;String&gt;** | The seller actions the order allows now. |  |
| **earnings** | [**Money**](Money.md) | What you are paid for the order, credited to your seller wallet once it settles. |  |
| **project** | [**SellerOrderProject**](SellerOrderProject.md) |  |  |
| **media** | [**OrderMedia**](OrderMedia.md) |  |  |
| **created_at** | **Time** |  |  |
| **updated_at** | **Time** | When the order last changed state. It changes on state changes only, so poll with GET /seller/orders?updatedSince&#x3D; on it. |  |
| **scheduled_publication_date** | **Time** |  |  |
| **delivery** | [**OrderDelivery**](OrderDelivery.md) |  |  |
| **briefing** | [**SellerOrderBriefing**](SellerOrderBriefing.md) |  |  |
| **draft** | [**SellerOrderDraft**](SellerOrderDraft.md) |  |  |
| **state_history** | [**Array&lt;OrderStateHistoryInner&gt;**](OrderStateHistoryInner.md) | Every state change, oldest first. |  |
| **channel** | [**SellerOrderChannel**](SellerOrderChannel.md) |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::SellerOrder.new(
  id: null,
  reference: null,
  type: null,
  state: null,
  requires_your_action: null,
  available_actions: null,
  earnings: null,
  project: null,
  media: null,
  created_at: null,
  updated_at: null,
  scheduled_publication_date: null,
  delivery: null,
  briefing: null,
  draft: null,
  state_history: null,
  channel: null
)
```

