# Growwer::Order

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **reference** | **String** |  |  |
| **type** | **String** |  |  |
| **state** | **String** | The raw state name. GET /orders documents the values its &#x60;state&#x60; filter takes. |  |
| **pending_action** | **String** | Who the order is waiting on, or null when it waits on no one. |  |
| **price** | [**Money**](Money.md) | What you pay for the order. |  |
| **project** | [**OrderProject**](OrderProject.md) |  |  |
| **media** | [**OrderMedia**](OrderMedia.md) |  |  |
| **created_at** | **Time** |  |  |
| **updated_at** | **Time** | When the order last changed state. It changes on state changes only, so poll with GET /orders?updatedSince&#x3D; on it. |  |
| **scheduled_publication_date** | **Time** |  |  |
| **delivery** | [**OrderDelivery**](OrderDelivery.md) |  |  |
| **briefing** | [**OrderBriefing**](OrderBriefing.md) |  |  |
| **draft** | [**OrderDraft**](OrderDraft.md) |  |  |
| **state_history** | [**Array&lt;OrderStateHistoryInner&gt;**](OrderStateHistoryInner.md) | Every state change, oldest first. |  |
| **channel** | [**OrderChannel**](OrderChannel.md) |  |  |

## Example

```ruby
require 'growwer'

instance = Growwer::Order.new(
  id: null,
  reference: null,
  type: null,
  state: null,
  pending_action: null,
  price: null,
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

