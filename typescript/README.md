# @growwer/api@2.0.0

A TypeScript SDK client for the tool.growwer.com API.

## Usage

First, install the SDK from npm.

```bash
npm install @growwer/api --save
```

Next, try it out.


```ts
import {
  Configuration,
  AccountApi,
} from '@growwer/api';
import type { GetMeRequest } from '@growwer/api';

async function example() {
  console.log("🚀 Testing @growwer/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: apiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AccountApi(config);

  try {
    const data = await api.getMe();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```


## Documentation

### API Endpoints

All URIs are relative to *https://tool.growwer.com*

| Class | Method | HTTP request | Description
| ----- | ------ | ------------ | -------------
*AccountApi* | [**getMe**](docs/AccountApi.md#getme) | **GET** /api/v1/me | Your account
*AccountApi* | [**getVocabulary**](docs/AccountApi.md#getvocabulary) | **GET** /api/v1/vocabulary | Codes and names
*BuyerOrdersApi* | [**approveOrder**](docs/BuyerOrdersApi.md#approveorder) | **POST** /api/v1/orders/{id}/approve | Approve an order\&#39;s delivery
*BuyerOrdersApi* | [**approveOrderDraft**](docs/BuyerOrdersApi.md#approveorderdraft) | **POST** /api/v1/orders/{id}/approve-draft | Approve a draft
*BuyerOrdersApi* | [**cancelOrder**](docs/BuyerOrdersApi.md#cancelorder) | **POST** /api/v1/orders/{id}/cancel | Cancel an order
*BuyerOrdersApi* | [**createOrder**](docs/BuyerOrdersApi.md#createorder) | **POST** /api/v1/orders | Place an order
*BuyerOrdersApi* | [**downloadOrderBriefing**](docs/BuyerOrdersApi.md#downloadorderbriefing) | **GET** /api/v1/orders/{id}/briefing | Download the draft you attached to an order
*BuyerOrdersApi* | [**downloadOrderDraft**](docs/BuyerOrdersApi.md#downloadorderdraft) | **GET** /api/v1/orders/{id}/draft | Download the draft of an order
*BuyerOrdersApi* | [**estimateOrder**](docs/BuyerOrdersApi.md#estimateorder) | **POST** /api/v1/orders/estimate | Estimate an order
*BuyerOrdersApi* | [**getOrder**](docs/BuyerOrdersApi.md#getorder) | **GET** /api/v1/orders/{id} | Get an order
*BuyerOrdersApi* | [**listOrders**](docs/BuyerOrdersApi.md#listorders) | **GET** /api/v1/orders | List your orders
*BuyerOrdersApi* | [**requestOrderDraftUpdate**](docs/BuyerOrdersApi.md#requestorderdraftupdate) | **POST** /api/v1/orders/{id}/request-draft-update | Request changes to a draft
*BuyerOrdersApi* | [**requestOrderUpdate**](docs/BuyerOrdersApi.md#requestorderupdate) | **POST** /api/v1/orders/{id}/request-update | Request changes to a delivery
*BuyerWalletApi* | [**downloadBuyerTransactionDocument**](docs/BuyerWalletApi.md#downloadbuyertransactiondocument) | **GET** /api/v1/wallets/buyer/transactions/{id}/document | Download the document of a wallet movement
*BuyerWalletApi* | [**getBuyerWallet**](docs/BuyerWalletApi.md#getbuyerwallet) | **GET** /api/v1/wallets/buyer | Get your buyer wallet
*BuyerWalletApi* | [**getInvoicePdf**](docs/BuyerWalletApi.md#getinvoicepdf) | **GET** /api/v1/invoices/{id}/pdf | Download an invoice
*BuyerWalletApi* | [**listBuyerTransactions**](docs/BuyerWalletApi.md#listbuyertransactions) | **GET** /api/v1/wallets/buyer/transactions | List your buyer wallet movements
*BuyerWalletApi* | [**listInvoices**](docs/BuyerWalletApi.md#listinvoices) | **GET** /api/v1/invoices | List your invoices
*CatalogueApi* | [**discardMedia**](docs/CatalogueApi.md#discardmedia) | **PUT** /api/v1/projects/{id}/discards/{mediaId} | Discard a media for a project
*CatalogueApi* | [**favouriteMedia**](docs/CatalogueApi.md#favouritemedia) | **PUT** /api/v1/projects/{id}/favourites/{mediaId} | Add a media to the favourites of a project
*CatalogueApi* | [**getCatalogueMedia**](docs/CatalogueApi.md#getcataloguemedia) | **GET** /api/v1/medias/{id} | Get a media
*CatalogueApi* | [**listFlashOffers**](docs/CatalogueApi.md#listflashoffers) | **GET** /api/v1/flash-offers | List flash offers
*CatalogueApi* | [**requestMedias**](docs/CatalogueApi.md#requestmediasoperation) | **POST** /api/v1/projects/{id}/media-requests | Request specific medias for a project
*CatalogueApi* | [**searchProjectMedias**](docs/CatalogueApi.md#searchprojectmedias) | **GET** /api/v1/projects/{id}/medias | Search the catalogue for a project
*CatalogueApi* | [**undiscardMedia**](docs/CatalogueApi.md#undiscardmedia) | **DELETE** /api/v1/projects/{id}/discards/{mediaId} | Restore a discarded media for a project
*CatalogueApi* | [**unfavouriteMedia**](docs/CatalogueApi.md#unfavouritemedia) | **DELETE** /api/v1/projects/{id}/favourites/{mediaId} | Remove a media from the favourites of a project
*FilesApi* | [**uploadFile**](docs/FilesApi.md#uploadfile) | **POST** /api/v1/files | Upload a file
*ManagedServicesApi* | [**estimateManagedServiceProposals**](docs/ManagedServicesApi.md#estimatemanagedserviceproposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/estimate | Estimate accepting proposals
*ManagedServicesApi* | [**getManagedServiceCampaign**](docs/ManagedServicesApi.md#getmanagedservicecampaign) | **GET** /api/v1/managed-service/campaigns/{id} | Get a managed service campaign
*ManagedServicesApi* | [**getManagedServiceProposalsSummary**](docs/ManagedServicesApi.md#getmanagedserviceproposalssummary) | **GET** /api/v1/managed-service/campaigns/{id}/proposals-summary | Download the summary of a campaign\&#39;s proposals
*ManagedServicesApi* | [**listManagedServiceCampaigns**](docs/ManagedServicesApi.md#listmanagedservicecampaigns) | **GET** /api/v1/managed-service/campaigns | List your managed service campaigns
*ManagedServicesApi* | [**listManagedServiceProposals**](docs/ManagedServicesApi.md#listmanagedserviceproposals) | **GET** /api/v1/managed-service/campaigns/{id}/proposals | List the proposals of a campaign
*ManagedServicesApi* | [**requestManagedServiceCampaign**](docs/ManagedServicesApi.md#requestmanagedservicecampaign) | **POST** /api/v1/managed-service/campaign-requests | Request a new campaign
*ManagedServicesApi* | [**requestManagedServiceInfo**](docs/ManagedServicesApi.md#requestmanagedserviceinfo) | **POST** /api/v1/managed-service/info-requests | Ask about the managed service
*ManagedServicesApi* | [**reviewManagedServiceProposals**](docs/ManagedServicesApi.md#reviewmanagedserviceproposals) | **POST** /api/v1/managed-service/campaigns/{id}/proposals/review | Accept or reject proposals
*ProjectsApi* | [**createProject**](docs/ProjectsApi.md#createprojectoperation) | **POST** /api/v1/projects | Create a project
*ProjectsApi* | [**deleteProject**](docs/ProjectsApi.md#deleteproject) | **DELETE** /api/v1/projects/{id} | Delete a project
*ProjectsApi* | [**getProject**](docs/ProjectsApi.md#getproject) | **GET** /api/v1/projects/{id} | Get a project
*ProjectsApi* | [**listProjects**](docs/ProjectsApi.md#listprojects) | **GET** /api/v1/projects | List your projects
*ProjectsApi* | [**updateProject**](docs/ProjectsApi.md#updateprojectoperation) | **PATCH** /api/v1/projects/{id} | Edit a project
*SavedFiltersApi* | [**countSavedFilterMedias**](docs/SavedFiltersApi.md#countsavedfiltermedias) | **GET** /api/v1/projects/{id}/saved-filters/{filterId}/media-count | Count the medias of a saved filter
*SavedFiltersApi* | [**createSavedFilter**](docs/SavedFiltersApi.md#createsavedfilteroperation) | **POST** /api/v1/projects/{id}/saved-filters | Save a filter
*SavedFiltersApi* | [**deleteSavedFilter**](docs/SavedFiltersApi.md#deletesavedfilter) | **DELETE** /api/v1/projects/{id}/saved-filters/{filterId} | Delete a saved filter
*SavedFiltersApi* | [**listSavedFilters**](docs/SavedFiltersApi.md#listsavedfilters) | **GET** /api/v1/projects/{id}/saved-filters | List the saved filters of a project
*SellerAccountApi* | [**putSellerHoliday**](docs/SellerAccountApi.md#putsellerholidayoperation) | **PUT** /api/v1/seller/holiday | Set your holiday
*SellerMediasApi* | [**applySellerMediaCompetitiveFees**](docs/SellerMediasApi.md#applysellermediacompetitivefees) | **POST** /api/v1/seller/medias/{id}/apply-competitive-fees | Set the competitive fees Growwer suggests
*SellerMediasApi* | [**createSellerMedia**](docs/SellerMediasApi.md#createsellermediaoperation) | **POST** /api/v1/seller/medias | Register a media you sell on
*SellerMediasApi* | [**deleteSellerMedia**](docs/SellerMediasApi.md#deletesellermedia) | **DELETE** /api/v1/seller/medias/{id} | Delete a media you sell on
*SellerMediasApi* | [**getSellerMedia**](docs/SellerMediasApi.md#getsellermedia) | **GET** /api/v1/seller/medias/{id} | Get a media you sell on
*SellerMediasApi* | [**listSellerMedias**](docs/SellerMediasApi.md#listsellermedias) | **GET** /api/v1/seller/medias | List the medias you sell on
*SellerMediasApi* | [**updateSellerMedia**](docs/SellerMediasApi.md#updatesellermediaoperation) | **PATCH** /api/v1/seller/medias/{id} | Edit the offer of a media you sell on
*SellerOrdersApi* | [**acceptSellerOrder**](docs/SellerOrdersApi.md#acceptsellerorder) | **POST** /api/v1/seller/orders/{id}/accept | Accept an order
*SellerOrdersApi* | [**deliverSellerOrder**](docs/SellerOrdersApi.md#deliversellerorder) | **POST** /api/v1/seller/orders/{id}/deliver | Deliver an order
*SellerOrdersApi* | [**deliverSellerOrderDraft**](docs/SellerOrdersApi.md#deliversellerorderdraft) | **POST** /api/v1/seller/orders/{id}/deliver-draft | Deliver a draft
*SellerOrdersApi* | [**deliverSellerOrderDraftUpdate**](docs/SellerOrdersApi.md#deliversellerorderdraftupdate) | **POST** /api/v1/seller/orders/{id}/deliver-draft-update | Deliver a draft update
*SellerOrdersApi* | [**deliverSellerOrderUpdate**](docs/SellerOrdersApi.md#deliversellerorderupdate) | **POST** /api/v1/seller/orders/{id}/deliver-update | Deliver an update
*SellerOrdersApi* | [**downloadSellerOrderBriefing**](docs/SellerOrdersApi.md#downloadsellerorderbriefing) | **GET** /api/v1/seller/orders/{id}/briefing | Download the draft the buyer attached to an order
*SellerOrdersApi* | [**downloadSellerOrderDraft**](docs/SellerOrdersApi.md#downloadsellerorderdraft) | **GET** /api/v1/seller/orders/{id}/draft | Download the draft of an order you sell
*SellerOrdersApi* | [**getSellerOrder**](docs/SellerOrdersApi.md#getsellerorder) | **GET** /api/v1/seller/orders/{id} | Get an order you sell
*SellerOrdersApi* | [**listSellerOrders**](docs/SellerOrdersApi.md#listsellerorders) | **GET** /api/v1/seller/orders | List the orders you sell
*SellerOrdersApi* | [**refuteSellerOrderDraftUpdate**](docs/SellerOrdersApi.md#refutesellerorderdraftupdate) | **POST** /api/v1/seller/orders/{id}/refute-draft-update | Refuse a draft update
*SellerOrdersApi* | [**refuteSellerOrderUpdate**](docs/SellerOrdersApi.md#refutesellerorderupdate) | **POST** /api/v1/seller/orders/{id}/refute-update | Refuse an update
*SellerOrdersApi* | [**rejectSellerOrder**](docs/SellerOrdersApi.md#rejectsellerorder) | **POST** /api/v1/seller/orders/{id}/reject | Reject an order
*SellerWalletApi* | [**downloadSellerTransactionDocument**](docs/SellerWalletApi.md#downloadsellertransactiondocument) | **GET** /api/v1/wallets/seller/transactions/{id}/document | Download the document of a seller wallet movement
*SellerWalletApi* | [**downloadWithdrawalInvoice**](docs/SellerWalletApi.md#downloadwithdrawalinvoice) | **GET** /api/v1/withdrawals/{id}/invoice | Download the invoice of a withdrawal
*SellerWalletApi* | [**getSellerWallet**](docs/SellerWalletApi.md#getsellerwallet) | **GET** /api/v1/wallets/seller | Get your seller wallet
*SellerWalletApi* | [**listSellerTransactions**](docs/SellerWalletApi.md#listsellertransactions) | **GET** /api/v1/wallets/seller/transactions | List your seller wallet movements
*SellerWalletApi* | [**listWithdrawals**](docs/SellerWalletApi.md#listwithdrawals) | **GET** /api/v1/withdrawals | List your withdrawals


### Models

- [Balance](docs/Balance.md)
- [CatalogueMedia](docs/CatalogueMedia.md)
- [CatalogueMediaFlashOffer](docs/CatalogueMediaFlashOffer.md)
- [CatalogueMediaMetrics](docs/CatalogueMediaMetrics.md)
- [CatalogueOffer](docs/CatalogueOffer.md)
- [CatalogueOfferOrNull](docs/CatalogueOfferOrNull.md)
- [CataloguePostOffer](docs/CataloguePostOffer.md)
- [CataloguePostOfferAllOfExtras](docs/CataloguePostOfferAllOfExtras.md)
- [CataloguePostOfferAllOfExtrasSensitiveTopic](docs/CataloguePostOfferAllOfExtrasSensitiveTopic.md)
- [CodeName](docs/CodeName.md)
- [CountSavedFilterMedias200Response](docs/CountSavedFilterMedias200Response.md)
- [CreateProjectRequest](docs/CreateProjectRequest.md)
- [CreateSavedFilterRequest](docs/CreateSavedFilterRequest.md)
- [CreateSellerMediaRequest](docs/CreateSellerMediaRequest.md)
- [CreateSellerMediaRequestPostOffer](docs/CreateSellerMediaRequestPostOffer.md)
- [GetBuyerWallet200Response](docs/GetBuyerWallet200Response.md)
- [GetMe200Response](docs/GetMe200Response.md)
- [GetMe200ResponseBuyer](docs/GetMe200ResponseBuyer.md)
- [GetMe200ResponseCatalogue](docs/GetMe200ResponseCatalogue.md)
- [GetMe200ResponseManagedService](docs/GetMe200ResponseManagedService.md)
- [GetMe200ResponseSeller](docs/GetMe200ResponseSeller.md)
- [GetSellerWallet200Response](docs/GetSellerWallet200Response.md)
- [GetVocabulary200Response](docs/GetVocabulary200Response.md)
- [GetVocabulary200ResponseTopicsInner](docs/GetVocabulary200ResponseTopicsInner.md)
- [Invoice](docs/Invoice.md)
- [LinkAdditionOrderBriefing](docs/LinkAdditionOrderBriefing.md)
- [LinkAdditionOrderBriefingRequest](docs/LinkAdditionOrderBriefingRequest.md)
- [ListBuyerTransactions200Response](docs/ListBuyerTransactions200Response.md)
- [ListFlashOffers200Response](docs/ListFlashOffers200Response.md)
- [ListInvoices200Response](docs/ListInvoices200Response.md)
- [ListManagedServiceCampaigns200Response](docs/ListManagedServiceCampaigns200Response.md)
- [ListManagedServiceProposals200Response](docs/ListManagedServiceProposals200Response.md)
- [ListOrders200Response](docs/ListOrders200Response.md)
- [ListProjects200Response](docs/ListProjects200Response.md)
- [ListSavedFilters200Response](docs/ListSavedFilters200Response.md)
- [ListSellerMedias200Response](docs/ListSellerMedias200Response.md)
- [ListSellerOrders200Response](docs/ListSellerOrders200Response.md)
- [ListSellerTransactions200Response](docs/ListSellerTransactions200Response.md)
- [ListWithdrawals200Response](docs/ListWithdrawals200Response.md)
- [ManagedServiceCampaign](docs/ManagedServiceCampaign.md)
- [ManagedServiceCampaignProject](docs/ManagedServiceCampaignProject.md)
- [ManagedServiceCampaignProposalCounts](docs/ManagedServiceCampaignProposalCounts.md)
- [ManagedServiceCampaignStrategy](docs/ManagedServiceCampaignStrategy.md)
- [ManagedServiceProposal](docs/ManagedServiceProposal.md)
- [ManagedServiceProposalBriefing](docs/ManagedServiceProposalBriefing.md)
- [ManagedServiceProposalBriefingLinksInner](docs/ManagedServiceProposalBriefingLinksInner.md)
- [ManagedServiceProposalMedia](docs/ManagedServiceProposalMedia.md)
- [ManagedServiceProposalReview](docs/ManagedServiceProposalReview.md)
- [ManagedServiceProposalReviewRequest](docs/ManagedServiceProposalReviewRequest.md)
- [ManagedServiceProposalReviewRequestReviewsInner](docs/ManagedServiceProposalReviewRequestReviewsInner.md)
- [ManagedServiceProposalsEstimate](docs/ManagedServiceProposalsEstimate.md)
- [ManagedServiceProposalsEstimateRequest](docs/ManagedServiceProposalsEstimateRequest.md)
- [ManagedServiceRequest](docs/ManagedServiceRequest.md)
- [ManagedServiceRequestSent](docs/ManagedServiceRequestSent.md)
- [ModelError](docs/ModelError.md)
- [Money](docs/Money.md)
- [MoneyOrNull](docs/MoneyOrNull.md)
- [Order](docs/Order.md)
- [OrderActionReason](docs/OrderActionReason.md)
- [OrderBriefing](docs/OrderBriefing.md)
- [OrderChannel](docs/OrderChannel.md)
- [OrderCreateRequest](docs/OrderCreateRequest.md)
- [OrderDelivery](docs/OrderDelivery.md)
- [OrderDraft](docs/OrderDraft.md)
- [OrderEstimate](docs/OrderEstimate.md)
- [OrderEstimateRequest](docs/OrderEstimateRequest.md)
- [OrderEstimateRequestBriefing](docs/OrderEstimateRequestBriefing.md)
- [OrderLink](docs/OrderLink.md)
- [OrderLinkRequest](docs/OrderLinkRequest.md)
- [OrderMedia](docs/OrderMedia.md)
- [OrderProject](docs/OrderProject.md)
- [OrderStateHistoryInner](docs/OrderStateHistoryInner.md)
- [OrderStateHistoryInnerReason](docs/OrderStateHistoryInnerReason.md)
- [PostOrderBriefing](docs/PostOrderBriefing.md)
- [PostOrderBriefingRequest](docs/PostOrderBriefingRequest.md)
- [Project](docs/Project.md)
- [ProjectCatalogueMedia](docs/ProjectCatalogueMedia.md)
- [ProjectCatalogueMediaAllOfProject](docs/ProjectCatalogueMediaAllOfProject.md)
- [ProjectCatalogueMediaAllOfProjectAiKeywords](docs/ProjectCatalogueMediaAllOfProjectAiKeywords.md)
- [PutSellerHoliday200Response](docs/PutSellerHoliday200Response.md)
- [PutSellerHolidayRequest](docs/PutSellerHolidayRequest.md)
- [RequestMedias201Response](docs/RequestMedias201Response.md)
- [RequestMediasRequest](docs/RequestMediasRequest.md)
- [SavedFilter](docs/SavedFilter.md)
- [SavedFilterNotifications](docs/SavedFilterNotifications.md)
- [SellerFees](docs/SellerFees.md)
- [SellerFeesOrNull](docs/SellerFeesOrNull.md)
- [SellerMedia](docs/SellerMedia.md)
- [SellerMediaFlashOffer](docs/SellerMediaFlashOffer.md)
- [SellerMediaLinkAdditionOffer](docs/SellerMediaLinkAdditionOffer.md)
- [SellerMediaLinkAdditionOfferPricingOptionsInner](docs/SellerMediaLinkAdditionOfferPricingOptionsInner.md)
- [SellerMediaPostOffer](docs/SellerMediaPostOffer.md)
- [SellerMediaPostOfferPricingOptionsInner](docs/SellerMediaPostOfferPricingOptionsInner.md)
- [SellerOrder](docs/SellerOrder.md)
- [SellerOrderBriefing](docs/SellerOrderBriefing.md)
- [SellerOrderChannel](docs/SellerOrderChannel.md)
- [SellerOrderDraft](docs/SellerOrderDraft.md)
- [SellerOrderDraftFile](docs/SellerOrderDraftFile.md)
- [SellerOrderPostDelivery](docs/SellerOrderPostDelivery.md)
- [SellerOrderProject](docs/SellerOrderProject.md)
- [SellerOrderRefutation](docs/SellerOrderRefutation.md)
- [SellerOrderRejection](docs/SellerOrderRejection.md)
- [SellerOrderRejectionReason](docs/SellerOrderRejectionReason.md)
- [SellerPostOrderBriefing](docs/SellerPostOrderBriefing.md)
- [SellerTransaction](docs/SellerTransaction.md)
- [Transaction](docs/Transaction.md)
- [UpdateProjectRequest](docs/UpdateProjectRequest.md)
- [UpdateSellerMediaRequest](docs/UpdateSellerMediaRequest.md)
- [UpdateSellerMediaRequestExtraServicesInner](docs/UpdateSellerMediaRequestExtraServicesInner.md)
- [UpdateSellerMediaRequestLinkAdditionOffer](docs/UpdateSellerMediaRequestLinkAdditionOffer.md)
- [UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner](docs/UpdateSellerMediaRequestLinkAdditionOfferPricingOptionsInner.md)
- [UpdateSellerMediaRequestPostOffer](docs/UpdateSellerMediaRequestPostOffer.md)
- [UpdateSellerMediaRequestPostOfferPricingOptionsInner](docs/UpdateSellerMediaRequestPostOfferPricingOptionsInner.md)
- [UploadFile201Response](docs/UploadFile201Response.md)
- [Withdrawal](docs/Withdrawal.md)

### Authorization


Authentication schemes defined for the API:
<a id="apiKey"></a>
#### apiKey


- **Type**: HTTP Bearer Token authentication

## About

This TypeScript SDK client supports the [Fetch API](https://fetch.spec.whatwg.org/)
and is automatically generated by the
[OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `1`
- Package version: `2.0.0`
- Generator version: `7.24.0`
- Build package: `org.openapitools.codegen.languages.TypeScriptFetchClientCodegen`

The generated npm module supports the following:

- Environments
  * Node.js
  * Webpack
  * Browserify
- Language levels
  * ES5 - you must have a Promises/A+ library installed
  * ES6
- Module systems
  * CommonJS
  * ES6 module system

For more information, please visit [https://growwer.com/contact/](https://growwer.com/contact/)

## Development

### Building

To build the TypeScript source code, you need to have Node.js and npm installed.
After cloning the repository, navigate to the project directory and run:

```bash
npm install
npm run build
```

### Publishing

Once you've built the package, you can publish it to npm:

```bash
npm publish
```

## License

[Proprietary](https://growwer.com/legal/terms-of-use/)
