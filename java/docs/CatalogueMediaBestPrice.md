

# CatalogueMediaBestPrice

The best-price badge the catalogue shows, or null for none: cheaper means the price is at least 1 EUR below the cheapest listing of the media found on the other platforms checked in the last 7 days; only_here means none of the platforms checked lists it. It names neither the platforms nor any price.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**badge** | [**BadgeEnum**](#BadgeEnum) |  |  |
|**platformCount** | **Integer** | How many platforms the claim was checked against. |  |
|**checkedOn** | **LocalDate** | The day of that check. |  |



## Enum: BadgeEnum

| Name | Value |
|---- | -----|
| CHEAPER | &quot;cheaper&quot; |
| ONLY_HERE | &quot;only_here&quot; |



