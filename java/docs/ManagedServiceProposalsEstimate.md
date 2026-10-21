

# ManagedServiceProposalsEstimate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptedTotal** | [**Money**](Money.md) | The proposals already accepted and still awaiting their order. |  |
|**selectedTotal** | [**Money**](Money.md) | The proposals named in &#x60;accept&#x60;. |  |
|**total** | [**Money**](Money.md) | &#x60;acceptedTotal&#x60; plus &#x60;selectedTotal&#x60;. |  |
|**availableBalance** | [**Money**](Money.md) | Your wallet&#39;s available balance. |  |
|**missing** | [**Money**](Money.md) | How much the available balance falls short of &#x60;total&#x60;; zero when it covers it. |  |
|**sufficientBalance** | **Boolean** | Whether the available balance covers &#x60;total&#x60;. |  |



