# OpenAPIClient-php

The Growwer customer API. Authenticate every call with an API key created on
your profile page, sent as `Authorization: Bearer <key>`. A read key can call
every GET operation; writes need a read and write key and an
`Idempotency-Key` header.

Idempotency: use a new `Idempotency-Key` (1 to 255 printable ASCII
characters without spaces) for each operation and reuse it only to retry that same
operation. Keys belong to your account, not to one API key.
- A successful write is stored for 30 days: a retry with the same key and
  the same request replays its response with `Idempotent-Replayed: true`
  and does nothing again.
- A refused write (4xx) has no effect and releases its key: once you fix the
  cause, retry with the same key and the write runs.
- A failed write (5xx) may have taken effect, so it is never run again under
  its key: a retry gets 409 `idempotency_outcome_unknown`. Check whether it
  took effect before retrying with a new key.
- A retry while the first request is still running gets 409
  `idempotency_request_in_progress`. A request still running after 5 minutes
  is treated as failed: a retry gets 409 `idempotency_outcome_unknown`.
- The same key with a different request (method, path, query or body) gets
  409 `idempotency_key_reused`. A write without the header gets 400
  `idempotency_key_required`.

Every response carries `X-Request-Id`. Errors share one shape,
`{code, message, requestId, details?}`. Money is integer cents plus a
currency code and dates are ISO-8601.


For more information, please visit [https://growwer.com/contact/](https://growwer.com/contact/).

## Installation & Usage

### Requirements

PHP 8.1 and later.

### Composer

To install the bindings via [Composer](https://getcomposer.org/), add the following to `composer.json`:

```json
{
  "repositories": [
    {
      "type": "vcs",
      "url": "https://github.com/viralitymedia/growwer-api-sdk.git"
    }
  ],
  "require": {
    "growwer/growwer-api-sdk": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
<?php
require_once('/path/to/OpenAPIClient-php/vendor/autoload.php');
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



// Configure Bearer authorization: apiKey
$config = Growwer\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Growwer\Api\Api\AccountApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getMe();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountApi->getMe: ', $e->getMessage(), PHP_EOL;
}

```

## API Endpoints

All URIs are relative to *https://tool.growwer.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**getMe**](docs/Api/AccountApi.md#getme) | **GET** /api/v1/me | Your account
*AccountApi* | [**getVocabulary**](docs/Api/AccountApi.md#getvocabulary) | **GET** /api/v1/vocabulary | Codes and names
*BuyerOrdersApi* | [**approveOrder**](docs/Api/BuyerOrdersApi.md#approveorder) | **POST** /api/v1/orders/{id}/approve | Approve an order&#39;s delivery
*BuyerOrdersApi* | [**approveOrderDraft**](docs/Api/BuyerOrdersApi.md#approveorderdraft) | **POST** /api/v1/orders/{id}/approve-draft | Approve a draft
*BuyerOrdersApi* | [**cancelOrder**](docs/Api/BuyerOrdersApi.md#cancelorder) | **POST** /api/v1/orders/{id}/cancel | Cancel an order
*BuyerOrdersApi* | [**createOrder**](docs/Api/BuyerOrdersApi.md#createorder) | **POST** /api/v1/orders | Place an order
*BuyerOrdersApi* | [**downloadOrderBriefing**](docs/Api/BuyerOrdersApi.md#downloadorderbriefing) | **GET** /api/v1/orders/{id}/briefing | Download the draft you attached to an order
*BuyerOrdersApi* | [**downloadOrderDraft**](docs/Api/BuyerOrdersApi.md#downloadorderdraft) | **GET** /api/v1/orders/{id}/draft | Download the draft of an order
*BuyerOrdersApi* | [**estimateOrder**](docs/Api/BuyerOrdersApi.md#estimateorder) | **POST** /api/v1/orders/estimate | Estimate an order
*BuyerOrdersApi* | [**getOrder**](docs/Api/BuyerOrdersApi.md#getorder) | **GET** /api/v1/orders/{id} | Get an order
*BuyerOrdersApi* | [**listOrders**](docs/Api/BuyerOrdersApi.md#listorders) | **GET** /api/v1/orders | List your orders
*BuyerOrdersApi* | [**requestOrderDraftUpdate**](docs/Api/BuyerOrdersApi.md#requestorderdraftupdate) | **POST** /api/v1/orders/{id}/request-draft-update | Request changes to a draft
*BuyerOrdersApi* | [**requestOrderUpdate**](docs/Api/BuyerOrdersApi.md#requestorderupdate) | **POST** /api/v1/orders/{id}/request-update | Request changes to a delivery
*BuyerWalletApi* | [**downloadBuyerTransactionDocument**](docs/Api/BuyerWalletApi.md#downloadbuyertransactiondocument) | **GET** /api/v1/wallets/buyer/transactions/{id}/document | Download the document of a wallet movement
*BuyerWalletApi* | [**getBuyerWallet**](docs/Api/BuyerWalletApi.md#getbuyerwallet) | **GET** /api/v1/wallets/buyer | Get your buyer wallet
*BuyerWalletApi* | [**getInvoicePdf**](docs/Api/BuyerWalletApi.md#getinvoicepdf) | **GET** /api/v1/invoices/{id}/pdf | Download an invoice
*BuyerWalletApi* | [**listBuyerTransactions**](docs/Api/BuyerWalletApi.md#listbuyertransactions) | **GET** /api/v1/wallets/buyer/transactions | List your buyer wallet movements
*BuyerWalletApi* | [**listInvoices**](docs/Api/BuyerWalletApi.md#listinvoices) | **GET** /api/v1/invoices | List your invoices
*CatalogueApi* | [**discardMedia**](docs/Api/CatalogueApi.md#discardmedia) | **PUT** /api/v1/projects/{id}/discards/{mediaId} | Discard a media for a project
*CatalogueApi* | [**favouriteMedia**](docs/Api/CatalogueApi.md#favouritemedia) | **PUT** /api/v1/projects/{id}/favourites/{mediaId} | Add a media to the favourites of a project
*CatalogueApi* | [**getCatalogueMedia**](docs/Api/CatalogueApi.md#getcataloguemedia) | **GET** /api/v1/medias/{id} | Get a media
*CatalogueApi* | [**listFlashOffers**](docs/Api/CatalogueApi.md#listflashoffers) | **GET** /api/v1/flash-offers | List flash offers
*CatalogueApi* | [**requestMedias**](docs/Api/CatalogueApi.md#requestmedias) | **POST** /api/v1/projects/{id}/media-requests | Request specific medias for a project
*CatalogueApi* | [**searchProjectMedias**](docs/Api/CatalogueApi.md#searchprojectmedias) | **GET** /api/v1/projects/{id}/medias | Search the catalogue for a project
*CatalogueApi* | [**undiscardMedia**](docs/Api/CatalogueApi.md#undiscardmedia) | **DELETE** /api/v1/projects/{id}/discards/{mediaId} | Restore a discarded media for a project
*CatalogueApi* | [**unfavouriteMedia**](docs/Api/CatalogueApi.md#unfavouritemedia) | **DELETE** /api/v1/projects/{id}/favourites/{mediaId} | Remove a media from the favourites of a project
*FilesApi* | [**uploadFile**](docs/Api/FilesApi.md#uploadfile) | **POST** /api/v1/files | Upload a file
*ManagedServicesApi* | [**estimateManagedServiceProposals**](docs/Api/ManagedServicesApi.md#estimatemanagedserviceproposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/estimate | Estimate accepting proposals
*ManagedServicesApi* | [**getManagedServiceCampaign**](docs/Api/ManagedServicesApi.md#getmanagedservicecampaign) | **GET** /api/v1/managed-service/campaigns/{id} | Get a managed service campaign
*ManagedServicesApi* | [**getManagedServiceProposalsSummary**](docs/Api/ManagedServicesApi.md#getmanagedserviceproposalssummary) | **GET** /api/v1/managed-service/campaigns/{id}/proposals-summary | Download the summary of a campaign&#39;s proposals
*ManagedServicesApi* | [**listManagedServiceCampaigns**](docs/Api/ManagedServicesApi.md#listmanagedservicecampaigns) | **GET** /api/v1/managed-service/campaigns | List your managed service campaigns
*ManagedServicesApi* | [**listManagedServiceProposals**](docs/Api/ManagedServicesApi.md#listmanagedserviceproposals) | **GET** /api/v1/managed-service/campaigns/{id}/proposals | List the proposals of a campaign
*ManagedServicesApi* | [**requestManagedServiceCampaign**](docs/Api/ManagedServicesApi.md#requestmanagedservicecampaign) | **POST** /api/v1/managed-service/campaign-requests | Request a new campaign
*ManagedServicesApi* | [**requestManagedServiceInfo**](docs/Api/ManagedServicesApi.md#requestmanagedserviceinfo) | **POST** /api/v1/managed-service/info-requests | Ask about the managed service
*ManagedServicesApi* | [**reviewManagedServiceProposals**](docs/Api/ManagedServicesApi.md#reviewmanagedserviceproposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/review | Accept or reject proposals
*ProjectsApi* | [**createProject**](docs/Api/ProjectsApi.md#createproject) | **POST** /api/v1/projects | Create a project
*ProjectsApi* | [**deleteProject**](docs/Api/ProjectsApi.md#deleteproject) | **DELETE** /api/v1/projects/{id} | Delete a project
*ProjectsApi* | [**getProject**](docs/Api/ProjectsApi.md#getproject) | **GET** /api/v1/projects/{id} | Get a project
*ProjectsApi* | [**listProjects**](docs/Api/ProjectsApi.md#listprojects) | **GET** /api/v1/projects | List your projects
*ProjectsApi* | [**updateProject**](docs/Api/ProjectsApi.md#updateproject) | **PATCH** /api/v1/projects/{id} | Edit a project
*SavedFiltersApi* | [**countSavedFilterMedias**](docs/Api/SavedFiltersApi.md#countsavedfiltermedias) | **GET** /api/v1/projects/{id}/saved-filters/{filterId}/media-count | Count the medias of a saved filter
*SavedFiltersApi* | [**createSavedFilter**](docs/Api/SavedFiltersApi.md#createsavedfilter) | **POST** /api/v1/projects/{id}/saved-filters | Save a filter
*SavedFiltersApi* | [**deleteSavedFilter**](docs/Api/SavedFiltersApi.md#deletesavedfilter) | **DELETE** /api/v1/projects/{id}/saved-filters/{filterId} | Delete a saved filter
*SavedFiltersApi* | [**listSavedFilters**](docs/Api/SavedFiltersApi.md#listsavedfilters) | **GET** /api/v1/projects/{id}/saved-filters | List the saved filters of a project
*SellerAccountApi* | [**putSellerHoliday**](docs/Api/SellerAccountApi.md#putsellerholiday) | **PUT** /api/v1/seller/holiday | Set your holiday
*SellerMediasApi* | [**applySellerMediaCompetitiveFees**](docs/Api/SellerMediasApi.md#applysellermediacompetitivefees) | **POST** /api/v1/seller/medias/{id}/apply-competitive-fees | Set the competitive fees Growwer suggests
*SellerMediasApi* | [**createSellerMedia**](docs/Api/SellerMediasApi.md#createsellermedia) | **POST** /api/v1/seller/medias | Register a media you sell on
*SellerMediasApi* | [**deleteSellerMedia**](docs/Api/SellerMediasApi.md#deletesellermedia) | **DELETE** /api/v1/seller/medias/{id} | Delete a media you sell on
*SellerMediasApi* | [**getSellerMedia**](docs/Api/SellerMediasApi.md#getsellermedia) | **GET** /api/v1/seller/medias/{id} | Get a media you sell on
*SellerMediasApi* | [**listSellerMedias**](docs/Api/SellerMediasApi.md#listsellermedias) | **GET** /api/v1/seller/medias | List the medias you sell on
*SellerMediasApi* | [**updateSellerMedia**](docs/Api/SellerMediasApi.md#updatesellermedia) | **PATCH** /api/v1/seller/medias/{id} | Edit the offer of a media you sell on
*SellerOrdersApi* | [**acceptSellerOrder**](docs/Api/SellerOrdersApi.md#acceptsellerorder) | **POST** /api/v1/seller/orders/{id}/accept | Accept an order
*SellerOrdersApi* | [**deliverSellerOrder**](docs/Api/SellerOrdersApi.md#deliversellerorder) | **POST** /api/v1/seller/orders/{id}/deliver | Deliver an order
*SellerOrdersApi* | [**deliverSellerOrderDraft**](docs/Api/SellerOrdersApi.md#deliversellerorderdraft) | **POST** /api/v1/seller/orders/{id}/deliver-draft | Deliver a draft
*SellerOrdersApi* | [**deliverSellerOrderDraftUpdate**](docs/Api/SellerOrdersApi.md#deliversellerorderdraftupdate) | **POST** /api/v1/seller/orders/{id}/deliver-draft-update | Deliver a draft update
*SellerOrdersApi* | [**deliverSellerOrderUpdate**](docs/Api/SellerOrdersApi.md#deliversellerorderupdate) | **POST** /api/v1/seller/orders/{id}/deliver-update | Deliver an update
*SellerOrdersApi* | [**downloadSellerOrderBriefing**](docs/Api/SellerOrdersApi.md#downloadsellerorderbriefing) | **GET** /api/v1/seller/orders/{id}/briefing | Download the draft the buyer attached to an order
*SellerOrdersApi* | [**downloadSellerOrderDraft**](docs/Api/SellerOrdersApi.md#downloadsellerorderdraft) | **GET** /api/v1/seller/orders/{id}/draft | Download the draft of an order you sell
*SellerOrdersApi* | [**getSellerOrder**](docs/Api/SellerOrdersApi.md#getsellerorder) | **GET** /api/v1/seller/orders/{id} | Get an order you sell
*SellerOrdersApi* | [**listSellerOrders**](docs/Api/SellerOrdersApi.md#listsellerorders) | **GET** /api/v1/seller/orders | List the orders you sell
*SellerOrdersApi* | [**refuteSellerOrderDraftUpdate**](docs/Api/SellerOrdersApi.md#refutesellerorderdraftupdate) | **POST** /api/v1/seller/orders/{id}/refute-draft-update | Refuse a draft update
*SellerOrdersApi* | [**refuteSellerOrderUpdate**](docs/Api/SellerOrdersApi.md#refutesellerorderupdate) | **POST** /api/v1/seller/orders/{id}/refute-update | Refuse an update
*SellerOrdersApi* | [**rejectSellerOrder**](docs/Api/SellerOrdersApi.md#rejectsellerorder) | **POST** /api/v1/seller/orders/{id}/reject | Reject an order
*SellerWalletApi* | [**downloadSellerTransactionDocument**](docs/Api/SellerWalletApi.md#downloadsellertransactiondocument) | **GET** /api/v1/wallets/seller/transactions/{id}/document | Download the document of a seller wallet movement
*SellerWalletApi* | [**downloadWithdrawalInvoice**](docs/Api/SellerWalletApi.md#downloadwithdrawalinvoice) | **GET** /api/v1/withdrawals/{id}/invoice | Download the invoice of a withdrawal
*SellerWalletApi* | [**getSellerWallet**](docs/Api/SellerWalletApi.md#getsellerwallet) | **GET** /api/v1/wallets/seller | Get your seller wallet
*SellerWalletApi* | [**listSellerTransactions**](docs/Api/SellerWalletApi.md#listsellertransactions) | **GET** /api/v1/wallets/seller/transactions | List your seller wallet movements
*SellerWalletApi* | [**listWithdrawals**](docs/Api/SellerWalletApi.md#listwithdrawals) | **GET** /api/v1/withdrawals | List your withdrawals

## Models

- [Balance](docs/Model/Balance.md)
- [CatalogueMedia](docs/Model/CatalogueMedia.md)
- [CatalogueMediaFlashOffer](docs/Model/CatalogueMediaFlashOffer.md)
- [CatalogueMediaMetrics](docs/Model/CatalogueMediaMetrics.md)
- [CatalogueOffer](docs/Model/CatalogueOffer.md)
- [CatalogueOfferOrNull](docs/Model/CatalogueOfferOrNull.md)
- [CataloguePostOffer](docs/Model/CataloguePostOffer.md)
- [CataloguePostOfferAllOfExtras](docs/Model/CataloguePostOfferAllOfExtras.md)
- [CataloguePostOfferAllOfExtrasSensitiveTopic](docs/Model/CataloguePostOfferAllOfExtrasSensitiveTopic.md)
- [CodeName](docs/Model/CodeName.md)
- [CountSavedFilterMedias200Response](docs/Model/CountSavedFilterMedias200Response.md)
- [CreateProjectRequest](docs/Model/CreateProjectRequest.md)
- [CreateSavedFilterRequest](docs/Model/CreateSavedFilterRequest.md)
- [CreateSellerMediaRequest](docs/Model/CreateSellerMediaRequest.md)
- [CreateSellerMediaRequestPostOffer](docs/Model/CreateSellerMediaRequestPostOffer.md)
- [Error](docs/Model/Error.md)
- [GetBuyerWallet200Response](docs/Model/GetBuyerWallet200Response.md)
- [GetMe200Response](docs/Model/GetMe200Response.md)
- [GetMe200ResponseBuyer](docs/Model/GetMe200ResponseBuyer.md)
- [GetMe200ResponseCatalogue](docs/Model/GetMe200ResponseCatalogue.md)
- [GetMe200ResponseManagedService](docs/Model/GetMe200ResponseManagedService.md)
- [GetMe200ResponseSeller](docs/Model/GetMe200ResponseSeller.md)
- [GetSellerWallet200Response](docs/Model/GetSellerWallet200Response.md)
- [GetVocabulary200Response](docs/Model/GetVocabulary200Response.md)
- [GetVocabulary200ResponseTopicsInner](docs/Model/GetVocabulary200ResponseTopicsInner.md)
- [Invoice](docs/Model/Invoice.md)
- [LinkAdditionOrderBriefing](docs/Model/LinkAdditionOrderBriefing.md)
- [LinkAdditionOrderBriefingRequest](docs/Model/LinkAdditionOrderBriefingRequest.md)
- [ListBuyerTransactions200Response](docs/Model/ListBuyerTransactions200Response.md)
- [ListFlashOffers200Response](docs/Model/ListFlashOffers200Response.md)
- [ListInvoices200Response](docs/Model/ListInvoices200Response.md)
- [ListManagedServiceCampaigns200Response](docs/Model/ListManagedServiceCampaigns200Response.md)
- [ListManagedServiceProposals200Response](docs/Model/ListManagedServiceProposals200Response.md)
- [ListOrders200Response](docs/Model/ListOrders200Response.md)
- [ListProjects200Response](docs/Model/ListProjects200Response.md)
- [ListSavedFilters200Response](docs/Model/ListSavedFilters200Response.md)
- [ListSellerMedias200Response](docs/Model/ListSellerMedias200Response.md)
- [ListSellerOrders200Response](docs/Model/ListSellerOrders200Response.md)
- [ListSellerTransactions200Response](docs/Model/ListSellerTransactions200Response.md)
- [ListWithdrawals200Response](docs/Model/ListWithdrawals200Response.md)
- [ManagedServiceCampaign](docs/Model/ManagedServiceCampaign.md)
- [ManagedServiceCampaignProject](docs/Model/ManagedServiceCampaignProject.md)
- [ManagedServiceCampaignProposalCounts](docs/Model/ManagedServiceCampaignProposalCounts.md)
- [ManagedServiceCampaignStrategy](docs/Model/ManagedServiceCampaignStrategy.md)
- [ManagedServiceProposal](docs/Model/ManagedServiceProposal.md)
- [ManagedServiceProposalBriefing](docs/Model/ManagedServiceProposalBriefing.md)
- [ManagedServiceProposalBriefingLinksInner](docs/Model/ManagedServiceProposalBriefingLinksInner.md)
- [ManagedServiceProposalMedia](docs/Model/ManagedServiceProposalMedia.md)
- [ManagedServiceProposalReview](docs/Model/ManagedServiceProposalReview.md)
- [ManagedServiceProposalReviewRequest](docs/Model/ManagedServiceProposalReviewRequest.md)
- [ManagedServiceProposalReviewRequestReviewsInner](docs/Model/ManagedServiceProposalReviewRequestReviewsInner.md)
- [ManagedServiceProposalsEstimate](docs/Model/ManagedServiceProposalsEstimate.md)
- [ManagedServiceProposalsEstimateRequest](docs/Model/ManagedServiceProposalsEstimateRequest.md)
- [ManagedServiceRequest](docs/Model/ManagedServiceRequest.md)
- [ManagedServiceRequestSent](docs/Model/ManagedServiceRequestSent.md)
- [Money](docs/Model/Money.md)
- [MoneyOrNull](docs/Model/MoneyOrNull.md)
- [Order](docs/Model/Order.md)
- [OrderActionReason](docs/Model/OrderActionReason.md)
- [OrderBriefing](docs/Model/OrderBriefing.md)
- [OrderChannel](docs/Model/OrderChannel.md)
- [OrderCreateRequest](docs/Model/OrderCreateRequest.md)
- [OrderDelivery](docs/Model/OrderDelivery.md)
- [OrderDraft](docs/Model/OrderDraft.md)
- [OrderEstimate](docs/Model/OrderEstimate.md)
- [OrderEstimateRequest](docs/Model/OrderEstimateRequest.md)
- [OrderEstimateRequestBriefing](docs/Model/OrderEstimateRequestBriefing.md)
- [OrderLink](docs/Model/OrderLink.md)
- [OrderLinkRequest](docs/Model/OrderLinkRequest.md)
- [OrderMedia](docs/Model/OrderMedia.md)
- [OrderProject](docs/Model/OrderProject.md)
- [OrderStateHistoryInner](docs/Model/OrderStateHistoryInner.md)
- [OrderStateHistoryInnerReason](docs/Model/OrderStateHistoryInnerReason.md)
- [PostOrderBriefing](docs/Model/PostOrderBriefing.md)
- [PostOrderBriefingRequest](docs/Model/PostOrderBriefingRequest.md)
- [Project](docs/Model/Project.md)
- [ProjectCatalogueMedia](docs/Model/ProjectCatalogueMedia.md)
- [ProjectCatalogueMediaAllOfProject](docs/Model/ProjectCatalogueMediaAllOfProject.md)
- [ProjectCatalogueMediaAllOfProjectAiKeywords](docs/Model/ProjectCatalogueMediaAllOfProjectAiKeywords.md)
- [PutSellerHoliday200Response](docs/Model/PutSellerHoliday200Response.md)
- [PutSellerHolidayRequest](docs/Model/PutSellerHolidayRequest.md)
- [RequestMedias201Response](docs/Model/RequestMedias201Response.md)
- [RequestMediasRequest](docs/Model/RequestMediasRequest.md)
- [SavedFilter](docs/Model/SavedFilter.md)
- [SavedFilterNotifications](docs/Model/SavedFilterNotifications.md)
- [SellerFees](docs/Model/SellerFees.md)
- [SellerFeesOrNull](docs/Model/SellerFeesOrNull.md)
- [SellerMedia](docs/Model/SellerMedia.md)
- [SellerMediaFlashOffer](docs/Model/SellerMediaFlashOffer.md)
- [SellerMediaLinkAdditionOffer](docs/Model/SellerMediaLinkAdditionOffer.md)
- [SellerMediaLinkAdditionOfferPricingOptionsInner](docs/Model/SellerMediaLinkAdditionOfferPricingOptionsInner.md)
- [SellerMediaPostOffer](docs/Model/SellerMediaPostOffer.md)
- [SellerMediaPostOfferPricingOptionsInner](docs/Model/SellerMediaPostOfferPricingOptionsInner.md)
- [SellerOrder](docs/Model/SellerOrder.md)
- [SellerOrderBriefing](docs/Model/SellerOrderBriefing.md)
- [SellerOrderChannel](docs/Model/SellerOrderChannel.md)
- [SellerOrderDraft](docs/Model/SellerOrderDraft.md)
- [SellerOrderDraftFile](docs/Model/SellerOrderDraftFile.md)
- [SellerOrderPostDelivery](docs/Model/SellerOrderPostDelivery.md)
- [SellerOrderProject](docs/Model/SellerOrderProject.md)
- [SellerOrderRefutation](docs/Model/SellerOrderRefutation.md)
- [SellerOrderRejection](docs/Model/SellerOrderRejection.md)
- [SellerOrderRejectionReason](docs/Model/SellerOrderRejectionReason.md)
- [SellerPostOrderBriefing](docs/Model/SellerPostOrderBriefing.md)
- [SellerTransaction](docs/Model/SellerTransaction.md)
- [Transaction](docs/Model/Transaction.md)
- [UpdateProjectRequest](docs/Model/UpdateProjectRequest.md)
- [UpdateSellerMediaRequest](docs/Model/UpdateSellerMediaRequest.md)
- [UpdateSellerMediaRequestExtraServicesInner](docs/Model/UpdateSellerMediaRequestExtraServicesInner.md)
- [UpdateSellerMediaRequestLinkAdditionOffer](docs/Model/UpdateSellerMediaRequestLinkAdditionOffer.md)
- [UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner](docs/Model/UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner.md)
- [UpdateSellerMediaRequestPostOffer](docs/Model/UpdateSellerMediaRequestPostOffer.md)
- [UpdateSellerMediaRequestPostOfferPricingOptionsInner](docs/Model/UpdateSellerMediaRequestPostOfferPricingOptionsInner.md)
- [UploadFile201Response](docs/Model/UploadFile201Response.md)
- [Withdrawal](docs/Model/Withdrawal.md)

## Authorization

Authentication schemes defined for the API:
### apiKey

- **Type**: Bearer authentication

## Tests

To run the tests, use:

```bash
composer install
vendor/bin/phpunit
```

## Author

support@growwer.com

## About this package

This PHP package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `1`
    - Generator version: `7.24.0`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`
